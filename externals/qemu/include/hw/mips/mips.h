#ifndef HW_MIPS_H
#define HW_MIPS_H
/* Definitions for mips board emulation.  */

/* Kernels can be configured with 64KB pages */
/* Considering BSS we enlarge the page align to 8MB */
#define INITRD_PAGE_MASK (~((1 << 23) - 1))
#define DTB_PAGE_MASK (~((1 << 12) -1))

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
    const char *dtb_filename;
    hwaddr dtb_start;
    hwaddr dtb_offset;
    hwaddr dtb_limit;
    int is_linux;
    hwaddr initrd_start;
    hwaddr initrd_size;
    hwaddr entry;
};

typedef struct CommonResetData {
    MIPSCPU *cpu;
    uint64_t vector;
} CommonResetData;

int mips_load_dtb(hwaddr addr, struct mips_boot_info *binfo,
                  hwaddr addr_limit, AddressSpace *as);
void mips_load_kernel(MIPSCPU *cpu, struct mips_boot_info *info);

#endif
