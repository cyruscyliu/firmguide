/* 
 * automatically generated, don't change
 */

#ifndef MV88F5181L_H
#define MV88F5181L_H

#include "hw/sysbus.h"
#include "hw/initc/mv88f5181L_ic.h"
#include "hw/gpio/mv88f5181L_gpio"

#define TYPE_MV88F5181L "mv88f5181L"
#define MV88F5181L(obj) \
    OBJECT_CHECK(MV88F5181LState, (obj), TYPE_MV88F5181L)

typedef struct MV88F5181LState {
    /*< private >*/
    DeviceState parent_obj;
    /*< public >*/

    char *cpu_type;
    ARMCPU cpu;

    MV88F5181LPeripheralState peripherals;
} MV88F5181LState;

#endif /* MV88F5181L_H */