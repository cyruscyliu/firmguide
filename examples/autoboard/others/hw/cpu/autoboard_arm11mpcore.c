/*
 * ARM11MPCore internal peripheral emulation for autoboard.
 *
 * Written by Zhang Cen
 *
 * This code is licensed under the GPL.
 */

#include "qemu/osdep.h"
#include "qapi/error.h"
//#include "hw/cpu/arm11mpcore.h"
#include "hw/cpu/autoboard_arm11mpcore.h"
//#include "hw/intc/realview_gic.h"
#include "hw/intc/autoboard_intc.h"


static void mpcore_priv_set_irq(void *opaque, int irq, int level)
{
    AUTOBOARDARM11MPCorePriveState *s = (AUTOBOARDARM11MPCorePriveState *)opaque;

    qemu_set_irq(qdev_get_gpio_in(DEVICE(&s->aic), irq), level);
}

static void mpcore_priv_map_setup(AUTOBOARDARM11MPCorePriveState *s)
{
    int i;
    SysBusDevice *scubusdev = SYS_BUS_DEVICE(&s->scu);
    DeviceState *aicdev = DEVICE(&s->aic);
    SysBusDevice *aicbusdev = SYS_BUS_DEVICE(&s->aic);
    SysBusDevice *timerbusdev = SYS_BUS_DEVICE(&s->mptimer);
    //SysBusDevice *wdtbusdev = SYS_BUS_DEVICE(&s->wdtimer);

    memory_region_add_subregion(&s->container, 0,
                                sysbus_mmio_get_region(scubusdev, 0));
    /* GIC CPU interfaces: "current CPU" at 0x100, then specific CPUs
     * at 0x200, 0x300...
     */
    //for (i = 0; i < (s->num_cpu + 1); i++) {
    for (i = 0; i < s->num_cpu; i++) {
        hwaddr offset = 0x100 + (i * 0x100);
        memory_region_add_subregion(&s->container, offset,
                                    sysbus_mmio_get_region(aicbusdev, i + 1));
    }

    /* Add the regions for timer and watchdog for "current CPU" and
     * for each specific CPU.
     */
    //for (i = 0; i < (s->num_cpu + 1); i++) {
    for (i = 0; i < s->num_cpu; i++) {
        /* Timers at 0x600, 0x700, ...; watchdogs at 0x620, 0x720, ... */
        hwaddr offset = 0x600 + i * 0x100;
        memory_region_add_subregion(&s->container, offset,
                                    sysbus_mmio_get_region(timerbusdev, i));
        //memory_region_add_subregion(&s->container, offset + 0x20,
        //                            sysbus_mmio_get_region(wdtbusdev, i));
    }
    memory_region_add_subregion(&s->container, 0x1000,
                                sysbus_mmio_get_region(aicbusdev, 0));
    /* Wire up the interrupt from each watchdog and timer.
     * For each core the timer is PPI 29 and the watchdog PPI 30.
     */
    for (i = 0; i < s->num_cpu; i++) {
        sysbus_connect_irq(timerbusdev, i,
                           qdev_get_gpio_in(aicdev, 29));
        //int ppibase = (s->num_irq - 32) + i * 32;
        //sysbus_connect_irq(timerbusdev, i,
        //                   qdev_get_gpio_in(aicdev, ppibase + 29));
        //sysbus_connect_irq(wdtbusdev, i,
        //                   qdev_get_gpio_in(aicdev, ppibase + 30));
    }
}

static void mpcore_priv_realize(DeviceState *dev, Error **errp)
{
    SysBusDevice *sbd = SYS_BUS_DEVICE(dev);
    AUTOBOARDARM11MPCorePriveState *s = AUTOBOARDARM11MPCORE_PRIV(dev);
    DeviceState *scudev = DEVICE(&s->scu);
    //DeviceState *aicdev = DEVICE(&s->aic);
    //DeviceState *mptimerdev = DEVICE(&s->mptimer);
    //DeviceState *wdtimerdev = DEVICE(&s->wdtimer);
    Error *err = NULL;

    qdev_prop_set_uint32(scudev, "num-cpu", s->num_cpu);
    object_property_set_bool(OBJECT(&s->scu), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }

    //qdev_prop_set_uint32(aicdev, "num-cpu", s->num_cpu);
    //qdev_prop_set_uint32(aicdev, "num-irq", s->num_irq);
    //object_property_set_bool(OBJECT(&s->aic), true, "realized", &err);
    //if (err != NULL) {
    //    error_propagate(errp, err);
    //    return;
    //}
    object_property_set_bool(OBJECT(&s->aic), true, "realized", &err);
    if (err != NULL) {
        error_propagate(errp, err);
        return;
    }

    /* Pass through outbound IRQ lines from the GIC */
    sysbus_pass_irq(sbd, SYS_BUS_DEVICE(&s->aic));

    /* Pass through inbound GPIO lines to the GIC */
    //qdev_init_gpio_in(dev, mpcore_priv_set_irq, s->num_irq - 32);
    qdev_init_gpio_in(dev, mpcore_priv_set_irq, s->num_irq);

    //qdev_prop_set_uint32(mptimerdev, "num-cpu", s->num_cpu);
    //object_property_set_bool(OBJECT(&s->mptimer), true, "realized", &err);
    //if (err != NULL) {
    //    error_propagate(errp, err);
    //    return;
    //}
    object_property_set_bool(OBJECT(&s->mptimer), true, "realized", &err);

    //qdev_prop_set_uint32(wdtimerdev, "num-cpu", s->num_cpu);
    //object_property_set_bool(OBJECT(&s->wdtimer), true, "realized", &err);
    //if (err != NULL) {
    //    error_propagate(errp, err);
    //    return;
    //}

    mpcore_priv_map_setup(s);
}

static void mpcore_priv_initfn(Object *obj)
{
    SysBusDevice *sbd = SYS_BUS_DEVICE(obj);
    AUTOBOARDARM11MPCorePriveState *s = AUTOBOARDARM11MPCORE_PRIV(obj);

    memory_region_init(&s->container, OBJECT(s),
                       "mpcore-priv-container", 0x2000);
    sysbus_init_mmio(sbd, &s->container);

    sysbus_init_child_obj(obj, "scu", &s->scu, sizeof(s->scu), TYPE_ARM11_SCU);

    //sysbus_init_child_obj(obj, "aic", &s->aic, sizeof(s->aic), TYPE_AUTOBOARD_INTC);

    set_autoboard_intc_cfg(AUTOBOARD_INTC_OXNAS_GENERIC_GIC, "auto-gic");
    sysbus_init_child_obj(obj, "aic", &s->aic, sizeof(s->aic), TYPE_AUTOBOARD_INTC);
    //object_initialize(&s->aic, sizeof(s->aic), TYPE_AUTOBOARD_INTC);
    //qdev_set_parent_bus(DEVICE(&s->aic), sysbus_get_default());

    /* Request the legacy 11MPCore GIC behaviour: */
    //qdev_prop_set_uint32(DEVICE(&s->gic), "revision", 0);

    //sysbus_init_child_obj(obj, "mptimer", &s->mptimer, sizeof(s->mptimer),
    //                      TYPE_ARM_MPTIMER);

    set_autoboard_timer_cfg(AUTOBOARD_TIMER_OXNAS_GENERIC_MPTIMER, "auto-mptimer");
    sysbus_init_child_obj(obj, "mptimer", &s->mptimer, sizeof(s->mptimer), TYPE_AUTOBOARD_TIMER);
    //object_initialize(&s->timer0, sizeof(s->timer0), TYPE_AUTOBOARD_TIMER);
    //qdev_set_parent_bus(DEVICE(&s->timer0), sysbus_get_default());

    //sysbus_init_child_obj(obj, "wdtimer", &s->wdtimer, sizeof(s->wdtimer),
    //                      TYPE_ARM_MPTIMER);

}

static Property mpcore_priv_properties[] = {
    DEFINE_PROP_UINT32("num-cpu", AUTOBOARDARM11MPCorePriveState, num_cpu, 1),
    /* The ARM11 MPCORE TRM says the on-chip controller may have
     * anything from 0 to 224 external interrupt IRQ lines (with another
     * 32 internal). We default to 32+32, which is the number provided by
     * the ARM11 MPCore test chip in the Realview Versatile Express
     * coretile. Other boards may differ and should set this property
     * appropriately. Some Linux kernels may not boot if the hardware
     * has more IRQ lines than the kernel expects.
     */
    DEFINE_PROP_UINT32("num-irq", AUTOBOARDARM11MPCorePriveState, num_irq, 64),
    DEFINE_PROP_END_OF_LIST(),
};

static void mpcore_priv_class_init(ObjectClass *klass, void *data)
{
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->realize = mpcore_priv_realize;
    dc->props = mpcore_priv_properties;
}

static const TypeInfo mpcore_priv_info = {
    .name          = TYPE_AUTOBOARDARM11MPCORE_PRIV,
    .parent        = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(AUTOBOARDARM11MPCorePriveState),
    .instance_init = mpcore_priv_initfn,
    .class_init    = mpcore_priv_class_init,
};

static void autoboardarm11mpcore_register_types(void)
{
    type_register_static(&mpcore_priv_info);
}

type_init(autoboardarm11mpcore_register_types)
