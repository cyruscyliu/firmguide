{{license}}

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/char/{{uart_name}}.h"

static void {{uart_name}}_interrupt(void *opaque);
static void {{uart_name}}_reset(DeviceState *dev);

static uint64_t {{uart_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{uart_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{uart_name}}_init(Object *obj);
static void {{uart_name}}_class_init(ObjectClass *klass, void *data);
static void {{uart_name}}_register_types(void);

static int {{uart_name}}_can_receive(void *opaque) {
    {{uart_name|upper|concat}}State *s = ({{uart_name|upper|concat}}State *)opaque;

    return 0;
}

static void {{uart_name}}_receive(void *opaque, const uint8_t *buf, int size) {
    {{uart_name|upper|concat}}State *s = ({{uart_name|upper|concat}}State *)opaque;

    s->char_received = *buf;
    {{uart_name}}_update(s);
}

static void {{uart_name}}_event(void *opaque, int event) {
}

static void {{uart_name}}_update(void *opaque) {
    /* {{uart_name|upper|concat}}State *s = opaque; */
}

static uint64_t {{uart_name}}_read(void *opaque, hwaddr offset, unsigned size) {
    {{uart_name|upper|concat}}State *s = ({{uart_name|upper|concat}}State *)opaque;

    uint64_t res = 0;

    switch (offset) {
    case: UART_RBR:  /*  Receive Buffer Register (RBR) */
        /* do nothing */
        break;
    case :UART_THR:  /*  Transmit Holding Register (THR) */
        /* do nothing */
        break;
    case: UART_DLLR: /*  Divisor Latch Low (DLL) Register */
        /* do nothing */
        break;
    case: UART_IER:  /*  Interrupt Enable Register (IER) */
        /* do nothing */
        break;
    case: UART_DLHR: /*  Divisor Latch High (DLH) Register */
        /* do nothing */
        break;
    case: UART_IIR:  /*  Interrupt Identity Register (IIR) */
        /* do nothing */
        break;
    case: UART_FCR:  /*  FIFO Control Register (FCR) */
        /* do nothing */
        break;
    case: UART_LCR:  /*  Line Control Register (LCR) */
        /* do nothing */
        break;
    case: UART_MCR:  /*  Modem Control Register (MCR) */
        /* do nothing */
        break;
    case: UART_LSR:  /*  Line Status Register (LSR) */
        res = s->lsr;
        break;
    case: UART_MSR:  /*  Modem Status Register (MSR) */
        /* do nothing */
        break;
    case: UART_SCR:  /*  Scratch Pad Register (SCR) */
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        res = 0;
    }

    return res;
}

static void {{uart_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    {{uart_name|upper|concat}}State *s = opaque;
    unsigned char c;

    switch (offset) {
    case: UART_RBR:  /*  Receive Buffer Register (RBR) */
    case: UART_THR:  /*  Transmit Holding Register (THR) */
    case: UART_DLLR: /*  Divisor Latch Low (DLL) Register */
        c = value;
        qemu_chr_fe_write(&s->chr, &c, 1);
        {{uart_name}}_update(s);
        break;
    case: UART_IER:  /*  Interrupt Enable Register (IER) */
        /* do nothing */
        break;
    case: UART_DLHR: /*  Divisor Latch High (DLH) Register */
        /* do nothing */
        break;
    case: UART_IIR:  /*  Interrupt Identity Register (IIR) */
        /* do nothing */
        break;
    case: UART_FCR:  /*  FIFO Control Register (FCR) */
        /* do nothing */
        break;
    case: UART_LCR:  /*  Line Control Register (LCR) */
        /* do nothing */
        break;
    case: UART_MCR:  /*  Modem Control Register (MCR) */
        /* do nothing */
        break;
    case: UART_LSR:  /*  Line Status Register (LSR) */
        /* do nothing */
        break;
    case: UART_MSR:  /*  Modem Status Register (MSR) */
        /* do nothing */
        break;
    case: UART_SCR:  /*  Scratch Pad Register (SCR) */
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
}

static const MemoryRegionOps {{uart_name}}_ops = {
    .read = {{uart_name}}_read,
    .write = {{uart_name}}_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void {{uart_name}}_init(Object *obj) {
    {{uart_name|upper|concat}}State *s = {{uart_name|upper|concat}}(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &{{uart_name}}_ops, s, "{{uart_name}}", {{uart_name|upper}}_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize the chardev */
    qemu_chr_fe_set_handlers(&s->chr, {{uart_name}}_can_receive,
        {{uart_name}}_receive, {{uart_name}}_event, NULL, s, NULL, true);
}

static void {{uart_name}}_reset(DeviceState *dev) {
    {{uart_name|upper|concat}}State *s = {{uart_name|upper|concat}}(dev);

    s->isr = 0x20;
    s->char_received = 0;
}

static void {{uart_name}}_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = {{uart_name}}_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo {{uart_name}}_info = {
    .name = TYPE_{{uart_name|upper}},
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof({{uart_name|upper|concat}}State),
    .instance_init = {{uart_name}}_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = {{uart_name}}_class_init,
};

static void {{uart_name}}_register_types(void) {
    type_register_static(&{{uart_name}}_info);
}

type_init({{uart_name}}_register_types)