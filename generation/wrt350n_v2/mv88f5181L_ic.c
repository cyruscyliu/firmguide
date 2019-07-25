/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "hw/intc/mv88f5181L_ic.h"
#include "qemu/log.h"

static void mv88f5181L_ic_set_irq(void *opaque, int irq, int level) {
    MV88F5181LICState *s = MV88F5181L_IC(obj);
    s->irq_level_0 = deposit32(s->irq_level_0, irq, 1, level != 0);
    mv88f5181L_ic_update(s);
}

static uint64_t mv88f5181L_ic_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    case MAIN_INTERRUPT_CAUSE_REGISTER:
        res = s->irq_level_0;
        break;
    case MAIN_IRQ_INTERRUPT_MASK_REGISTER:
        res = s->irq_enable_0;
        break;
    case MAIN_FIQ_INTERRUPT_MASK_REGISTER:
        res = s->fiq_enable_0;
        break;
    case MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER:
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    }
    return res;
}

static void mv88f5181L_ic_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LICState *s = opaque;

    switch (offset) {
    case MAIN_INTERRUPT_CAUSE_REGISTER:
        s->irq_level_0 = extract64(val, 0, 32);
        break;
    case MAIN_IRQ_INTERRUPT_MASK_REGISTER:
        s->irq_enable_0 |= extract64(val, 0, 32);
        break;
    case MAIN_FIQ_INTERRUPT_MASK_REGISTER:
        s->fiq_enable_0 |= extract64(val, 0, 32);
        break;
    case MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER:
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
    mv88f5181L_ic_update(s);
}

static void mv88f5181L_ic_update(MV88F5181LICState *s) {
    bool set = false;

    set = (s->irq_level_0 & s->fiq_enable_0);
    qemu_set_irq(s->fiq, set);
    set = (s->irq_level_0 & s->irq_enable_0);
    qemu_set_irq(s->irq, set);
}

static const MemoryRegionOps mv88f5181L_ic_ops = {
    .read = mv88f5181L_ic_read,
    .write = mv88f5181L_ic_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
    .valid.min_access_size = 4,
    .valid.max_access_size = 4,
};

static void mv88f5181L_ic_init(Object *obj) {
    MV88F5181LICState *s = MV88F5181L_IC(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_ic_ops, s, TYPE_MV88F5181L_IC, mv88f5181L_ic_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the interrupt input */
    qdev_init_gpio_in_named(DEVICE(s), mv88f5181L_ic_set_irq, mv88f5181L_ic_IRQ), mv88f5181L_ic_N_IRQS);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out_named(dev, s->irq, "irq", 1);
    qdev_init_gpio_out_named(dev, s->fiq, "fiq", 1);
}

static void mv88f5181L_ic_reset(DeviceState *d) {
    MV88F5181LICState *s = MV88F5181L_IC(d);
    
    s->irq_enable_0 = 0;

    s->fiq_enable = false;
    s->fiq_select = 0;
}

static void mv88f5181L_ic_class_init(ObjectClass *kclass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_ic_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static TypeInfo mv88f5181L_ic_type_info = {
    .name = TYPE_MV88F5181L_IC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LICICState,
    .instance_init = mv88f5181L_ic_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_ic_class_init,
};

static void mv88f5181L_ic_register_types(void) {
    type_register_static(&mv88f5181L_ic_type_info);
}

type_init(mv88f5181L_ic_register_types)