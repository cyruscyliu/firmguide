/*
 * autoboard common utility header file
 */

#ifndef TYPE_AUTOBOARD_UTILS_H
#define TYPE_AUTOBOARD_UTILS_H

#include "hw/sysbus.h"

#define __u32_native(p) (*(uint32_t *) (p))
#define __u32_big(p) \
    ((uint32_t) \
    (((*(uint8_t *) (p)) << 24) | \
     ((*(uint8_t *) (p)) << 16) | \
     ((*(uint8_t *) (p)) << 8) | \
     ((*(uint8_t *) (p)) << 0)) )
#define __u32_little(p) \
    ((uint32_t) \
    (((*(uint8_t *) (p)) << 0) | \
     ((*(uint8_t *) (p)) << 8) | \
     ((*(uint8_t *) (p)) << 16) | \
     ((*(uint8_t *) (p)) << 24)) )

#define __swap32(num) \
    (((num)>>24)&0xff) | \
    (((num)<<8)&0xff0000) | \
    (((num)>>8)&0xff00) | \
    (((num)<<24)&0xff000000)

#define TRIFLE_INVALID       0
#define TRIFLE_KER_READ      1
#define TRIFLE_KER_WRITE     2
#define TRIFLE_HW_EVT        3

typedef struct auto_trifle {
    int type;
    // kernel read & write use the off & old value
    // this specifies the index of mmio regions
    uint32_t mmio_idx;
    hwaddr off;
    uint64_t old_val;
    // only kernel write use the new value
    uint64_t new_val;
    // onlt hw event use the following
    uint32_t hw_evt;
} auto_trifle;

#endif /* TYPE_AUTOBOARD_UTILS_H */