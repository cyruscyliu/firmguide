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

typedef struct write_once {
    hwaddr off;
    uint64_t old_val;
    uint64_t new_val;
} write_once;

#endif /* TYPE_AUTOBOARD_UTILS_H */