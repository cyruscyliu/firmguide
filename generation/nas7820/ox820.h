/* 
 * automatically generated, don't change
 */

#ifndef OX820_H
#define OX820_H

#include "hw/arm/arm.h"
#include "hw/sysbus.h"
#include "hw/cpu/arm11mpcore.h"

#define TYPE_OX820 "ox820"
#define OX820(obj) \
    OBJECT_CHECK(OX820State, (obj), TYPE_OX820)

#define GPIO_RESERVED 0x0 ... 0x100
#define PCIE_RESERVED 0x0 ... 0x500000
#define SATA_RESERVED 0x0 ... 0x100000
#define GMAC_RESERVED 0x0 ... 0x2000
#define EHCI_RESERVED 0x0 ... 0xf00
#define PLL_RESERVED 0x0 ... 0x10
#define RESET_RESERVED 0x0 ... 0x8
#define RPS_TIMER_RESERVED 0x0 ... 0x40
#define RPS_RESERVED 0x0 ... 0x14

#define OXMAS782X_GPIO_MMIO_SIZE 0x200000
#define OXMAS782X_GPIO_MMIO_BASE 0x44000000
#define NAS782X_PCIE_MMIO_SIZE 0x500000
#define NAS782X_PCIE_MMIO_BASE 0x47C00000
#define NAS782X_SATA_MMIO_SIZE 0x100000
#define NAS782X_SATA_MMIO_BASE 0x45900000
#define NAS782X_GMAC_MMIO_SIZE 0x2000
#define NAS782X_GMAC_MMIO_BASE 0x40400000
#define NAS782X_EHCI_MMIO_SIZE 0xf00
#define NAS782X_EHCI_MMIO_BASE 0x40200100
#define NAS782X_PLL_MMIO_SIZE 0x10
#define NAS782X_PLL_MMIO_BASE 0x44e001f0
#define NAS782X_RESET_MMIO_SIZE 0x8
#define NAS782X_RESET_MMIO_BASE 0x44e00034
#define NAS782X_RPS_TIMER_MMIO_SIZE 0x40
#define NAS782X_RPS_TIMER_MMIO_BASE 0x44400200
#define NAS782X_RPS_MMIO_SIZE 0x14
#define NAS782X_RPS_MMIO_BASE 0x44400000

#define NS16550A_MMIO_SIZE 0x100
#define NS16550A_MMIO_BASE 0x44200000

typedef struct OX820State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion oxmas782x_gpio_mmio;
    uint32_t gpio_reserved;
    MemoryRegion nas782x_pcie_mmio;
    uint32_t pcie_reserved;
    MemoryRegion nas782x_sata_mmio;
    uint32_t sata_reserved;
    MemoryRegion nas782x_gmac_mmio;
    uint32_t gmac_reserved;
    MemoryRegion nas782x_ehci_mmio;
    uint32_t ehci_reserved;
    MemoryRegion nas782x_pll_mmio;
    uint32_t pll_reserved;
    MemoryRegion nas782x_reset_mmio;
    uint32_t reset_reserved;
    MemoryRegion nas782x_rps_timer_mmio;
    uint32_t rps_timer_reserved;
    MemoryRegion nas782x_rps_mmio;
    uint32_t rps_reserved;
    
    ARM11MPCorePriveState cpu_pp;
} OX820State;

#endif /* OX820_H */