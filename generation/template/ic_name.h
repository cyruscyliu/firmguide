#ifndef {{soc_name|upper}}_IC_H
#define {{soc_name|upper}}_IC_H

#include "hw/sysbus.h"

#define TYPE_{{soc_name|upper}}_IC "{{soc_name}}-ic"
#define {{soc_name|upper}}_IC(obj) OBJECT_CHECK({{soc_name|upper}}ICState, (obj), TYPE_{{soc_name|upper}}_IC)

#define {{soc_name|upper}}_IC_IRQ "{{soc_name}}-irq"

typedef struct {{soc_name|upper}}ICState {
    /*< private >*/
    SysBusDevice sysbus;
    /*< public >*/

    MemoryRegion mmio;
    qemu_irq irq;
    qemu_irq fiq;

    /* {{n_irqs}} IRQs */{% for i in i_irqs %}{% for n in l_irqs %}
    uint{{n}}_t irq_level_{{i}}, irq_enable_{{i}};{% endfor %}{% endfor %}

    bool fiq_enable;
    uint{{b_fiqs}}_t fiq_select;
} {{soc_name|upper}}ICState