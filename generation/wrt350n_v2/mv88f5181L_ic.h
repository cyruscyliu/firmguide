/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_IC_H
#define MV88F5181L_IC_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_IC "mv88f5181L_ic"
#define MV88F5181L_IC(obj) \
    OBJECT_CHECK(MV88F5181LICState, (obj), TYPE_MV88F5181L_IC)

#define MV88F5181L_IC_IRQ "irq"
#define MV88F5181L_IC_N_IRQS "32"

#define MAIN_INTERRUPT_CAUSE_REGISTER         0x00
#define MAIN_IRQ_INTERRUPT_MASK_REGISTER      0x04
#define MAIN_FIQ_INTERRUPT_MASK_REGISTER      0x08
#define MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER 0x0C

#define MV88F5181L_IC_RAM_SIZE 0x100

typedef struct MV88F5181LICState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the cpu */
    qemu_irq irq;
    qemu_irq fiq;

    /* 32 IRQs */
    uint32_t irq_level_0;
    uint32_t irq_enable_0;
    uint32_t fiq_enable_0;
} MV88F5181LICState;

static void mv88f5181L_ic_set_irq(void *opaque, int irq, int level);
static void mv88f5181L_ic_update(MV88F5181LICState *s);
static void mv88f5181L_ic_reset(DeviceState *d);

static uint64_t mv88f5181L_ic_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_ic_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_ic_init(Object *obj);
static void mv88f5181L_ic_class_init(ObjectClass *kclass, void *data);
static void mv88f5181L_ic_register_types(void);

#endif /* MV88F5181L_IC_H */