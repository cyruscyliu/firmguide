/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "hw/arm/wrt350n_v2.h"
#include "hw/arm/mv88f5181L_peripherals.h"

static void mv88f5181L_peripherals_realize(DeviceState *dev, Error **errp);

static void mv88f5181L_peripherals_init(Object *obj);
static void mv88f5181L_peripherals_class_init(ObjectClass *oc, void *data);
static void mv88f5181L_peripherals_register_types(void);

static void mv88f5181L_bridge_update(MV88F5181LPERIPHERALSState *s) {
}

static uint64_t mv88f5181L_bridge_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LPERIPHERALSState *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    case BRIDGE_CONFIGURATION_REGISTER:
        /* do nothing */
        break;
    case BRIDGE_CONTROL_AND_STATUS_REGISTER:
        /* do nothing */
        break;
    case BRIDGE_RSTOUTn_MASK_RESTIER:
        /* do nothing */
        break;
    case BRIDGE_SYSTEM_SOFT_RESET_REGISTER:
        /* do nothing */
        break;
    case BRIDGE_INTERRUPT_CAUSE_REGISTER:
        res = s->bridge_interrupt_cause_register;
        break;
    case BRIDGE_INTERRUPT_MASK_REGISTER:
        res = s->bridge_interrupt_mask_register;
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    }
    return res;
}

static void mv88f5181L_bridge_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LPERIPHERALSState *s = opaque;

    switch (offset) {
    case BRIDGE_CONFIGURATION_REGISTER:
        /* do nothing */
        break;
    case BRIDGE_CONTROL_AND_STATUS_REGISTER:
        /* do nothing */
        break;
    case BRIDGE_RSTOUTn_MASK_RESTIER:
        /* do nothing */
        break;
    case BRIDGE_SYSTEM_SOFT_RESET_REGISTER:
        /* do nothing */
        break;
    case BRIDGE_INTERRUPT_CAUSE_REGISTER:
        s->bridge_interrupt_cause_register = val;
        break;
    case BRIDGE_INTERRUPT_MASK_REGISTER:
        s->bridge_interrupt_mask_register = val;
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
    mv88f5181L_bridge_update(s);
}


static const MemoryRegionOps mv88f5181L_bridge_ops = {
    .read = mv88f5181L_bridge_read,
    .write = mv88f5181L_bridge_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_peripherals_init(Object *obj) {
    MV88F5181LPERIPHERALSState *s = MV88F5181L_PERIPHERALS(obj);

    /* initialize the peripheral mmio */
    memory_region_init_io(&s->bridge_mmio, obj, &mv88f5181L_bridge_ops, s, TYPE_MV88F5181L_PERIPHERALS, MV88F5181L_BRIDGE_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->bridge_mmio);

    /* initialize the timer */
    sysbus_init_child_obj(obj, "timer", &s->timer, sizeof(s->timer), TYPE_MV88F5181L_TIMER);

    /* initialize the uart */
    sysbus_init_child_obj(obj, "uart", &s->uart, sizeof(s->uart), TYPE_MV88F5181L_UART);

    /* initialize the gpio */
    sysbus_init_child_obj(obj, "gpio", &s->gpio, sizeof(s->gpio), TYPE_MV88F5181L_GPIO);

    /* initialize the pcie */
    sysbus_init_child_obj(obj, "pcie", &s->pcie, sizeof(s->pcie), TYPE_MV88F5181L_PCIE);
}

static void mv88f5181L_peripherals_realize(DeviceState *dev, Error **errp) {
    MV88F5181LPERIPHERALSState *s = MV88F5181L_PERIPHERALS(dev);
    Error *err = NULL;

    /* realize the timer */
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, MV88F5181L_TIMER_RAM_BASE);
    sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->timer));

    /* realize the uart */
    object_property_set_bool(OBJECT(&s->uart), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->uart), 0, MV88F5181L_UART_RAM_BASE);
    /* fix me */
    /* sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->uart)); */

    /* realize the uart */
    object_property_set_bool(OBJECT(&s->gpio), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->gpio), 0, MV88F5181L_GPIO_RAM_BASE);
    /* fix me */
    /* sysbus_pass_irq(SYS_BUS_DEVICE(s), SYS_BUS_DEVICE(&s->uart)); */

    /* realize the pcie */
    object_property_set_bool(OBJECT(&s->pcie), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->pcie), 0, MV88F5181L_PCIE_RAM_BASE);
}

static void mv88f5181L_bridge_reset(DeviceState *d) {
    MV88F5181LPERIPHERALSState *s = MV88F5181L_PERIPHERALS(d);
    s->bridge_interrupt_cause_register = 0;
    s->bridge_interrupt_mask_register = 0;
}

static void mv88f5181L_peripherals_class_init(ObjectClass *oc, void *data) {
    DeviceClass *dc = DEVICE_CLASS(oc);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_bridge_reset;
    dc->realize = mv88f5181L_peripherals_realize;
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_peripherals_type_info = {
    .name = TYPE_MV88F5181L_PERIPHERALS,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LPERIPHERALSState),
    .instance_init = mv88f5181L_peripherals_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_peripherals_class_init,
};

static void mv88f5181L_peripherals_register_types(void) {
    type_register_static(&mv88f5181L_peripherals_type_info);
}

type_init(mv88f5181L_peripherals_register_types)