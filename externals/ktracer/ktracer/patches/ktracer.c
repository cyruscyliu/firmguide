/*
 * ktracer code
 * Used for recording what instrcutions has been executed in qemu
 */

#include "ktracer.h"


#if defined(TARGET_ARM)
/*

*/
typedef struct TraceContextUnit {
	uint32_t block_addr;
	uint32_t insn_start;
	uint32_t insn_end;
	uint32_t regs[18];
} TraceContextUnit;
#elif defined(TARGET_MIPS)
/*
    zero       at       v0       v1       a0       a1       a2       a3
00000000 00000001 00000000 00000000 803b21d4 0000082c 00000000 00000000
      t0       t1       t2       t3       t4       t5       t6       t7
29303030 73656974 30783020 30303030 00000000 00000001 00000000 00000000
      s0       s1       s2       s3       s4       s5       s6       s7
803b21a8 803b22fc 00000080 00000000 00000000 00000000 00000000 00000000
      t8       t9       k0       k1       gp       sp       s8       ra
00000000 0009e31c 00000000 00000000 8035e000 8035fe08 00000000 801def34
      sr       lo       hi      bad    cause       pc
11000000 00000000 00000000 00000000 00800000 801db6b0
     fsr      fir
00000000 00739300
*/

typedef struct TraceContextUnit {
	uint32_t block_addr;
	uint32_t insn_start;
	uint32_t insn_end;
	uint32_t regs[40];
} TraceContextUnit;
#endif


typedef struct TraceExecUnit {
	//uint32_t block_idx;
	//uint32_t insn_addr;
	uint32_t insn_raw;
} TraceExecUnit;


static FILE *ctx_file = NULL;
static FILE *exec_file = NULL;
static TraceContextUnit *ctx_unit = NULL;
static TraceExecUnit *exec_units = NULL;
static uint8_t *block_raw = NULL;
static uint32_t block_idx = 0;
static uint32_t insn_idx = 0;


static inline int panda_physical_memory_rw(hwaddr addr, uint8_t *buf, int len,
                                           bool is_write)
{
    hwaddr l = len;
    hwaddr addr1;
    MemoryRegion *mr = address_space_translate(&address_space_memory, addr,
                                               &addr1, &l, is_write, MEMTXATTRS_UNSPECIFIED);

    if (!memory_access_is_direct(mr, is_write)) {
        // fail for MMIO regions of physical address space
        return MEMTX_ERROR;
    }
    void *ram_ptr = qemu_map_ram_ptr(mr->ram_block, addr1);

    if (is_write) {
        memcpy(ram_ptr, buf, len);
    } else {
        memcpy(buf, ram_ptr, len);
    }
    return MEMTX_OK;
}

static inline int panda_virtual_memory_rw(CPUState *env, target_ulong addr,
                                          uint8_t *buf, int len, bool is_write)
{
    int l;
    int ret;
    hwaddr phys_addr;
    target_ulong page;

    while (len > 0) {
        page = addr & TARGET_PAGE_MASK;
        phys_addr = cpu_get_phys_page_debug(env, page);
        if (phys_addr == -1) {
            // no physical page mapped
            return -1;
        }
        l = (page + TARGET_PAGE_SIZE) - addr;
        if (l > len) {
            l = len;
        }
        phys_addr += (addr & ~TARGET_PAGE_MASK);
        ret = panda_physical_memory_rw(phys_addr, buf, l, is_write);
        if (ret != MEMTX_OK) {
            return ret;
        }
        len -= l;
        buf += l;
        addr += l;
    }
    return 0;
}

static inline int prepare_global(void)
{
    if (!ctx_file) 
	    ctx_file = fopen("/tmp/context.trace", "w");

    if (!exec_file) 
	    exec_file = fopen("/tmp/execution.trace", "w");

    if (!ctx_unit) 
	    ctx_unit = (TraceContextUnit *)malloc(sizeof(TraceContextUnit));

    if (!exec_units) 
	    exec_units = (TraceExecUnit *)malloc(1024 * sizeof(TraceExecUnit));

    if (!block_raw)
	    block_raw = (uint8_t *)malloc(1024);

    if (!ctx_file || !exec_file || !ctx_unit || !exec_units || !block_raw) 
        return -1;

    return 0;
}

static inline int record_the_trace(CPUState *cs, TranslationBlock *tb)
{
    uint32_t i, step;
    CPUArchState *env;

    env = (CPUArchState *) cs->env_ptr;
    // determine the instruction size
#if defined(TARGET_ARM)
    step = env->thumb ? 2 : 4;
#elif defined(TARGET_MIPS)
    step = 4;
#endif

    if (tb->size % step != 0)
        return -1;

    if (panda_virtual_memory_rw(cs, tb->pc, block_raw, tb->size, false)) 
        return -1;

    // block context trace
#if defined(TARGET_ARM)
    for (i = 0; i < 16; i++) {
	    ctx_unit->regs[i] = env->regs[i];
    }
    ctx_unit->regs[16] = cpsr_read(env);
    ctx_unit->regs[17] = xpsr_read(env);
    ctx_unit->block_addr = tb->pc;
    ctx_unit->insn_start = insn_idx;
    ctx_unit->insn_end = insn_idx + tb->size/step;
#elif defined(TARGET_MIPS)
    for (i = 0; i < 32; i++) {
	    ctx_unit->regs[i] = env->active_tc.gpr[i];
    }
    ctx_unit->regs[32] = env->CP0_Status;
    ctx_unit->regs[33] = env->active_tc.LO[0];
    ctx_unit->regs[34] = env->active_tc.HI[0];
    ctx_unit->regs[35] = env->CP0_BadVAddr;
    ctx_unit->regs[36] = env->CP0_Cause;
    ctx_unit->regs[37] = env->active_tc.PC | !!(env->hflags & MIPS_HFLAG_M16);
    ctx_unit->regs[38] = env->active_fpu.fcr31;
    ctx_unit->regs[39] = env->active_fpu.fcr0;
    ctx_unit->block_addr = tb->pc;
    ctx_unit->insn_start = insn_idx;
    ctx_unit->insn_end = insn_idx + tb->size/step;
#endif

    // exec insn trace
    for (i = 0; i < tb->size/step; i++) {
	    //exec_units[i].block_idx = block_idx;
	    //exec_units[i].insn_addr = (uint32_t)tb->pc + i * step;
	    if (step == 2)
	    	exec_units[i].insn_raw = (uint32_t)(*((uint16_t *)(&block_raw[i * step])));
	    else
	    	exec_units[i].insn_raw = *((uint32_t *)(&block_raw[i * step]));
    }

    // increment of the counter
    block_idx++;
    insn_idx += tb->size/step;

    // dump to file and flush
    fwrite(ctx_unit, sizeof(TraceContextUnit), 1, ctx_file);
    fwrite(exec_units, sizeof(TraceExecUnit), i, exec_file);
	fflush(ctx_file);
	fflush(exec_file);

    return 0;
}

int before_block_exec(CPUState *cs, TranslationBlock *tb)
{
    if (prepare_global())
        exit(-1);

    if (record_the_trace(cs, tb))
        exit(-1);

    return 0;
}

