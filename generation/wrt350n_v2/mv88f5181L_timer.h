/* 
 * automatically generated, don't change
 */

#include "hw/sysbus.h"
#include "qemu/timer.h"

#ifndef MV88F5181L_TIMER_H
#define MV88F5181L_TIMER_H

#define TYPE_MV88F5181L_TIMER "mv88f5181L_timer"
#define MV88F5181LTIMER(obj) \
    OBJECT_CHECK(MV88F5181LTIMERState, (obj), TYPE_MV88F5181L_TIMER)

#define CPU_TIMERS_CONTROL_REGISTER         0x00
#define CPU_TIMER0_RELOAD_REGISTER          0x10
#define CPU_TIMER0_REGISTER                 0x14
#define CPU_TIMER1_RELOAD_REGISTER          0x18
#define CPU_TIMER1_REGISTER                 0x1C
#define CPU_WATCHDOG_TIMER_RELOAD_REGISTER  0x20
#define CPU_WATCHDOG_TIMER_REGISTER         0x24

#define MV88F5181L_TIMER_RAM_SIZE 0x100

typedef struct MV88F5181LTIMERState {
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
} MV88F5181LTIMERState;

#endif /* MV88F5181L_TIMER_H */
