{{license}}

#include "hw/sysbus.h"
#include "chardev/char-fe.h"

#ifndef {{uart_name|upper}}_H
#define {{uart_name|upper}}_H

#define TYPE_{{uart_name|upper}} "{{uart_name}}"
#define {{uart_name|upper|concat}}(obj) \
    OBJECT_CHECK({{uart_name|upper|concat}}State, (obj), TYPE_{{uart_name|upper}})

#define UART_RBR  0x00	/*  Receive Buffer Register (RBR) */
#define UART_THR  0x00	/*  Transmit Holding Register (THR) */
#define UART_DLLR 0x00	/*  Divisor Latch Low (DLL) Register */
#define UART_IER  0x04	/*  Interrupt Enable Register (IER) */
#define UART_DLHR 0x04	/*  Divisor Latch High (DLH) Register */
#define UART_IIR  0x08	/*  Interrupt Identity Register (IIR) */
#define UART_FCR  0x08	/*  FIFO Control Register (FCR) */
#define UART_LCR  0x0C	/*  Line Control Register (LCR) */
#define UART_MCR  0x10	/*  Modem Control Register (MCR) */
#define UART_LSR  0x14	/*  Line Status Register (LSR) */
#define UART_MSR  0x18	/*  Modem Status Register (MSR) */
#define UART_SCR  0x1C	/*  Scratch Pad Register (SCR) */

#define {{uart_name|upper}}_RAM_SIZE {{uart_ram_size}}

typedef struct {{uart_name|upper|concat}}State {
    /* <private> */
    SysBusDevice sys_bus;
    /* <public> */

    MemoryRegion mmio;
    CharBackend chr;
    uint8_t isr;
    uint8_t char_received;
    qemu_irq irq;
} {{uart_name|upper|concat}}State;

#endif /* {{uart_name|upper}}_H */