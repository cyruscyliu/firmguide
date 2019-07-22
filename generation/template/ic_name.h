{{license}}

#ifndef {{ic_name|upper}}_H
#define {{ic_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{ic_name|upper}} "{{ic_name}}"
#define {{ic_name|upper}}(obj) \
    OBJECT_CHECK({{soc_name|upper}}ICState, (obj), TYPE_{{ic_name|upper}})

#define {{ic_name|upper}}_IRQ "irq"

#define MAIN_INTERRUPT_CAUSE_REGISTER         0x00
#define MAIN_IRQ_INTERRUPT_MASK_REGISTER      0x04
#define MAIN_FIQ_INTERRUPT_MASK_REGISTER      0x08
#define MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER 0x0C

typedef struct {{soc_name|upper}}ICState {
    /*< private >*/
    SysBusDevice sysbus;
    /*< public >*/

    MemoryRegion mmio;
    qemu_irq irq;
    qemu_irq fiq;

    /* {{n_irqs}} IRQs */{% for i in i_irqs %}{% for n in l_irqs %}
    uint{{n}}_t irq_level_{{i}};
    uint{{n}}_t irq_enable_{{i}};
    uint{{n}}_t fiq_enable_{{i}};{% endfor %}{% endfor %}
} {{soc_name|upper}}ICState;

#endif /* {{ic_name|upper}}_H */