/*
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"
#include "qemu/timer.h"
#include "hw/timer/autoboard_timer.h"
#include "hw/timer/autoboard_clksrc.h"
#include "hw/timer/autoboard_clkevt.h"
#include "hw/timer/autoboard_timer_gen.h"
#include "hw/timer/autoboard_timer_utils.h"
#include "hw/misc/autoboard_utils.h"

static autoboard_timer_cfg_id choosen_id = AUTOBOARD_TIMER_INVALID;
static const char *timer_name = "anonymous";

void set_autoboard_timer_cfg(autoboard_timer_cfg_id id, const char *name)
{
    choosen_id = id; 
    timer_name = name;
}

static uint32_t autoboard_mmio_read(autoboard_mmio *mmio, hwaddr off)
{
    // TODO: may need add lock here in future
    return __u32_native(mmio->caches + off);
}

static uint32_t autoboard_mmio_write(autoboard_mmio *mmio, hwaddr off, uint64_t val)
{
    // TODO: may need add lock here in future
    *((uint32_t *) (mmio->caches + off)) = (uint32_t) val;
    return 0;
}

static void autoboard_timer_act_irq(AUTOBOARD_TIMERState *s)
{
    if (s->is_level_irq) {
        // level irq raise
        qemu_set_irq(s->irq, 1);
    } else {
        // edge irq pulse
        qemu_set_irq(s->irq, 1);
        qemu_set_irq(s->irq, 0);
    }
}

static void autoboard_timer_deact_irq(AUTOBOARD_TIMERState *s)
{
    if (s->is_level_irq) {
        // level irq lower
        qemu_set_irq(s->irq, 0);
    }
}

static void autoboard_timer_tick_callback(void *opaque)
{
    AUTOBOARD_TIMERState *s;
    auto_trifle at;

    s = opaque;

    /* naive timer */
    int64_t now = qemu_clock_get_ns(QEMU_CLOCK_VIRTUAL);
    timer_mod(s->timer, s->ns_per_cycle + now);

    /* trigger hwevt one cycle */
    switch(s->clkdev->type) {
        case STAT_MACH_CLKDEV_EVENT:
        {
            clkevt_stat_mach *mach;

            at.type = TRIFLE_HW_EVT;
            at.hw_evt = CLKEVT_HW_EVT_ONE_CYCLE;
            
            mach = s->clkdev->stat_mach;
            mach->dispatch(mach, &at);
        }
            break;

        case STAT_MACH_CLKDEV_SOURCE:
        {
            clksrc_stat_mach *mach;

            at.type = TRIFLE_HW_EVT;
            at.hw_evt = CLKSRC_HW_EVT_ONE_CYCLE;
            
            mach = s->clkdev->stat_mach;
            mach->dispatch(mach, &at);
        }
            break;

        default:
            assert("wierd timer type:" && s->clkdev->type && false);
            break;
    }
}

static uint32_t dispatch_mmio_rw(AUTOBOARD_TIMERState *s, auto_trifle *at)
{
    uint32_t triggered = 0;

    // using mmio_rw_once to infer which irq is involved
    // TODO: here may add trigger series feature
    switch (s->clkdev->type) {
    case STAT_MACH_CLKDEV_EVENT:
        {
        clkevt_stat_mach *mach = s->clkdev->stat_mach;
        triggered += mach->dispatch(mach, at);
        }
        break;

    case STAT_MACH_CLKDEV_SOURCE:
        {
        clksrc_stat_mach *mach = s->clkdev->stat_mach;
        triggered += mach->dispatch(mach, at);
        }
        break;

    case STAT_MACH_CLKDEV_EMPTY:
        break;

    default:
        printf("[+] wierd timer type %d\n", s->clkdev->type);
        break;
    }

    return triggered;
}

static uint64_t autoboard_timer_read(void *opaque, hwaddr offset, unsigned size, unsigned mmio_idx)
{
    AUTOBOARD_TIMERState *s;
    auto_trifle at;
    uint32_t triggered;
    uint32_t res;

    s = opaque;

    res = s->aummios[mmio_idx].read(&s->aummios[mmio_idx], offset);

    at.type = TRIFLE_KER_READ;
    at.mmio_idx = mmio_idx;
    at.off = offset;
    at.old_val = res;
    at.new_val = 0;

    triggered = dispatch_mmio_rw(s, &at);

    if (triggered) {
        // do nothing now
    }

    // read again as the mmio read may induce the change of mmio content
    res = s->aummios[mmio_idx].read(&s->aummios[mmio_idx], offset);

    //printf("[+] %s read idx %d off 0x%lx, size %d, value 0x%x, %u event(s) are triggered\n", s->name, mmio_idx, offset, size, res, triggered);
    return res;
}

static void autoboard_timer_write(void *opaque, hwaddr offset, uint64_t val, unsigned size, unsigned mmio_idx)
{
    AUTOBOARD_TIMERState *s;
    auto_trifle at;
    uint32_t triggered;

    s = opaque;

    // offset, old_value, new_value
    at.type = TRIFLE_KER_WRITE;
    at.mmio_idx = mmio_idx;
    at.off = offset;
    at.old_val = (uint64_t)s->aummios[mmio_idx].read(&s->aummios[mmio_idx], offset);
    at.new_val = val;

    // update the value
    s->aummios[mmio_idx].write(&s->aummios[mmio_idx], offset, val);

    triggered = dispatch_mmio_rw(s, &at);

    if (triggered) {
        // do nothing now
    }

    //printf("[+] %s write idx %d off 0x%lx, size %d, change value from 0x%lx to 0x%lx, %u event(s) are triggered\n", s->name, mmio_idx, at.off, size, at.old_val, at.new_val, triggered);
}

AUTOBOARD_MAKE_MMIO_RANGE_RW_FUNCS(timer, 0)

static const MemoryRegionOps autoboard_timer_ops[AUTOBOARD_TIMER_MMIO_REGION_NUM] = {
    AUTOBOARD_MMIO_OPS_STATIC_STRUCT(timer, 0)
};

static void autoboard_timer_init(Object *obj)
{
    AUTOBOARD_TIMERState *s = AUTOBOARD_TIMER(obj);
    int i;

    s->name = timer_name;
    s->cfg = get_autoboard_timer_config(choosen_id);
    s->is_level_irq = s->cfg->is_level_irq;
    s->ns_per_cycle = s->cfg->ns_per_cycle;
    s->act_irq = autoboard_timer_act_irq;
    s->deact_irq = autoboard_timer_deact_irq;

    /* initialize the mmio cache & the mmio */
    assert(s->cfg->mm_amount > 0 && s->cfg->mm_amount <= AUTOBOARD_TIMER_MMIO_REGION_NUM && "wierd s->cfg->mm_amount");

    s->mmios = calloc(s->cfg->mm_amount, sizeof(MemoryRegion));
    s->aummios = calloc(s->cfg->mm_amount, sizeof(autoboard_mmio));
    for (i = 0; i < s->cfg->mm_amount; i++) {
        s->aummios[i].mmio_len = s->cfg->mm_lens[i];
        s->aummios[i].caches = calloc(1, s->aummios[i].mmio_len);
        s->aummios[i].read = autoboard_mmio_read;
        s->aummios[i].write = autoboard_mmio_write;

        memory_region_init_io(&(s->mmios[i]), obj, &(autoboard_timer_ops[i]), s, TYPE_AUTOBOARD_TIMER, s->aummios[i].mmio_len);
        sysbus_init_mmio(SYS_BUS_DEVICE(s), &(s->mmios[i]));
    }

    /* initialize an irq to the timer */
    // TODO: ugly fix for the gic timer, re-do this when free
    if (choosen_id == AUTOBOARD_TIMER_OXNAS_GENERIC_MPTIMER)
        sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);
    else
        qdev_init_gpio_out(DEVICE(s), &s->irq, 1);


    /* setup the s->clkdev */
    s->clkdev = (timer_bundle *)calloc(1, sizeof(struct timer_bundle));
    s->clkdev->type = s->cfg->timer_cfgs->timer_type;
    switch(s->clkdev->type) {
        case STAT_MACH_CLKDEV_EMPTY:
            break;

        case STAT_MACH_CLKDEV_EVENT:
            s->clkdev->stat_mach = init_clkevt_stat_mach(s);
            break;

        case STAT_MACH_CLKDEV_SOURCE:
            s->clkdev->stat_mach = init_clksrc_stat_mach(s);
            break;

        default:
            assert("wierd timer type:" && s->clkdev->type && false);
            break;
    }

    /* initialize the timer finally*/
    s->timer = timer_new_ns(QEMU_CLOCK_VIRTUAL, autoboard_timer_tick_callback, s);
}

static void autoboard_timer_reset(DeviceState *dev)
{
    AUTOBOARD_TIMERState *s;
    auto_trifle at;

    s = AUTOBOARD_TIMER(dev);

    switch (s->clkdev->type) {
    case STAT_MACH_CLKDEV_EVENT:
        {
        clkevt_stat_mach *mach;

        at.type = TRIFLE_HW_EVT;
        at.hw_evt = CLKEVT_EVT_RESET;

        mach = s->clkdev->stat_mach;
        mach->dispatch(mach, &at);
        }
        break;

    case STAT_MACH_CLKDEV_SOURCE:
        {
        clksrc_stat_mach *mach;

        at.type = TRIFLE_HW_EVT;
        at.hw_evt = CLKSRC_EVT_RESET;

        mach = s->clkdev->stat_mach;
        mach->dispatch(mach, &at);
        }
        break;

    case STAT_MACH_CLKDEV_EMPTY:
        break;

    default:
        printf("[+] wierd timer type %d\n", s->clkdev->type);
        break;
    }

    // kickoff the timer
    autoboard_timer_tick_callback(s);
}

static void autoboard_timer_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = autoboard_timer_reset;
}

static TypeInfo autoboard_timer_type_info = {
    .name = TYPE_AUTOBOARD_TIMER,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(AUTOBOARD_TIMERState),
    .instance_init = autoboard_timer_init,
    /* .class_size = sizeof(SysBusDeviceClass), */
    .class_init = autoboard_timer_class_init,
};

static void autoboard_timer_register_types(void)
{
    type_register_static(&autoboard_timer_type_info);
}

type_init(autoboard_timer_register_types)
