{{license}}

#ifndef {{peripheral_name|upper}}_H
#define {{peripheral_name|upper}}_H

#include "hw/sysbus.h"
#include "hw/timer/{{timer_name}}.h"
#include "hw/char/{{uart_name}}.h"
#include "hw/gpio/{{gpio_name}}.h"

#define TYPE_{{peripheral_name|upper}} "{{peripheral_name|upper}}"
#define {{peripheral_name|upper}}(obj) \
    OBJECT_CHECK({{peripheral_name|upper|concat}}State, (obj),  TYPE_{{peripheral_name|upper}})
#define {{peripheral_name|upper}}_RAM_SIZE {{peripheral_ram_size}}

typedef struct {{peripheral_name|upper|concat}}State {
    /*< private >*/
    SysBusDevice sys_bus;
    /*< public >*/

    MemoryRegion mmio;
    {{timer_name|upper|concat}}State timer;
    {{uart_name|upper|concat}}State uart;
    {{gpio_name|upper|concat}}State gpio;
} {{peripheral_name|upper|concat}}State;

#endif /* {{peripheral_name|upper}}_H */