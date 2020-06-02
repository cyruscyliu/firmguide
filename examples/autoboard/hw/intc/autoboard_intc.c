/*
 * autoboard intc implementation
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "qapi/error.h"

#include "hw/intc/autoboard_utils.h"
#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_level_irq.h"
#include "hw/intc/autoboard_intc.h"

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

static uint64_t autoboard_intc_read(void *opaque, hwaddr offset, unsigned size)
{
    // as this is a read-only function, we may not need raise an event but read w/w.o lock
    AUTOBOARD_INTCState *s = opaque;

    uint32_t res = s->aummio->read(s->aummio, offset);
    return res;
}

static uint32_t get_related_irq(AUTOBOARD_INTCState *s, write_once *wep)
{
    for (uint32_t i = 0; i < s->in_irq_num; i++) {
        switch (s->in_irqs[i].type)
        {
        case STAT_MACH_LEVEL_IRQ:
            {
            level_irq_stat_mach *mach = s->in_irqs[i].stat_mach;
            if (mach->is_related(mach, wep))
                return i;
            }
            break;
        
        default:
            return -1;
        }
    }

    return -1;
}

static void autoboard_intc_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    AUTOBOARD_INTCState *s;
    write_once wo;
    uint32_t irq_idx, irq_event;
    uint8_t type;

    s = opaque;

    // offset, old_value, new_value
    wo.off = offset;
    wo.old_val = (uint64_t)s->aummio->read(s->aummio, offset);
    wo.new_val = val;

    // update the value
    s->aummio->write(s->aummio, offset, val);

    // using write_event to infer which irq is involved
    irq_idx = get_related_irq(s, &wo);
    if (irq_idx == -1)
        // -1 means unrelated noise
        return;

    // TODO: here may add trigger series feature
    type = s->in_irqs[irq_idx].type;
    switch (type)
    {
    case STAT_MACH_LEVEL_IRQ:
        {
        level_irq_stat_mach *mach = s->in_irqs[irq_idx].stat_mach;

        irq_event = mach->is_which_event(mach, &wo);
        if (irq_event == -1)
            // another noise
            return;

        // update irq status in its state machine
        mach->handle_event(mach, irq_event);
        }
        break;
    
    default:
        break;
    }
}

static const MemoryRegionOps autoboard_intc_ops = {
    .read = autoboard_intc_read,
    .write = autoboard_intc_write,
    .endianness = DEVICE_LITTLE_ENDIAN,
};

static void autoboard_intc_device_irq_cb(void *opaque, int irq, int level)
{
    AUTOBOARD_INTCState *s = opaque;

    // raise an irq act/deact event
    switch (s->in_irqs[irq].type)
    {
    case STAT_MACH_LEVEL_IRQ:
        {
        level_irq_stat_mach *mach = s->in_irqs[irq].stat_mach;
        if (level == 0)
            mach->handle_event(mach, LVL_EVT_ACT);
        else
            mach->handle_event(mach, LVL_EVT_DEACT);
        }
        break;
    
    default:
        return;
    }

}

static void autoboard_intc_init(Object *obj)
{
    AUTOBOARD_INTCState *s = AUTOBOARD_INTC(obj);

    init_autoboard_intc_config();

    /* initialize the mmio cache & the mmio */
    s->aummio = calloc(1, sizeof(autoboard_mmio));
    s->aummio->mmio_len = mmio_len;
    s->aummio->caches = calloc(1, s->aummio->mmio_len);
    s->aummio->read = autoboard_mmio_read;
    s->aummio->write = autoboard_mmio_write;

    memory_region_init_io(&s->mmio, obj, &autoboard_intc_ops, s, TYPE_AUTOBOARD_INTC, s->aummio->mmio_len);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the out irq to cpu */
    qdev_init_gpio_out_named(DEVICE(s), &s->irq, "irq2cpu", 1);

    /* initialize the in irqs connected with device */
    qdev_init_gpio_in_named(DEVICE(s), autoboard_intc_device_irq_cb, "irq2devs", autoboard_irq_num);

    // TODO: maybe some other init ops for members of s
    //       ...

    /* init irq related */
    s->in_irq_num = autoboard_irq_num;
    s->in_irqs = (irq_bundle *)calloc(autoboard_irq_num, sizeof(struct irq_bundle));

    for (uint32_t i = 0; i < s->in_irq_num; i++) {
        uint8_t type = autoboard_irq_cfgs[i].irq_type;
        s->in_irqs[i].type = type;
        switch(type) {
            case STAT_MACH_LEVEL_IRQ:
                s->in_irqs[i].stat_mach = init_level_irq_stat_mach(s, i);
                break;
            default:
                break;
        }
    }
}

static void autoboard_intc_reset(DeviceState *dev)
{
    AUTOBOARD_INTCState *s = AUTOBOARD_INTC(dev);

    // TODO: some other reset ops for members of s
    // ...

    // raise evt_reset event for all irqs
    for (uint32_t i = 0; i < s->in_irq_num; i++) {
        switch (s->in_irqs[i].type)
        {
        case STAT_MACH_LEVEL_IRQ:
            {
            level_irq_stat_mach *mach = s->in_irqs[i].stat_mach;
            mach->handle_event(mach, LVL_EVT_RESET);
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