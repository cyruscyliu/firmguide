# 1 "arch/arm/mm/proc-feroceon.S"
# 1 "/root/openwrt-build-docker/share/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8//"
# 1 "<built-in>"
# 1 "<command-line>"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/include/linux/kconfig.h" 1



# 1 "include/generated/autoconf.h" 1
# 5 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/include/linux/kconfig.h" 2
# 1 "<command-line>" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/unified.h" 1
# 64 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/unified.h"
 .macro it, cond
 .endm
 .macro itt, cond
 .endm
 .macro ite, cond
 .endm
 .macro ittt, cond
 .endm
 .macro itte, cond
 .endm
 .macro itet, cond
 .endm
 .macro itee, cond
 .endm
 .macro itttt, cond
 .endm
 .macro ittte, cond
 .endm
 .macro ittet, cond
 .endm
 .macro ittee, cond
 .endm
 .macro itett, cond
 .endm
 .macro itete, cond
 .endm
 .macro iteet, cond
 .endm
 .macro iteee, cond
 .endm
# 1 "<command-line>" 2
# 1 "arch/arm/mm/proc-feroceon.S"
# 22 "arch/arm/mm/proc-feroceon.S"
# 1 "include/linux/linkage.h" 1



# 1 "include/linux/compiler.h" 1
# 5 "include/linux/linkage.h" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/linkage.h" 1
# 6 "include/linux/linkage.h" 2
# 23 "arch/arm/mm/proc-feroceon.S" 2
# 1 "include/linux/init.h" 1




# 1 "include/linux/types.h" 1



# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/types.h" 1



# 1 "include/asm-generic/int-ll64.h" 1
# 11 "include/asm-generic/int-ll64.h"
# 1 "arch/arm/include/generated/asm/bitsperlong.h" 1
# 1 "include/asm-generic/bitsperlong.h" 1
# 1 "arch/arm/include/generated/asm/bitsperlong.h" 2
# 12 "include/asm-generic/int-ll64.h" 2
# 5 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/types.h" 2
# 5 "include/linux/types.h" 2
# 6 "include/linux/init.h" 2
# 24 "arch/arm/mm/proc-feroceon.S" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h" 1
# 23 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/ptrace.h" 1
# 13 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/ptrace.h"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/hwcap.h" 1
# 14 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/ptrace.h" 2
# 24 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/domain.h" 1
# 25 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h" 2
# 89 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h"
 .macro disable_irq_notrace
 msr cpsr_c, #0x00000080 | 0x00000013
 .endm

 .macro enable_irq_notrace
 msr cpsr_c, #0x00000013
 .endm


 .macro asm_trace_hardirqs_off





 .endm

 .macro asm_trace_hardirqs_on_cond, cond
# 116 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h"
 .endm

 .macro asm_trace_hardirqs_on
 asm_trace_hardirqs_on_cond al
 .endm

 .macro disable_irq
 disable_irq_notrace
 asm_trace_hardirqs_off
 .endm

 .macro enable_irq
 asm_trace_hardirqs_on
 enable_irq_notrace
 .endm




 .macro save_and_disable_irqs, oldcpsr
 mrs \oldcpsr, cpsr
 disable_irq
 .endm

 .macro save_and_disable_irqs_notrace, oldcpsr
 mrs \oldcpsr, cpsr
 disable_irq_notrace
 .endm





 .macro restore_irqs_notrace, oldcpsr
 msr cpsr_c, \oldcpsr
 .endm

 .macro restore_irqs, oldcpsr
 tst \oldcpsr, #0x00000080
 asm_trace_hardirqs_on_cond eq
 restore_irqs_notrace \oldcpsr
 .endm
# 197 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h"
 .macro instr_sync





 .endm




 .macro smp_dmb mode
# 227 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h"
 .endm







 .macro setmode, mode, reg
 msr cpsr_c, #\mode
 .endm
# 285 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/assembler.h"
 .macro usracc, instr, reg, ptr, inc, cond, rept, abort, t=t
 .rept \rept
9999:
 .if \inc == 1
 \instr\cond\()b\()\t \reg, [\ptr], #\inc
 .elseif \inc == 4
 \instr\cond\()\t \reg, [\ptr], #\inc
 .else
 .error "Unsupported inc macro argument"
 .endif

 .pushsection __ex_table,"a"
 .align 3
 .long 9999b, \abort
 .popsection
 .endr
 .endm



 .macro strusr, reg, ptr, inc, cond=al, rept=1, abort=9001f
 usracc str, \reg, \ptr, \inc, \cond, \rept, \abort
 .endm

 .macro ldrusr, reg, ptr, inc, cond=al, rept=1, abort=9001f
 usracc ldr, \reg, \ptr, \inc, \cond, \rept, \abort
 .endm


 .macro string name:req, string
 .type \name , #object
\name:
 .asciz "\string"
 .size \name , . - \name
 .endm
# 25 "arch/arm/mm/proc-feroceon.S" 2

# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable-hwdef.h" 1
# 16 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable-hwdef.h"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable-2level-hwdef.h" 1
# 17 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable-hwdef.h" 2
# 27 "arch/arm/mm/proc-feroceon.S" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h" 1
# 13 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h"
# 1 "include/linux/const.h" 1
# 14 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/proc-fns.h" 1
# 16 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/proc-fns.h"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/glue-proc.h" 1
# 14 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/glue-proc.h"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/glue.h" 1
# 15 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/glue-proc.h" 2
# 17 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/proc-fns.h" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/page.h" 1
# 176 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/page.h"
# 1 "include/asm-generic/getorder.h" 1
# 177 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/page.h" 2
# 18 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/proc-fns.h" 2
# 15 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h" 2
# 23 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h"
# 1 "include/asm-generic/pgtable-nopud.h" 1
# 24 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/memory.h" 1
# 19 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/memory.h"
# 1 "arch/arm/include/generated/asm/sizes.h" 1
# 1 "include/asm-generic/sizes.h" 1
# 1 "arch/arm/include/generated/asm/sizes.h" 2
# 20 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/memory.h" 2
# 283 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/memory.h"
# 1 "include/asm-generic/memory_model.h" 1
# 284 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/memory.h" 2
# 25 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h" 2





# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable-2level.h" 1
# 31 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/pgtable.h" 2
# 28 "arch/arm/mm/proc-feroceon.S" 2


# 1 "arch/arm/mm/proc-macros.S" 1






# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/asm-offsets.h" 1
# 1 "include/generated/asm-offsets.h" 1
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/asm-offsets.h" 2
# 8 "arch/arm/mm/proc-macros.S" 2
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/thread_info.h" 1
# 16 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/thread_info.h"
# 1 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/fpstate.h" 1
# 17 "/root/firmware/12.09-1aabbfa34c562c1f2d2261e33e109635/archive-12.09/build_dir/linux-orion_generic/linux-3.3.8/arch/arm/include/asm/thread_info.h" 2
# 9 "arch/arm/mm/proc-macros.S" 2




 .macro vma_vm_mm, rd, rn
 ldr \rd, [\rn, #0]
 .endm




 .macro vma_vm_flags, rd, rn
 ldr \rd, [\rn, #24]
 .endm

 .macro tsk_mm, rd, rn
 ldr \rd, [\rn, #12]
 ldr \rd, [\rd, #168]
 .endm




 .macro act_mm, rd
 bic \rd, sp, #8128
 bic \rd, \rd, #63
 ldr \rd, [\rd, #12]
 ldr \rd, [\rd, #168]
 .endm




 .macro mmid, rd, rn
 ldr \rd, [\rn, #MM_CONTEXT_ID]
 .endm




 .macro asid, rd, rn
 and \rd, \rn, #255
 .endm

 .macro crval, clear, mmuset, ucset

 .word \clear
 .word \mmuset




 .endm





 .macro dcache_line_size, reg, tmp
 mrc p15, 0, \tmp, c0, c0, 1 @ read ctr
 lsr \tmp, \tmp, #16
 and \tmp, \tmp, #0xf @ cache line size encoding
 mov \reg, #4 @ bytes per word
 mov \reg, \reg, lsl \tmp @ actual cache line size
 .endm





 .macro icache_line_size, reg, tmp
 mrc p15, 0, \tmp, c0, c0, 1 @ read ctr
 and \tmp, \tmp, #0xf @ cache line size encoding
 mov \reg, #4 @ bytes per word
 mov \reg, \reg, lsl \tmp @ actual cache line size
 .endm
# 118 "arch/arm/mm/proc-macros.S"
 .macro armv6_mt_table pfx
\pfx\()_mt_table:
 .long 0x00 @ (0x00 << 2)
 .long ((1) << 6) @ (0x01 << 2)
 .long (1 << 3) @ (0x02 << 2)
 .long (1 << 3) | (1 << 2) @ (0x03 << 2)
 .long (1 << 2) @ (0x04 << 2)
 .long 0x00 @ unused
 .long 0x00 @ (0x06 << 2) (not present)
 .long ((1) << 6) | (1 << 3) | (1 << 2) @ (0x07 << 2)
 .long 0x00 @ unused
 .long ((1) << 6) @ (0x09 << 2)
 .long 0x00 @ unused
 .long (1 << 3) | (1 << 2) @ (0x0b << 2)
 .long ((2) << 6) @ (0x0c << 2)
 .long 0x00 @ unused
 .long 0x00 @ unused
 .long 0x00 @ unused
 .endm

 .macro armv6_set_pte_ext pfx
 str r1, [r0], #2048 @ 1 version

 bic r3, r1, #0x000003fc
 bic r3, r3, #(3 << 0)
 orr r3, r3, r2
 orr r3, r3, #(1 << 4) | 2

 adr ip, \pfx\()_mt_table
 and r2, r1, #(0x0f << 2)
 ldr r2, [ip, r2]

 eor r1, r1, #(1 << 6)
 tst r1, #(1 << 6)|(1 << 7)
 orrne r3, r3, #(1 << 9)

 tst r1, #(1 << 8)
 orrne r3, r3, #(2 << 4)

 @ allow kernel read/write access to read-only user pages
 tstne r3, #(1 << 9)
 bicne r3, r3, #(1 << 9) | (1 << 4)


 tst r1, #(1 << 9)
 orrne r3, r3, #(1 << 0)

 orr r3, r3, r2

 tst r1, #(1 << 1)
 tstne r1, #(1 << 0)
 moveq r3, #0

 str r3, [r0]
 mcr p15, 0, r0, c7, c10, 1 @ flush_pte
 .endm
# 190 "arch/arm/mm/proc-macros.S"
 .macro armv3_set_pte_ext wc_disable=1
 str r1, [r0], #2048 @ 1 version

 eor r3, r1, #(1 << 0) | (1 << 1) | (1 << 6)

 bic r2, r1, #(0xff << 4) @ keep C, B bits
 bic r2, r2, #(3 << 0)
 orr r2, r2, #(2 << 0)

 tst r3, #(1 << 8) @ user?
 orrne r2, r2, #(0xaa << 4)

 tst r3, #(1 << 7) | (1 << 6) @ write and dirty?
 orreq r2, r2, #(0x55 << 4)

 tst r3, #(1 << 0) | (1 << 1) @ present and young?
 movne r2, #0

 .if \wc_disable




 .endif
 str r2, [r0] @ hardware version
 .endm
# 233 "arch/arm/mm/proc-macros.S"
 .macro xscale_set_pte_ext_prologue
 str r1, [r0] @ 1 version

 eor r3, r1, #(1 << 0) | (1 << 1) | (1 << 6)

 bic r2, r1, #(0xff << 4) @ keep C, B bits
 orr r2, r2, #(3 << 0) @ extended page

 tst r3, #(1 << 8) @ user?
 orrne r2, r2, #((2 << 4)) @ yes -> user r/o, system r/w

 tst r3, #(1 << 7) | (1 << 6) @ write and dirty?
 orreq r2, r2, #((1 << 4)) @ yes -> user n/a, system r/w
      @ combined with user -> user r/w
 .endm

 .macro xscale_set_pte_ext_epilogue
 tst r3, #(1 << 0) | (1 << 1) @ present and young?
 movne r2, #0 @ no -> fault

 str r2, [r0, #2048]! @ hardware version
 mov ip, #0
 mcr p15, 0, r0, c7, c10, 1 @ clean L1 D line
 mcr p15, 0, ip, c7, c10, 4 @ data write barrier
 .endm

.macro define_processor_functions name:req, dabort:req, pabort:req, nommu=0, suspend=0
 .type \name\()_processor_functions, #object
 .align 2
.globl \name\()_processor_functions; .align 0; \name\()_processor_functions:
 .word \dabort
 .word \pabort
 .word cpu_\name\()_proc_init
 .word cpu_\name\()_proc_fin
 .word cpu_\name\()_reset
 .word cpu_\name\()_do_idle
 .word cpu_\name\()_dcache_clean_area
 .word cpu_\name\()_switch_mm

 .if \nommu
 .word 0
 .else
 .word cpu_\name\()_set_pte_ext
 .endif

 .if \suspend
 .word cpu_\name\()_suspend_size




 .word 0
 .word 0

 .else
 .word 0
 .word 0
 .word 0
 .endif

 .size \name\()_processor_functions, . - \name\()_processor_functions
.endm

.macro define_cache_functions name:req
 .align 2
 .type \name\()_cache_fns, #object
.globl \name\()_cache_fns; .align 0; \name\()_cache_fns:
 .long \name\()_flush_icache_all
 .long \name\()_flush_kern_cache_all
 .long \name\()_flush_user_cache_all
 .long \name\()_flush_user_cache_range
 .long \name\()_coherent_kern_range
 .long \name\()_coherent_user_range
 .long \name\()_flush_kern_dcache_area
 .long \name\()_dma_map_area
 .long \name\()_dma_unmap_area
 .long \name\()_dma_flush_range
 .size \name\()_cache_fns, . - \name\()_cache_fns
.endm

.macro define_tlb_functions name:req, flags_up:req, flags_smp
 .type \name\()_tlb_fns, #object
.globl \name\()_tlb_fns; .align 0; \name\()_tlb_fns:
 .long \name\()_flush_user_tlb_range
 .long \name\()_flush_kern_tlb_range
 .ifnb \flags_smp
 
  .long \flags_up
 .else
  .long \flags_up
 .endif
 .size \name\()_tlb_fns, . - \name\()_tlb_fns
.endm
# 31 "arch/arm/mm/proc-feroceon.S" 2
# 47 "arch/arm/mm/proc-feroceon.S"
 .bss
 .align 3
__cache_params_loc:
 .space 8

 .text
__cache_params:
 .word __cache_params_loc




.globl cpu_feroceon_proc_init; .align 0; cpu_feroceon_proc_init:
 mrc p15, 0, r0, c0, c0, 1 @ read cache type register
 ldr r1, __cache_params
 mov r2, #(16 << 5)
 tst r0, #(1 << 16) @ get way
 mov r0, r0, lsr #18 @ get cache size order
 movne r3, #((4 - 1) << 30) @ 4-way
 and r0, r0, #0xf
 moveq r3, #0 @ 1-way
 mov r2, r2, lsl r0 @ actual cache size
 movne r2, r2, lsr #2 @ turned into # of sets
 sub r2, r2, #(1 << 5)
 stmia r1, {r2, r3}
 mov pc, lr




.globl cpu_feroceon_proc_fin; .align 0; cpu_feroceon_proc_fin:







 mrc p15, 0, r0, c1, c0, 0 @ ctrl register
 bic r0, r0, #0x1000 @ ...i............
 bic r0, r0, #0x000e @ ............wca.
 mcr p15, 0, r0, c1, c0, 0 @ disable caches
 mov pc, lr
# 100 "arch/arm/mm/proc-feroceon.S"
 .align 5
 .pushsection .idmap.text, "ax"
.globl cpu_feroceon_reset; .align 0; cpu_feroceon_reset:
 mov ip, #0
 mcr p15, 0, ip, c7, c7, 0 @ invalidate I,D caches
 mcr p15, 0, ip, c7, c10, 4 @ drain WB

 mcr p15, 0, ip, c8, c7, 0 @ invalidate I & D TLBs

 mrc p15, 0, ip, c1, c0, 0 @ ctrl register
 bic ip, ip, #0x000f @ ............wcam
 bic ip, ip, #0x1100 @ ...i...s........
 mcr p15, 0, ip, c1, c0, 0 @ ctrl register
 mov pc, r0
.type cpu_feroceon_reset, %function; .size cpu_feroceon_reset, .-cpu_feroceon_reset
 .popsection






 .align 5
.globl cpu_feroceon_do_idle; .align 0; cpu_feroceon_do_idle:
 mov r0, #0
 mcr p15, 0, r0, c7, c10, 4 @ Drain write buffer
 mcr p15, 0, r0, c7, c0, 4 @ Wait for interrupt
 mov pc, lr






.globl feroceon_flush_icache_all; .align 0; feroceon_flush_icache_all:
 mov r0, #0
 mcr p15, 0, r0, c7, c5, 0 @ invalidate I cache
 mov pc, lr
.type feroceon_flush_icache_all, %function; .size feroceon_flush_icache_all, .-feroceon_flush_icache_all







 .align 5
.globl feroceon_flush_user_cache_all; .align 0; feroceon_flush_user_cache_all:







.globl feroceon_flush_kern_cache_all; .align 0; feroceon_flush_kern_cache_all:
 mov r2, #4

__flush_whole_cache:
 ldr r1, __cache_params
 ldmia r1, {r1, r3}
1: orr ip, r1, r3
2: mcr p15, 0, ip, c7, c14, 2 @ clean + invalidate D set/way
 subs ip, ip, #(1 << 30) @ next way
 bcs 2b
 subs r1, r1, #(1 << 5) @ next set
 bcs 1b

 tst r2, #4
 mov ip, #0
 mcrne p15, 0, ip, c7, c5, 0 @ invalidate I cache
 mcrne p15, 0, ip, c7, c10, 4 @ drain WB
 mov pc, lr
# 184 "arch/arm/mm/proc-feroceon.S"
 .align 5
.globl feroceon_flush_user_cache_range; .align 0; feroceon_flush_user_cache_range:
 sub r3, r1, r0 @ calculate total size
 cmp r3, #16384
 bgt __flush_whole_cache
1: tst r2, #4
 mcr p15, 0, r0, c7, c14, 1 @ clean and invalidate D entry
 mcrne p15, 0, r0, c7, c5, 1 @ invalidate I entry
 add r0, r0, #32
 mcr p15, 0, r0, c7, c14, 1 @ clean and invalidate D entry
 mcrne p15, 0, r0, c7, c5, 1 @ invalidate I entry
 add r0, r0, #32
 cmp r0, r1
 blo 1b
 tst r2, #4
 mov ip, #0
 mcrne p15, 0, ip, c7, c10, 4 @ drain WB
 mov pc, lr
# 213 "arch/arm/mm/proc-feroceon.S"
 .align 5
.globl feroceon_coherent_kern_range; .align 0; feroceon_coherent_kern_range:
# 227 "arch/arm/mm/proc-feroceon.S"
.globl feroceon_coherent_user_range; .align 0; feroceon_coherent_user_range:
 bic r0, r0, #32 - 1
1: mcr p15, 0, r0, c7, c10, 1 @ clean D entry
 mcr p15, 0, r0, c7, c5, 1 @ invalidate I entry
 add r0, r0, #32
 cmp r0, r1
 blo 1b
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr
# 246 "arch/arm/mm/proc-feroceon.S"
 .align 5
.globl feroceon_flush_kern_dcache_area; .align 0; feroceon_flush_kern_dcache_area:
 add r1, r0, r1
1: mcr p15, 0, r0, c7, c14, 1 @ clean+invalidate D entry
 add r0, r0, #32
 cmp r0, r1
 blo 1b
 mov r0, #0
 mcr p15, 0, r0, c7, c5, 0 @ invalidate I cache
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr

 .align 5
.globl feroceon_range_flush_kern_dcache_area; .align 0; feroceon_range_flush_kern_dcache_area:
 mrs r2, cpsr
 add r1, r0, #4096 - 32 @ top addr is inclusive
 orr r3, r2, #0x00000080
 msr cpsr_c, r3 @ disable interrupts
 mcr p15, 5, r0, c15, c15, 0 @ D clean/inv range start
 mcr p15, 5, r1, c15, c15, 1 @ D clean/inv range top
 msr cpsr_c, r2 @ restore interrupts
 mov r0, #0
 mcr p15, 0, r0, c7, c5, 0 @ invalidate I cache
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr
# 285 "arch/arm/mm/proc-feroceon.S"
 .align 5
feroceon_dma_inv_range:
 tst r0, #32 - 1
 bic r0, r0, #32 - 1
 mcrne p15, 0, r0, c7, c10, 1 @ clean D entry
 tst r1, #32 - 1
 mcrne p15, 0, r1, c7, c10, 1 @ clean D entry
1: mcr p15, 0, r0, c7, c6, 1 @ invalidate D entry
 add r0, r0, #32
 cmp r0, r1
 blo 1b
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr

 .align 5
feroceon_range_dma_inv_range:
 mrs r2, cpsr
 tst r0, #32 - 1
 mcrne p15, 0, r0, c7, c10, 1 @ clean D entry
 tst r1, #32 - 1
 mcrne p15, 0, r1, c7, c10, 1 @ clean D entry
 cmp r1, r0
 subne r1, r1, #1 @ top address is inclusive
 orr r3, r2, #0x00000080
 msr cpsr_c, r3 @ disable interrupts
 mcr p15, 5, r0, c15, c14, 0 @ D inv range start
 mcr p15, 5, r1, c15, c14, 1 @ D inv range top
 msr cpsr_c, r2 @ restore interrupts
 mov pc, lr
# 325 "arch/arm/mm/proc-feroceon.S"
 .align 5
feroceon_dma_clean_range:
 bic r0, r0, #32 - 1
1: mcr p15, 0, r0, c7, c10, 1 @ clean D entry
 add r0, r0, #32
 cmp r0, r1
 blo 1b
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr

 .align 5
feroceon_range_dma_clean_range:
 mrs r2, cpsr
 cmp r1, r0
 subne r1, r1, #1 @ top address is inclusive
 orr r3, r2, #0x00000080
 msr cpsr_c, r3 @ disable interrupts
 mcr p15, 5, r0, c15, c13, 0 @ D clean range start
 mcr p15, 5, r1, c15, c13, 1 @ D clean range top
 msr cpsr_c, r2 @ restore interrupts
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr
# 356 "arch/arm/mm/proc-feroceon.S"
 .align 5
.globl feroceon_dma_flush_range; .align 0; feroceon_dma_flush_range:
 bic r0, r0, #32 - 1
1: mcr p15, 0, r0, c7, c14, 1 @ clean+invalidate D entry
 add r0, r0, #32
 cmp r0, r1
 blo 1b
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr

 .align 5
.globl feroceon_range_dma_flush_range; .align 0; feroceon_range_dma_flush_range:
 mrs r2, cpsr
 cmp r1, r0
 subne r1, r1, #1 @ top address is inclusive
 orr r3, r2, #0x00000080
 msr cpsr_c, r3 @ disable interrupts
 mcr p15, 5, r0, c15, c15, 0 @ D clean/inv range start
 mcr p15, 5, r1, c15, c15, 1 @ D clean/inv range top
 msr cpsr_c, r2 @ restore interrupts
 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr







.globl feroceon_dma_map_area; .align 0; feroceon_dma_map_area:
 add r1, r1, r0
 cmp r2, #1
 beq feroceon_dma_clean_range
 bcs feroceon_dma_inv_range
 b feroceon_dma_flush_range
.type feroceon_dma_map_area, %function; .size feroceon_dma_map_area, .-feroceon_dma_map_area







.globl feroceon_range_dma_map_area; .align 0; feroceon_range_dma_map_area:
 add r1, r1, r0
 cmp r2, #1
 beq feroceon_range_dma_clean_range
 bcs feroceon_range_dma_inv_range
 b feroceon_range_dma_flush_range
.type feroceon_range_dma_map_area, %function; .size feroceon_range_dma_map_area, .-feroceon_range_dma_map_area







.globl feroceon_dma_unmap_area; .align 0; feroceon_dma_unmap_area:
 mov pc, lr
.type feroceon_dma_unmap_area, %function; .size feroceon_dma_unmap_area, .-feroceon_dma_unmap_area

 @ define struct cpu_cache_fns (see <asm/cacheflush.h> and proc-macros.S)
 define_cache_functions feroceon

.macro range_alias basename
 .globl feroceon_range_\basename
 .type feroceon_range_\basename , %function
 .equ feroceon_range_\basename , feroceon_\basename
.endm





 range_alias flush_icache_all
 range_alias flush_user_cache_all
 range_alias flush_kern_cache_all
 range_alias flush_user_cache_range
 range_alias coherent_kern_range
 range_alias coherent_user_range
 range_alias dma_unmap_area

 define_cache_functions feroceon_range

 .align 5
.globl cpu_feroceon_dcache_clean_area; .align 0; cpu_feroceon_dcache_clean_area:





1: mcr p15, 0, r0, c7, c10, 1 @ clean D entry
 add r0, r0, #32
 subs r1, r1, #32
 bhi 1b







 mcr p15, 0, r0, c7, c10, 4 @ drain WB
 mov pc, lr
# 470 "arch/arm/mm/proc-feroceon.S"
 .align 5
.globl cpu_feroceon_switch_mm; .align 0; cpu_feroceon_switch_mm:







 mov r2, lr @ abuse r2 to preserve lr
 bl __flush_whole_cache
 @ if r2 contains the 4 bit then the next 2 ops are done already
 tst r2, #4
 mcreq p15, 0, ip, c7, c5, 0 @ invalidate I cache
 mcreq p15, 0, ip, c7, c10, 4 @ drain WB

 mcr p15, 0, r0, c2, c0, 0 @ load page table pointer
 mcr p15, 0, ip, c8, c7, 0 @ invalidate I & D TLBs
 mov pc, r2
# 498 "arch/arm/mm/proc-feroceon.S"
 .align 5
.globl cpu_feroceon_set_pte_ext; .align 0; cpu_feroceon_set_pte_ext:

 armv3_set_pte_ext wc_disable=0
 mov r0, r0
 mcr p15, 0, r0, c7, c10, 1 @ clean D entry




 mcr p15, 0, r0, c7, c10, 4 @ drain WB

 mov pc, lr

 .section ".cpuinit.text", "ax"

 .type __feroceon_setup, #function
__feroceon_setup:
 mov r0, #0
 mcr p15, 0, r0, c7, c7 @ invalidate I,D caches on v4
 mcr p15, 0, r0, c7, c10, 4 @ drain write buffer on v4

 mcr p15, 0, r0, c8, c7 @ invalidate I,D TLBs on v4


 adr r5, feroceon_crval
 ldmia r5, {r5, r6}
 mrc p15, 0, r0, c1, c0 @ get control register v4
 bic r0, r0, r5
 orr r0, r0, r6
 mov pc, lr
 .size __feroceon_setup, . - __feroceon_setup
# 538 "arch/arm/mm/proc-feroceon.S"
 .type feroceon_crval, #object
feroceon_crval:
 crval clear=0x0000773f, mmuset=0x00003135, ucset=0x00001134

 .section ".init.data","aw",%progbits

 @ define struct processor (see <asm/proc-fns.h> and proc-macros.S)
 define_processor_functions feroceon, dabort=v5t_early_abort, pabort=legacy_pabort

 .section ".rodata"

 string cpu_arch_name, "armv5te"
 string cpu_elf_name, "v5"
 string cpu_feroceon_name, "Feroceon"
 string cpu_88fr531_name, "Feroceon 88FR531-vd"
 string cpu_88fr571_name, "Feroceon 88FR571-vd"
 string cpu_88fr131_name, "Feroceon 88FR131"

 .align

 .section ".proc.info.init", #alloc, #execinstr

.macro feroceon_proc_info name:req, cpu_val:req, cpu_mask:req, cpu_name:req, cache:req
 .type __\name\()_proc_info,#object
__\name\()_proc_info:
 .long \cpu_val
 .long \cpu_mask
 .long (2 << 0) | (1 << 2) | (1 << 3) | (1 << 4) | (1 << 10) | (1 << 11)





 .long (2 << 0) | (1 << 4) | (1 << 10) | (1 << 11)



 b __feroceon_setup
 .long cpu_arch_name
 .long cpu_elf_name
 .long (1 << 0)|(1 << 1)|(1 << 2)|(1 << 4)|(1 << 7)
 .long \cpu_name
 .long feroceon_processor_functions
 .long v4wbi_tlb_fns
 .long feroceon_user_fns
 .long \cache
  .size __\name\()_proc_info, . - __\name\()_proc_info
.endm


 feroceon_proc_info feroceon_old_id, 0x41009260, 0xff00fff0, cpu_name=cpu_feroceon_name, cache=feroceon_cache_fns



 feroceon_proc_info 88fr531, 0x56055310, 0xfffffff0, cpu_88fr531_name, cache=feroceon_cache_fns

 feroceon_proc_info 88fr571, 0x56155710, 0xfffffff0, cpu_88fr571_name, cache=feroceon_range_cache_fns

 feroceon_proc_info 88fr131, 0x56251310, 0xfffffff0, cpu_88fr131_name, cache=feroceon_range_cache_fns
