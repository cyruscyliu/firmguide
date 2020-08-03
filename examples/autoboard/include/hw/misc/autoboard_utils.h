/*
 * autoboard timer common utility header file
 */

#ifndef TYPE_AUTOBOARD_UTILS_H
#define TYPE_AUTOBOARD_UTILS_H

#include "hw/sysbus.h"


/*
 * bit ops
 */ 

#define __bit(b) (1 << b)


/*
 * MMIO region related
 */

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

#define AUTOBOARD_MAKE_MMIO_RANGE_RW_FUNCS(name, idx) \
static uint64_t autoboard_##name##_read_range##idx(void *opaque, hwaddr offset, unsigned size)\
{\
    return autoboard_##name##_read(opaque, offset, size, idx);\
}\
static void autoboard_##name##_write_range##idx(void *opaque, hwaddr offset, uint64_t val, unsigned size)\
{\
    autoboard_##name##_write(opaque, offset, val, size, idx);\
}

#define AUTOBOARD_MMIO_OPS_STATIC_STRUCT(name, idx) \
    {\
        .read = autoboard_##name##_read_range##idx,\
        .write = autoboard_##name##_write_range##idx,\
        .endianness = DEVICE_LITTLE_ENDIAN,\
    },

#define AUTOBOARD_INTC_MMIO_REGION_NUM 2
#define AUTOBOARD_TIMER_MMIO_REGION_NUM 1

typedef struct autoboard_mmio {
    uint32_t mmio_len;
    unsigned char *caches;
    uint32_t (* read)(struct autoboard_mmio *mmio, hwaddr off);
    uint32_t (* write)(struct autoboard_mmio *mmio, hwaddr off, uint64_t val);
} autoboard_mmio;


/*
 * Definition of the trifle, presenting an outside event
 */

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
    uint32_t evt_arg;
} auto_trifle;

#endif /* TYPE_AUTOBOARD_UTILS_H */