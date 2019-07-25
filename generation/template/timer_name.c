{{license}}

#include "qemu/osdep.h"
#include "hw/timer/{{timer_name}}.h"
#define TYPE_{{timer_name|upper}} "{{timer_name}}"

static void {{timer_name}}_interrupt(void *opaque) {
    {{timer_name|upper|concat}}State *s = opaque;

    if (!s->timer0_enable ) {
        return;
    }
    s->timer0_counter--;
    if (s->timer0_counter == 0) {
        if (s->timer0_auto_mode == 0) {
            return;
        } else {
            s->timer0_counter == s->timer0_reload;
        }
        qemu_irq_pulse(s->irq);
    } else {
        s->timer0_counter--;
    }
}

static uint64_t {{timer_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{timer_name|upper|concat}}State *s = opaque;

    uint64_t res = 0;

    switch (offset) {
    case CPU_TIMERS_CONTROL_REGISTER:
        /* do nothing */
        break;
    case CPU_TIMER0_RELOAD_REGISTER:
        /* do nothing */
        break;
    case CPU_TIMER0_REGISTER:
        /* do nothing */
        break;
    case CPU_TIMER1_RELOAD_REGISTER:
        /* do nothing */
        break;
    case CPU_TIMER1_REGISTER:
        /* do nothing */
        break;
    case CPU_WATCHDOG_TIMER_RELOAD_REGISTER:
        /* do nothing */
        break;
    case CPU_WATCHDOG_TIMER_REGISTER:
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    }
    return res;
}

static void {{timer_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{timer_name|upper|concat}}State *s = opaque;

    switch (offset) {
    case CPU_TIMERS_CONTROL_REGISTER:
        s->timer0_enable = extract64(val, 0, 1);
        s->timer0_auto_mode = extract64(val, 1, 1);
        break;
    case CPU_TIMER0_RELOAD_REGISTER:
        s->timer0_reload = extract64(val, 0, 32);
        break;
    case CPU_TIMER0_REGISTER:
        s->timer0_counter = extract64(val, 0, 32);
        break;
    case CPU_TIMER1_RELOAD_REGISTER:
        /* do nothing */
        break;
    case CPU_TIMER1_REGISTER:
        /* do nothing */
        break;
    case CPU_WATCHDOG_TIMER_RELOAD_REGISTER:
        /* do nothing */
        break;
    case CPU_WATCHDOG_TIMER_REGISTER:
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
}

static const MemoryRegionOps {{timer_name}}_ops = {
    .read = {{timer_name}}_read,
    .write = {{timer_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
}

static void {{timer_name}}_init(Object *obj) {
    {{timer_name|upper|concat}}State *s = {{timer_name|upper|concat}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{timer_name}}_ops, s, "{{timer_name}}", {{timer_name}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize the timer */
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, {{timer_name}}_interrupt, s);
}

static void {{timer_name}}_resete(DeviceState *dev) {
    {{timer_name|upper|concat}}State *s = {{timer_name|upper|concat}}(dev);

    s->timer0_enable = 0;
    s->timer0_auto_mode = 0;
    s->timer0_reload = 0;
    s->timer0_counter = 0;
    s->timer0_interrupted = False;
}

static void {{timer_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->reset = {{timer_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{timer_name}}_info = {
    .name = TYPE_{{timer_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{timer_name|upper|concat}}State),
    .instance_init = {{timer_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{timer_name}}_class_init,
}

static void {{timer_name}}_register_types(void) {
    type_register_static(&{{timer_name}}_info);
}

type_init({{timer_name}}_register_types)