/*
 * autoboard timer clock event device stat machine implementation
 */

#include "qemu/osdep.h"

#include "hw/timer/autoboard_timer_gen.h"
#include "hw/timer/autoboard_clkevt.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"

#define IMPOSSIBLE 0xffffffff

static void clkevt_past_one_cycle(struct clkevt_stat_mach *m)
{
    if (m->repeat || m->enable) {
        m->countdown--;
        if (m->countdown == 0) {
            // act irq
            m->act_irq(m->s);
            m->countdown = IMPOSSIBLE;
            m->enable = false;
        }
    }
}

static int clkevt_dispatch(struct clkevt_stat_mach *m, auto_trifle *at)
{
    int triggered;

    triggered = 0;

    if (at->type == TRIFLE_HW_EVT && at->hw_evt == CLKEVT_HW_EVT_ONE_CYCLE) {
        //printf("[+] one cycle past for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_HW_EVT_ONE_CYCLE);
        return 0;
    }

    if (m->is_evt_off(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger off event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_OFF);
        triggered++;
    }

    if (m->is_evt_on(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger on event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_ON);
        triggered++;
    }

    if (m->is_evt_init(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger init event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_INIT);
        triggered++;
    }

    if (m->is_evt_reset(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger reset event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_RESET);
        triggered++;
    }

    if (m->is_evt_set_unused(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger set unused event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_SET_UNUSED);
        triggered++;
    }

    if (m->is_evt_set_perio(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger set perio event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_SET_PERIO);
        triggered++;
    }

    if (m->is_evt_set_oneshot(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger set oneshot event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_SET_ONESHOT);
        triggered++;
    }

    if (m->is_evt_ack(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger set ack event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_ACK);
        triggered++;
    }

    if (m->is_evt_oneshot_set_next(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger oneshot set next event for clock event %s\n", m->name);
        m->handle_event(m, CLKEVT_EVT_ONESHOT_SET_NEXT);
        triggered++;
    }

    return triggered;
}

static void clkevt_handle_event(clkevt_stat_mach *m, clkevt_event ce)
{
    switch (ce)
    {
    case CLKEVT_EVT_OFF:
    case CLKEVT_EVT_RESET:
        m->stat = CLKEVT_STAT_OFF;
        m->on = false;
        m->enable = false;
        m->repeat = false;
        break;
    
    case CLKEVT_EVT_ON:
    case CLKEVT_EVT_INIT:
        if (m->stat == CLKEVT_STAT_OFF)
            m->stat = CLKEVT_STAT_UNUSED;

        m->on = true;
        m->enable = false;
        m->repeat = false;
        break;
    
    case CLKEVT_EVT_SET_UNUSED:
        if (m->on) {
            m->stat = CLKEVT_STAT_UNUSED;
            m->enable = false;
            m->repeat = false;
        }
        break;
    
    case CLKEVT_EVT_SET_PERIO:
        if (m->on) {
            m->stat = CLKEVT_STAT_PERIODIC;
            m->enable = true;
            m->repeat = true;
        }
        break;
    
    case CLKEVT_EVT_SET_ONESHOT:
        if (m->on) {
            m->stat = CLKEVT_STAT_ONESHOT;
            m->enable = false;
            m->repeat = false;
        }
        break;
    
    case CLKEVT_EVT_ACK:
        if (m->stat == CLKEVT_STAT_PERIODIC || m->stat == CLKEVT_STAT_ONESHOT) {
            m->deact_irq(m->s);
        }
        break;
    
    case CLKEVT_EVT_ONESHOT_SET_NEXT:
        if (m->stat == CLKEVT_STAT_ONESHOT) {
            m->enable = true;
        }
        break;
    
    case CLKEVT_HW_EVT_ONE_CYCLE:
        m->pass_one_cycle(m);
        break;

    default:
        break;
    }

    return;
}

static uint8_t clkevt_acu_func_flow(clkevt_stat_mach *m, auto_config_action *aca, auto_trifle *at, uint8_t evt)
{
    uint32_t stat;
    uint32_t *prog;
    auto_config_unit *acu;

    prog = &m->progs[evt];

    do {
        // continue the execution from the last time
        acu = &aca->acus[*prog];
        stat = timer_try_process_at_on_acu(m->s, acu, at);
        if (stat == ACU_ST_NEXT) {
            *prog = acu->next;
        }
    } while (ACU_IS_DO_REACT(acu->type) && stat == ACU_ST_NEXT);

    // if done, means trigger
    if (stat == ACU_ST_DONE) {
        *prog = 0;
        return stat;
    }

    // matching...
    if (stat == ACU_ST_NEXT) {
        return stat;
    }

    // if mismatch, re-match from the start again
    if (stat == ACU_ST_MISMATCH) {
        // for lvl irq, we only have doact/dodeact now
        // TODO: for lvl irq, maybe we shoule do cmp for specific hw evt 
        //     when we have not start usage of hw evt
        if ( (at->type == TRIFLE_HW_EVT && ACU_IS_DO_HW_WATCH(acu->type)) ||
             ((at->type == TRIFLE_KER_READ || at->type == TRIFLE_KER_WRITE) && 
                ACU_IS_DO_KER_WATCH(acu->type))
           ) {
            // if wait & come are same sources of event
            //    then reset the prog & try match 1st thing again
            if (*prog != 0) {
                *prog = 0;
                return clkevt_acu_func_flow(m, aca, at, evt);
            }
        }

        return stat;
    }

    assert(false && "shouldn't come to here in clkevt_acu_func_flow");
    return stat;
}

static uint8_t clkevt_is_evt_off(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_off;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_OFF);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_on(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_on;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_ON);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_init(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_init;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_INIT);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_reset(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_reset;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_RESET);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_set_unused(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_set_unused;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_SET_UNUSED);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_set_perio(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_set_perio;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_SET_PERIO);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_set_oneshot(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_set_oneshot;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_SET_ONESHOT);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_ack(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_ack;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_ACK);

    return ACU_ST_MISMATCH;
}

static uint8_t clkevt_is_evt_oneshot_set_next(clkevt_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_oneshot_set_next;
    if (aca) 
        return clkevt_acu_func_flow(m, aca, at, CLKEVT_EVT_ONESHOT_SET_NEXT);

    return ACU_ST_MISMATCH;
}

clkevt_stat_mach *init_clkevt_stat_mach(AUTOBOARD_TIMERState *s)
{
    int i;
    clkevt_stat_mach *m;

    assert(s->cfg->timer_cfgs->timer_type == STAT_MACH_CLKDEV_EVENT);
    assert(s->act_irq != NULL);
    assert(s->deact_irq != NULL);

    m = calloc(1, sizeof(clkevt_stat_mach));

    m->s = s;
    m->name = s->name;
    m->cfg = (clkevt_cfg *)(s->cfg->timer_cfgs->timer_stat_mach_cfg);

    m->on = false;
    m->enable = false;
    m->repeat = false;
    m->countdown = IMPOSSIBLE;
    // at the very beginning, the timer is off
    m->stat = CLKEVT_STAT_OFF;

    for (i = 0; i < CLKEVT_ALL_EVT_NUM; i++)
        m->progs[i] = 0;

    m->is_evt_off = clkevt_is_evt_off;
    m->is_evt_on = clkevt_is_evt_on;
    m->is_evt_init = clkevt_is_evt_init;
    m->is_evt_reset = clkevt_is_evt_reset;
    m->is_evt_set_unused = clkevt_is_evt_set_unused;
    m->is_evt_set_perio = clkevt_is_evt_set_perio;
    m->is_evt_set_oneshot = clkevt_is_evt_set_oneshot;
    m->is_evt_ack = clkevt_is_evt_ack;
    m->is_evt_oneshot_set_next = clkevt_is_evt_oneshot_set_next;

    m->act_irq = s->act_irq;
    m->deact_irq = s->deact_irq;

    m->pass_one_cycle = clkevt_past_one_cycle;
    m->handle_event = clkevt_handle_event;
    m->dispatch = clkevt_dispatch;

    return m;
}
