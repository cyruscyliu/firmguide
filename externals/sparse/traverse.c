/* 
 * Sparse traverse
 * 
 * Copyright (C) 2020 Qiang Liu <qiangliu@zju.edu.cn>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
#include <stdarg.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <unistd.h>
#include <fcntl.h>

#include "lib.h"
#include "allocate.h"
#include "token.h"
#include "parse.h"
#include "symbol.h"
#include "expression.h"
#include "linearize.h"


static void func_traversal(struct entrypoint *ep)
{
	struct basic_block *bb;
	struct instruction *insn;

	const char *fname, *sname;
	int i = 0;

	fname = show_ident(ep->name->ident);
	sname = stream_name(ep->entry->bb->pos.stream);

	printf("subgraph cluster%p {\n"
	       "    color=blue;\n"
	       "    label=<<TABLE BORDER=\"0\" CELLBORDER=\"0\">\n"
	       "             <TR><TD>%s</TD></TR>\n"
	       "             <TR><TD><FONT POINT-SIZE=\"21\">%s()</FONT></TD></TR>\n"
	       "           </TABLE>>;\n"
	       "    file=\"%s\";\n"
	       "    fun=\"%s\";\n",
	       ep, sname, fname, sname, fname);

	FOR_EACH_PTR(ep->bbs, bb) {
		/* List loads and stores */
		FOR_EACH_PTR(bb->insns, insn) {
			if (!insn->bb)
				continue;
			switch(insn->opcode) {
			case OP_CALL:
				printf("    \"%s\" -> \"%s\" [label=%d]\n", show_ident(ep->name->ident),
					  show_ident(insn->func->ident), i);
				i++;
				break;
			case OP_INLINED_CALL:
				printf("    \"%s\" -> \"%s\" [label=%d]\n", show_ident(ep->name->ident),
					  show_ident(insn->func->ident), i);
				i++;
				break;
			}
		} END_FOR_EACH_PTR(insn);
	} END_FOR_EACH_PTR(bb);
	printf("}\n");
}

int main(int argc, char **argv)
{
	struct string_list *filelist = NULL;
	char *file;
	struct symbol *sym;

	struct symbol_list *fsyms, *all_syms=NULL;

	printf("digraph function_graph {\n");
	fsyms = sparse_initialize(argc, argv, &filelist);
	concat_symbol_list(fsyms, &all_syms);

	FOR_EACH_PTR(filelist, file) {
		fsyms = sparse(file);
		concat_symbol_list(fsyms, &all_syms);

		FOR_EACH_PTR(fsyms, sym) {
			expand_symbol(sym);
			linearize_symbol(sym);
		} END_FOR_EACH_PTR(sym);

		FOR_EACH_PTR(fsyms, sym) {
			if (sym->ep) {
				func_traversal(sym->ep);
			}
		} END_FOR_EACH_PTR(sym);
	} END_FOR_EACH_PTR(file);
	printf("}\n");
	return 0;
}
