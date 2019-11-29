# Code Generation

## QEMU Programming Model

### Layered Devices 

```text
                                        /-> SysBusDeviceClass/State
MachineClass/State -> DeviceClass/State  
                                        \-> CPU
```

### Register a Device

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
### `machine_class_init` and `machine_init`

### Initialize and Realize a Device

#### Traditional Approach

#### Direct Implementation

### Headers

`qemu/osdep.h` is very helpful.

## Multi-Level Template Based Code Generation

### Template for Aeblia Device Models

[bridge.c](./template/bridge.c), [bridge.h](./template/bridge.h), 
[interrupt_controller.c](./template/ic.c), [interrupt_controller.h](./template/ic.h), 
[timer.c](./template/timer.c), [timer.h](./template/timer.h)

### Code Snippets for Device Components

### Template for Direct Programming Model

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
