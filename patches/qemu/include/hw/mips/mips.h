#ifndef HW_MIPS_H
#define HW_MIPS_H
/* Definitions for mips board emulation.  */

/* Kernels can be configured with 64KB pages */
/* Considering BSS we enlarge the page align to 1MB */
#define INITRD_PAGE_MASK (~((1 << 20) - 1))

#include "exec/memory.h"
#include "target/mips/cpu-qom.h"
#include "hw/irq.h"
#include "qemu/notify.h"

/* gt64xxx.c */
PCIBus *gt64120_register(qemu_irq *pic);

/* bonito.c */
PCIBus *bonito_init(qemu_irq *pic);

/* rc4030.c */
typedef struct rc4030DMAState *rc4030_dma;
void rc4030_dma_read(void *dma, uint8_t *buf, int len);
void rc4030_dma_write(void *dma, uint8_t *buf, int len);

DeviceState *rc4030_init(rc4030_dma **dmas, IOMMUMemoryRegion **dma_mr);

struct mips_boot_info {
    int board_id;
    uint64_t ram_size;
    const char *kernel_filename;
    const char *kernel_cmdline;
    const char *initrd_filename;
};

typedef struct CommonResetData {
    MIPSCPU *cpu;
    uint64_t vector;
} CommonResetData;


void mips_load_kernel(MIPSCPU *cpu, struct mips_boot_info *info);

#endif
