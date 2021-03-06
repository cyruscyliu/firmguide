/*
 * autoboard intc implementation
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"

#include "hw/intc/autoboard_intc_utils.h"
#include "hw/misc/autoboard_utils.h"
#include "hw/intc/autoboard_intc_gen.h"
#include "hw/intc/autoboard_edge_irq.h"
#include "hw/intc/autoboard_level_irq.h"
#include "hw/intc/autoboard_eoi_lvl_irq.h"
#include "hw/intc/autoboard_intc.h"

static autoboard_intc_cfg_id choosen_id = AUTOBOARD_INTC_INVALID;
static const char *intc_name = "anonymous";

void set_autoboard_intc_cfg(autoboard_intc_cfg_id id, const char *name)
{
    choosen_id = id; 
    intc_name = name;
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

// check whether an irq is act or not, and do the act/deact action based on the arg 3
static bool is_irq_act(AUTOBOARD_INTCState *s, int32_t irq_idx, int32_t action)
{
    uint8_t type;
    auto_trifle at;

    type = s->in_irqs[irq_idx].type;
    switch(type) {
    case STAT_MACH_IRQ_LEVEL:
        {
        level_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
        if (action == 1) {
            //printf("[+] send do act lvl hwevt on irq %d\n", irq_idx);
            at.type = TRIFLE_HW_EVT;
            at.hw_evt = LVL_HW_EVT_DOACT;
            mach->dispatch(mach, &at);
        }
        if (action == 2) {
            //printf("[+] send do deact lvl hwevt on irq %d\n", irq_idx);
            at.type = TRIFLE_HW_EVT;
            at.hw_evt = LVL_HW_EVT_DODEACT;
            mach->dispatch(mach, &at);
        }

        return mach->is_acted(mach);
        }
        break;
    
    case STAT_MACH_IRQ_EDGE:
        {
        edge_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
        if (action == 1) {
            //printf("[+] send do act edge hwevt on irq %d\n", irq_idx);
            at.type = TRIFLE_HW_EVT;
            at.hw_evt = EDGE_HW_EVT_DOACT;
            mach->dispatch(mach, &at);
        }
        if (action == 2) {
            //printf("[+] send do deact edge hwevt on irq %d\n", irq_idx);
            at.type = TRIFLE_HW_EVT;
            at.hw_evt = EDGE_HW_EVT_DODEACT;
            mach->dispatch(mach, &at);
        }

        return mach->is_acted(mach);
        }
        break;

    case STAT_MACH_IRQ_EOI_LVL:
        {
        eoi_lvl_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
        if (action == 1) {
            //printf("[+] send do act eoi lvl hwevt on irq %d\n", irq_idx);
            at.type = TRIFLE_HW_EVT;
            at.hw_evt = EOI_LVL_HW_EVT_DOACT;
            mach->dispatch(mach, &at);
        }
        if (action == 2) {
            //printf("[+] send do deact eoi lvl hwevt on irq %d\n", irq_idx);
            at.type = TRIFLE_HW_EVT;
            at.hw_evt = EOI_LVL_HW_EVT_DODEACT;
            mach->dispatch(mach, &at);
        }

        return mach->is_acted(mach);
        }
        break;
    case STAT_MACH_IRQ_EMPTY:
        return false;
        break;

    default:
        assert(false && "wierd irq type");
        break;
    }
}

// iterate all irqs beginning from start_idx, to find an act irq
static int32_t find_next_act_irq_round_robin(AUTOBOARD_INTCState *s, int32_t start_idx)
{
    int32_t i, irq_idx;
    uint8_t type;

    for (i = 0; i < s->in_irq_num; i++) {
        irq_idx = (start_idx + 1 + i) % (s->in_irq_num);
        type = s->in_irqs[irq_idx].type;
        switch(type) {
        case STAT_MACH_IRQ_LEVEL:
            {
            level_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
            if (mach->is_acted(mach))
                return irq_idx;
            }
            break;
    
        case STAT_MACH_IRQ_EDGE:
            {
            edge_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
            if (mach->is_acted(mach))
                return irq_idx;
            }
            break;

        case STAT_MACH_IRQ_EOI_LVL:
            {
            eoi_lvl_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
            if (mach->is_acted(mach))
                return irq_idx;
            }
            break;

        case STAT_MACH_IRQ_EMPTY:
            break;

        default:
            assert(false && "wierd irq type");
            break;
        }
    }

    // found nothing
    return -1;
}

static void autoboard_refresh_irq_lines(AUTOBOARD_INTCState *s)
{
    // we use round robin to activate irq
    int32_t *act_irq = &(s->act_irq);
    int32_t irq_idx;
    
    static int count = 0;
    count++;

    //printf("[+][%d] %s start refresh\n", count, s->name);

    if (*act_irq != -1) {
        if (is_irq_act(s, *act_irq, 0)) {
            // still act, do nothing
            is_irq_act(s, *act_irq, 1);
            //printf("[+][%d] %s keep raise irq %d\n", count, s->name, *act_irq);
            qemu_set_irq(s->irq, 1);
            //printf("[+][%d] %s end 1 refresh\n", count, s->name);
            return;
        } else {
            //printf("[+][%d] %s deact irq, irq %d\n", count, s->name, *act_irq);
            is_irq_act(s, *act_irq, 2);
        }
    }

    irq_idx = find_next_act_irq_round_robin(s, *act_irq);
    if (irq_idx == -1) {
        // no act irq
        *act_irq = -1;
        //printf("[+][%d] %s lower irq line off\n", count, s->name);
        qemu_set_irq(s->irq, 0);
    } else {
        // act act_irq 
        is_irq_act(s, irq_idx, 1);
        *act_irq = irq_idx;
        //printf("[+][%d] %s raise irq %d\n", count, s->name, irq_idx);
        qemu_set_irq(s->irq, 1);
    }

    //printf("[+][%d] %s end 2 refresh\n", count, s->name);
}

static uint32_t dispatch_mmio_rw(AUTOBOARD_INTCState *s, auto_trifle *at)
{
    uint8_t type;
    uint32_t irq_idx, triggered = 0;

    // using mmio_rw_once to infer which irq is involved
    for (irq_idx = 0; irq_idx < s->in_irq_num; irq_idx++) {
        // TODO: here may add trigger series feature
        type = s->in_irqs[irq_idx].type;
        switch (type) {
        case STAT_MACH_IRQ_LEVEL:
            {
            level_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
            triggered += mach->dispatch(mach, at);
            }
            break;
    
        case STAT_MACH_IRQ_EDGE:
            {
            edge_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
            triggered += mach->dispatch(mach, at);
            }
            break;

        case STAT_MACH_IRQ_EOI_LVL:
            {
            eoi_lvl_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;
            triggered += mach->dispatch(mach, at);
            }
            break;

        case STAT_MACH_IRQ_EMPTY:
            break;

        default:
            printf("[+] wierd irq type %d\n", type);
            break;
        }
    }

    return triggered;
}

static uint64_t autoboard_intc_read(void *opaque, hwaddr offset, unsigned size, unsigned mmio_idx)
{
    // as this is a read-only function, we may not need raise an event but read w/w.o lock
    AUTOBOARD_INTCState *s;
    auto_trifle at;
    uint32_t triggered;
    uint64_t res;

    s = opaque;

    res = s->aummios[mmio_idx].read(&s->aummios[mmio_idx], offset);

    at.type = TRIFLE_KER_READ;
    at.mmio_idx = mmio_idx;
    at.off = offset;
    at.old_val = res;
    at.new_val = 0;

    triggered = dispatch_mmio_rw(s, &at);

    if (triggered) 
        autoboard_refresh_irq_lines(s);

    // read again as the mmio read may induce the change of mmio content
    res = s->aummios[mmio_idx].read(&s->aummios[mmio_idx], offset);

    //printf("[+] %s read idx %d off 0x%lx, size %d, value 0x%lx, %d event(s) are triggered\n", s->name, mmio_idx, offset, size, res, triggered);

    return res;
}

static void autoboard_intc_write(void *opaque, hwaddr offset, uint64_t val, unsigned size, unsigned mmio_idx)
{
    AUTOBOARD_INTCState *s;
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

    if (triggered) 
        autoboard_refresh_irq_lines(s);

    //printf("[+] %s write idx %d off 0x%lx, size %d, change value from 0x%lx to 0x%lx, %d event(s) are triggered\n", s->name, mmio_idx, at.off, size, at.old_val, at.new_val, triggered);
}

AUTOBOARD_MAKE_MMIO_RANGE_RW_FUNCS(intc, 0)
AUTOBOARD_MAKE_MMIO_RANGE_RW_FUNCS(intc, 1)

static const MemoryRegionOps autoboard_intc_ops[AUTOBOARD_INTC_MMIO_REGION_NUM] = {
    AUTOBOARD_MMIO_OPS_STATIC_STRUCT(intc, 0)
    AUTOBOARD_MMIO_OPS_STATIC_STRUCT(intc, 1)
};

static void autoboard_intc_device_irq_cb(void *opaque, int irq, int level)
{
    AUTOBOARD_INTCState *s;
    auto_trifle at;

    s = opaque;

    // too many
    //printf("[+] come into autoboard intc callback for irq #%d %s\n", irq, (level == 0)?("act"):("deact"));

    // raise an irq act/deact event
    switch (s->in_irqs[irq].type)
    {
    case STAT_MACH_IRQ_LEVEL:
        {
        level_irq_stat_mach *mach;

        at.type = TRIFLE_HW_EVT;
        if (level)
            at.hw_evt = LVL_EVT_ACT;
        else
            at.hw_evt = LVL_EVT_DEACT;

        mach = s->in_irqs[irq].stat_mach;
        mach->dispatch(mach, &at);
        }
        break;
    
    case STAT_MACH_IRQ_EDGE:
        {
        edge_irq_stat_mach *mach;

        at.type = TRIFLE_HW_EVT;
        if (level)
            at.hw_evt = EDGE_HW_EVT_PULSE_UP;
        else
            at.hw_evt = EDGE_HW_EVT_PULSE_DOWN;

        mach = s->in_irqs[irq].stat_mach;
        mach->dispatch(mach, &at);
        }
        break;
    
    case STAT_MACH_IRQ_EOI_LVL:
        {
        eoi_lvl_irq_stat_mach *mach;

        at.type = TRIFLE_HW_EVT;
        if (level)
            at.hw_evt = EOI_LVL_EVT_ACT;
        else
            at.hw_evt = EOI_LVL_EVT_DEACT;

        mach = s->in_irqs[irq].stat_mach;
        mach->dispatch(mach, &at);
        }
        break;
    
    default:
        return;
        break;
    }

    autoboard_refresh_irq_lines(s);
}

static void autoboard_intc_init(Object *obj)
{
    AUTOBOARD_INTCState *s = AUTOBOARD_INTC(obj);
    int i;

    s->act_irq = -1;
    s->name = intc_name;
    s->cfg = get_autoboard_intc_config(choosen_id);

    /* initialize the mmio cache & the mmio */
    assert(s->cfg->mm_amount > 0 && s->cfg->mm_amount <= AUTOBOARD_INTC_MMIO_REGION_NUM && "wierd s->cfg->mm_amount");

    s->mmios = calloc(s->cfg->mm_amount, sizeof(MemoryRegion));
    s->aummios = calloc(s->cfg->mm_amount, sizeof(autoboard_mmio));
    for (i = 0; i < s->cfg->mm_amount; i++) {
        s->aummios[i].mmio_len = s->cfg->mm_lens[i];
        s->aummios[i].caches = calloc(1, s->aummios[i].mmio_len);
        s->aummios[i].read = autoboard_mmio_read;
        s->aummios[i].write = autoboard_mmio_write;

        memory_region_init_io(&(s->mmios[i]), obj, &(autoboard_intc_ops[i]), s, TYPE_AUTOBOARD_INTC, s->aummios[i].mmio_len);
        sysbus_init_mmio(SYS_BUS_DEVICE(s), &(s->mmios[i]));
    }

    // TODO: ugly fix for init value of one addr in oxnas.gic
    if (choosen_id == AUTOBOARD_INTC_OXNAS_GENERIC_GIC)
        s->aummios[0].write(&s->aummios[0], 0x4, 0x1);

    /* initialize the out irq to cpu */
    // seems xxx & xxx_named cannot be mixly used
    //qdev_init_gpio_out_named(DEVICE(s), &s->irq, "irq2cpu", 1);
    // TODO: another ugly fix for the gic, re-do this when free
    if (choosen_id == AUTOBOARD_INTC_OXNAS_GENERIC_GIC)
        sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);
    else
        qdev_init_gpio_out(DEVICE(s), &s->irq, 1);

    /* initialize the in irqs connected with device */
    //printf("autoboard_irq_num %d\n", s->cfg->irq_num);
    //qdev_init_gpio_in_named(DEVICE(s), autoboard_intc_device_irq_cb, "irq2devs", s->cfg->irq_num);
    qdev_init_gpio_in(DEVICE(s), autoboard_intc_device_irq_cb, s->cfg->irq_num);

    // TODO: maybe some other init ops for members of s
    //       ...

    /* init irq related */
    s->in_irq_num = s->cfg->irq_num;
    s->in_irqs = (irq_bundle *)calloc(s->cfg->irq_num, sizeof(struct irq_bundle));

    for (uint32_t i = 0; i < s->in_irq_num; i++) {
        uint8_t type = s->cfg->irq_cfgs[i].irq_type;
        s->in_irqs[i].type = type;
        switch(type) {
            case STAT_MACH_IRQ_EMPTY:
                break;
            case STAT_MACH_IRQ_LEVEL:
                s->in_irqs[i].stat_mach = init_level_irq_stat_mach(s, i);
                break;
            case STAT_MACH_IRQ_EDGE:
                s->in_irqs[i].stat_mach = init_edge_irq_stat_mach(s, i);
                break;
            case STAT_MACH_IRQ_EOI_LVL:
                s->in_irqs[i].stat_mach = init_eoi_lvl_irq_stat_mach(s, i);
                break;
            default:
                assert("wierd irq type:" && type && false);
                break;
        }
    }
}

static void autoboard_intc_reset(DeviceState *dev)
{
    AUTOBOARD_INTCState *s;
    auto_trifle at;

    s = AUTOBOARD_INTC(dev);

    // TODO: some other reset ops for members of s
    // ...

    // raise evt_reset event for all irqs
    for (uint32_t i = 0; i < s->in_irq_num; i++) {
        switch (s->in_irqs[i].type)
        {
        case STAT_MACH_IRQ_LEVEL:
            {
            level_irq_stat_mach *mach;

            at.type = TRIFLE_HW_EVT;
            at.hw_evt = LVL_EVT_RESET;

            mach = s->in_irqs[i].stat_mach;
            mach->dispatch(mach, &at);
            }
            break;
        
        case STAT_MACH_IRQ_EDGE:
            {
            edge_irq_stat_mach *mach;

            at.type = TRIFLE_HW_EVT;
            at.hw_evt = EDGE_EVT_RESET;

            mach = s->in_irqs[i].stat_mach;
            mach->dispatch(mach, &at);
            }
            break;

        case STAT_MACH_IRQ_EOI_LVL:
            {
            eoi_lvl_irq_stat_mach *mach;

            at.type = TRIFLE_HW_EVT;
            at.hw_evt = EOI_LVL_EVT_RESET;

            mach = s->in_irqs[i].stat_mach;
            mach->dispatch(mach, &at);
            }
            break;

        default:
            break;
        }
    }
}

static void autoboard_intc_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = autoboard_intc_reset;
}

static TypeInfo autoboard_intc_type_info = {
    .name = TYPE_AUTOBOARD_INTC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(AUTOBOARD_INTCState),
    .instance_init = autoboard_intc_init,
    .class_init = autoboard_intc_class_init,
};

static void autoboard_intc_register_types(void)
{
    type_register_static(&autoboard_intc_type_info);
}

type_init(autoboard_intc_register_types)