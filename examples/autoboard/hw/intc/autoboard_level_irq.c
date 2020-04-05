/*
 * autoboard level irq stat machine implementation
 */

#include "qemu/osdep.h"

#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_level_irq.h"
#include "hw/intc/autoboard_utils.h"

static level_irq_event level_irq_which_event(level_irq_stat_mach *m, write_once *wo)
{
    // only need to consider the on/off/msk/unmsk/init events
    if (m->is_evt_msk(m, wo) == ACU_DONE)
        return LVL_EVT_MSK;
    else if (m->is_evt_unmsk(m, wo) == ACU_DONE)
        return LVL_EVT_UNMSK;
    else if (m->is_evt_init(m, wo) == ACU_DONE)
        return LVL_EVT_INIT;
    else if (m->is_evt_on(m, wo) == ACU_DONE)
        return LVL_EVT_ON;
    else if (m->is_evt_off(m, wo) == ACU_DONE)
        return LVL_EVT_OFF;
    else
        return LVL_EVT_INVALID;
}

static uint8_t level_irq_related(level_irq_stat_mach *m, write_once *wo)
{
    // TODO: leave for future optimization by peeking off info
    return (m->is_which_event(m, wo) == LVL_EVT_INVALID);
}

static void level_irq_enter_act_stat(level_irq_stat_mach *m)
{
    // operate mmio value for presenting this irq is activated
    m->do_act(m);
    // notify cpu
    qemu_set_irq(m->out_irq, 1);
}

static void level_irq_leave_act_stat(level_irq_stat_mach *m)
{
    // operate mmio value for presenting this irq is activated
    m->do_deact(m);
    // notify cpu
    qemu_set_irq(m->out_irq, 0);
}

static void level_irq_handle_event(level_irq_stat_mach *m, level_irq_event lie)
{
    switch (lie)
    {
    case LVL_EVT_OFF:
        if (m->stat == LVL_STAT_ACT)
            level_irq_leave_act_stat(m);
        
        m->stat = LVL_STAT_OFF;
        m->on = 0;

        break;
    
    case LVL_EVT_ON:
        if (m->stat == LVL_STAT_OFF) {
            if (m->msk)
                m->stat = LVL_STAT_MSK;
            else if (m->act) {
                level_irq_enter_act_stat(m);
                m->stat = LVL_STAT_ACT;
            } else
                m->stat = LVL_STAT_IDLE;
        }

        m->on = 1;

        break;
    
    case LVL_EVT_INIT:
        if (m->stat == LVL_STAT_OFF) {
            m->stat = LVL_STAT_IDLE;
        }

        m->on = 1;

        break;

    case LVL_EVT_ACT:
        if (m->stat == LVL_STAT_IDLE) {
            level_irq_enter_act_stat(m);
            m->stat = LVL_STAT_ACT;
        }

        m->act = 1;

        break;
    
    case LVL_EVT_DEACT:
        if (m->stat == LVL_STAT_ACT) {
            level_irq_leave_act_stat(m);
            m->stat = LVL_STAT_IDLE;
        }

        m->act = 0;

        break;
    
    case LVL_EVT_MSK:
        if (m->stat == LVL_STAT_IDLE) {
            m->stat = LVL_STAT_MSK;
        } else if (m->stat == LVL_STAT_ACT) {
            level_irq_leave_act_stat(m);
            m->stat = LVL_STAT_MSK;
        }

        m->msk = 1;

        break;
    
    case LVL_EVT_UNMSK:
        if (m->stat == LVL_STAT_MSK) {
            if (m->act) {
                level_irq_enter_act_stat(m);
                m->stat = LVL_STAT_ACT;
            } else 
                m->stat = LVL_STAT_IDLE;
        }

        m->msk = 0;

        break;
    
    case LVL_EVT_RESET:
        // TODO: here may need re-consider suitable reset logic
        if (m->stat == LVL_STAT_ACT)
            level_irq_leave_act_stat(m);

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

static uint8_t level_irq_acu_func_flow(level_irq_stat_mach *m, auto_config_action *aca, write_once *wo)
{
    uint32_t stat;
    auto_config_unit *acu;

    // first time just execute
    acu = &aca->acus[aca->prog];
    stat = acu->func(m->s, acu, wo);

    if (stat == ACU_NEXT) {
        // then just run until we meet no next or next is ACU_WATCH

        for (aca->prog = acu->next, acu = &aca->acus[acu->next];
             (acu->type == ACU_REACT) && (stat == ACU_NEXT);
             aca->prog = acu->next, acu = &aca->acus[acu->next])
            stat = acu->func(m->s, acu, wo);
    }

    if (stat != ACU_NEXT) 
        aca->prog = 0;

    return stat;
}

static uint8_t level_irq_is_evt_on(level_irq_stat_mach *m, write_once *wo)
{
    auto_config_action *aca = m->cfg->on;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, wo);

    return ACU_MISMATCH;
}

static uint8_t level_irq_is_evt_off(level_irq_stat_mach *m, write_once *wo)
{
    auto_config_action *aca = m->cfg->off;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, wo);

    return ACU_MISMATCH;
}

static uint8_t level_irq_is_evt_init(level_irq_stat_mach *m, write_once *wo)
{
    auto_config_action *aca = m->cfg->init;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, wo);

    return ACU_MISMATCH;
}

static uint8_t level_irq_is_evt_msk(level_irq_stat_mach *m, write_once *wo)
{
    auto_config_action *aca = m->cfg->msk;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, wo);

    return ACU_MISMATCH;
}

static uint8_t level_irq_is_evt_unmsk(level_irq_stat_mach *m, write_once *wo)
{
    auto_config_action *aca = m->cfg->unmsk;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, wo);

    return ACU_MISMATCH;
}

static uint8_t level_irq_do_act(level_irq_stat_mach *m)
{
    auto_config_action *aca = m->cfg->act;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, NULL);

    return ACU_MISMATCH;
}

static uint8_t level_irq_do_deact(level_irq_stat_mach *m)
{
    auto_config_action *aca = m->cfg->deact;
    if (aca) 
        return level_irq_acu_func_flow(m, aca, NULL);

    return ACU_MISMATCH;
}

level_irq_stat_mach *init_level_irq_stat_mach(AUTOBOARD_INTCState *s, uint32_t cfg_idx)
{
    level_irq_stat_mach *m = calloc(1, sizeof(level_irq_stat_mach));

    m->s = s;
    m->cfg = (level_irq_cfg *)(&autoboard_irq_cfgs[cfg_idx]);
    m->out_irq = s->irq;
    m->stat = LVL_STAT_OFF;
    m->is_evt_on = level_irq_is_evt_on;
    m->is_evt_off = level_irq_is_evt_off;
    m->is_evt_init = level_irq_is_evt_init;
    m->is_evt_msk = level_irq_is_evt_msk;
    m->is_evt_unmsk = level_irq_is_evt_unmsk;
    m->do_act = level_irq_do_act;
    m->do_deact = level_irq_do_deact;
    m->is_related = level_irq_related;
    m->is_which_event = level_irq_which_event;
    m->handle_event = level_irq_handle_event;

    return m;
}