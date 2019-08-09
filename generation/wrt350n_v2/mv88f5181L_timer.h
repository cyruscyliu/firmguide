/* 
 * automatically generated, don't change
 */

#include "hw/sysbus.h"
#include "qemu/timer.h"

#ifndef MV88F5181L_TIMER_H
#define MV88F5181L_TIMER_H

#define TYPE_MV88F5181L_TIMER "mv88f5181L_timer"
#define MV88F5181L_TIMER(obj) \
    OBJECT_CHECK(MV88F5181LTIMERState, (obj), TYPE_MV88F5181L_TIMER)

#define CPU_TIMERS_CONTROL_REGISTER 0x00
#define CPU_TIMER0_RELOAD_REGISTER 0x10
#define CPU_TIMER0_REGISTER 0x14
#define CPU_TIMER1_RELOAD_REGISTER 0x18
#define CPU_TIMER1_REGISTER 0x1c
#define CPU_WATCHDOG_TIMER_RELOAD_REGISTER 0x20
#define CPU_WATCHDOG_TIMER_REGISTER 0x24

#define MV88F5181L_TIMER_MMIO_SIZE 0x100
#define MV88F5181L_TIMER_MMIO_BASE 0xf1020300

typedef struct MV88F5181LTIMERState {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    MemoryRegion mmio;
    QEMUTimer *timer;
    qemu_irq irq_0, irq_1;

    uint32_t cpu_timers_control_register;
    uint32_t cpu_timer0_reload_register;
    uint32_t cpu_timer0_register;
    uint32_t cpu_timer1_reload_register;
    uint32_t cpu_timer1_register;
    uint32_t cpu_watchdog_timer_reload_register;
    uint32_t cpu_watchdog_timer_register;
    
    uint32_t reserved_0;
    uint32_t reserved_1;
    uint32_t reserved_2;
} MV88F5181LTIMERState;

#endif /* MV88F5181L_TIMER_H */
