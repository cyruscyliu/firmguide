#ifndef _FAKE_GNUEXT_H
#define _FAKE_GNUEXT_H

#define __attribute __attribute__
#define __attribute__(...)
#define __extension__

#define __asm__ asm
#define asm(...)
#define __volatile__ volatile
#define volatile(...)

#define __signed__ signed
#define __const__ const

#define __alignof__(...) 0
#define __builtin_constant_p(...) 0
#define __builtin_memset memset
#define __builtin_memcpy memcpy
#define __typeof__ typeof
#define __typeof typeof
#define typeof(...) void
#define __builtin_expect(...) 0

#endif /* _FAKE_GNUEXT_H */

