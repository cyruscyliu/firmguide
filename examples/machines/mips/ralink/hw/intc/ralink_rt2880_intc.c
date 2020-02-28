/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/intc/ralink_rt2880_intc.h"

static bool set_ralink_rt2880_intc_irqn_to_regs(void *opaque, int irqn)
{
    RALINK_RT2880_INTCState *s = opaque;
    switch(irqn) { 
        case 5:
            s->r0 |= 0x00000020;
            break;
        case 12:
            s->r0 |= 0x00001000;
            break;
    }
    return true;
}

static bool clear_ralink_rt2880_intc_irqn_to_regs(void *opaque, int irqn)
{
    RALINK_RT2880_INTCState *s = opaque;
    switch(irqn) { 
        case 5:
            s->r0 &= ~0x00000020;
            break;
        case 12:
            s->r0 &= ~0x00001000;
            break;
    }
    return true;
}

static void ralink_rt2880_intc_update(void *opaque)
{
    RALINK_RT2880_INTCState *s = opaque;
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
    for (i = 0; i < 32; i++) {
        switch(s->state[i]) {
            case STATE_REST:
                if (s->pending[i]) {
                    s->state[i] = STATE_NOISE;
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_ralink_rt2880_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                }
                break;
            case STATE_NOISE:
                if (s->pending[i]) {
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_ralink_rt2880_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_ralink_rt2880_intc_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
            case STATE_ALARM:
                if (s->pending[i]) {
                    if (s->masked[i]) {
                        clear_ralink_rt2880_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 0);
                        s->state[i] = STATE_NOISE;
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_ralink_rt2880_intc_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
        }
    }
}

static uint64_t ralink_rt2880_intc_read(void *opaque, hwaddr offset, unsigned size)
{
    RALINK_RT2880_INTCState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
        default:
            return 0;
        case 0x00:
            res = s->r0;
            break;
        case 0x34:
            res = s->r1;
            break;
        case 0x38:
            res = s->r2;
            break;
    }
    return res;
}

static void ralink_rt2880_intc_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    RALINK_RT2880_INTCState *s = opaque;
    uint64_t irqn;
    uint32_t old;

    switch (offset) {
        default:
            return;
        case 0x00:
            old = (uint32_t)s->r0;
            s->r0= val;
            break;
        case 0x34:
            old = (uint32_t)s->r1;
            for (irqn = 0; irqn < 32; irqn++)
                if ((1 << irqn) == (uint32_t)val) {
                    s->masked[irqn] = false;
                }
            s->r1= val;
            break;
        case 0x38:
            old = (uint32_t)s->r2;
            for (irqn = 0; irqn < 32; irqn++)
                if ((1 << irqn) == (uint32_t)val) {
                    s->masked[irqn] = true;
                    s->pending[irqn] = false;
                }
            for (irqn = 0; irqn < 32; irqn++)
                if ((1 << irqn) == (uint32_t)val) {
                    s->masked[irqn] = true;
                }
            s->r2= val;
            break;
    }
    ralink_rt2880_intc_update(s);
}

static const MemoryRegionOps ralink_rt2880_intc_ops = {
    .read = ralink_rt2880_intc_read,
    .write = ralink_rt2880_intc_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void ralink_rt2880_intc_set_irq(void *opaque, int irq, int level)
{
    RALINK_RT2880_INTCState *s = opaque;

    if (level)
        s->pending[irq] = true;
    else
        s->pending[irq] = false;

    ralink_rt2880_intc_update(s);
}

static void ralink_rt2880_intc_init(Object *obj)
{
    RALINK_RT2880_INTCState *s = RALINK_RT2880_INTC(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &ralink_rt2880_intc_ops, s, TYPE_RALINK_RT2880_INTC, 0x100);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out(DEVICE(s), &s->irq, 1);
    qdev_init_gpio_in(DEVICE(s), ralink_rt2880_intc_set_irq, 32);
}

static void ralink_rt2880_intc_reset(DeviceState *dev)
{
    int irqn;
    RALINK_RT2880_INTCState *s = RALINK_RT2880_INTC(dev);
    s->r0 = 0;
    s->r1 = 0;
    s->r2 = 0;

    for (irqn = 0; irqn < 32; irqn++)
        s->masked[irqn] = true;
}

static void ralink_rt2880_intc_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = ralink_rt2880_intc_reset;
}

static TypeInfo ralink_rt2880_intc_type_info = {
    .name = TYPE_RALINK_RT2880_INTC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(RALINK_RT2880_INTCState),
    .instance_init = ralink_rt2880_intc_init,
    .class_init = ralink_rt2880_intc_class_init,
};

static void ralink_rt2880_intc_register_types(void)
{
    type_register_static(&ralink_rt2880_intc_type_info);
}

type_init(ralink_rt2880_intc_register_types)

