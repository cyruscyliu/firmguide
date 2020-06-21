/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/intc/qca_ar7240_misc_intc.h"

static bool set_qca_ar7240_misc_intc_irqn_to_regs(void *opaque, int irqn)
{
    QCA_AR7240_MISC_INTCState *s = opaque;
    switch(irqn) { 
        case 2:
            s->r0 |= (1 << 2);
            break;
        case 3:
            s->r0 |= (1 << 3);
            break;
        case 4:
            s->r0 |= (1 << 4);
            break;
    }
    return true;
}

static bool clear_qca_ar7240_misc_intc_irqn_to_regs(void *opaque, int irqn)
{
    QCA_AR7240_MISC_INTCState *s = opaque;
    switch(irqn) { 
        case 2:
            s->r0 &= ~(1 << 2);
            break;
        case 3:
            s->r0 &= ~(1 << 3);
            break;
        case 4:
            s->r0 &= ~(1 << 4);
            break;
    }
    return true;
}

static void qca_ar7240_misc_intc_update(void *opaque)
{
    QCA_AR7240_MISC_INTCState *s = opaque;
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
                        set_qca_ar7240_misc_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                }
                break;
            case STATE_NOISE:
                if (s->pending[i]) {
                    if (!s->masked[i]) {
                        s->state[i] = STATE_ALARM;
                        set_qca_ar7240_misc_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 1);
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_qca_ar7240_misc_intc_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
            case STATE_ALARM:
                if (s->pending[i]) {
                    if (s->masked[i]) {
                        clear_qca_ar7240_misc_intc_irqn_to_regs(s, i);
                        qemu_set_irq(s->irq, 0);
                        s->state[i] = STATE_NOISE;
                    }
                } else {
                    s->state[i] = STATE_REST;
                    clear_qca_ar7240_misc_intc_irqn_to_regs(s, i);
                    qemu_set_irq(s->irq, 0);
                }
                break;
        }
    }
}

static uint64_t qca_ar7240_misc_intc_read(void *opaque, hwaddr offset, unsigned size)
{
    QCA_AR7240_MISC_INTCState *s = opaque;
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

static void qca_ar7240_misc_intc_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    QCA_AR7240_MISC_INTCState *s = opaque;
    uint64_t irqn;
    uint32_t old;

    switch (offset) {
        default:
            return;
        case 0x00:
            old = (uint32_t)s->r0;
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ((old & (~(1 << (irqn)))) == (uint32_t)val) {
                    s->pending[irqn] = false;
                }
            s->r0= val;
            break;
        case 0x04:
            old = (uint32_t)s->r1;
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ((old & (~(1 << irqn))) == (uint32_t)val) {
                    s->masked[irqn] = true;
                }
            for (irqn = 0; irqn < N_IRQ; irqn++)
                if ((old | ((1 << irqn))) == (uint32_t)val) {
                    s->masked[irqn] = false;
                }
            s->r1= val;
            break;
    }
    qca_ar7240_misc_intc_update(s);
}

static const MemoryRegionOps qca_ar7240_misc_intc_ops = {
    .read = qca_ar7240_misc_intc_read,
    .write = qca_ar7240_misc_intc_write,
    .endianness = DEVICE_BIG_ENDIAN,
};

static void qca_ar7240_misc_intc_set_irq(void *opaque, int irq, int level)
{
    QCA_AR7240_MISC_INTCState *s = opaque;

    if (level)
        s->pending[irq] = true;
    else
        s->pending[irq] = false;

    qca_ar7240_misc_intc_update(s);
}

static void qca_ar7240_misc_intc_init(Object *obj)
{
    QCA_AR7240_MISC_INTCState *s = QCA_AR7240_MISC_INTC(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &qca_ar7240_misc_intc_ops, s, TYPE_QCA_AR7240_MISC_INTC, 0x8);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out(DEVICE(s), &s->irq, 1);
    qdev_init_gpio_in(DEVICE(s), qca_ar7240_misc_intc_set_irq, N_IRQ);
}

static void qca_ar7240_misc_intc_reset(DeviceState *dev)
{
    int irqn;
    QCA_AR7240_MISC_INTCState *s = QCA_AR7240_MISC_INTC(dev);
    s->r0 = 0;
    s->r1 = 0;

    for (irqn = 0; irqn < N_IRQ; irqn++)
        s->masked[irqn] = true;
}

static void qca_ar7240_misc_intc_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = qca_ar7240_misc_intc_reset;
}

static TypeInfo qca_ar7240_misc_intc_type_info = {
    .name = TYPE_QCA_AR7240_MISC_INTC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(QCA_AR7240_MISC_INTCState),
    .instance_init = qca_ar7240_misc_intc_init,
    .class_init = qca_ar7240_misc_intc_class_init,
};

static void qca_ar7240_misc_intc_register_types(void)
{
    type_register_static(&qca_ar7240_misc_intc_type_info);
}

type_init(qca_ar7240_misc_intc_register_types)
