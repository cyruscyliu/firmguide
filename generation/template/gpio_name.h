{{license}}

#ifndef {{gpio_name|upper}}_H
#define {{gpio_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{gpio_name|upper}} "{{gpio_name}}"
#define {{gpio_name|upper}}(obj) \
    OBJECT_CHECK({{gpio_name|upper|concat}}State, (obj), TYPE_{{gpio_name|upper}})

#define GPIO_DOR    0x00	/* GPIO Data Out Register */
#define GPIO_DOECR  0x04	/* GPIO Data Out Enable Control Register */
#define GPIO_BER    0x08	/* GPIO Blink Enable Register */
#define GPIO_DIPR   0x0C	/* GPIO Data In Polarity Register */
#define GPIO_DIR    0x10	/* GPIO Data In Register */
#define GPIO_ICR    0x14	/* GPIO Interrupt Cause Register */
#define GPIO_IMR    0x18	/* GPIO Interrupt Mask Register */
#define GPIO_ILMR   0x1C	/* GPIO Interrupt Level Mask Register */

#define {{gpio_name|upper}}_RAM_SIZE {{gpio_ram_size}}
#define {{gpio_name|upper}}_RAM_BASE {{gpio_ram_base}}

typedef struct {{gpio_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    uint32_t icr;
    uint32_t imr;
    uint32_t ilmr;
    qemu_irq out[{{gpio_n}}];
} {{gpio_name|upper|concat}}State;

#endif /* {{gpio_name|upper}}_H */