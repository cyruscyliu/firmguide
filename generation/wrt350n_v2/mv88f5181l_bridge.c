/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/arm/mv88f5181l_bridge.h"
#include "hw/timer/mv88f5181l_timer.h"

static void mv88f5181l_bridge_realize(DeviceState *dev, Error **errp);

static void mv88f5181l_bridge_init(Object *obj);
static void mv88f5181l_bridge_class_init(ObjectClass *oc, void *data);
static void mv88f5181l_bridge_register_types(void);

static void mv88f5181l_bridge_update(void *opaque) 
{
    MV88F5181LBRIDGEState *s = opaque;
    if (extract32(s->bridge_interrupt_cause_register, 1, 1)) {
        if (s->bridge_interrupt_cause_register & s->bridge_interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    } else {
        /* clear the interrupt */
        qemu_set_irq(s->irq, 0);
    }
    if (extract32(s->bridge_interrupt_cause_register, 2, 1)) {
        if (s->bridge_interrupt_cause_register & s->bridge_interrupt_mask_register) {
            qemu_set_irq(s->irq, 1);
        }
    } else {
        /* clear the interrupt */
        qemu_set_irq(s->irq, 0);
    }
}

static void mv88f5181l_bridge_set_irq(void *opaque, int irq, int level) 
{
    MV88F5181LBRIDGEState *s = opaque;
    s->bridge_interrupt_cause_register &= 0x1;
    s->bridge_interrupt_cause_register = deposit32(s->bridge_interrupt_cause_register, irq, 1, level);
    mv88f5181l_bridge_update(s);
}

static uint64_t mv88f5181l_bridge_read(void *opaque, hwaddr offset, unsigned size) 
{
    MV88F5181LBRIDGEState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case BRIDGE_CONFIGURATION_REGISTER:
        res = s->bridge_configuration_register;
        break;
    case BRIDGE_CONTROL_AND_STATUS_REGISTER:
        res = s->bridge_control_and_status_register;
        break;
    case BRIDGE_RSTOUTN_MASK_REGISTER:
        res = s->bridge_rstoutn_mask_register;
        break;
    case BRIDGE_SYSTEM_SOFT_RESET_REGISTER:
        res = s->bridge_system_soft_reset_register;
        break;
    case BRIDGE_INTERRUPT_CAUSE_REGISTER:
        res = s->bridge_interrupt_cause_register;
        break;
    case BRIDGE_INTERRUPT_MASK_REGISTER:
        res = s->bridge_interrupt_mask_register;
        break;
    }
    return res;
}

static void mv88f5181l_bridge_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) 
{
    MV88F5181LBRIDGEState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case BRIDGE_CONFIGURATION_REGISTER:
        s->bridge_configuration_register = val;
        break;
    case BRIDGE_CONTROL_AND_STATUS_REGISTER:
        s->bridge_control_and_status_register = val;
        break;
    case BRIDGE_RSTOUTN_MASK_REGISTER:
        s->bridge_rstoutn_mask_register = val;
        break;
    case BRIDGE_SYSTEM_SOFT_RESET_REGISTER:
        s->bridge_system_soft_reset_register = val;
        break;
    case BRIDGE_INTERRUPT_CAUSE_REGISTER:
        s->bridge_interrupt_cause_register = val;
        break;
    case BRIDGE_INTERRUPT_MASK_REGISTER:
        s->bridge_interrupt_mask_register = val;
        break;
    }
    mv88f5181l_bridge_update(s);
}

static const MemoryRegionOps mv88f5181l_bridge_ops = {
    .read = mv88f5181l_bridge_read,
    .write = mv88f5181l_bridge_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181l_bridge_init(Object *obj) 
{
    MV88F5181LBRIDGEState *s = MV88F5181L_BRIDGE(obj);

    /* initialize the bridge mmio */
    memory_region_init_io(
        &s->bridge_mmio, obj, &mv88f5181l_bridge_ops, s, TYPE_MV88F5181L_BRIDGE, MV88F5181L_BRIDGE_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);

    /* initialize the bridge irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize GPIO in */
    qdev_init_gpio_in_named(DEVICE(s), mv88f5181l_bridge_set_irq, MV88F5181L_BRIDGE_IRQ, 32);
}

static void mv88f5181l_bridge_realize(DeviceState *dev, Error **errp) 
{
    MV88F5181LBRIDGEState *s = MV88F5181L_BRIDGE(dev);
    Object *obj;
    MV88F5181LTIMERState *timer;
    Error *err = NULL;

    /* connect the timer to the bridge */
    obj = object_property_get_link(OBJECT(dev), "timer", &err) ;
    timer = MV88F5181L_TIMER(obj);
    if (timer == NULL) {
        error_setg(errp, "%s: required ram link not found: %s",
                   __func__, error_get_pretty(err));
        return;
    }
    sysbus_connect_irq(SYS_BUS_DEVICE(timer), 0,
        qdev_get_gpio_in_named(DEVICE(s), MV88F5181L_BRIDGE_IRQ, 1));
    sysbus_connect_irq(SYS_BUS_DEVICE(timer), 1,
        qdev_get_gpio_in_named(DEVICE(s), MV88F5181L_BRIDGE_IRQ, 2));
}

static void mv88f5181l_bridge_reset(DeviceState *d) 
{
    MV88F5181LBRIDGEState *s = MV88F5181L_BRIDGE(d);
    
    s->bridge_configuration_register = 0;
    s->bridge_control_and_status_register = 0;
    s->bridge_rstoutn_mask_register = 0;
    s->bridge_system_soft_reset_register = 0;
    s->bridge_interrupt_cause_register = 0;
    s->bridge_interrupt_mask_register = 0;
}

static void mv88f5181l_bridge_class_init(ObjectClass *oc, void *data) 
{
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181l_bridge_reset;
    dc->realize = mv88f5181l_bridge_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181l_bridge_type_info = {
    .name = TYPE_MV88F5181L_BRIDGE,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LBRIDGEState),
    .instance_init = mv88f5181l_bridge_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181l_bridge_class_init,
};

static void mv88f5181l_bridge_register_types(void) 
{
    type_register_static(&mv88f5181l_bridge_type_info);
}

type_init(mv88f5181l_bridge_register_types)
