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

#define GPIOA_0_RESERVED 0x0 ... 0x100
#define GPIOA_1_RESERVED 0x0 ... 0x200
#define GPIOB_0_RESERVED 0x0 ... 0x100
#define GPIOB_1_RESERVED 0x0 ... 0x200
#define PCIE0_CFG_RESERVED 0x0 ... 0x1000
#define PCIE0_IT_RESERVED 0x0 ... 0x100
#define PCIE0_PHY_RESERVED 0x0 ... 0x10
#define PCIE1_CFG_RESERVED 0x0 ... 0x1000
#define PCIE1_IT_RESERVED 0x0 ... 0x100
#define PCIE1_PHY_RESERVED 0x0 ... 0x10
#define SATA_PORTS_RESERVED 0x0 ... 0x20000
#define SATA_DMACTL_RESERVED 0x0 ... 0x40
#define SATA_SGDMA_RESERVED 0x0 ... 0x20
#define SATA_CORE_RESERVED 0x0 ... 0x2000
#define SATA_PYH_RESERVED 0x0 ... 0xC
#define SATA_DESCRIPTORS_RESERVED 0x0 ... 0x1000
#define GMAC_RESERVED 0x0 ... 0x2000
#define EHCI_RESERVED 0x0 ... 0xf00
#define PLLA_CTRL_0 0x0
#define PLLA_CTRL_1 0x4
#define PLLA_RESERVED 0x8 ... 0x10
#define PLLB_RESERVED 0x0 ... 0x10
#define RESET_RESERVED 0x0 ... 0x8
#define RPS_TIMER_RESERVED 0x0 ... 0x40
#define RPS_RESERVED 0x0 ... 0x14
#define NAND_RESEVERD 0x0 ... 0x20

#define OXMAS782X_GPIOA_0_MMIO_SIZE 0x100
#define OXMAS782X_GPIOA_0_MMIO_BASE 0x44000000
#define OXMAS782X_GPIOA_1_MMIO_SIZE 0x200
#define OXMAS782X_GPIOA_1_MMIO_BASE 0x44E00000
#define OXMAS782X_GPIOB_0_MMIO_SIZE 0x100
#define OXMAS782X_GPIOB_0_MMIO_BASE 0x44100000
#define OXMAS782X_GPIOB_1_MMIO_SIZE 0x200
#define OXMAS782X_GPIOB_1_MMIO_BASE 0x44F00000
#define NAS782X_PCIE0_CFG_MMIO_SIZE 0x1000
#define NAS782X_PCIE0_CFG_MMIO_BASE 0x47C00000
#define NAS782X_PCIE0_IT_MMIO_SIZE 0x100
#define NAS782X_PCIE0_IT_MMIO_BASE 0x47D00000
#define NAS782X_PCIE0_PHY_MMIO_SIZE 0x10
#define NAS782X_PCIE0_PHY_MMIO_BASE 0x47A00000
#define NAS782X_PCIE1_CFG_MMIO_SIZE 0x1000
#define NAS782X_PCIE1_CFG_MMIO_BASE 0x47E00000
#define NAS782X_PCIE1_IT_MMIO_SIZE 0x100
#define NAS782X_PCIE1_IT_MMIO_BASE 0x47F00000
#define NAS782X_PCIE1_PHY_MMIO_SIZE 0x10
#define NAS782X_PCIE1_PHY_MMIO_BASE 0x44A00000
#define NAS782X_SATA_PORTS_MMIO_SIZE 0x20000
#define NAS782X_SATA_PORTS_MMIO_BASE 0x45900000
#define NAS782X_SATA_DMACTL_MMIO_SIZE 0x40
#define NAS782X_SATA_DMACTL_MMIO_BASE 0x459A0000
#define NAS782X_SATA_SGDMA_MMIO_SIZE 0x20
#define NAS782X_SATA_SGDMA_MMIO_BASE 0x459B0000
#define NAS782X_SATA_CORE_MMIO_SIZE 0x2000
#define NAS782X_SATA_CORE_MMIO_BASE 0x459E0000
#define NAS782X_SATA_PYH_MMIO_SIZE 0xC
#define NAS782X_SATA_PYH_MMIO_BASE 0x44900000
#define NAS782X_SATA_DESCRIPTORS_MMIO_SIZE 0x1000
#define NAS782X_SATA_DESCRIPTORS_MMIO_BASE 0x50000000
#define NAS782X_GMAC_MMIO_SIZE 0x2000
#define NAS782X_GMAC_MMIO_BASE 0x40400000
#define NAS782X_EHCI_MMIO_SIZE 0xf00
#define NAS782X_EHCI_MMIO_BASE 0x40200100
#define NAS782X_PLLA_MMIO_SIZE 0x10
#define NAS782X_PLLA_MMIO_BASE 0x44e001f0
#define NAS782X_PLLB_MMIO_SIZE 0x10
#define NAS782X_PLLB_MMIO_BASE 0x44f001f0
#define NAS782X_RESET_MMIO_SIZE 0x8
#define NAS782X_RESET_MMIO_BASE 0x44e00034
#define NAS782X_RPS_TIMER_MMIO_SIZE 0x40
#define NAS782X_RPS_TIMER_MMIO_BASE 0x44400200
#define NAS782X_RPS_MMIO_SIZE 0x14
#define NAS782X_RPS_MMIO_BASE 0x44400000
#define NAS782X_NAND_MMIO_SIZE 0x20
#define NAS782X_NAND_MMIO_BASE 0x41C00000

typedef struct OX820State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    const char *cpu_type;
    ARMCPU *cpu;
    qemu_irq irq, fiq;

    MemoryRegion oxmas782x_gpioa_0_mmio;
    uint32_t gpioa_0_reserved;
    MemoryRegion oxmas782x_gpioa_1_mmio;
    uint32_t gpioa_1_reserved;
    MemoryRegion oxmas782x_gpiob_0_mmio;
    uint32_t gpiob_0_reserved;
    MemoryRegion oxmas782x_gpiob_1_mmio;
    uint32_t gpiob_1_reserved;
    MemoryRegion nas782x_pcie0_cfg_mmio;
    uint32_t pcie0_cfg_reserved;
    MemoryRegion nas782x_pcie0_it_mmio;
    uint32_t pcie0_it_reserved;
    MemoryRegion nas782x_pcie0_phy_mmio;
    uint32_t pcie0_phy_reserved;
    MemoryRegion nas782x_pcie1_cfg_mmio;
    uint32_t pcie1_cfg_reserved;
    MemoryRegion nas782x_pcie1_it_mmio;
    uint32_t pcie1_it_reserved;
    MemoryRegion nas782x_pcie1_phy_mmio;
    uint32_t pcie1_phy_reserved;
    MemoryRegion nas782x_sata_ports_mmio;
    uint32_t sata_ports_reserved;
    MemoryRegion nas782x_sata_dmactl_mmio;
    uint32_t sata_dmactl_reserved;
    MemoryRegion nas782x_sata_sgdma_mmio;
    uint32_t sata_sgdma_reserved;
    MemoryRegion nas782x_sata_core_mmio;
    uint32_t sata_core_reserved;
    MemoryRegion nas782x_sata_pyh_mmio;
    uint32_t sata_pyh_reserved;
    MemoryRegion nas782x_sata_descriptors_mmio;
    uint32_t sata_descriptors_reserved;
    MemoryRegion nas782x_gmac_mmio;
    uint32_t gmac_reserved;
    MemoryRegion nas782x_ehci_mmio;
    uint32_t ehci_reserved;
    MemoryRegion nas782x_plla_mmio;
    uint32_t plla_ctrl_0;
    uint32_t plla_ctrl_1;
    uint32_t plla_reserved;
    MemoryRegion nas782x_pllb_mmio;
    uint32_t pllb_reserved;
    MemoryRegion nas782x_reset_mmio;
    uint32_t reset_reserved;
    MemoryRegion nas782x_rps_timer_mmio;
    uint32_t rps_timer_reserved;
    MemoryRegion nas782x_rps_mmio;
    uint32_t rps_reserved;
    MemoryRegion nas782x_nand_mmio;
    uint32_t nand_reseverd;
    
    ARM11MPCorePriveState cpu_pp;
} OX820State;

#endif /* OX820_H */