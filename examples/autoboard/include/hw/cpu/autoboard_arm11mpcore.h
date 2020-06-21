/*
 * ARM11MPCore internal peripheral emulation for autoboard.
 *
 * Written by Zhang Cen
 *
 * This code is licensed under the GPL.
 */

#ifndef HW_CPU_AUTOBOARDARM11MPCORE_H
#define HW_CPU_AUTOBOARDARM11MPCORE_H

#include "hw/sysbus.h"
#include "hw/misc/arm11scu.h"
//#include "hw/intc/arm_gic.h"
#include "hw/intc/autoboard_intc.h"
//#include "hw/timer/arm_mptimer.h"
#include "hw/timer/autoboard_timer.h"

#define TYPE_AUTOBOARDARM11MPCORE_PRIV "autoboardarm11mpcore_priv"
#define AUTOBOARDARM11MPCORE_PRIV(obj) \
    OBJECT_CHECK(AUTOBOARDARM11MPCorePriveState, (obj), TYPE_AUTOBOARDARM11MPCORE_PRIV)

typedef struct AUTOBOARDARM11MPCorePriveState {
    SysBusDevice parent_obj;

    uint32_t num_cpu;
    MemoryRegion container;
    uint32_t num_irq;

    ARM11SCUState scu;
    AUTOBOARD_INTCState aic;
    AUTOBOARD_TIMERState mptimer;
    //ARMMPTimerState mptimer;
    //ARMMPTimerState wdtimer;
} AUTOBOARDARM11MPCorePriveState;

#endif
