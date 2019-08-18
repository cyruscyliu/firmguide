/* 
 * automatically generated, don't change
 */

#ifndef OX820_H
#define OX820_H

#include "hw/arm/arm.h"

#define TYPE_OX820 "ox820"
#define OX820(obj) \
    OBJECT_CHECK(OX820State, (obj), TYPE_OX820)

#define GPIO_RESERVED 0x0...0x100
#define PCIE_RESERVED 0x0...0x500000
#define SATA_RESERVED 0x0...0x100000
#define EHCI_RESERVED 0x0...0xf00
#define GMAC_RESERVED 0x0...0x2000

#define OX820_GPIO_MMIO_SIZE 0x100
#define OX820_GPIO_MMIO_BASE 0xf1010100
#define OX820_PCIE_INTERFACE_MMIO_SIZE 0x500000
#define OX820_PCIE_INTERFACE_MMIO_BASE 0x47C00000
#define OX820_SATA_MMIO_SIZE 0x100000
#define OX820_SATA_MMIO_BASE 0x45900000
#define OX820_EHCI_MMIO_SIZE 0xf00
#define OX820_EHCI_MMIO_BASE 0x40200100
#define OX820_GMAC_MMIO_SIZE 0x2000
#define OX820_GMAC_MMIO_BASE 0x40400000

#define OX820_UART_MMIO_SIZE 0x100
#define OX820_UART_MMIO_BASE 0x44200000

typedef struct OX820State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion ox820_gpio_mmio;
    uint32_t gpio_reserved;
    MemoryRegion ox820_pcie_interface_mmio;
    uint32_t pcie_reserved;
    MemoryRegion ox820_sata_mmio;
    uint32_t sata_reserved;
    MemoryRegion ox820_ehci_mmio;
    uint32_t ehci_reserved;
    MemoryRegion ox820_gmac_mmio;
    uint32_t gmac_reserved;
    
    ARM11MPCorePriveState cpu_pp;
} OX820State;

#endif /* OX820_H */