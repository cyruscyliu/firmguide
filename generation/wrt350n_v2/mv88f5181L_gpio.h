/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_GPIO_H
#define MV88F5181L_GPIO_H

#include "hw/sysbus.h"

#define TYPE_MV88F5181L_GPIO "mv88f5181L_gpio"
#define MV88F5181L_GPIO(obj) \
    OBJECT_CHECK(MV88F5181LGPIOState, (obj), TYPE_MV88F5181L_GPIO)

#define GPIO_DATA_OUT_REGISTER 0x00
#define GPIO_DATA_OUT_ENABLE_CONTROL_REGISTER 0x04
#define GPIO_BLINK_ENABLE_REGISTER 0x08
#define GPIO_DATA_IN_POLARITY_REGISTER 0x0c
#define GPIO_DATA_IN_REGISTER 0x10
#define GPIO_INTERRUPT_CAUSE_REGISTER 0x14
#define GPIO_INTERRUPT_MASK_REGISTER 0x18
#define GPIO_INTERRUPT_LEVEL_MASK_REGISTER 0x1c

#define MV88F5181L_GPIO_MMIO_SIZE 0x100
#define MV88F5181L_GPIO_MMIO_BASE 0xf1010100

typedef struct MV88F5181LGPIOState {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion gpio_mmio;
    qemu_irq irq[4];
    qemu_irq out[26];

    uint32_t gpio_data_out_register;
    uint32_t gpio_data_out_enable_control_register;
    uint32_t gpio_blink_enable_register;
    uint32_t gpio_data_in_polarity_register;
    uint32_t gpio_data_in_register;
    uint32_t gpio_interrupt_cause_register;
    uint32_t gpio_interrupt_mask_register;
    uint32_t gpio_interrupt_level_mask_register;
    
} MV88F5181LGPIOState;

#endif /* MV88F5181L_GPIO_H */