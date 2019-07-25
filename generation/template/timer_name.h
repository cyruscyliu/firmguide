{{license}}

#include "hw/sysbus.h"
#include "qemu/timer.h"

#ifndef {{timer_name|upper}}_H
#define {{timer_name|upper}}_H

#define TYPE_{{timer_name|upper}} "{{timer_name}}"
#define {{timer_name|upper|concat}}(obj) \
    OBJECT_CHECK({{timer_name|upper|concat}}State, (obj), TYPE_{{timer_name|upper}})

#define CPU_TIMERS_CONTROL_REGISTER         0x00
#define CPU_TIMER0_RELOAD_REGISTER          0x10
#define CPU_TIMER0_REGISTER                 0x14
#define CPU_TIMER1_RELOAD_REGISTER          0x18
#define CPU_TIMER1_REGISTER                 0x1C
#define CPU_WATCHDOG_TIMER_RELOAD_REGISTER  0x20
#define CPU_WATCHDOG_TIMER_REGISTER         0x24

typedef struct {{timer_name|upper|concat}}State {
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
} {{timer_name|upper|concat}}State;

#endif /* {{timer_name|upper}}_H
