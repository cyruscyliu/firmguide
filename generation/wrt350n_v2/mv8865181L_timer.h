/* 
 * automatically generated, don't change
 */

#include "hw/sysbus.h"
#include "qemu/timer.h"

#ifndef MV8865181L_TIMER_H
#define MV8865181L_TIMER_H

#define TYPE_MV8865181L_TIMER "mv8865181L_timer"
#define MV8865181LTIMER(obj) \
    OBJECT_CHECK(MV8865181LTIMERState, (obj), TYPE_MV8865181L_TIMER)

#define CPU_TIMERS_CONTROL_REGISTER         0x00
#define CPU_TIMER0_RELOAD_REGISTER          0x10
#define CPU_TIMER0_REGISTER                 0x14
#define CPU_TIMER1_RELOAD_REGISTER          0x18
#define CPU_TIMER1_REGISTER                 0x1C
#define CPU_WATCHDOG_TIMER_RELOAD_REGISTER  0x20
#define CPU_WATCHDOG_TIMER_REGISTER         0x24

typedef struct MV8865181LTIMERState {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    MemoryRegion mmio;
    QEMUTimer *timer;
    qemu_irq irq;

    uint8_t timer0_enable;
    uint8_t timer0_auto_mode;
    uint32_t timer0_reload;
    uint32_t timer0_counter;
    bool timer0_interrupted;
} MV8865181LTIMERState;

static void mv8865181L_timer_interrupt(void *opaque);
static void mv8865181L_timer_reset(DeviceState *dev);

static uint64_t mv8865181L_timer_read(void *opaque, hwaddr offset, unsigned size);
static void mv8865181L_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv8865181L_timer_init(Object *obj);
static void mv8865181L_timer_class_init(ObjectClass *klass, void *data);
static void mv8865181L_timer_register_types(void);

#endif /* MV8865181L_TIMER_H
