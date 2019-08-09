/* 
 * automatically generated, don't change
 */

#include "hw/sysbus.h"
#include "chardev/char-fe.h"

#ifndef MV88F5181L_UART_H
#define MV88F5181L_UART_H

#define TYPE_MV88F5181L_UART "mv88f5181L_uart"
#define MV88F5181L_UART(obj) \
    OBJECT_CHECK(MV88F5181LUARTState, (obj), TYPE_MV88F5181L_UART)

#define UART_0_RECEIVE_BUFFER_REGISTER_RBR 0x000
#define UART_0_INTERRUPT_ENABLE_REGISTER_IER 0x004
#define UART_0_INTERRUPT_IDENTITY_REGISTER_IIR 0x008
#define UART_0_LINE_CONTROL_REGISTER_LCR 0x00c
#define UART_0_MODEM_CONTROL_REGISTER_MCR 0x010
#define UART_0_LINE_STATUS_REGISTER_LSR 0x014
#define UART_0_MODEM_STATUS_REGISTER_MSR 0x018
#define UART_0_SCRATCH_PAD_REGISTER_SCR 0x01c
#define UART_1_RECEIVE_BUFFER_REGISTER_RBR 0x100
#define UART_1_INTERRUPT_ENABLE_REGISTER_IER 0x104
#define UART_1_INTERRUPT_IDENTITY_REGISTER_IIR 0x108
#define UART_1_LINE_CONTROL_REGISTER_LCR 0x10c
#define UART_1_MODEM_CONTROL_REGISTER_MCR 0x110
#define UART_1_LINE_STATUS_REGISTER_LSR 0x114
#define UART_1_MODEM_STATUS_REGISTER_MSR 0x118
#define UART_1_SCRATCH_PAD_REGISTER_SCR 0x11c

#define MV88F5181L_UART_MMIO_SIZE 0x200
#define MV88F5181L_UART_MMIO_BASE 0xf1012000

typedef struct MV88F5181LUARTState {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    qemu_irq irq;
    CharBackend chr;

    MemoryRegion mmio;
    uint32_t uart_0_receive_buffer_register_rbr;
    uint32_t uart_0_interrupt_enable_register_ier;
    uint32_t uart_0_interrupt_identity_register_iir;
    uint32_t uart_0_line_control_register_lcr;
    uint32_t uart_0_modem_control_register_mcr;
    uint32_t uart_0_line_status_register_lsr;
    uint32_t uart_0_modem_status_register_msr;
    uint32_t uart_0_scratch_pad_register_scr;
    uint32_t uart_1_receive_buffer_register_rbr;
    uint32_t uart_1_interrupt_enable_register_ier;
    uint32_t uart_1_interrupt_identity_register_iir;
    uint32_t uart_1_line_control_register_lcr;
    uint32_t uart_1_modem_control_register_mcr;
    uint32_t uart_1_line_status_register_lsr;
    uint32_t uart_1_modem_status_register_msr;
    uint32_t uart_1_scratch_pad_register_scr;
    
} MV88F5181LUARTState;

#endif /* MV88F5181L_UART_H */