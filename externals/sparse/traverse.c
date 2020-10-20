#include <string.h>
#include "dissect.h"

int counter = 0;
bool start = false;
unsigned curr_stream = -1;

static inline const char *show_mode(unsigned mode)
{
	static char str[3];

	if (mode == -1)
		return "def";

#define	U(u_r)	"-rwm"[(mode / u_r) & 3]
	str[0] = U(U_R_AOF);
	str[1] = U(U_R_VAL);
	str[2] = U(U_R_PTR);
#undef	U

	return str;
}

static void r_symbol(unsigned mode, struct position *pos, struct symbol *sym)
{
	// prepare
	static struct ident null;
	struct ident *ctx = &null;
	if (dissect_ctx)
		ctx = dissect_ctx->ident;

	if (!sym->ident)
		sym->ident = built_in_ident("__asm__");

	// detect function
	if (ctx->len == 0) {
		// not in function
		// keep function definition
		if (mode == -1 && sym->kind == 'f') {
			if (start)
				printf("}\n\n");
			if (curr_stream != pos->stream) {
				curr_stream = pos->stream;
			}
			// caller: sym->ident->name
			printf("subgraph \"%s\" {\n"
			       "    color=blue;\n"
			       "    label=<<TABLE BORDER=\"0\" CELLBORDER=\"0\">\n"
			       "             <TR><TD>%s</TD></TR>\n"
			       "             <TR><TD><FONT POINT-SIZE=\"21\">%s()</FONT></TD></TR>\n"
			       "           </TABLE>>;\n"
			       "    file=\"%s\";\n"
			       "    fun=\"%s\";\n",
			       sym->ident->name,
			       stream_name(curr_stream), sym->ident->name,
			       stream_name(curr_stream), sym->ident->name);
			start = true;
			counter = 0;
			return;
		} else
			return;
	} else {
		// in function
		// remove variable defined in caller
		// keep callees in caller 
		if (sym->kind == 'v')
			return;
	}
	// caller: ctx->name
	// callee: sym->ident->name
	printf("    \"%s\" -> \"%s\" [label=%d, line=%d, pos=%d, kind=%d]\n",
	       ctx->name, sym->ident->name, counter++,
	       pos->line, pos->pos, sym->kind);

	switch (sym->kind) {
	case 's':
		if (sym->type == SYM_STRUCT || sym->type == SYM_UNION)
			break;
		goto err;

	case 'f':
		if (sym->type != SYM_BAD && sym->ctype.base_type->type != SYM_FN)
			goto err;
	case 'v':
		if (sym->type == SYM_NODE || sym->type == SYM_BAD)
			break;
		goto err;
	default:
		goto err;
	}

	return;
err:
	warning(*pos, "r_symbol bad sym type=%d kind=%d", sym->type, sym->kind);
}

static void r_member(unsigned mode, struct position *pos, struct symbol *sym, struct symbol *mem)
{
	struct ident *ni, *si, *mi;

	static struct ident null;
	struct ident *ctx = &null;
	if (dissect_ctx)
		ctx = dissect_ctx->ident;

	// remove struct member defined in caller
	if (ctx->len == 0)
		return;

	ni = built_in_ident("?");
	si = sym->ident ?: ni;
	/* mem == NULL means entire struct accessed */
	mi = mem ? (mem->ident ?: ni) : built_in_ident("*");

	// remove struct member used but not pointered
	const char *mode_str = show_mode(mode);
	if (mode_str[2] != 'r')
		return;

	printf("    \"%s\" -> \"%s.%s\" [label=%d, line=%d, pos=%d, kind=%d]\n",
	       ctx->name, si->name, mi->name, counter++,
	       pos->line, pos->pos, sym->kind);

	if (sym->ident && sym->kind != 's')
		warning(*pos, "r_member bad sym type=%d kind=%d", sym->type, sym->kind);
	if (mem && mem->kind != 'm')
		warning(*pos, "r_member bad mem->kind = %d", mem->kind);
}

static void r_symdef(struct symbol *sym)
{
	r_symbol(-1, &sym->pos, sym);
}

static void r_memdef(struct symbol *sym, struct symbol *mem)
{
	r_member(-1, &mem->pos, sym, mem);
}

int main(int argc, char **argv)
{
	static struct reporter reporter = {
		.r_symdef = r_symdef,
		.r_memdef = r_memdef,
		.r_symbol = r_symbol,
		.r_member = r_member,
	};

	struct string_list *filelist = NULL;
	sparse_initialize(argc, argv, &filelist);
	printf("digraph function_graph {\n"
	       "       rankdir=LR\n"
	       "       ratio=compress\n");
	dissect(&reporter, filelist);
	if (start)
		printf("}\n");
	printf("}\n");

	return 0;
}
