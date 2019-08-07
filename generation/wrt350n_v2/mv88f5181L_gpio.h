/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_GPIO_H
#define MV88F5181L_GPIO_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_GPIO "mv88f5181L_gpio"
#define MV88F5181L_GPIO(obj) \
    OBJECT_CHECK(MV88F5181LGPIOState, (obj), TYPE_MV88F5181L_GPIO)

#define GPIO_DOR    0x00	/* GPIO Data Out Register */
#define GPIO_DOECR  0x04	/* GPIO Data Out Enable Control Register */
#define GPIO_BER    0x08	/* GPIO Blink Enable Register */
#define GPIO_DIPR   0x0C	/* GPIO Data In Polarity Register */
#define GPIO_DIR    0x10	/* GPIO Data In Register */
#define GPIO_ICR    0x14	/* GPIO Interrupt Cause Register */
#define GPIO_IMR    0x18	/* GPIO Interrupt Mask Register */
#define GPIO_ILMR   0x1C	/* GPIO Interrupt Level Mask Register */

#define MV88F5181L_GPIO_RAM_SIZE 0x100
#define MV88F5181L_GPIO_RAM_BASE 0xf1010100

typedef struct MV88F5181LGPIOState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    uint32_t icr;
    uint32_t imr;
    uint32_t ilmr;
    qemu_irq out[32];
} MV88F5181LGPIOState;

#endif /* MV88F5181L_GPIO_H */