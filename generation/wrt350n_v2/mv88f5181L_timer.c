/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/timer/mv88f5181L_timer.h"

static void mv88f5181L_timer_interrupt(void *opaque);
static void mv88f5181L_timer_reset(DeviceState *dev);

static uint64_t mv88f5181L_timer_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_timer_init(Object *obj);
static void mv88f5181L_timer_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_timer_register_types(void);

static void mv88f5181L_timer_interrupt(void *opaque) {
    MV88F5181LTIMERState *s = opaque;

    if (!s->timer0_enable ) {
        return;
    }
    if (s->timer0_counter == 0) {
        if (s->timer0_auto_mode == 0) {
            return;
        } else {
            s->timer0_counter = s->timer0_reload;
        }
        qemu_irq_pulse(s->irq);
    }
    s->timer0_counter--;
}

static uint64_t mv88f5181L_timer_read(void *opaque, hwaddr offset, unsigned size) {
    /* MV88F5181LTIMERState *s = opaque; */

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

static void mv88f5181L_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LTIMERState *s = opaque;

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

static const MemoryRegionOps mv88f5181L_timer_ops = {
    .read = mv88f5181L_timer_read,
    .write = mv88f5181L_timer_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_timer_init(Object *obj) {
    MV88F5181LTIMERState *s = MV88F5181L_TIMER(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_timer_ops, s, "mv88f5181L_timer", MV88F5181L_TIMER_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize the timer */
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, mv88f5181L_timer_interrupt, s);
}

static void mv88f5181L_timer_reset(DeviceState *dev) {
    MV88F5181LTIMERState *s = MV88F5181LTIMER(dev);

    s->timer0_enable = 0;
    s->timer0_auto_mode = 0;
    s->timer0_reload = 0;
    s->timer0_counter = 0;
    s->timer0_interrupted = false;
}

static void mv88f5181L_timer_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    /* dc->reset = ; */
    dc->reset = mv88f5181L_timer_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_timer_info = {
    .name = TYPE_MV88F5181L_TIMER,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LTIMERState),
    .instance_init = mv88f5181L_timer_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_timer_class_init,
};

static void mv88f5181L_timer_register_types(void) {
    type_register_static(&mv88f5181L_timer_info);
}

type_init(mv88f5181L_timer_register_types)