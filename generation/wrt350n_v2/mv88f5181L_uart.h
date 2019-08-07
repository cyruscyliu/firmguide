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

#define UART_RBR  0x00	/*  Receive Buffer Register (RBR) */
#define UART_THR  0x00	/*  Transmit Holding Register (THR) */
#define UART_DLL  0x00	/*  Divisor Latch Low (DLL) Register */
#define UART_IER  0x04	/*  Interrupt Enable Register (IER) */
#define UART_DLH  0x04	/*  Divisor Latch High (DLH) Register */
#define UART_IIR  0x08	/*  Interrupt Identity Register (IIR) */
#define UART_FCR  0x08	/*  FIFO Control Register (FCR) */
#define UART_LCR  0x0C	/*  Line Control Register (LCR) */
#define UART_MCR  0x10	/*  Modem Control Register (MCR) */
#define UART_LSR  0x14	/*  Line Status Register (LSR) */
#define UART_MSR  0x18	/*  Modem Status Register (MSR) */
#define UART_SCR  0x1C	/*  Scratch Pad Register (SCR) */

#define MV88F5181L_UART_RAM_SIZE 0x100
#define MV88F5181L_UART_RAM_BASE 0xf1012000

typedef struct MV88F5181LUARTState {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    MemoryRegion mmio;
    CharBackend chr;
    uint8_t lsr;
    uint8_t char_received;
    qemu_irq irq;
} MV88F5181LUARTState;

#endif /* MV88F5181L_UART_H */