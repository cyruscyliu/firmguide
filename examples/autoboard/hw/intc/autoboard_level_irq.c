/*
 * autoboard level irq stat machine implementation
 */

#include "qemu/osdep.h"

#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_level_irq.h"
#include "hw/intc/autoboard_utils.h"

static bool level_irq_is_acted(struct level_irq_stat_mach *m)
{
    //return (m->stat == LVL_STAT_ACT);
    return (m->on == 1 && m->act == 1);
}

static int level_irq_dispatch(struct level_irq_stat_mach *m, auto_trifle *at)
{
    int triggered;

    if (at->type == TRIFLE_HW_EVT) {
        // do act & do deact are mutually exclusive
        if (at->hw_evt == LVL_HW_EVT_DOACT) 
            m->progs[LVL_HW_EVT_DODEACT] = 0;
        if (at->hw_evt == LVL_HW_EVT_DODEACT) 
            m->progs[LVL_HW_EVT_DOACT] = 0;
    }

    triggered = 0;

    if (m->is_evt_off(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger off event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_OFF);
        triggered++;
    }

    if (m->is_evt_on(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger on event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_ON);
        triggered++;
    }

    if (m->is_evt_act(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger act event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_ACT);
        triggered++;
    }

    if (m->is_evt_deact(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger deact event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_DEACT);
        triggered++;
    }

    if (m->is_evt_msk(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger msk event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_MSK);
        triggered++;
    }

    if (m->is_evt_unmsk(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger unmsk event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_UNMSK);
        triggered++;
    }

    if (m->is_evt_reset(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger reset event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_RESET);
        triggered++;
    }

    if (m->is_evt_init(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger init event for lvl irq %d\n", m->irq_idx);
        m->handle_event(m, LVL_EVT_INIT);
        triggered++;
    }

    if (m->do_act(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger do act event for lvl irq %d\n", m->irq_idx);
        triggered++;
    }

    if (m->do_deact(m, at) == ACU_ST_DONE) {
        //printf("[+] trigger do deact event for lvl irq %d\n", m->irq_idx);
        triggered++;
    }

    return triggered;
}

static void level_irq_handle_event(level_irq_stat_mach *m, level_irq_event lie)
{
    switch (lie)
    {
    case LVL_EVT_OFF:
        m->stat = LVL_STAT_OFF;
        m->on = 0;

        break;
    
    case LVL_EVT_ON:
        if (m->stat == LVL_STAT_OFF) {
            if (m->msk)
                m->stat = LVL_STAT_MSK;
            else if (m->act) 
                m->stat = LVL_STAT_ACT;
            else
                m->stat = LVL_STAT_IDLE;
        }

        m->on = 1;

        break;
    
    case LVL_EVT_INIT:
        if (m->stat == LVL_STAT_OFF) {
            // when init, the irq is set as masked according to the kernel intc drivers' code we've seen
            //m->stat = LVL_STAT_IDLE;
            m->stat = LVL_STAT_MSK;
            m->msk = 1;
        }

        m->on = 1;

        break;

    case LVL_EVT_ACT:
        if (m->stat == LVL_STAT_IDLE)
            m->stat = LVL_STAT_ACT;

        m->act = 1;

        break;
    
    case LVL_EVT_DEACT:
        if (m->stat == LVL_STAT_ACT)
            m->stat = LVL_STAT_IDLE;

        m->act = 0;

        break;
    
    case LVL_EVT_MSK:
        if (m->stat == LVL_STAT_IDLE)
            m->stat = LVL_STAT_MSK;
        else if (m->stat == LVL_STAT_ACT)
            m->stat = LVL_STAT_MSK;

        m->msk = 1;

        break;
    
    case LVL_EVT_UNMSK:
        if (m->stat == LVL_STAT_MSK) {
            if (m->act) 
                m->stat = LVL_STAT_ACT;
            else 
                m->stat = LVL_STAT_IDLE;
        }

        m->msk = 0;

        break;
    
    case LVL_EVT_RESET:
        // TODO: here may need re-consider suitable reset logic
        m->on = 1;
        m->act = 0;
        m->msk = 0;
        m->stat = LVL_STAT_IDLE;

        break;
    
    default:
        break;
    }

    return;
}

static uint8_t level_irq_acu_func_flow(level_irq_stat_mach *m, auto_config_action *aca, auto_trifle *at, uint8_t evt)
{
    uint32_t stat;
    uint32_t *prog;
    auto_config_unit *acu;

    prog = &m->progs[evt];

    do {
        // continue the execution from the last time
        acu = &aca->acus[*prog];
        stat = try_process_at_on_acu(m->s, acu, at);
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
                return level_irq_acu_func_flow(m, aca, at, evt);
            }
        }

        return stat;
    }

    assert(false && "shouldn't come to here in level_irq_acu_func_flow");
    return stat;
}

static uint8_t level_irq_is_evt_off(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_off;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_OFF);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_on(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_on;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_ON);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_act(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_act;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_ACT);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_deact(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_deact;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_DEACT);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_msk(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_msk;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_MSK);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_unmsk(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_unmsk;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_UNMSK);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_reset(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_reset;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_RESET);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_is_evt_init(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->is_init;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_EVT_INIT);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_do_act(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->do_act;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_HW_EVT_DOACT);

    return ACU_ST_MISMATCH;
}

static uint8_t level_irq_do_deact(level_irq_stat_mach *m, auto_trifle *at)
{
    auto_config_action *aca = m->cfg->do_deact;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, at, LVL_HW_EVT_DODEACT);

    return ACU_ST_MISMATCH;
}

level_irq_stat_mach *init_level_irq_stat_mach(AUTOBOARD_INTCState *s, uint32_t cfg_idx)
{
    int i;
    level_irq_stat_mach *m;

    assert(s->cfg->irq_cfgs[cfg_idx].irq_type == STAT_MACH_LEVEL_IRQ);

    m = calloc(1, sizeof(level_irq_stat_mach));

    m->s = s;
    m->irq_idx = cfg_idx;
    m->cfg = (level_irq_cfg *)(s->cfg->irq_cfgs[cfg_idx].irq_stat_mach_cfg);

    // at the very beginning, the intc is uninitialized & not activated & not masked
    m->stat = LVL_STAT_OFF;
    m->on = 0;
    m->act = 0;
    m->msk = 0;

    for (i = 0; i < LVL_ALL_EVT_NUM; i++)
        m->progs[i] = 0;

    m->is_evt_off = level_irq_is_evt_off;
    m->is_evt_on = level_irq_is_evt_on;
    m->is_evt_act = level_irq_is_evt_act;
    m->is_evt_deact = level_irq_is_evt_deact;
    m->is_evt_msk = level_irq_is_evt_msk;
    m->is_evt_unmsk = level_irq_is_evt_unmsk;
    m->is_evt_reset = level_irq_is_evt_reset;
    m->is_evt_init = level_irq_is_evt_init;

    m->is_acted = level_irq_is_acted;
    m->do_act = level_irq_do_act;
    m->do_deact = level_irq_do_deact;

    m->handle_event = level_irq_handle_event;
    m->dispatch = level_irq_dispatch;

    return m;
}
