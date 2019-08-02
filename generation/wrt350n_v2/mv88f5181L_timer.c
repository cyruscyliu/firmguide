/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qemu/timer.h"
#include "hw/timer/mv88f5181L_timer.h"

static void mv88f5181L_timer_callback(void *opaque);
static void mv88f5181L_timer_update(void *opaque);
static void mv88f5181L_timer_reset(DeviceState *dev);

static uint64_t mv88f5181L_timer_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_timer_init(Object *obj);
static void mv88f5181L_timer_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_timer_register_types(void);

static void mv88f5181L_timer_update(void *opaque) {
    MV88F5181LTIMERState *s = opaque;

    timer_mod(s->timer, 0xffffffffffffff + qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL));
    qemu_set_irq(s->irq, 1);
}

static void mv88f5181L_timer_callback(void *opaque) {
    MV88F5181LTIMERState *s = opaque;

    mv88f5181L_timer_update(s);
}

static uint64_t mv88f5181L_timer_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LTIMERState *s = opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case CPU_TIMERS_CONTROL_REGISTER:
        res = s->cpu_timers_control_register;;
        break;
    case CPU_TIMER0_RELOAD_REGISTER:
        res = s->cpu_timer0_reload_register;;
        break;
    case CPU_TIMER0_REGISTER:
        res = s->cpu_timer0_register;;
        break;
    case CPU_TIMER1_RELOAD_REGISTER:
        res = s->cpu_timer1_reload_register;;
        break;
    case CPU_TIMER1_REGISTER:
        res = s->cpu_timer1_register;;
        break;
    case CPU_WATCHDOG_TIMER_RELOAD_REGISTER:
        res = s->cpu_watchdog_timer_reload_register;;
        break;
    case CPU_WATCHDOG_TIMER_REGISTER:
        res = s->cpu_watchdog_timer_register;;
        break;
    }
    return res;
}

static void mv88f5181L_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LTIMERState *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    case CPU_TIMERS_CONTROL_REGISTER:
        s->cpu_timers_control_register = val;
        break;
    case CPU_TIMER0_RELOAD_REGISTER:
        s->cpu_timer0_reload_register = val;
        break;
    case CPU_TIMER0_REGISTER:
        s->cpu_timer0_register = val;
        break;
    case CPU_TIMER1_RELOAD_REGISTER:
        s->cpu_timer1_reload_register = val;
        break;
    case CPU_TIMER1_REGISTER:
        s->cpu_timer1_register = val;
        break;
    case CPU_WATCHDOG_TIMER_RELOAD_REGISTER:
        s->cpu_watchdog_timer_reload_register = val;
        break;
    case CPU_WATCHDOG_TIMER_REGISTER:
        s->cpu_watchdog_timer_register = val;
        break;
    }
    mv88f5181L_timer_update(s);
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
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, mv88f5181L_timer_callback, s);
}

static void mv88f5181L_timer_reset(DeviceState *dev) {
    MV88F5181LTIMERState *s = MV88F5181L_TIMER(dev);
    
    s->cpu_timers_control_register = 0;
    s->cpu_timer0_reload_register = 0;
    s->cpu_timer0_register = 0;
    s->cpu_timer1_reload_register = 0;
    s->cpu_timer1_register = 0;
    s->cpu_watchdog_timer_reload_register = 0;
    s->cpu_watchdog_timer_register = 0;
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