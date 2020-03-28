/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/intc/marvell_orion_intc.h"

static bool set_marvell_orion_intc_irqn_to_regs(void *opaque, int irqn)
{
    MARVELL_ORION_INTCState *s = opaque;
    switch(irqn) { 
        case 0:
            s->r0 |= 0x00000001;
            break;
        case 1:
            s->r0 |= 0x00000002;
            break;
        case 3:
            s->r0 |= 0x00000008;
            break;
        case 4:
            s->r0 |= 0x00000010;
            break;
    }
    return true;
}

static bool clear_marvell_orion_intc_irqn_to_regs(void *opaque, int irqn)
{
    MARVELL_ORION_INTCState *s = opaque;
    switch(irqn) { 
        case 0:
            s->r0 &= ~0x00000001;
            break;
        case 1:
            s->r0 &= ~0x00000002;
            break;
        case 3:
            s->r0 &= ~0x00000008;
            break;
        case 4:
            s->r0 &= ~0x00000010;
            break;
    }
    return true;
}

static void marvell_orion_intc_update(void *opaque)
{
    MARVELL_ORION_INTCState *s = opaque;
    int i;

    // state transition table
    // state_from pending masked state_to
    //    REST       0      0     REST
    //    REST       0      1     REST
    //    REST       1      0     NOISE
    //    REST       1      1     NOISE
    //    NOISE      0      0     REST
    //    NOISE      0      1     REST
    //    NOISE      1      0     ALARM(*)
    //    NOISE      1      1     NOISE
    //    ALARM      0      0     REST(*)
    //    ALARM      0      1     REST(*)
    //    ALARM      1      0     ALARM(*)
    //    ALARM      1      1     NOISE(*)
    for (i = 0; i < N_IRQ; i++) {
        switch(s->state[i]) {
            case STATE_REST:
                if (s->pending[i]) {
                    s->state[i] = STATE_NOISE;
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_marvell_orion_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                }
                break;
            case STATE_NOISE:
                if (s->pending[i]) {
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_marvell_orion_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_marvell_orion_intc_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
            case STATE_ALARM:
                if (s->pending[i]) {
                    if (s->masked[i]) {
                        clear_marvell_orion_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 0);
                        s->state[i] = STATE_NOISE;
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_marvell_orion_intc_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
        }
    }
}

static uint64_t marvell_orion_intc_read(void *opaque, hwaddr offset, unsigned size)
{
    MARVELL_ORION_INTCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0x00:
            res = s->r0;
            break;
        case 0x04:
            res = s->r1;
            break;
    }
    return res;
}

static void marvell_orion_intc_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    MARVELL_ORION_INTCState *s = opaque;
    uint64_t irqn;
    uint32_t old;

    switch (offset) {
        default:
            return;
        case 0x00:
            old = (uint32_t)s->r0;
            s->r0= val;
            break;
        case 0x04:
            old = (uint32_t)s->r1;
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ((old & (~(1 << (irqn % 32)))) == (uint32_t)val) {
                    s->masked[irqn] = true;
                }
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ((old | ((1 << (irqn % 32)))) == (uint32_t)val) {
                    s->masked[irqn] = false;
                }
            s->r1= val;
            break;
    }
    marvell_orion_intc_update(s);
}

static const MemoryRegionOps marvell_orion_intc_ops = {
    .read = marvell_orion_intc_read,
    .write = marvell_orion_intc_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void marvell_orion_intc_set_irq(void *opaque, int irq, int level)
{
    MARVELL_ORION_INTCState *s = opaque;

    if (level)
        s->pending[irq] = true;
    else
        s->pending[irq] = false;

    marvell_orion_intc_update(s);
}

static void marvell_orion_intc_init(Object *obj)
{
    MARVELL_ORION_INTCState *s = MARVELL_ORION_INTC(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &marvell_orion_intc_ops, s, TYPE_MARVELL_ORION_INTC, 0x10);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out(DEVICE(s), &s->irq, 1);
    qdev_init_gpio_in(DEVICE(s), marvell_orion_intc_set_irq, N_IRQ);
}

static void marvell_orion_intc_reset(DeviceState *dev)
{
    int irqn;
    MARVELL_ORION_INTCState *s = MARVELL_ORION_INTC(dev);
    s->r0 = 0;
    s->r1 = 0;

    for (irqn = 0; irqn < N_IRQ; irqn++)
        s->masked[irqn] = true;
}

static void marvell_orion_intc_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = marvell_orion_intc_reset;
}

static TypeInfo marvell_orion_intc_type_info = {
    .name = TYPE_MARVELL_ORION_INTC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MARVELL_ORION_INTCState),
    .instance_init = marvell_orion_intc_init,
    .class_init = marvell_orion_intc_class_init,
};

static void marvell_orion_intc_register_types(void)
{
    type_register_static(&marvell_orion_intc_type_info);
}

type_init(marvell_orion_intc_register_types)

