{{license}}

#ifndef {{ic_name|upper}}_H
#define {{ic_name|upper}}_H

#include "hw/sysbus.h"

#define TYPE_{{ic_name|upper}} "{{ic_name}}"
#define {{ic_name|upper}}(obj) \
    OBJECT_CHECK({{ic_name|upper|concat}}State, (obj), TYPE_{{ic_name|upper}})

#define {{ic_name|upper}}_IRQ "irq"
#define {{ic_name|upper}}_N_IRQS "{{n_irqs}}"

#define MAIN_INTERRUPT_CAUSE_REGISTER         0x00
#define MAIN_IRQ_INTERRUPT_MASK_REGISTER      0x04
#define MAIN_FIQ_INTERRUPT_MASK_REGISTER      0x08
#define MAIN_ENDPOINT_INTERRUPT_MASK_REGISTER 0x0C

#define {{ic_name|upper}}_RAM_SIZE {{ic_ram_size}}

typedef struct {{ic_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    /* output to the cpu */
    qemu_irq irq;
    qemu_irq fiq;

    /* {{n_irqs}} IRQs */{% for i in i_irqs %}{% for n in l_irqs %}
    uint{{n}}_t irq_level_{{i}};
    uint{{n}}_t irq_enable_{{i}};
    uint{{n}}_t fiq_enable_{{i}};{% endfor %}{% endfor %}
} {{ic_name|upper|concat}}State;

static void {{ic_name}}_set_irq(void *opaque, int irq, int level);
static void {{ic_name}}_update({{ic_name|upper|concat}}State *s);
static void {{ic_name}}_reset(DeviceState *d);

static uint64_t {{ic_name}}_read(void *opaque, hwaddr offset, unsigned size);
static void {{ic_name}}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size);

static void {{ic_name}}_init(Object *obj);
static void {{ic_name}}_class_init(ObjectClass *kclass, void *data);
static void {{ic_name}}_register_types(void);

#endif /* {{ic_name|upper}}_H */