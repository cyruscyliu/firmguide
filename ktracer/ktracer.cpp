/*
 * capstone support: https://www.capstone-engine.org/lang_c.html
 * initial panda plugin supported by huamao
 */

#define __STDC_FORMAT_MACROS

#include "panda/plugin.h"
#include "panda/plugin_plugin.h"

#include <cstdio>
#include <cstdlib>
#include <inttypes.h>
#include <capstone/capstone.h>
#include "syscalls2/syscalls2_info.h"
#include "syscalls2/syscalls2_ext.h"

struct Record {
    uint32_t n_regs;
    uint32_t *regs;
    uint32_t code_size;
    uint8_t *code;
};

/* output */
FILE *output;

/* capstone */
csh handle;
bool init_capstone_done = false;

bool init_capstone(CPUState *cs);

/* callbacks */

int before_block_exec(CPUState *cs, TranslationBlock *tb);

size_t disassemble_block(CPUState *cs, TranslationBlock *tb, uint8_t **code);

extern "C" {
bool init_plugin(void *);
void uninit_plugin(void *);
}

int before_block_exec(CPUState *cs, TranslationBlock *tb) {
    CPUArchState *env = (CPUArchState *) cs->env_ptr;
    Record record = Record();
    if (!init_capstone_done) {
        if (!init_capstone(cs)) return -1;
        init_capstone_done = true;
    }
#if defined(TARGET_ARM)
    record.n_regs = 18;
    // add r0 to r12, sp(r13), lr(r14), pc(r15)
    record.regs = (uint32_t *)malloc(record.n_regs * sizeof(uint32_t));
    for (size_t i = 0; i < 16; i++) {
        record.regs[i] = env->regs[i];
    }
    // add others
    record.regs[16] = cpsr_read(env);
    record.regs[17] = xpsr_read(env);
#endif
    fwrite(&record.n_regs, sizeof(uint32_t), 1, output);
    fwrite(record.regs, record.n_regs * sizeof(uint32_t), 1, output);
    record.code_size = disassemble_block(cs, tb, &record.code);
    fwrite(&record.code_size, sizeof(uint32_t), 1, output);
    fwrite(record.code, record.code_size, 1, output);
    free(record.regs);
    free(record.code);
    return 0;
}

size_t disassemble_block(CPUState *cs, TranslationBlock *tb, uint8_t **code) {
    size_t count, length = 0;
    cs_insn *insn;
    uint8_t *mem = (uint8_t *) malloc(1024 * sizeof(uint8_t));

    panda_virtual_memory_rw(cs, tb->pc, mem, tb->size, false);
    count = cs_disasm(handle, mem, tb->size, tb->pc, 0, &insn);
    for (size_t i = 0; i < count; i++) {
        length += sprintf(
                (char *) mem + length,
                "0x%x :%s\t\t%s\n", (unsigned int) insn[i].address, insn[i].mnemonic, insn[i].op_str
        );
    }
    *code = (uint8_t *) malloc(length * sizeof(uint8_t));
    memcpy(*code, mem, length);
    cs_free(insn, count);
    return length;
}

bool init_capstone(CPUState *cs) {
    CPUArchState *env = (CPUArchState *) cs->env_ptr;
#if defined(TARGET_ARM)
    cs_arch arch = CS_ARCH_ARM;
    cs_mode mode = env->thumb ? CS_MODE_THUMB : CS_MODE_ARM;
#endif
    if (cs_open(arch, mode, &handle) != CS_ERR_OK) {
        cs_close(&handle);
        return false;
    }
    return true;
}

bool init_plugin(void *self) {
    panda_cb pcb;
    const char *filename;

    panda_arg_list *args = panda_get_args("ktracer");
    filename = panda_parse_string(args, "filename", "/tmp/log");
    output = fopen(filename, "w");
    if (!output) return false;

    panda_do_flush_tb();
    panda_enable_precise_pc();
    panda_disable_tb_chaining();

    pcb.before_block_exec = before_block_exec;
    panda_register_callback(self, PANDA_CB_BEFORE_BLOCK_EXEC, pcb);

    return true;
}

void uninit_plugin(void *self) {
    fclose(output);
    cs_close(&handle);
}

