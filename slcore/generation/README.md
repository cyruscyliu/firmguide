# Code Generation

### QEMU Programming Model

#### Layered Devices 

```text
                                        /-> SysBusDeviceClass/State
MachineClass/State -> DeviceClass/State  
                                        \-> CPU
```

#### Register a Device

```c
#include “hw/…/your_custom.h”  
static TypeInfo your_custom_type_info = {  
    .name = TYPE_YOUR_CUSTOM_NAME,  
    .parent = TYPE_SYS_BUS_DEVICE, // or else, see above  
    .instance_size = sizeof(YourCustomState),  
    .instance_init = your_custom_init,  
    /* .class_size = sizeof(SysBusDeviceClass), */ // or else, see above  
    .class_init = your_custom_class_init,  
};  

static void your_custom_register_types(void) {  
    type_register_static(&your_custom_type_info);  
}  
```
#### `machine_class_init` and `machine_init`

#### Initialize and Realize a Device

##### Traditional Approach

##### Direct Implementation

#### Headers

`qemu/osdep.h` is very helpful.

### Multi-Level Template Based Code Generation

#### Template for Aeblia Device Models

[bridge.c](templates/bridge.c), [bridge.h](templates/bridge.h), 
[interrupt_controller.c](templates/ic.c), [interrupt_controller.h](templates/ic.h), 
[timer.c](templates/timer.c), [timer.h](templates/timer.h)

#### Code Snippets for Device Components

Define(register) a machine.
```text
DEFINE_MACHINE("wrt350n_v2", wrt350n_v2_machine_init)
```

machine_init & machine_class_init
```text
static void wrt350n_v2_machine_init(MachineClass *mc)
{
    /* mc->name = "wrt350n_v2"; */
    mc->desc = "Linksys WRT350N v2 (MV88F5181L)";
    mc->init = wrt350n_v2_init;
    mc->default_ram_size = 32 * MiB;
    mc->default_cpu_type = ARM_CPU_TYPE_NAME("arm926");
    mc->ignore_memory_transaction_failures = true;
}
```
```text
static void wrt350n_v2_init(MachineState *machine)
{
    WRT350NV2State *s = g_new0(WRT350NV2State, 1);
    Error *err = NULL;
    DriveInfo *dinfo;
    static struct arm_boot_info binfo;

    s->cpu = ARM_CPU(object_new(machine->cpu_type));
    object_property_set_bool(OBJECT(s->cpu), true, "realized", &err);
    memory_region_allocate_system_memory(&s->ram, OBJECT(machine), "ram", machine->ram_size);
    memory_region_add_subregion_overlap(get_system_memory(), 0, &s->ram, 0);
    object_initialize(&s->ic, sizeof(s->ic), TYPE_MV88F5181L_IC);
    qdev_set_parent_bus(DEVICE(&s->ic), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->ic), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->ic), 0, 0xf1020200);
    object_initialize(&s->bridge, sizeof(s->bridge), TYPE_MV88F5181L_BRIDGE);
    qdev_set_parent_bus(DEVICE(&s->bridge), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->bridge), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->bridge), 0, 0xf1020100);
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->bridge), 0, qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 0));
    object_initialize(&s->timer, sizeof(s->timer), TYPE_MV88F5181L_TIMER);
    qdev_set_parent_bus(DEVICE(&s->timer), sysbus_get_default());
    object_property_set_bool(OBJECT(&s->timer), true, "realized", &err);
    sysbus_mmio_map(SYS_BUS_DEVICE(&s->timer), 0, 0xf1020300);
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), 0, qdev_get_gpio_in_named(DEVICE(&s->bridge), BRIDGE_IRQ, 1));
    sysbus_connect_irq(SYS_BUS_DEVICE(&s->timer), 1, qdev_get_gpio_in_named(DEVICE(&s->bridge), BRIDGE_IRQ, 2));
    serial_mm_init(get_system_memory(), 0xf1012000, 2, qdev_get_gpio_in_named(DEVICE(&s->ic), MV88F5181L_IC_IRQ, 3), 115200, serial_hd(0), DEVICE_LITTLE_ENDIAN);
    dinfo = drive_get(IF_PFLASH, 0, 0);
    pflash_cfi01_register(0xf4000000, "flash", 8 * MiB, dinfo ? blk_by_legacy_dinfo(dinfo): NULL, 64 * KiB, 4, 0, 0, 0, 0, 0);

    memory_region_init_io(&s->mv88f5181l_gpio_mmio, NULL, &mv88f5181l_gpio_ops, s, TYPE_WRT350N_V2, 0x100);
    memory_region_add_subregion_overlap(get_system_memory(), 0xf1010100, &s->mv88f5181l_gpio_mmio, 0);
    memory_region_init_io(&s->mv88f5181l_cpu_address_map_mmio, NULL, &mv88f5181l_cpu_address_map_ops, s, TYPE_WRT350N_V2, 0x100);
    // ...

    wrt350n_v2_reset(s);

    qdev_connect_gpio_out_named(DEVICE(&s->ic), "irq", 0, qdev_get_gpio_in(DEVICE(s->cpu), ARM_CPU_IRQ));
    binfo.board_id = 0x661;
    binfo.ram_size = machine->ram_size;
    binfo.kernel_filename = machine->kernel_filename;
    binfo.kernel_cmdline = machine->kernel_cmdline;
    binfo.initrd_filename = machine->initrd_filename;
    arm_load_kernel(ARM_CPU(first_cpu), &binfo);
}
```

MMIO operations.
```text
static void mv88f5181l_gpio_update(void *opaque)
{
    /* WRT350NV2State *s = opaque; */
}

static uint64_t mv88f5181l_gpio_read(void *opaque, hwaddr offset, unsigned size)
{
    WRT350NV2State *s = opaque;
    uint32_t res = 0;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return 0;
    case 0x00 ... 0x1C:
        res = s->gpio_reserved;
        break;
    }
    return res;
}

static void mv88f5181l_gpio_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{
    WRT350NV2State *s = opaque;

    switch (offset) {
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\n", __func__, offset);
        return;
    case 0x00 ...0x1C:
        s->gpio_reserved = val;
        break;
    }
    mv88f5181l_gpio_update(s);
}

static const MemoryRegionOps mv88f5181l_gpio_ops = {
    .read = mv88f5181l_gpio_read,
    .write = mv88f5181l_gpio_write,
    .endianness = DEVICE_NATIVE_ENDIAN,
};
```

Related structs.

```text
#define TYPE_WRT350N_V2 "wrt350n_v2"
#define WRT350N_V2(obj) \
    OBJECT_CHECK(WRT350NV2State, (obj), TYPE_WRT350N_V2)

typedef struct WRT350NV2State {
    ARMCPU *cpu;
    MemoryRegion ram;
    MV88F5181LICState ic;
    MV88F5181LBRIDGEState bridge;
    MV88F5181LTIMERState timer;
    MemoryRegion mv88f5181l_gpio_mmio;
    uint32_t gpio_reserved;
} WRT350NV2State;
```

And includings.
```text
#include "qemu/osdep.h"
#include "qemu/log.h"
#include "hw/sysbus.h"
#include "target/arm/cpu-qom.h"
#include "exec/address-spaces.h"
#include "hw/intc/mv88f5181l_ic.h"
#include "hw/arm/mv88f5181l_bridge.h"
#include "hw/timer/mv88f5181l_timer.h"
#include "hw/char/serial.h"
#include "sysemu/blockdev.h"
#include "hw/block/flash.h"
#include "hw/arm/arm.h"
#include "qemu/units.h"
#include "target/arm/cpu.h"
#include "hw/boards.h"
```

#### Template for Direct Programming Model

```text
*(license)
*(includings)
*(defines)
*(struct)
*(mmio_ops)
    *(update)
    *(read)
    *(write)
    *(ops)
*(machine_init)
*(machine_class_init)
*(define_machine)
```
