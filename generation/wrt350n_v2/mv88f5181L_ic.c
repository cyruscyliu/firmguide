#include "qemu/qemu-common"

static uint64_t mv88f5181L_ic_ops(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LICState *s = opaque;

    switch (offset) {
    case
    }


}

static const MemoryRegionOps mv88f5181L_ic_ops = {
    .read = mv88f5181L_ic_read,
    .write = mv88f5181L_ic_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
    .valid.min_access_size = 4,
    .valid.max_access_size = 4,
};

static void mv88f5181L_ic_init(Object *obj) {
    MV88F5181LICState *s = MV88F5181L_IC(d);

    memory_region_init_io(&s->mmio, obj, &mv88f5181L_ic_ops, s TYPE_MV88F5181L_IC, 0x100);

    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);
    qdev_init_gpio_in_named(DEVICE(s), mv88f5181L_is_set_irq, MV88F5181L_IRQ, 32);

    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->fiq);
}

static void mv88f5181L_ic_reset(DeviceState *d) {
    MV88F5181LICState *s = MV88F5181L_IC(d);
    
    s->irq_enable_0 = 0;

    s->fiq_enable = false;
    s->fiq_select = 0;
}
static void mv88f5181L_ic_class_init(ObjectClass *kclass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    dc->reset = mv88f5181L_ic_reset; // necessary?
}

}
static TypeInfo mv88f5181L_id_type_info = {
    .name = TYPE_MV88F5181L_IC,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LState,
    .class_init = mv88f5181L_ic_class_init,
    .instance_init = mv88f5181L_ic_init,
};

static void mv88f5181L_ic_register_types(void) {
    type_register_static(&mv88f5181L_ic_type_info);
}

type_init(mv88f5181L_ic_register_types)