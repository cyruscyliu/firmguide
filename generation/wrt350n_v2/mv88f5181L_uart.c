/* 
 * automatically generated, don't change
 */

#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/char/mv88f5181L_uart.h"
#include "chardev/char-fe.h"

static int mv88f5181L_uart_can_receive(void *opaque);
static void mv88f5181L_uart_receive(void *opaque, const uint8_t *buf, int size);
static void mv88f5181L_uart_event(void *opaque, int event);

static void mv88f5181L_uart_update(void *opaque);
static void mv88f5181L_uart_reset(DeviceState *dev);

static uint64_t mv88f5181L_uart_read(void *opaque, hwaddr offset, unsigned size);
static void mv88f5181L_uart_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void mv88f5181L_uart_init(Object *obj);
static void mv88f5181L_uart_class_init(ObjectClass *klass, void *data);
static void mv88f5181L_uart_register_types(void);

static void mv88f5181L_uart_update(void *opaque) {
    /* MV88F5181LUARTState *s = opaque; */
}

static int mv88f5181L_uart_can_receive(void *opaque) {
    /* MV88F5181LUARTState *s = (MV88F5181LUARTState *)opaque; */

    return 0;
}

static void mv88f5181L_uart_receive(void *opaque, const uint8_t *buf, int size) {
    MV88F5181LUARTState *s = (MV88F5181LUARTState *)opaque;

    s->char_received = *buf;
    mv88f5181L_uart_update(s);
}

static void mv88f5181L_uart_event(void *opaque, int event) {
}

static uint64_t mv88f5181L_uart_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LUARTState *s = (MV88F5181LUARTState *)opaque;

    uint64_t res = 0;

    switch (offset) {
    case UART_RBR:  /*  Receive Buffer Register (RBR) */
    /* case UART_THR: */  /*  Transmit Holding Register (THR) */
    /* case UART_DLL: */  /*  Divisor Latch Low (DLL) Register */
        /* do nothing */
        break;
    case UART_IER:  /*  Interrupt Enable Register (IER) */
    /* case UART_DLH: */  /*  Divisor Latch High (DLH) Register */
        /* do nothing */
        break;
    case UART_IIR:  /*  Interrupt Identity Register (IIR) */
    /* case UART_FCR: */  /*  FIFO Control Register (FCR) */
        /* do nothing */
        break;
    case UART_LCR:  /*  Line Control Register (LCR) */
        /* do nothing */
        break;
    case UART_MCR:  /*  Modem Control Register (MCR) */
        /* do nothing */
        break;
    case UART_LSR:  /*  Line Status Register (LSR) */
        res = s->lsr;
        break;
    case UART_MSR:  /*  Modem Status Register (MSR) */
        /* do nothing */
        break;
    case UART_SCR:  /*  Scratch Pad Register (SCR) */
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        res = 0;
    }

    return res;
}

static void mv88f5181L_uart_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LUARTState *s = opaque;
    unsigned char c;

    switch (offset) {
    case UART_RBR:  /*  Receive Buffer Register (RBR) */
    /* case UART_THR: */  /*  Transmit Holding Register (THR) */
    /* case UART_DLL: */  /*  Divisor Latch Low (DLL) Register */
        c = val;
        qemu_chr_fe_write(&s->chr, &c, 1);
        mv88f5181L_uart_update(s);
        break;
    case UART_IER:  /*  Interrupt Enable Register (IER) */
    /* case UART_DLH: */  /*  Divisor Latch High (DLH) Register */
        /* do nothing */
        break;
    case UART_IIR:  /*  Interrupt Identity Register (IIR) */
    /* case UART_FCR: */  /*  FIFO Control Register (FCR) */
        /* do nothing */
        break;
    case UART_LCR:  /*  Line Control Register (LCR) */
        /* do nothing */
        break;
    case UART_MCR:  /*  Modem Control Register (MCR) */
        /* do nothing */
        break;
    case UART_LSR:  /*  Line Status Register (LSR) */
        /* do nothing */
        break;
    case UART_MSR:  /*  Modem Status Register (MSR) */
        /* do nothing */
        break;
    case UART_SCR:  /*  Scratch Pad Register (SCR) */
        /* do nothing */
        break;
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    }
}

static const MemoryRegionOps mv88f5181L_uart_ops = {
    .read = mv88f5181L_uart_read,
    .write = mv88f5181L_uart_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_uart_init(Object *obj) {
    MV88F5181LUARTState *s = MV88F5181LUART(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_uart_ops, s, "mv88f5181L_uart", MV88F5181L_UART_RAM_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize the chardev */
    qemu_chr_fe_set_handlers(&s->chr, mv88f5181L_uart_can_receive,
        mv88f5181L_uart_receive, mv88f5181L_uart_event, NULL, s, NULL, true);
}

static void mv88f5181L_uart_reset(DeviceState *dev) {
    MV88F5181LUARTState *s = MV88F5181LUART(dev);

    s->lsr = 0x20;
    s->char_received = 0;
}

static void mv88f5181L_uart_class_init(ObjectClass *klass, void *data) {
    DeviceClass *dc = DEVICE_CLASS(klass);

    /* dc->fw_name = ; */
    /* dc->desc = ; */
    /* dc->props = ; */
    /* dc->user_creatable = ; */
    /* dc->hotpluggable = ; */
    dc->reset = mv88f5181L_uart_reset;
    /* dc->realize = ; */
    /* dc->unrealize = ; */
    /* dc->vmsd = ; */
    /* dc->bus_type = ; */

    /* SysBusDeviceClass sbc = SYS_BUS_DEVICE_CLASS(klass); */

    /* sbc->explicit_ofw_unit_address = ; */
    /* sbc->connect_irq_notifier = ; */
}

static const TypeInfo mv88f5181L_uart_info = {
    .name = TYPE_MV88F5181L_UART,
    .parent = TYPE_SYS_BUS_DEVICE,
    .instance_size = sizeof(MV88F5181LUARTState),
    .instance_init = mv88f5181L_uart_init,
    /* .class_zie = sizeof(SysBusDeviceClass), */
    .class_init = mv88f5181L_uart_class_init,
};

static void mv88f5181L_uart_register_types(void) {
    type_register_static(&mv88f5181L_uart_info);
}

type_init(mv88f5181L_uart_register_types)