/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "hw/intc/mv88f5181l_ic.h"
#include "qemu/log.h"

static void mv88f5181l_ic_set_irq(void *opaque, int irq, int level);
static void mv88f5181l_ic_update(void *opaque);
static void mv88f5181l_ic_reset(DeviceState *d);

static uint64_t mv88f5181l_ic_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181l_ic_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181l_ic_init(Object *obj);
static void mv88f5181l_ic_class_init(ObjectClass *kclass, void *data);
static void mv88f5181l_ic_register_types(void);

static void mv88f5181l_ic_update(void *opaque) 
{
    MV88F5181LICState *s = opaque;
    if (extract32(s->main_interrupt_cause_register, 0, 1)) {
        if (s->main_interrupt_cause_register & s->main_irq_interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    } else {
        qemu_set_irq(s->irq, 0);
    }
}

static void mv88f5181l_ic_set_irq(void *opaque, int irq, int level) 
{
    MV88F5181LICState *s = opaque;
    s->main_interrupt_cause_register = deposit32(s->main_interrupt_cause_register, irq, 1, level);
    mv88f5181l_ic_update(s);
}

static uint64_t mv88f5181l_ic_read(void *opaque, hwaddr offset, unsigned size) 
{
    MV88F5181LICState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case MAIN_INTERRUPT_CAUSE_REGISTER:
        res = s->main_interrupt_cause_register;
        break;
    case MAIN_IRQ_INTERRUPT_MASK_REGISTER:
        res = s->main_irq_interrupt_mask_register;
        break;
    case MAIN_FIQ_INTERRUPT_MASK_REGISTER:
        res = s->main_fiq_interrupt_mask_register;
        break;
    case MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER:
        res = s->main_endpoint_interrupt_mask_register;
        break;
    }
    return res;
}

static void mv88f5181l_ic_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    MV88F5181LICState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case MAIN_INTERRUPT_CAUSE_REGISTER:
        s->main_interrupt_cause_register = val;
        break;
    case MAIN_IRQ_INTERRUPT_MASK_REGISTER:
        s->main_irq_interrupt_mask_register = val;
        break;
    case MAIN_FIQ_INTERRUPT_MASK_REGISTER:
        s->main_fiq_interrupt_mask_register = val;
        break;
    case MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER:
        s->main_endpoint_interrupt_mask_register = val;
        break;
    }
    mv88f5181l_ic_update(s);
}

static const MemoryRegionOps mv88f5181l_ic_ops = {
    .read = mv88f5181l_ic_read,
    .write = mv88f5181l_ic_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_ic_init(Object *obj) 
{
    MV88F5181LICState *s = MV88F5181L_IC(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181l_ic_ops, s, TYPE_MV88F5181L_IC, MV88F5181L_IC_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the interrupt input */
    qdev_init_gpio_in_named(DEVICE(s), mv88f5181l_ic_set_irq, MV88F5181L_IC_IRQ, MV88F5181L_IC_N_IRQS);

    /* initialize the irq/fip to cpu */
    qdev_init_gpio_out_named(DEVICE(s), &s->irq, "irq", 1);
}

static void mv88f5181l_ic_reset(DeviceState *dev) 
{
    MV88F5181LICState *s = MV88F5181L_IC(dev);
    
    s->main_interrupt_cause_register = 0;
    s->main_irq_interrupt_mask_register = 0;
    s->main_fiq_interrupt_mask_register = 0;
    s->main_endpoint_interrupt_mask_register = 0;
}

static void mv88f5181l_ic_class_init(ObjectClass *klass, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181l_ic_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static TypeInfo mv88f5181l_ic_type_info = {
    .name = TYPE_MV88F5181L_IC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LICState),
    .instance_init = mv88f5181l_ic_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181l_ic_class_init,
};

static void mv88f5181l_ic_register_types(void) 
{
    type_register_static(&mv88f5181l_ic_type_info);
}

type_init(mv88f5181l_ic_register_types)
