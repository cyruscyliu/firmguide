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
    /* MV88F5181LUARTState *s = opaque; */

    return 0;
}

static void mv88f5181L_uart_receive(void *opaque, const uint8_t *buf, int size) {
    MV88F5181LUARTState *s = opaque;
    mv88f5181L_uart_update(s);
}

static void mv88f5181L_uart_event(void *opaque, int event) {
}

static uint64_t mv88f5181L_uart_read(void *opaque, hwaddr offset, unsigned size) {
    MV88F5181LUARTState *s = (MV88F5181LUARTState *)opaque;

    uint64_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case UART_0_RECEIVE_BUFFER_REGISTER_RBR:
        res = s->uart_0_receive_buffer_register_rbr;
        break;
    case UART_0_INTERRUPT_ENABLE_REGISTER_IER:
        res = s->uart_0_interrupt_enable_register_ier;
        break;
    case UART_0_INTERRUPT_IDENTITY_REGISTER_IIR:
        res = s->uart_0_interrupt_identity_register_iir;
        break;
    case UART_0_LINE_CONTROL_REGISTER_LCR:
        res = s->uart_0_line_control_register_lcr;
        break;
    case UART_0_MODEM_CONTROL_REGISTER_MCR:
        res = s->uart_0_modem_control_register_mcr;
        break;
    case UART_0_LINE_STATUS_REGISTER_LSR:
        res = s->uart_0_line_status_register_lsr;
        break;
    case UART_0_MODEM_STATUS_REGISTER_MSR:
        res = s->uart_0_modem_status_register_msr;
        break;
    case UART_0_SCRATCH_PAD_REGISTER_SCR:
        res = s->uart_0_scratch_pad_register_scr;
        break;
    case UART_1_RECEIVE_BUFFER_REGISTER_RBR:
        res = s->uart_1_receive_buffer_register_rbr;
        break;
    case UART_1_INTERRUPT_ENABLE_REGISTER_IER:
        res = s->uart_1_interrupt_enable_register_ier;
        break;
    case UART_1_INTERRUPT_IDENTITY_REGISTER_IIR:
        res = s->uart_1_interrupt_identity_register_iir;
        break;
    case UART_1_LINE_CONTROL_REGISTER_LCR:
        res = s->uart_1_line_control_register_lcr;
        break;
    case UART_1_MODEM_CONTROL_REGISTER_MCR:
        res = s->uart_1_modem_control_register_mcr;
        break;
    case UART_1_LINE_STATUS_REGISTER_LSR:
        res = s->uart_1_line_status_register_lsr;
        break;
    case UART_1_MODEM_STATUS_REGISTER_MSR:
        res = s->uart_1_modem_status_register_msr;
        break;
    case UART_1_SCRATCH_PAD_REGISTER_SCR:
        res = s->uart_1_scratch_pad_register_scr;
        break;
    }
    return res;
}

static void mv88f5181L_uart_write(void *opaque, hwaddr offset, uint64_t val, unsigned size) {
    MV88F5181LUARTState *s = (MV88F5181LUARTState *)opaque;
    unsigned char c;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset 0x%"HWADDR_PRIx"\n", __func__, offset);
        return;
    case UART_0_RECEIVE_BUFFER_REGISTER_RBR:
        s->uart_0_receive_buffer_register_rbr = val;
        break;
    case UART_0_INTERRUPT_ENABLE_REGISTER_IER:
        s->uart_0_interrupt_enable_register_ier = val;
        break;
    case UART_0_INTERRUPT_IDENTITY_REGISTER_IIR:
        s->uart_0_interrupt_identity_register_iir = val;
        break;
    case UART_0_LINE_CONTROL_REGISTER_LCR:
        s->uart_0_line_control_register_lcr = val;
        break;
    case UART_0_MODEM_CONTROL_REGISTER_MCR:
        s->uart_0_modem_control_register_mcr = val;
        break;
    case UART_0_LINE_STATUS_REGISTER_LSR:
        s->uart_0_line_status_register_lsr = val;
        break;
    case UART_0_MODEM_STATUS_REGISTER_MSR:
        s->uart_0_modem_status_register_msr = val;
        break;
    case UART_0_SCRATCH_PAD_REGISTER_SCR:
        s->uart_0_scratch_pad_register_scr = val;
        break;
    case UART_1_RECEIVE_BUFFER_REGISTER_RBR:
        s->uart_1_receive_buffer_register_rbr = val;
        break;
    case UART_1_INTERRUPT_ENABLE_REGISTER_IER:
        s->uart_1_interrupt_enable_register_ier = val;
        break;
    case UART_1_INTERRUPT_IDENTITY_REGISTER_IIR:
        s->uart_1_interrupt_identity_register_iir = val;
        break;
    case UART_1_LINE_CONTROL_REGISTER_LCR:
        s->uart_1_line_control_register_lcr = val;
        break;
    case UART_1_MODEM_CONTROL_REGISTER_MCR:
        s->uart_1_modem_control_register_mcr = val;
        break;
    case UART_1_LINE_STATUS_REGISTER_LSR:
        s->uart_1_line_status_register_lsr = val;
        break;
    case UART_1_MODEM_STATUS_REGISTER_MSR:
        s->uart_1_modem_status_register_msr = val;
        break;
    case UART_1_SCRATCH_PAD_REGISTER_SCR:
        s->uart_1_scratch_pad_register_scr = val;
        break;
    }
    mv88f5181L_uart_update(s);
}

static const MemoryRegionOps mv88f5181L_uart_ops = {
    .read = mv88f5181L_uart_read,
    .write = mv88f5181L_uart_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};

static void mv88f5181L_uart_init(Object *obj) {
    MV88F5181LUARTState *s = MV88F5181L_UART(obj);

    /* initialize the mmio */
    memory_region_init_io(&s->mmio, obj, &mv88f5181L_uart_ops, s, "mv88f5181L_uart", MV88F5181L_UART_MMIO_SIZE);
    sysbus_init_mmio(SYS_BUS_DEVICE(s), &s->mmio);

    /* initialize the irq */
    sysbus_init_irq(SYS_BUS_DEVICE(s), &s->irq);

    /* initialize the chardev */
    qemu_chr_fe_set_handlers(&s->chr, mv88f5181L_uart_can_receive,
        mv88f5181L_uart_receive, mv88f5181L_uart_event, NULL, s, NULL, true);
}

static void mv88f5181L_uart_reset(DeviceState *dev) {
    MV88F5181LUARTState *s = MV88F5181L_UART(dev);
    
    s->uart_0_receive_buffer_register_rbr = 0;
    s->uart_0_interrupt_enable_register_ier = 0;
    s->uart_0_interrupt_identity_register_iir = 0;
    s->uart_0_line_control_register_lcr = 0;
    s->uart_0_modem_control_register_mcr = 0;
    s->uart_0_line_status_register_lsr = 0;
    s->uart_0_modem_status_register_msr = 0;
    s->uart_0_scratch_pad_register_scr = 0;
    s->uart_1_receive_buffer_register_rbr = 0;
    s->uart_1_interrupt_enable_register_ier = 0;
    s->uart_1_interrupt_identity_register_iir = 0;
    s->uart_1_line_control_register_lcr = 0;
    s->uart_1_modem_control_register_mcr = 0;
    s->uart_1_line_status_register_lsr = 0;
    s->uart_1_modem_status_register_msr = 0;
    s->uart_1_scratch_pad_register_scr = 0;
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