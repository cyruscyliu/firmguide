/*
 * autoboard timer clock source device stat machine implementation
 */

#include "qemu/osdep.h"

#include "hw/timer/autoboard_timer_gen.h"
#include "hw/timer/autoboard_clksrc.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"

static void clksrc_past_one_cycle(struct clksrc_stat_mach *m)
{
    if (m->increment)
        m->cycles++;
    else 
        m->cycles--;

    m->do_convert(m, NULL);
}

static int clksrc_dispatch(struct clksrc_stat_mach *m, auto_trifle *at)
{
    int triggered;

    triggered = 0;

    if (at->type == TRIFLE_HW_EVT && at->hw_evt == CLKSRC_HW_EVT_ONE_CYCLE) {
        //printf("[+] one cycle past for clock source %s\n", m->name);
        m->handle_event(m, CLKSRC_HW_EVT_ONE_CYCLE);
        return 0;
    }

    if (m->is_evt_off(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger off event for clock source %s\n", m->name);
        m->handle_event(m, CLKSRC_EVT_OFF);
        triggered++;
    }

    if (m->is_evt_on(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger on event for clock source %s\n", m->name);
        m->handle_event(m, CLKSRC_EVT_ON);
        triggered++;
    }

    if (m->is_evt_init(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger init event for clock source %s\n", m->name);
        m->handle_event(m, CLKSRC_EVT_INIT);
        triggered++;
    }

    if (m->is_evt_reset(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger reset event for clock source %s\n", m->name);
        m->handle_event(m, CLKSRC_EVT_RESET);
        triggered++;
    }

    return triggered;
}

static void clksrc_handle_event(clksrc_stat_mach *m, clksrc_event ce)
{
    switch (ce)
    {
    case CLKSRC_EVT_OFF:
    case CLKSRC_EVT_RESET:
        m->stat = CLKSRC_STAT_OFF;
        m->on = false;
        break;
    
    case CLKSRC_EVT_ON:
    case CLKSRC_EVT_INIT:
        if (m->stat == CLKSRC_STAT_OFF)
            m->stat = CLKSRC_STAT_RUN;

        m->on = true;
        break;
    
    case CLKSRC_HW_EVT_ONE_CYCLE:
        if (m->stat == CLKSRC_STAT_RUN) {
            m->pass_one_cycle(m);
        }
        break;

    default:
        break;
    }

    return;
}

static uint8_t clksrc_acu_func_flow(clksrc_stat_mach *m, auto_config_action *aca, auto_trifle *at, uint8_t evt)
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
                return clksrc_acu_func_flow(m, aca, at, evt);
            }
        }

        return stat;
    }

    assert(false && "shouldn't come to here in clksrc_acu_func_flow");
    return stat;
}

static uint8_t clksrc_is_evt_off(clksrc_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_off;
    if (aca) 
        return clksrc_acu_func_flow(m, aca, at, CLKSRC_EVT_OFF);

    return ACU_ST_MISMATCH;
}

static uint8_t clksrc_is_evt_on(clksrc_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_on;
    if (aca) 
        return clksrc_acu_func_flow(m, aca, at, CLKSRC_EVT_ON);

    return ACU_ST_MISMATCH;
}

static uint8_t clksrc_is_evt_init(clksrc_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_init;
    if (aca) 
        return clksrc_acu_func_flow(m, aca, at, CLKSRC_EVT_INIT);

    return ACU_ST_MISMATCH;
}

static uint8_t clksrc_is_evt_reset(clksrc_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_reset;
    if (aca) 
        return clksrc_acu_func_flow(m, aca, at, CLKSRC_EVT_RESET);

    return ACU_ST_MISMATCH;
}

static uint8_t clksrc_do_convert(clksrc_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->do_convert;
    if (aca) 
        // use this hwevt's prog slot as only this hwevt can trigger this do_convert
        return clksrc_acu_func_flow(m, aca, at, CLKSRC_HW_EVT_ONE_CYCLE);

    return ACU_ST_MISMATCH;
}

clksrc_stat_mach *init_clksrc_stat_mach(AUTOBOARD_TIMERState *s)
{
    int i;
    clksrc_stat_mach *m;

    assert(s->cfg->timer_cfgs->timer_type == STAT_MACH_CLKDEV_SOURCE);

    m = calloc(1, sizeof(clksrc_stat_mach));

    m->s = s;
    m->name = s->name;
    m->cfg = (clksrc_cfg *)(s->cfg->timer_cfgs->timer_stat_mach_cfg);

    m->on = false;
    m->increment = m->cfg->increment;
    m->cycles = 0;
    // at the very beginning, the timer is off
    m->stat = CLKSRC_STAT_OFF;

    for (i = 0; i < CLKSRC_ALL_EVT_NUM; i++)
        m->progs[i] = 0;

    m->is_evt_off = clksrc_is_evt_off;
    m->is_evt_on = clksrc_is_evt_on;
    m->is_evt_init = clksrc_is_evt_init;
    m->is_evt_reset = clksrc_is_evt_reset;
    m->do_convert = clksrc_do_convert;

    m->pass_one_cycle = clksrc_past_one_cycle;
    m->handle_event = clksrc_handle_event;
    m->dispatch = clksrc_dispatch;

    return m;
}
