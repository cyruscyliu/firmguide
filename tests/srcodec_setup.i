# 1 "arch/mips/ath79/setup.c"
# 1 "/root/openwrt-build-docker/share/15.05-cc3a47a374475253f93a08eea6eaadce/chaos_calmer-15.05/build_dir/target-mips_34kc_uClibc-0.9.33.2/linux-ar71xx_generic/linux-3.18.20//"
# 1 "<command-line>"
# 1 "././include/linux/kconfig.h" 1



# 1 "include/generated/autoconf.h" 1
# 5 "././include/linux/kconfig.h" 2
# 1 "<command-line>" 2
# 1 "arch/mips/ath79/setup.c"
# 15 "arch/mips/ath79/setup.c"
# 1 "include/linux/kernel.h" 1




# 1 "/root/firmware/15.05-cc3a47a374475253f93a08eea6eaadce/chaos_calmer-15.05/staging_dir/toolchain-mips_34kc_gcc-4.8-linaro_uClibc-0.9.33.2/lib/gcc/mips-openwrt-linux-uclibc/4.8.3/include/stdarg.h" 1 3 4
# 40 "/root/firmware/15.05-cc3a47a374475253f93a08eea6eaadce/chaos_calmer-15.05/staging_dir/toolchain-mips_34kc_gcc-4.8-linaro_uClibc-0.9.33.2/lib/gcc/mips-openwrt-linux-uclibc/4.8.3/include/stdarg.h" 3 4
typedef __builtin_va_list __gnuc_va_list;
# 98 "/root/firmware/15.05-cc3a47a374475253f93a08eea6eaadce/chaos_calmer-15.05/staging_dir/toolchain-mips_34kc_gcc-4.8-linaro_uClibc-0.9.33.2/lib/gcc/mips-openwrt-linux-uclibc/4.8.3/include/stdarg.h" 3 4
typedef __gnuc_va_list va_list;
# 6 "include/linux/kernel.h" 2
# 1 "include/linux/linkage.h" 1



# 1 "include/linux/compiler.h" 1
# 54 "include/linux/compiler.h"
# 1 "include/linux/compiler-gcc.h" 1
# 106 "include/linux/compiler-gcc.h"
# 1 "include/linux/compiler-gcc4.h" 1
# 107 "include/linux/compiler-gcc.h" 2
# 55 "include/linux/compiler.h" 2
# 79 "include/linux/compiler.h"
struct ftrace_branch_data {
 const char *func;
 const char *file;
 unsigned line;
 union {
  struct {
   unsigned long correct;
   unsigned long incorrect;
  };
  struct {
   unsigned long miss;
   unsigned long hit;
  };
  unsigned long miss_hit[2];
 };
};
# 189 "include/linux/compiler.h"
# 1 "include/uapi/linux/types.h" 1



# 1 "./arch/mips/include/asm/types.h" 1
# 14 "./arch/mips/include/asm/types.h"
# 1 "include/asm-generic/int-ll64.h" 1
# 10 "include/asm-generic/int-ll64.h"
# 1 "include/uapi/asm-generic/int-ll64.h" 1
# 11 "include/uapi/asm-generic/int-ll64.h"
# 1 "./arch/mips/include/uapi/asm/bitsperlong.h" 1





# 1 "include/asm-generic/bitsperlong.h" 1



# 1 "include/uapi/asm-generic/bitsperlong.h" 1
# 5 "include/asm-generic/bitsperlong.h" 2
# 7 "./arch/mips/include/uapi/asm/bitsperlong.h" 2
# 12 "include/uapi/asm-generic/int-ll64.h" 2







typedef __signed__ char __s8;
typedef unsigned char __u8;

typedef __signed__ short __s16;
typedef unsigned short __u16;

typedef __signed__ int __s32;
typedef unsigned int __u32;


__extension__ typedef __signed__ long long __s64;
__extension__ typedef unsigned long long __u64;
# 11 "include/asm-generic/int-ll64.h" 2




typedef signed char s8;
typedef unsigned char u8;

typedef signed short s16;
typedef unsigned short u16;

typedef signed int s32;
typedef unsigned int u32;

typedef signed long long s64;
typedef unsigned long long u64;
# 15 "./arch/mips/include/asm/types.h" 2
# 1 "./arch/mips/include/uapi/asm/types.h" 1
# 16 "./arch/mips/include/asm/types.h" 2
# 28 "./arch/mips/include/asm/types.h"
typedef unsigned long phys_t;
# 5 "include/uapi/linux/types.h" 2
# 13 "include/uapi/linux/types.h"
# 1 "./include/uapi/linux/posix_types.h" 1



# 1 "include/linux/stddef.h" 1



# 1 "include/uapi/linux/stddef.h" 1
# 1 "include/linux/compiler.h" 1
# 1 "include/uapi/linux/stddef.h" 2
# 5 "include/linux/stddef.h" 2





enum {
 false = 0,
 true = 1
};
# 5 "./include/uapi/linux/posix_types.h" 2
# 24 "./include/uapi/linux/posix_types.h"
typedef struct {
 unsigned long fds_bits[1024 / (8 * sizeof(long))];
} __kernel_fd_set;


typedef void (*__kernel_sighandler_t)(int);


typedef int __kernel_key_t;
typedef int __kernel_mqd_t;

# 1 "./arch/mips/include/uapi/asm/posix_types.h" 1
# 12 "./arch/mips/include/uapi/asm/posix_types.h"
# 1 "./arch/mips/include/uapi/asm/sgidefs.h" 1
# 13 "./arch/mips/include/uapi/asm/posix_types.h" 2







typedef long __kernel_daddr_t;



typedef struct {
 long val[2];
} __kernel_fsid_t;



# 1 "./include/uapi/asm-generic/posix_types.h" 1
# 14 "./include/uapi/asm-generic/posix_types.h"
typedef long __kernel_long_t;
typedef unsigned long __kernel_ulong_t;



typedef __kernel_ulong_t __kernel_ino_t;



typedef unsigned int __kernel_mode_t;



typedef int __kernel_pid_t;



typedef int __kernel_ipc_pid_t;



typedef unsigned int __kernel_uid_t;
typedef unsigned int __kernel_gid_t;



typedef __kernel_long_t __kernel_suseconds_t;







typedef unsigned int __kernel_uid32_t;
typedef unsigned int __kernel_gid32_t;



typedef __kernel_uid_t __kernel_old_uid_t;
typedef __kernel_gid_t __kernel_old_gid_t;



typedef unsigned int __kernel_old_dev_t;
# 67 "./include/uapi/asm-generic/posix_types.h"
typedef unsigned int __kernel_size_t;
typedef int __kernel_ssize_t;
typedef int __kernel_ptrdiff_t;
# 86 "./include/uapi/asm-generic/posix_types.h"
typedef __kernel_long_t __kernel_off_t;
typedef long long __kernel_loff_t;
typedef __kernel_long_t __kernel_time_t;
typedef __kernel_long_t __kernel_clock_t;
typedef int __kernel_timer_t;
typedef int __kernel_clockid_t;
typedef char * __kernel_caddr_t;
typedef unsigned short __kernel_uid16_t;
typedef unsigned short __kernel_gid16_t;
# 31 "./arch/mips/include/uapi/asm/posix_types.h" 2
# 36 "./include/uapi/linux/posix_types.h" 2
# 14 "include/uapi/linux/types.h" 2
# 32 "include/uapi/linux/types.h"
typedef __u16 __le16;
typedef __u16 __be16;
typedef __u32 __le32;
typedef __u32 __be32;
typedef __u64 __le64;
typedef __u64 __be64;

typedef __u16 __sum16;
typedef __u32 __wsum;
# 190 "include/linux/compiler.h" 2

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void data_access_exceeds_word_size(void)

__attribute__((warning("data access exceeds word size and won't be atomic")))

;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void data_access_exceeds_word_size(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void __read_once_size(const volatile void *p, void *res, int size)
{
 switch (size) {
 case 1: *(__u8 *)res = *(volatile __u8 *)p; break;
 case 2: *(__u16 *)res = *(volatile __u16 *)p; break;
 case 4: *(__u32 *)res = *(volatile __u32 *)p; break;



 default:
  __asm__ __volatile__("": : :"memory");
  __builtin_memcpy((void *)res, (const void *)p, size);
  data_access_exceeds_word_size();
  __asm__ __volatile__("": : :"memory");
 }
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void __write_once_size(volatile void *p, void *res, int size)
{
 switch (size) {
 case 1: *(volatile __u8 *)p = *(__u8 *)res; break;
 case 2: *(volatile __u16 *)p = *(__u16 *)res; break;
 case 4: *(volatile __u32 *)p = *(__u32 *)res; break;



 default:
  __asm__ __volatile__("": : :"memory");
  __builtin_memcpy((void *)p, (const void *)res, size);
  data_access_exceeds_word_size();
  __asm__ __volatile__("": : :"memory");
 }
}
# 5 "include/linux/linkage.h" 2
# 1 "include/linux/stringify.h" 1
# 6 "include/linux/linkage.h" 2
# 1 "include/linux/export.h" 1
# 26 "include/linux/export.h"
struct kernel_symbol
{
 unsigned long value;
 const char *name;
};
# 7 "include/linux/linkage.h" 2
# 1 "./arch/mips/include/asm/linkage.h" 1
# 8 "include/linux/linkage.h" 2
# 7 "include/linux/kernel.h" 2

# 1 "include/linux/types.h" 1
# 12 "include/linux/types.h"
typedef __u32 __kernel_dev_t;

typedef __kernel_fd_set fd_set;
typedef __kernel_dev_t dev_t;
typedef __kernel_ino_t ino_t;
typedef __kernel_mode_t mode_t;
typedef unsigned short umode_t;
typedef __u32 nlink_t;
typedef __kernel_off_t off_t;
typedef __kernel_pid_t pid_t;
typedef __kernel_daddr_t daddr_t;
typedef __kernel_key_t key_t;
typedef __kernel_suseconds_t suseconds_t;
typedef __kernel_timer_t timer_t;
typedef __kernel_clockid_t clockid_t;
typedef __kernel_mqd_t mqd_t;

typedef _Bool bool;

typedef __kernel_uid32_t uid_t;
typedef __kernel_gid32_t gid_t;
typedef __kernel_uid16_t uid16_t;
typedef __kernel_gid16_t gid16_t;

typedef unsigned long uintptr_t;
# 45 "include/linux/types.h"
typedef __kernel_loff_t loff_t;
# 54 "include/linux/types.h"
typedef __kernel_size_t size_t;




typedef __kernel_ssize_t ssize_t;




typedef __kernel_ptrdiff_t ptrdiff_t;




typedef __kernel_time_t time_t;




typedef __kernel_clock_t clock_t;




typedef __kernel_caddr_t caddr_t;



typedef unsigned char u_char;
typedef unsigned short u_short;
typedef unsigned int u_int;
typedef unsigned long u_long;


typedef unsigned char unchar;
typedef unsigned short ushort;
typedef unsigned int uint;
typedef unsigned long ulong;




typedef __u8 u_int8_t;
typedef __s8 int8_t;
typedef __u16 u_int16_t;
typedef __s16 int16_t;
typedef __u32 u_int32_t;
typedef __s32 int32_t;



typedef __u8 uint8_t;
typedef __u16 uint16_t;
typedef __u32 uint32_t;


typedef __u64 uint64_t;
typedef __u64 u_int64_t;
typedef __s64 int64_t;
# 130 "include/linux/types.h"
typedef u64 sector_t;
typedef u64 blkcnt_t;
# 149 "include/linux/types.h"
typedef u32 dma_addr_t;
# 158 "include/linux/types.h"
typedef unsigned gfp_t;
typedef unsigned fmode_t;
typedef unsigned oom_flags_t;




typedef u32 phys_addr_t;


typedef phys_addr_t resource_size_t;





typedef unsigned long irq_hw_number_t;

typedef struct {
 int counter;
} atomic_t;







struct list_head {
 struct list_head *next, *prev;
};

struct hlist_head {
 struct hlist_node *first;
};

struct hlist_node {
 struct hlist_node *next, **pprev;
};

struct ustat {
 __kernel_daddr_t f_tfree;
 __kernel_ino_t f_tinode;
 char f_fname[6];
 char f_fpack[6];
};






struct callback_head {
 struct callback_head *next;
 void (*func)(struct callback_head *head);
};


struct net_hdr_word {
       u32 words[1];
} __attribute__((packed, aligned(2)));
# 9 "include/linux/kernel.h" 2

# 1 "include/linux/bitops.h" 1
# 27 "include/linux/bitops.h"
extern unsigned int __sw_hweight8(unsigned int w);
extern unsigned int __sw_hweight16(unsigned int w);
extern unsigned int __sw_hweight32(unsigned int w);
extern unsigned long __sw_hweight64(__u64 w);





# 1 "./arch/mips/include/asm/bitops.h" 1
# 18 "./arch/mips/include/asm/bitops.h"
# 1 "./arch/mips/include/asm/barrier.h" 1
# 11 "./arch/mips/include/asm/barrier.h"
# 1 "./arch/mips/include/asm/addrspace.h" 1
# 13 "./arch/mips/include/asm/addrspace.h"
# 1 "./arch/mips/include/asm/mach-generic/spaces.h" 1
# 13 "./arch/mips/include/asm/mach-generic/spaces.h"
# 1 "./include/uapi/linux/const.h" 1
# 14 "./arch/mips/include/asm/mach-generic/spaces.h" 2
# 14 "./arch/mips/include/asm/addrspace.h" 2
# 12 "./arch/mips/include/asm/barrier.h" 2
# 19 "./arch/mips/include/asm/bitops.h" 2
# 1 "./arch/mips/include/uapi/asm/byteorder.h" 1
# 12 "./arch/mips/include/uapi/asm/byteorder.h"
# 1 "include/linux/byteorder/big_endian.h" 1



# 1 "include/uapi/linux/byteorder/big_endian.h" 1
# 12 "include/uapi/linux/byteorder/big_endian.h"
# 1 "include/linux/swab.h" 1



# 1 "include/uapi/linux/swab.h" 1





# 1 "./arch/mips/include/uapi/asm/swab.h" 1
# 19 "./arch/mips/include/uapi/asm/swab.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u16 __arch_swab16(__u16 x)
{
 __asm__(
 "	.set	push			\n"
 "	.set	arch=mips32r2		\n"
 "	wsbh	%0, %1			\n"
 "	.set	pop			\n"
 : "=r" (x)
 : "r" (x));

 return x;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u32 __arch_swab32(__u32 x)
{
 __asm__(
 "	.set	push			\n"
 "	.set	arch=mips32r2		\n"
 "	wsbh	%0, %1			\n"
 "	rotr	%0, %0, 16		\n"
 "	.set	pop			\n"
 : "=r" (x)
 : "r" (x));

 return x;
}
# 7 "include/uapi/linux/swab.h" 2
# 46 "include/uapi/linux/swab.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u16 __fswab16(__u16 val)
{



 return __arch_swab16(val);



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u32 __fswab32(__u32 val)
{



 return __arch_swab32(val);



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u64 __fswab64(__u64 val)
{





 __u32 h = val >> 32;
 __u32 l = val & ((1ULL << 32) - 1);
 return (((__u64)__fswab32(l)) << 32) | ((__u64)(__fswab32(h)));



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u32 __fswahw32(__u32 val)
{



 return ((__u32)( (((__u32)(val) & (__u32)0x0000ffffUL) << 16) | (((__u32)(val) & (__u32)0xffff0000UL) >> 16)));

}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__)) __u32 __fswahb32(__u32 val)
{



 return ((__u32)( (((__u32)(val) & (__u32)0x00ff00ffUL) << 8) | (((__u32)(val) & (__u32)0xff00ff00UL) >> 8)));

}
# 154 "include/uapi/linux/swab.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u16 __swab16p(const __u16 *p)
{



 return (__builtin_constant_p((__u16)(*p)) ? ((__u16)( (((__u16)(*p) & (__u16)0x00ffU) << 8) | (((__u16)(*p) & (__u16)0xff00U) >> 8))) : __fswab16(*p));

}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 __swab32p(const __u32 *p)
{



 return (__builtin_constant_p((__u32)(*p)) ? ((__u32)( (((__u32)(*p) & (__u32)0x000000ffUL) << 24) | (((__u32)(*p) & (__u32)0x0000ff00UL) << 8) | (((__u32)(*p) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(*p) & (__u32)0xff000000UL) >> 24))) : __fswab32(*p));

}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u64 __swab64p(const __u64 *p)
{



 return (__builtin_constant_p((__u64)(*p)) ? ((__u64)( (((__u64)(*p) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(*p) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(*p) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(*p) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(*p) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(*p) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(*p) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(*p) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(*p));

}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 __swahw32p(const __u32 *p)
{



 return (__builtin_constant_p((__u32)(*p)) ? ((__u32)( (((__u32)(*p) & (__u32)0x0000ffffUL) << 16) | (((__u32)(*p) & (__u32)0xffff0000UL) >> 16))) : __fswahw32(*p));

}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 __swahb32p(const __u32 *p)
{



 return (__builtin_constant_p((__u32)(*p)) ? ((__u32)( (((__u32)(*p) & (__u32)0x00ff00ffUL) << 8) | (((__u32)(*p) & (__u32)0xff00ff00UL) >> 8))) : __fswahb32(*p));

}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __swab16s(__u16 *p)
{



 *p = __swab16p(p);

}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __swab32s(__u32 *p)
{



 *p = __swab32p(p);

}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __swab64s(__u64 *p)
{



 *p = __swab64p(p);

}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __swahw32s(__u32 *p)
{



 *p = __swahw32p(p);

}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __swahb32s(__u32 *p)
{



 *p = __swahb32p(p);

}
# 5 "include/linux/swab.h" 2
# 13 "include/uapi/linux/byteorder/big_endian.h" 2
# 43 "include/uapi/linux/byteorder/big_endian.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __le64 __cpu_to_le64p(const __u64 *p)
{
 return ( __le64)__swab64p(p);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u64 __le64_to_cpup(const __le64 *p)
{
 return __swab64p((__u64 *)p);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __le32 __cpu_to_le32p(const __u32 *p)
{
 return ( __le32)__swab32p(p);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 __le32_to_cpup(const __le32 *p)
{
 return __swab32p((__u32 *)p);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __le16 __cpu_to_le16p(const __u16 *p)
{
 return ( __le16)__swab16p(p);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u16 __le16_to_cpup(const __le16 *p)
{
 return __swab16p((__u16 *)p);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __be64 __cpu_to_be64p(const __u64 *p)
{
 return ( __be64)*p;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u64 __be64_to_cpup(const __be64 *p)
{
 return ( __u64)*p;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __be32 __cpu_to_be32p(const __u32 *p)
{
 return ( __be32)*p;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 __be32_to_cpup(const __be32 *p)
{
 return ( __u32)*p;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __be16 __cpu_to_be16p(const __u16 *p)
{
 return ( __be16)*p;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u16 __be16_to_cpup(const __be16 *p)
{
 return ( __u16)*p;
}
# 5 "include/linux/byteorder/big_endian.h" 2

# 1 "include/linux/byteorder/generic.h" 1
# 143 "include/linux/byteorder/generic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void le16_add_cpu(__le16 *var, u16 val)
{
 *var = (( __le16)(__builtin_constant_p((__u16)(((__builtin_constant_p((__u16)(( __u16)(__le16)(*var))) ? ((__u16)( (((__u16)(( __u16)(__le16)(*var)) & (__u16)0x00ffU) << 8) | (((__u16)(( __u16)(__le16)(*var)) & (__u16)0xff00U) >> 8))) : __fswab16(( __u16)(__le16)(*var))) + val))) ? ((__u16)( (((__u16)(((__builtin_constant_p((__u16)(( __u16)(__le16)(*var))) ? ((__u16)( (((__u16)(( __u16)(__le16)(*var)) & (__u16)0x00ffU) << 8) | (((__u16)(( __u16)(__le16)(*var)) & (__u16)0xff00U) >> 8))) : __fswab16(( __u16)(__le16)(*var))) + val)) & (__u16)0x00ffU) << 8) | (((__u16)(((__builtin_constant_p((__u16)(( __u16)(__le16)(*var))) ? ((__u16)( (((__u16)(( __u16)(__le16)(*var)) & (__u16)0x00ffU) << 8) | (((__u16)(( __u16)(__le16)(*var)) & (__u16)0xff00U) >> 8))) : __fswab16(( __u16)(__le16)(*var))) + val)) & (__u16)0xff00U) >> 8))) : __fswab16(((__builtin_constant_p((__u16)(( __u16)(__le16)(*var))) ? ((__u16)( (((__u16)(( __u16)(__le16)(*var)) & (__u16)0x00ffU) << 8) | (((__u16)(( __u16)(__le16)(*var)) & (__u16)0xff00U) >> 8))) : __fswab16(( __u16)(__le16)(*var))) + val))));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void le32_add_cpu(__le32 *var, u32 val)
{
 *var = (( __le32)(__builtin_constant_p((__u32)(((__builtin_constant_p((__u32)(( __u32)(__le32)(*var))) ? ((__u32)( (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x000000ffUL) << 24) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0xff000000UL) >> 24))) : __fswab32(( __u32)(__le32)(*var))) + val))) ? ((__u32)( (((__u32)(((__builtin_constant_p((__u32)(( __u32)(__le32)(*var))) ? ((__u32)( (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x000000ffUL) << 24) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0xff000000UL) >> 24))) : __fswab32(( __u32)(__le32)(*var))) + val)) & (__u32)0x000000ffUL) << 24) | (((__u32)(((__builtin_constant_p((__u32)(( __u32)(__le32)(*var))) ? ((__u32)( (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x000000ffUL) << 24) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0xff000000UL) >> 24))) : __fswab32(( __u32)(__le32)(*var))) + val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(((__builtin_constant_p((__u32)(( __u32)(__le32)(*var))) ? ((__u32)( (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x000000ffUL) << 24) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0xff000000UL) >> 24))) : __fswab32(( __u32)(__le32)(*var))) + val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(((__builtin_constant_p((__u32)(( __u32)(__le32)(*var))) ? ((__u32)( (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x000000ffUL) << 24) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0xff000000UL) >> 24))) : __fswab32(( __u32)(__le32)(*var))) + val)) & (__u32)0xff000000UL) >> 24))) : __fswab32(((__builtin_constant_p((__u32)(( __u32)(__le32)(*var))) ? ((__u32)( (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x000000ffUL) << 24) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x0000ff00UL) << 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)(( __u32)(__le32)(*var)) & (__u32)0xff000000UL) >> 24))) : __fswab32(( __u32)(__le32)(*var))) + val))));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void le64_add_cpu(__le64 *var, u64 val)
{
 *var = (( __le64)(__builtin_constant_p((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val))) ? ((__u64)( (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(((__builtin_constant_p((__u64)(( __u64)(__le64)(*var))) ? ((__u64)( (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)(( __u64)(__le64)(*var)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64(( __u64)(__le64)(*var))) + val))));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void be16_add_cpu(__be16 *var, u16 val)
{
 *var = (( __be16)(__u16)((( __u16)(__be16)(*var)) + val));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void be32_add_cpu(__be32 *var, u32 val)
{
 *var = (( __be32)(__u32)((( __u32)(__be32)(*var)) + val));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void be64_add_cpu(__be64 *var, u64 val)
{
 *var = (( __be64)(__u64)((( __u64)(__be64)(*var)) + val));
}
# 7 "include/linux/byteorder/big_endian.h" 2
# 13 "./arch/mips/include/uapi/asm/byteorder.h" 2
# 20 "./arch/mips/include/asm/bitops.h" 2
# 1 "./arch/mips/include/asm/cpu-features.h" 1
# 12 "./arch/mips/include/asm/cpu-features.h"
# 1 "./arch/mips/include/asm/cpu.h" 1
# 265 "./arch/mips/include/asm/cpu.h"
enum cpu_type_enum {
 CPU_UNKNOWN,




 CPU_R2000, CPU_R3000, CPU_R3000A, CPU_R3041, CPU_R3051, CPU_R3052,
 CPU_R3081, CPU_R3081E,




 CPU_R6000, CPU_R6000A,




 CPU_R4000PC, CPU_R4000SC, CPU_R4000MC, CPU_R4200, CPU_R4300, CPU_R4310,
 CPU_R4400PC, CPU_R4400SC, CPU_R4400MC, CPU_R4600, CPU_R4640, CPU_R4650,
 CPU_R4700, CPU_R5000, CPU_R5500, CPU_NEVADA, CPU_R5432, CPU_R10000,
 CPU_R12000, CPU_R14000, CPU_VR41XX, CPU_VR4111, CPU_VR4121, CPU_VR4122,
 CPU_VR4131, CPU_VR4133, CPU_VR4181, CPU_VR4181A, CPU_RM7000,
 CPU_SR71000, CPU_TX49XX,




 CPU_R8000,




 CPU_TX3912, CPU_TX3922, CPU_TX3927,




 CPU_4KC, CPU_4KEC, CPU_4KSC, CPU_24K, CPU_34K, CPU_1004K, CPU_74K,
 CPU_ALCHEMY, CPU_PR4450, CPU_BMIPS32, CPU_BMIPS3300, CPU_BMIPS4350,
 CPU_BMIPS4380, CPU_BMIPS5000, CPU_JZRISC, CPU_LOONGSON1, CPU_M14KC,
 CPU_M14KEC, CPU_INTERAPTIV, CPU_P5600, CPU_PROAPTIV, CPU_1074K, CPU_M5150,




 CPU_5KC, CPU_5KE, CPU_20KC, CPU_25KF, CPU_SB1, CPU_SB1A, CPU_LOONGSON2,
 CPU_LOONGSON3, CPU_CAVIUM_OCTEON, CPU_CAVIUM_OCTEON_PLUS,
 CPU_CAVIUM_OCTEON2, CPU_CAVIUM_OCTEON3, CPU_XLR, CPU_XLP,

 CPU_LAST
};
# 13 "./arch/mips/include/asm/cpu-features.h" 2
# 1 "./arch/mips/include/asm/cpu-info.h" 1
# 17 "./arch/mips/include/asm/cpu-info.h"
# 1 "./arch/mips/include/asm/cache.h" 1
# 12 "./arch/mips/include/asm/cache.h"
# 1 "./arch/mips/include/asm/mach-generic/kmalloc.h" 1
# 13 "./arch/mips/include/asm/cache.h" 2
# 18 "./arch/mips/include/asm/cpu-info.h" 2




struct cache_desc {
 unsigned int waysize;
 unsigned short sets;
 unsigned char ways;
 unsigned char linesz;
 unsigned char waybit;
 unsigned char flags;
};
# 41 "./arch/mips/include/asm/cpu-info.h"
struct cpuinfo_mips {
 unsigned long asid_cache;




 unsigned long ases;
 unsigned long long options;
 unsigned int udelay_val;
 unsigned int processor_id;
 unsigned int fpu_id;
 unsigned int msa_id;
 unsigned int cputype;
 int isa_level;
 int tlbsize;
 int tlbsizevtlb;
 int tlbsizeftlbsets;
 int tlbsizeftlbways;
 struct cache_desc icache;
 struct cache_desc dcache;
 struct cache_desc scache;
 struct cache_desc tcache;
 int srsets;
 int package;
 int core;
# 76 "./arch/mips/include/asm/cpu-info.h"
 void *data;
 unsigned int watch_reg_count;
 unsigned int watch_reg_use_cnt;

 u16 watch_reg_masks[4];
 unsigned int kscratch_mask;




 unsigned int writecombine;




 unsigned int htw_seq;
} __attribute__((aligned((1 << 5))));

extern struct cpuinfo_mips cpu_data[];




extern void cpu_probe(void);
extern void cpu_report(void);

extern const char *__cpu_name[];


struct seq_file;
struct notifier_block;

extern int register_proc_cpuinfo_notifier(struct notifier_block *nb);
extern int proc_cpuinfo_notifier_call_chain(unsigned long val, void *v);
# 121 "./arch/mips/include/asm/cpu-info.h"
struct proc_cpuinfo_notifier_args {
 struct seq_file *m;
 unsigned long n;
};
# 14 "./arch/mips/include/asm/cpu-features.h" 2
# 1 "./arch/mips/include/asm/mach-ath79/cpu-feature-overrides.h" 1
# 15 "./arch/mips/include/asm/cpu-features.h" 2
# 21 "./arch/mips/include/asm/bitops.h" 2

# 1 "./arch/mips/include/asm/war.h" 1
# 12 "./arch/mips/include/asm/war.h"
# 1 "./arch/mips/include/asm/mach-ath79/war.h" 1
# 13 "./arch/mips/include/asm/war.h" 2
# 23 "./arch/mips/include/asm/bitops.h" 2
# 44 "./arch/mips/include/asm/bitops.h"
void __mips_set_bit(unsigned long nr, volatile unsigned long *addr);
void __mips_clear_bit(unsigned long nr, volatile unsigned long *addr);
void __mips_change_bit(unsigned long nr, volatile unsigned long *addr);
int __mips_test_and_set_bit(unsigned long nr,
       volatile unsigned long *addr);
int __mips_test_and_set_bit_lock(unsigned long nr,
     volatile unsigned long *addr);
int __mips_test_and_clear_bit(unsigned long nr,
         volatile unsigned long *addr);
int __mips_test_and_change_bit(unsigned long nr,
          volatile unsigned long *addr);
# 67 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_bit(unsigned long nr, volatile unsigned long *addr)
{
 unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
 int bit = nr & 31UL;
 unsigned long temp;

 if (1 && 0) {
  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	" "ll	" "%0, %1			# set_bit	\n"
  "	or	%0, %2					\n"
  "	" "sc	" "%0, %1					\n"
  "	beqzl	%0, 1b					\n"
  "	.set	mips0					\n"
  : "=&r" (temp), "=m" (*m)
  : "ir" (1UL << bit), "m" (*m));

 } else if (1 && __builtin_constant_p(bit)) {
  do {
   __asm__ __volatile__(
   "	" "ll	" "%0, %1		# set_bit	\n"
   "	" "ins	" "%0, %3, %2, 1			\n"
   "	" "sc	" "%0, %1				\n"
   : "=&r" (temp), "+m" (*m)
   : "ir" (bit), "r" (~0));
  } while (__builtin_expect(!!(!temp), 0));

 } else if (1) {
  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1		# set_bit	\n"
   "	or	%0, %2				\n"
   "	" "sc	" "%0, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m)
   : "ir" (1UL << bit));
  } while (__builtin_expect(!!(!temp), 0));
 } else
  __mips_set_bit(nr, addr);
}
# 119 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_bit(unsigned long nr, volatile unsigned long *addr)
{
 unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
 int bit = nr & 31UL;
 unsigned long temp;

 if (1 && 0) {
  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	" "ll	" "%0, %1			# clear_bit	\n"
  "	and	%0, %2					\n"
  "	" "sc	" "%0, %1					\n"
  "	beqzl	%0, 1b					\n"
  "	.set	mips0					\n"
  : "=&r" (temp), "+m" (*m)
  : "ir" (~(1UL << bit)));

 } else if (1 && __builtin_constant_p(bit)) {
  do {
   __asm__ __volatile__(
   "	" "ll	" "%0, %1		# clear_bit	\n"
   "	" "ins	" "%0, $0, %2, 1			\n"
   "	" "sc	" "%0, %1				\n"
   : "=&r" (temp), "+m" (*m)
   : "ir" (bit));
  } while (__builtin_expect(!!(!temp), 0));

 } else if (1) {
  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1		# clear_bit	\n"
   "	and	%0, %2				\n"
   "	" "sc	" "%0, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m)
   : "ir" (~(1UL << bit)));
  } while (__builtin_expect(!!(!temp), 0));
 } else
  __mips_clear_bit(nr, addr);
}
# 169 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_bit_unlock(unsigned long nr, volatile unsigned long *addr)
{
 __asm__ __volatile__("		\n" : : :"memory");
 clear_bit(nr, addr);
}
# 184 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void change_bit(unsigned long nr, volatile unsigned long *addr)
{
 int bit = nr & 31UL;

 if (1 && 0) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  __asm__ __volatile__(
  "	.set	arch=r4000			\n"
  "1:	" "ll	" "%0, %1		# change_bit	\n"
  "	xor	%0, %2				\n"
  "	" "sc	" "%0, %1				\n"
  "	beqzl	%0, 1b				\n"
  "	.set	mips0				\n"
  : "=&r" (temp), "+m" (*m)
  : "ir" (1UL << bit));
 } else if (1) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1		# change_bit	\n"
   "	xor	%0, %2				\n"
   "	" "sc	" "%0, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m)
   : "ir" (1UL << bit));
  } while (__builtin_expect(!!(!temp), 0));
 } else
  __mips_change_bit(nr, addr);
}
# 227 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_set_bit(unsigned long nr,
 volatile unsigned long *addr)
{
 int bit = nr & 31UL;
 unsigned long res;

 __asm__ __volatile__("		\n" : : :"memory");

 if (1 && 0) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	" "ll	" "%0, %1		# test_and_set_bit	\n"
  "	or	%2, %0, %3				\n"
  "	" "sc	" "%2, %1					\n"
  "	beqzl	%2, 1b					\n"
  "	and	%2, %0, %3				\n"
  "	.set	mips0					\n"
  : "=&r" (temp), "+m" (*m), "=&r" (res)
  : "r" (1UL << bit)
  : "memory");
 } else if (1) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1	# test_and_set_bit	\n"
   "	or	%2, %0, %3			\n"
   "	" "sc	" "%2, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m), "=&r" (res)
   : "r" (1UL << bit)
   : "memory");
  } while (__builtin_expect(!!(!res), 0));

  res = temp & (1UL << bit);
 } else
  res = __mips_test_and_set_bit(nr, addr);

 __asm__ __volatile__("		\n" : : :"memory");

 return res != 0;
}
# 283 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_set_bit_lock(unsigned long nr,
 volatile unsigned long *addr)
{
 int bit = nr & 31UL;
 unsigned long res;

 if (1 && 0) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	" "ll	" "%0, %1		# test_and_set_bit	\n"
  "	or	%2, %0, %3				\n"
  "	" "sc	" "%2, %1					\n"
  "	beqzl	%2, 1b					\n"
  "	and	%2, %0, %3				\n"
  "	.set	mips0					\n"
  : "=&r" (temp), "+m" (*m), "=&r" (res)
  : "r" (1UL << bit)
  : "memory");
 } else if (1) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1	# test_and_set_bit	\n"
   "	or	%2, %0, %3			\n"
   "	" "sc	" "%2, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m), "=&r" (res)
   : "r" (1UL << bit)
   : "memory");
  } while (__builtin_expect(!!(!res), 0));

  res = temp & (1UL << bit);
 } else
  res = __mips_test_and_set_bit_lock(nr, addr);

 __asm__ __volatile__("		\n" : : :"memory");

 return res != 0;
}
# 336 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_clear_bit(unsigned long nr,
 volatile unsigned long *addr)
{
 int bit = nr & 31UL;
 unsigned long res;

 __asm__ __volatile__("		\n" : : :"memory");

 if (1 && 0) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	" "ll	" "%0, %1		# test_and_clear_bit	\n"
  "	or	%2, %0, %3				\n"
  "	xor	%2, %3					\n"
  "	" "sc	" "%2, %1					\n"
  "	beqzl	%2, 1b					\n"
  "	and	%2, %0, %3				\n"
  "	.set	mips0					\n"
  : "=&r" (temp), "+m" (*m), "=&r" (res)
  : "r" (1UL << bit)
  : "memory");

 } else if (1 && __builtin_constant_p(nr)) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  do {
   __asm__ __volatile__(
   "	" "ll	" "%0, %1 # test_and_clear_bit	\n"
   "	" "ext	" "%2, %0, %3, 1			\n"
   "	" "ins	" "%0, $0, %3, 1			\n"
   "	" "sc	" "%0, %1				\n"
   : "=&r" (temp), "+m" (*m), "=&r" (res)
   : "ir" (bit)
   : "memory");
  } while (__builtin_expect(!!(!temp), 0));

 } else if (1) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1 # test_and_clear_bit	\n"
   "	or	%2, %0, %3			\n"
   "	xor	%2, %3				\n"
   "	" "sc	" "%2, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m), "=&r" (res)
   : "r" (1UL << bit)
   : "memory");
  } while (__builtin_expect(!!(!res), 0));

  res = temp & (1UL << bit);
 } else
  res = __mips_test_and_clear_bit(nr, addr);

 __asm__ __volatile__("		\n" : : :"memory");

 return res != 0;
}
# 410 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_change_bit(unsigned long nr,
 volatile unsigned long *addr)
{
 int bit = nr & 31UL;
 unsigned long res;

 __asm__ __volatile__("		\n" : : :"memory");

 if (1 && 0) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	" "ll	" "%0, %1		# test_and_change_bit	\n"
  "	xor	%2, %0, %3				\n"
  "	" "sc	" "%2, %1					\n"
  "	beqzl	%2, 1b					\n"
  "	and	%2, %0, %3				\n"
  "	.set	mips0					\n"
  : "=&r" (temp), "+m" (*m), "=&r" (res)
  : "r" (1UL << bit)
  : "memory");
 } else if (1) {
  unsigned long *m = ((unsigned long *) addr) + (nr >> 5);
  unsigned long temp;

  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	" "ll	" "%0, %1 # test_and_change_bit	\n"
   "	xor	%2, %0, %3			\n"
   "	" "sc	" "\t%2, %1			\n"
   "	.set	mips0				\n"
   : "=&r" (temp), "+m" (*m), "=&r" (res)
   : "r" (1UL << bit)
   : "memory");
  } while (__builtin_expect(!!(!res), 0));

  res = temp & (1UL << bit);
 } else
  res = __mips_test_and_change_bit(nr, addr);

 __asm__ __volatile__("		\n" : : :"memory");

 return res != 0;
}

# 1 "include/asm-generic/bitops/non-atomic.h" 1
# 15 "include/asm-generic/bitops/non-atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __set_bit(int nr, volatile unsigned long *addr)
{
 unsigned long mask = (1UL << ((nr) % 32));
 unsigned long *p = ((unsigned long *)addr) + ((nr) / 32);

 *p |= mask;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __clear_bit(int nr, volatile unsigned long *addr)
{
 unsigned long mask = (1UL << ((nr) % 32));
 unsigned long *p = ((unsigned long *)addr) + ((nr) / 32);

 *p &= ~mask;
}
# 40 "include/asm-generic/bitops/non-atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __change_bit(int nr, volatile unsigned long *addr)
{
 unsigned long mask = (1UL << ((nr) % 32));
 unsigned long *p = ((unsigned long *)addr) + ((nr) / 32);

 *p ^= mask;
}
# 57 "include/asm-generic/bitops/non-atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __test_and_set_bit(int nr, volatile unsigned long *addr)
{
 unsigned long mask = (1UL << ((nr) % 32));
 unsigned long *p = ((unsigned long *)addr) + ((nr) / 32);
 unsigned long old = *p;

 *p = old | mask;
 return (old & mask) != 0;
}
# 76 "include/asm-generic/bitops/non-atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __test_and_clear_bit(int nr, volatile unsigned long *addr)
{
 unsigned long mask = (1UL << ((nr) % 32));
 unsigned long *p = ((unsigned long *)addr) + ((nr) / 32);
 unsigned long old = *p;

 *p = old & ~mask;
 return (old & mask) != 0;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __test_and_change_bit(int nr,
         volatile unsigned long *addr)
{
 unsigned long mask = (1UL << ((nr) % 32));
 unsigned long *p = ((unsigned long *)addr) + ((nr) / 32);
 unsigned long old = *p;

 *p = old ^ mask;
 return (old & mask) != 0;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_bit(int nr, const volatile unsigned long *addr)
{
 return 1UL & (addr[((nr) / 32)] >> (nr & (32 -1)));
}
# 459 "./arch/mips/include/asm/bitops.h" 2
# 469 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __clear_bit_unlock(unsigned long nr, volatile unsigned long *addr)
{
 __asm__ __volatile__("": : :"memory");
 __clear_bit(nr, addr);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __fls(unsigned long word)
{
 int num;

 if (32 == 32 &&
     __builtin_constant_p((1 | 1 | 0 | 0)) && (1 | 1 | 0 | 0)) {
  __asm__(
  "	.set	push					\n"
  "	.set	mips32					\n"
  "	clz	%0, %1					\n"
  "	.set	pop					\n"
  : "=r" (num)
  : "r" (word));

  return 31 - num;
 }

 if (32 == 64 &&
     __builtin_constant_p((0 | 0)) && (0 | 0)) {
  __asm__(
  "	.set	push					\n"
  "	.set	mips64					\n"
  "	dclz	%0, %1					\n"
  "	.set	pop					\n"
  : "=r" (num)
  : "r" (word));

  return 63 - num;
 }

 num = 32 - 1;







 if (!(word & (~0ul << (32 -16)))) {
  num -= 16;
  word <<= 16;
 }
 if (!(word & (~0ul << (32 -8)))) {
  num -= 8;
  word <<= 8;
 }
 if (!(word & (~0ul << (32 -4)))) {
  num -= 4;
  word <<= 4;
 }
 if (!(word & (~0ul << (32 -2)))) {
  num -= 2;
  word <<= 2;
 }
 if (!(word & (~0ul << (32 -1))))
  num -= 1;
 return num;
}
# 545 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __ffs(unsigned long word)
{
 return __fls(word & -word);
}
# 557 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int fls(int x)
{
 int r;

 if (__builtin_constant_p((1 | 1 | 0 | 0)) && (1 | 1 | 0 | 0)) {
  __asm__(
  "	.set	push					\n"
  "	.set	mips32					\n"
  "	clz	%0, %1					\n"
  "	.set	pop					\n"
  : "=r" (x)
  : "r" (x));

  return 32 - x;
 }

 r = 32;
 if (!x)
  return 0;
 if (!(x & 0xffff0000u)) {
  x <<= 16;
  r -= 16;
 }
 if (!(x & 0xff000000u)) {
  x <<= 8;
  r -= 8;
 }
 if (!(x & 0xf0000000u)) {
  x <<= 4;
  r -= 4;
 }
 if (!(x & 0xc0000000u)) {
  x <<= 2;
  r -= 2;
 }
 if (!(x & 0x80000000u)) {
  x <<= 1;
  r -= 1;
 }
 return r;
}

# 1 "include/asm-generic/bitops/fls64.h" 1
# 18 "include/asm-generic/bitops/fls64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) int fls64(__u64 x)
{
 __u32 h = x >> 32;
 if (h)
  return fls(h) + 32;
 return fls(x);
}
# 600 "./arch/mips/include/asm/bitops.h" 2
# 609 "./arch/mips/include/asm/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ffs(int word)
{
 if (!word)
  return 0;

 return fls(word & -word);
}

# 1 "include/asm-generic/bitops/ffz.h" 1
# 618 "./arch/mips/include/asm/bitops.h" 2
# 1 "include/asm-generic/bitops/find.h" 1
# 14 "include/asm-generic/bitops/find.h"
extern unsigned long find_next_bit(const unsigned long *addr, unsigned long
  size, unsigned long offset);
# 28 "include/asm-generic/bitops/find.h"
extern unsigned long find_next_zero_bit(const unsigned long *addr, unsigned
  long size, unsigned long offset);
# 619 "./arch/mips/include/asm/bitops.h" 2



# 1 "include/asm-generic/bitops/sched.h" 1
# 12 "include/asm-generic/bitops/sched.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int sched_find_first_bit(const unsigned long *b)
{





 if (b[0])
  return __ffs(b[0]);
 if (b[1])
  return __ffs(b[1]) + 32;
 if (b[2])
  return __ffs(b[2]) + 64;
 return __ffs(b[3]) + 96;



}
# 623 "./arch/mips/include/asm/bitops.h" 2

# 1 "./arch/mips/include/asm/arch_hweight.h" 1
# 35 "./arch/mips/include/asm/arch_hweight.h"
# 1 "include/asm-generic/bitops/arch_hweight.h" 1





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int __arch_hweight32(unsigned int w)
{
 return __sw_hweight32(w);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int __arch_hweight16(unsigned int w)
{
 return __sw_hweight16(w);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int __arch_hweight8(unsigned int w)
{
 return __sw_hweight8(w);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __arch_hweight64(__u64 w)
{
 return __sw_hweight64(w);
}
# 36 "./arch/mips/include/asm/arch_hweight.h" 2
# 625 "./arch/mips/include/asm/bitops.h" 2
# 1 "include/asm-generic/bitops/const_hweight.h" 1
# 626 "./arch/mips/include/asm/bitops.h" 2

# 1 "include/asm-generic/bitops/le.h" 1
# 34 "include/asm-generic/bitops/le.h"
extern unsigned long find_next_zero_bit_le(const void *addr,
  unsigned long size, unsigned long offset);



extern unsigned long find_next_bit_le(const void *addr,
  unsigned long size, unsigned long offset);
# 52 "include/asm-generic/bitops/le.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_bit_le(int nr, const void *addr)
{
 return test_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_bit_le(int nr, void *addr)
{
 set_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_bit_le(int nr, void *addr)
{
 clear_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __set_bit_le(int nr, void *addr)
{
 __set_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __clear_bit_le(int nr, void *addr)
{
 __clear_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_set_bit_le(int nr, void *addr)
{
 return test_and_set_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_clear_bit_le(int nr, void *addr)
{
 return test_and_clear_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __test_and_set_bit_le(int nr, void *addr)
{
 return __test_and_set_bit(nr ^ ((32 -1) & ~0x7), addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __test_and_clear_bit_le(int nr, void *addr)
{
 return __test_and_clear_bit(nr ^ ((32 -1) & ~0x7), addr);
}
# 628 "./arch/mips/include/asm/bitops.h" 2
# 1 "include/asm-generic/bitops/ext2-atomic.h" 1
# 629 "./arch/mips/include/asm/bitops.h" 2
# 37 "include/linux/bitops.h" 2
# 60 "include/linux/bitops.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int get_bitmask_order(unsigned int count)
{
 int order;

 order = fls(count);
 return order;
}

static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int get_count_order(unsigned int count)
{
 int order;

 order = fls(count) - 1;
 if (count & (count - 1))
  order++;
 return order;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long hweight_long(unsigned long w)
{
 return sizeof(w) == 4 ? (__builtin_constant_p(w) ? ((((unsigned int) ((!!((w) & (1ULL << 0))) + (!!((w) & (1ULL << 1))) + (!!((w) & (1ULL << 2))) + (!!((w) & (1ULL << 3))) + (!!((w) & (1ULL << 4))) + (!!((w) & (1ULL << 5))) + (!!((w) & (1ULL << 6))) + (!!((w) & (1ULL << 7))))) + ((unsigned int) ((!!(((w) >> 8) & (1ULL << 0))) + (!!(((w) >> 8) & (1ULL << 1))) + (!!(((w) >> 8) & (1ULL << 2))) + (!!(((w) >> 8) & (1ULL << 3))) + (!!(((w) >> 8) & (1ULL << 4))) + (!!(((w) >> 8) & (1ULL << 5))) + (!!(((w) >> 8) & (1ULL << 6))) + (!!(((w) >> 8) & (1ULL << 7)))))) + (((unsigned int) ((!!(((w) >> 16) & (1ULL << 0))) + (!!(((w) >> 16) & (1ULL << 1))) + (!!(((w) >> 16) & (1ULL << 2))) + (!!(((w) >> 16) & (1ULL << 3))) + (!!(((w) >> 16) & (1ULL << 4))) + (!!(((w) >> 16) & (1ULL << 5))) + (!!(((w) >> 16) & (1ULL << 6))) + (!!(((w) >> 16) & (1ULL << 7))))) + ((unsigned int) ((!!((((w) >> 16) >> 8) & (1ULL << 0))) + (!!((((w) >> 16) >> 8) & (1ULL << 1))) + (!!((((w) >> 16) >> 8) & (1ULL << 2))) + (!!((((w) >> 16) >> 8) & (1ULL << 3))) + (!!((((w) >> 16) >> 8) & (1ULL << 4))) + (!!((((w) >> 16) >> 8) & (1ULL << 5))) + (!!((((w) >> 16) >> 8) & (1ULL << 6))) + (!!((((w) >> 16) >> 8) & (1ULL << 7))))))) : __arch_hweight32(w)) : (__builtin_constant_p(w) ? (((((unsigned int) ((!!((w) & (1ULL << 0))) + (!!((w) & (1ULL << 1))) + (!!((w) & (1ULL << 2))) + (!!((w) & (1ULL << 3))) + (!!((w) & (1ULL << 4))) + (!!((w) & (1ULL << 5))) + (!!((w) & (1ULL << 6))) + (!!((w) & (1ULL << 7))))) + ((unsigned int) ((!!(((w) >> 8) & (1ULL << 0))) + (!!(((w) >> 8) & (1ULL << 1))) + (!!(((w) >> 8) & (1ULL << 2))) + (!!(((w) >> 8) & (1ULL << 3))) + (!!(((w) >> 8) & (1ULL << 4))) + (!!(((w) >> 8) & (1ULL << 5))) + (!!(((w) >> 8) & (1ULL << 6))) + (!!(((w) >> 8) & (1ULL << 7)))))) + (((unsigned int) ((!!(((w) >> 16) & (1ULL << 0))) + (!!(((w) >> 16) & (1ULL << 1))) + (!!(((w) >> 16) & (1ULL << 2))) + (!!(((w) >> 16) & (1ULL << 3))) + (!!(((w) >> 16) & (1ULL << 4))) + (!!(((w) >> 16) & (1ULL << 5))) + (!!(((w) >> 16) & (1ULL << 6))) + (!!(((w) >> 16) & (1ULL << 7))))) + ((unsigned int) ((!!((((w) >> 16) >> 8) & (1ULL << 0))) + (!!((((w) >> 16) >> 8) & (1ULL << 1))) + (!!((((w) >> 16) >> 8) & (1ULL << 2))) + (!!((((w) >> 16) >> 8) & (1ULL << 3))) + (!!((((w) >> 16) >> 8) & (1ULL << 4))) + (!!((((w) >> 16) >> 8) & (1ULL << 5))) + (!!((((w) >> 16) >> 8) & (1ULL << 6))) + (!!((((w) >> 16) >> 8) & (1ULL << 7))))))) + ((((unsigned int) ((!!(((w) >> 32) & (1ULL << 0))) + (!!(((w) >> 32) & (1ULL << 1))) + (!!(((w) >> 32) & (1ULL << 2))) + (!!(((w) >> 32) & (1ULL << 3))) + (!!(((w) >> 32) & (1ULL << 4))) + (!!(((w) >> 32) & (1ULL << 5))) + (!!(((w) >> 32) & (1ULL << 6))) + (!!(((w) >> 32) & (1ULL << 7))))) + ((unsigned int) ((!!((((w) >> 32) >> 8) & (1ULL << 0))) + (!!((((w) >> 32) >> 8) & (1ULL << 1))) + (!!((((w) >> 32) >> 8) & (1ULL << 2))) + (!!((((w) >> 32) >> 8) & (1ULL << 3))) + (!!((((w) >> 32) >> 8) & (1ULL << 4))) + (!!((((w) >> 32) >> 8) & (1ULL << 5))) + (!!((((w) >> 32) >> 8) & (1ULL << 6))) + (!!((((w) >> 32) >> 8) & (1ULL << 7)))))) + (((unsigned int) ((!!((((w) >> 32) >> 16) & (1ULL << 0))) + (!!((((w) >> 32) >> 16) & (1ULL << 1))) + (!!((((w) >> 32) >> 16) & (1ULL << 2))) + (!!((((w) >> 32) >> 16) & (1ULL << 3))) + (!!((((w) >> 32) >> 16) & (1ULL << 4))) + (!!((((w) >> 32) >> 16) & (1ULL << 5))) + (!!((((w) >> 32) >> 16) & (1ULL << 6))) + (!!((((w) >> 32) >> 16) & (1ULL << 7))))) + ((unsigned int) ((!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 0))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 1))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 2))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 3))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 4))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 5))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 6))) + (!!(((((w) >> 32) >> 16) >> 8) & (1ULL << 7)))))))) : __arch_hweight64(w));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u64 rol64(__u64 word, unsigned int shift)
{
 return (word << shift) | (word >> (64 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u64 ror64(__u64 word, unsigned int shift)
{
 return (word >> shift) | (word << (64 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 rol32(__u32 word, unsigned int shift)
{
 return (word << shift) | (word >> (32 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u32 ror32(__u32 word, unsigned int shift)
{
 return (word >> shift) | (word << (32 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u16 rol16(__u16 word, unsigned int shift)
{
 return (word << shift) | (word >> (16 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u16 ror16(__u16 word, unsigned int shift)
{
 return (word >> shift) | (word << (16 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u8 rol8(__u8 word, unsigned int shift)
{
 return (word << shift) | (word >> (8 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __u8 ror8(__u8 word, unsigned int shift)
{
 return (word >> shift) | (word << (8 - shift));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __s32 sign_extend32(__u32 value, int index)
{
 __u8 shift = 31 - index;
 return (__s32)(value << shift) >> shift;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned fls_long(unsigned long l)
{
 if (sizeof(l) == 4)
  return fls(l);
 return fls64(l);
}
# 189 "include/linux/bitops.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __ffs64(u64 word)
{

 if (((u32)word) == 0UL)
  return __ffs((u32)(word >> 32)) + 32;



 return __ffs((unsigned long)word);
}
# 225 "include/linux/bitops.h"
extern unsigned long find_last_bit(const unsigned long *addr,
       unsigned long size);
# 11 "include/linux/kernel.h" 2
# 1 "include/linux/log2.h" 1
# 21 "include/linux/log2.h"
extern __attribute__((const, noreturn))
int ____ilog2_NaN(void);
# 31 "include/linux/log2.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((const))
int __ilog2_u32(u32 n)
{
 return fls(n) - 1;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((const))
int __ilog2_u64(u64 n)
{
 return fls64(n) - 1;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((const))
bool is_power_of_2(unsigned long n)
{
 return (n != 0 && ((n & (n - 1)) == 0));
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((const))
unsigned long __roundup_pow_of_two(unsigned long n)
{
 return 1UL << fls_long(n - 1);
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((const))
unsigned long __rounddown_pow_of_two(unsigned long n)
{
 return 1UL << (fls_long(n) - 1);
}
# 12 "include/linux/kernel.h" 2
# 1 "include/linux/typecheck.h" 1
# 13 "include/linux/kernel.h" 2
# 1 "include/linux/printk.h" 1




# 1 "include/linux/init.h" 1
# 135 "include/linux/init.h"
typedef int (*initcall_t)(void);
typedef void (*exitcall_t)(void);

extern initcall_t __con_initcall_start[], __con_initcall_end[];
extern initcall_t __security_initcall_start[], __security_initcall_end[];


typedef void (*ctor_fn_t)(void);


extern int do_one_initcall(initcall_t fn);
extern char __attribute__ ((__section__(".init.data"))) boot_command_line[];
extern char *saved_command_line;
extern unsigned int reset_devices;


void setup_arch(char **);
void prepare_namespace(void);
void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) load_default_modules(void);
int __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) init_rootfs(void);

extern void (*late_time_init)(void);

extern bool initcall_debug;
# 243 "include/linux/init.h"
struct obs_kernel_param {
 const char *str;
 int (*setup_func)(char *);
 int early;
};
# 272 "include/linux/init.h"
void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) parse_early_param(void);
void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) parse_early_options(char *cmdline);
# 6 "include/linux/printk.h" 2
# 1 "include/linux/kern_levels.h" 1
# 7 "include/linux/printk.h" 2

# 1 "include/linux/cache.h" 1



# 1 "include/uapi/linux/kernel.h" 1



# 1 "./include/uapi/linux/sysinfo.h" 1






struct sysinfo {
 __kernel_long_t uptime;
 __kernel_ulong_t loads[3];
 __kernel_ulong_t totalram;
 __kernel_ulong_t freeram;
 __kernel_ulong_t sharedram;
 __kernel_ulong_t bufferram;
 __kernel_ulong_t totalswap;
 __kernel_ulong_t freeswap;
 __u16 procs;
 __u16 pad;
 __kernel_ulong_t totalhigh;
 __kernel_ulong_t freehigh;
 __u32 mem_unit;
 char _f[20-2*sizeof(__kernel_ulong_t)-sizeof(__u32)];
};
# 5 "include/uapi/linux/kernel.h" 2
# 5 "include/linux/cache.h" 2
# 9 "include/linux/printk.h" 2

extern const char linux_banner[];
extern const char linux_proc_banner[];

extern char *log_buf_addr_get(void);
extern u32 log_buf_len_get(void);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int printk_get_level(const char *buffer)
{
 if (buffer[0] == '\001' && buffer[1]) {
  switch (buffer[1]) {
  case '0' ... '7':
  case 'd':
   return buffer[1];
  }
 }
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) const char *printk_skip_level(const char *buffer)
{
 if (printk_get_level(buffer))
  return buffer + 2;

 return buffer;
}
# 47 "include/linux/printk.h"
extern int console_printk[];






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void console_silent(void)
{
 (console_printk[0]) = 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void console_verbose(void)
{
 if ((console_printk[0]))
  (console_printk[0]) = 15;
}

struct va_format {
 const char *fmt;
 va_list *va;
};
# 112 "include/linux/printk.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((format(printf, 1, 2)))
int no_printk(const char *fmt, ...)
{
 return 0;
}


extern __attribute__((format(printf, 1, 2)))
void early_printk(const char *fmt, ...);
void early_vprintk(const char *fmt, va_list ap);






 __attribute__((format(printf, 5, 0)))
int vprintk_emit(int facility, int level,
   const char *dict, size_t dictlen,
   const char *fmt, va_list args);

 __attribute__((format(printf, 1, 0)))
int vprintk(const char *fmt, va_list args);

 __attribute__((format(printf, 5, 6))) __attribute__((__cold__))
int printk_emit(int facility, int level,
  const char *dict, size_t dictlen,
  const char *fmt, ...);

 __attribute__((format(printf, 1, 2))) __attribute__((__cold__))
int printk(const char *fmt, ...);




__attribute__((format(printf, 1, 2))) __attribute__((__cold__)) int printk_deferred(const char *fmt, ...);






extern int __printk_ratelimit(const char *func);

extern bool printk_timed_ratelimit(unsigned long *caller_jiffies,
       unsigned int interval_msec);

extern int printk_delay_msec;
extern int dmesg_restrict;
extern int kptr_restrict;

extern void wake_up_klogd(void);

void log_buf_kexec_setup(void);
void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) setup_log_buf(int early);
void dump_stack_set_arch_desc(const char *fmt, ...);
void dump_stack_print_info(const char *log_lvl);
void show_regs_print_info(const char *log_lvl);
# 221 "include/linux/printk.h"
extern void dump_stack(void) __attribute__((__cold__));
# 260 "include/linux/printk.h"
# 1 "include/linux/dynamic_debug.h" 1
# 9 "include/linux/dynamic_debug.h"
struct _ddebug {




 const char *modname;
 const char *function;
 const char *filename;
 const char *format;
 unsigned int lineno:18;
# 35 "include/linux/dynamic_debug.h"
 unsigned int flags:8;
} __attribute__((aligned(8)));


int ddebug_add_module(struct _ddebug *tab, unsigned int n,
    const char *modname);
# 111 "include/linux/dynamic_debug.h"
# 1 "include/linux/string.h" 1
# 9 "include/linux/string.h"
# 1 "include/uapi/linux/string.h" 1
# 10 "include/linux/string.h" 2

extern char *strndup_user(const char *, long);
extern void *memdup_user(const void *, size_t);




# 1 "./arch/mips/include/asm/string.h" 1
# 23 "./arch/mips/include/asm/string.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) char *strcpy(char *__dest, __const__ char *__src)
{
  char *__xdest = __dest;

  __asm__ __volatile__(
 ".set\tnoreorder\n\t"
 ".set\tnoat\n"
 "1:\tlbu\t$1,(%1)\n\t"
 "addiu\t%1,1\n\t"
 "sb\t$1,(%0)\n\t"
 "bnez\t$1,1b\n\t"
 "addiu\t%0,1\n\t"
 ".set\tat\n\t"
 ".set\treorder"
 : "=r" (__dest), "=r" (__src)
 : "0" (__dest), "1" (__src)
 : "memory");

  return __xdest;
}


static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) char *strncpy(char *__dest, __const__ char *__src, size_t __n)
{
  char *__xdest = __dest;

  if (__n == 0)
    return __xdest;

  __asm__ __volatile__(
 ".set\tnoreorder\n\t"
 ".set\tnoat\n"
 "1:\tlbu\t$1,(%1)\n\t"
 "subu\t%2,1\n\t"
 "sb\t$1,(%0)\n\t"
 "beqz\t$1,2f\n\t"
 "addiu\t%0,1\n\t"
 "bnez\t%2,1b\n\t"
 "addiu\t%1,1\n"
 "2:\n\t"
 ".set\tat\n\t"
 ".set\treorder"
 : "=r" (__dest), "=r" (__src), "=r" (__n)
 : "0" (__dest), "1" (__src), "2" (__n)
 : "memory");

  return __xdest;
}


static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int strcmp(__const__ char *__cs, __const__ char *__ct)
{
  int __res;

  __asm__ __volatile__(
 ".set\tnoreorder\n\t"
 ".set\tnoat\n\t"
 "lbu\t%2,(%0)\n"
 "1:\tlbu\t$1,(%1)\n\t"
 "addiu\t%0,1\n\t"
 "bne\t$1,%2,2f\n\t"
 "addiu\t%1,1\n\t"
 "bnez\t%2,1b\n\t"
 "lbu\t%2,(%0)\n\t"



 "move\t%2,$1\n"
 "2:\tsubu\t%2,$1\n"
 "3:\t.set\tat\n\t"
 ".set\treorder"
 : "=r" (__cs), "=r" (__ct), "=r" (__res)
 : "0" (__cs), "1" (__ct));

  return __res;
}




static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int
strncmp(__const__ char *__cs, __const__ char *__ct, size_t __count)
{
 int __res;

 __asm__ __volatile__(
 ".set\tnoreorder\n\t"
 ".set\tnoat\n"
 "1:\tlbu\t%3,(%0)\n\t"
 "beqz\t%2,2f\n\t"
 "lbu\t$1,(%1)\n\t"
 "subu\t%2,1\n\t"
 "bne\t$1,%3,3f\n\t"
 "addiu\t%0,1\n\t"
 "bnez\t%3,1b\n\t"
 "addiu\t%1,1\n"
 "2:\n\t"



 "move\t%3,$1\n"
 "3:\tsubu\t%3,$1\n\t"
 ".set\tat\n\t"
 ".set\treorder"
 : "=r" (__cs), "=r" (__ct), "=r" (__count), "=r" (__res)
 : "0" (__cs), "1" (__ct), "2" (__count));

 return __res;
}



extern void *memset(void *__s, int __c, size_t __count);
# 148 "./arch/mips/include/asm/string.h"
extern void *memcpy(void *__to, __const__ void *__from, size_t __n);
# 161 "./arch/mips/include/asm/string.h"
extern void *memmove(void *__dest, __const__ void *__src, size_t __n);
# 18 "include/linux/string.h" 2
# 26 "include/linux/string.h"
size_t strlcpy(char *, const char *, size_t);


extern char * strcat(char *, const char *);


extern char * strncat(char *, const char *, __kernel_size_t);


extern size_t strlcat(char *, const char *, __kernel_size_t);
# 47 "include/linux/string.h"
extern int strcasecmp(const char *s1, const char *s2);


extern int strncasecmp(const char *s1, const char *s2, size_t n);


extern char * strchr(const char *,int);


extern char * strchrnul(const char *,int);


extern char * strnchr(const char *, size_t, int);


extern char * strrchr(const char *,int);

extern char * skip_spaces(const char *);

extern char *strim(char *);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) char *strstrip(char *str)
{
 return strim(str);
}


extern char * strstr(const char *, const char *);


extern char * strnstr(const char *, const char *, size_t);


extern __kernel_size_t strlen(const char *);


extern __kernel_size_t strnlen(const char *,__kernel_size_t);


extern char * strpbrk(const char *,const char *);


extern char * strsep(char **,const char *);


extern __kernel_size_t strspn(const char *,const char *);


extern __kernel_size_t strcspn(const char *,const char *);
# 108 "include/linux/string.h"
extern void * memscan(void *,int,__kernel_size_t);





extern void * memchr(const void *,int,__kernel_size_t);

void *memchr_inv(const void *s, int c, size_t n);

extern char *kstrdup(const char *s, gfp_t gfp);
extern char *kstrndup(const char *s, size_t len, gfp_t gfp);
extern void *kmemdup(const void *src, size_t len, gfp_t gfp);

extern char **argv_split(gfp_t gfp, const char *str, int *argcp);
extern void argv_free(char **argv);

extern bool sysfs_streq(const char *s1, const char *s2);
extern int strtobool(const char *s, bool *res);







extern ssize_t memory_read_from_buffer(void *to, size_t count, loff_t *ppos,
           const void *from, size_t available);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool strstarts(const char *str, const char *prefix)
{
 return strncmp(str, prefix, strlen(prefix)) == 0;
}

size_t memweight(const void *ptr, size_t bytes);
void memzero_explicit(void *s, size_t count);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) const char *kbasename(const char *path)
{
 const char *tail = strrchr(path, '/');
 return tail ? tail + 1 : path;
}
# 112 "include/linux/dynamic_debug.h" 2
# 1 "include/linux/errno.h" 1



# 1 "include/uapi/linux/errno.h" 1
# 1 "./arch/mips/include/asm/errno.h" 1
# 11 "./arch/mips/include/asm/errno.h"
# 1 "./arch/mips/include/uapi/asm/errno.h" 1
# 15 "./arch/mips/include/uapi/asm/errno.h"
# 1 "./include/uapi/asm-generic/errno-base.h" 1
# 16 "./arch/mips/include/uapi/asm/errno.h" 2
# 12 "./arch/mips/include/asm/errno.h" 2
# 1 "include/uapi/linux/errno.h" 2
# 5 "include/linux/errno.h" 2
# 113 "include/linux/dynamic_debug.h" 2

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ddebug_remove_module(const char *mod)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ddebug_dyndbg_module_param_cb(char *param, char *val,
      const char *modname)
{
 if (strstr(param, "dyndbg")) {

  printk("\001" "4" "dyndbg param is supported only in "
   "CONFIG_DYNAMIC_DEBUG builds\n");
  return 0;
 }
 return -22;
}
# 261 "include/linux/printk.h" 2
# 403 "include/linux/printk.h"
extern const struct file_operations kmsg_fops;

enum {
 DUMP_PREFIX_NONE,
 DUMP_PREFIX_ADDRESS,
 DUMP_PREFIX_OFFSET
};
extern void hex_dump_to_buffer(const void *buf, size_t len,
          int rowsize, int groupsize,
          char *linebuf, size_t linebuflen, bool ascii);

extern void print_hex_dump(const char *level, const char *prefix_str,
      int prefix_type, int rowsize, int groupsize,
      const void *buf, size_t len, bool ascii);




extern void print_hex_dump_bytes(const char *prefix_str, int prefix_type,
     const void *buf, size_t len);
# 14 "include/linux/kernel.h" 2
# 124 "include/linux/kernel.h"
# 1 "./arch/mips/include/asm/div64.h" 1
# 12 "./arch/mips/include/asm/div64.h"
# 1 "include/asm-generic/div64.h" 1
# 35 "include/asm-generic/div64.h"
extern uint32_t __div64_32(uint64_t *dividend, uint32_t divisor);
# 13 "./arch/mips/include/asm/div64.h" 2
# 125 "include/linux/kernel.h" 2
# 153 "include/linux/kernel.h"
struct completion;
struct pt_regs;
struct user;
# 179 "include/linux/kernel.h"
  static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __might_sleep(const char *file, int line,
       int preempt_offset) { }
# 223 "include/linux/kernel.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 reciprocal_scale(u32 val, u32 ep_ro)
{
 return (u32)(((u64) val * ep_ro) >> 32);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void might_fault(void) { }


extern struct atomic_notifier_head panic_notifier_list;
extern long (*panic_blink)(int state);
__attribute__((format(printf, 1, 2)))
void panic(const char *fmt, ...)
 __attribute__((noreturn)) __attribute__((__cold__));
extern void oops_enter(void);
extern void oops_exit(void);
void print_oops_end_marker(void);
extern int oops_may_print(void);
void do_exit(long error_code)
 __attribute__((noreturn));
void complete_and_exit(struct completion *, long)
 __attribute__((noreturn));


int _kstrtoul(const char *s, unsigned int base, unsigned long *res);
int _kstrtol(const char *s, unsigned int base, long *res);

int kstrtoull(const char *s, unsigned int base, unsigned long long *res);
int kstrtoll(const char *s, unsigned int base, long long *res);
# 272 "include/linux/kernel.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtoul(const char *s, unsigned int base, unsigned long *res)
{




 if (sizeof(unsigned long) == sizeof(unsigned long long) &&
     __alignof__(unsigned long) == __alignof__(unsigned long long))
  return kstrtoull(s, base, (unsigned long long *)res);
 else
  return _kstrtoul(s, base, res);
}
# 301 "include/linux/kernel.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtol(const char *s, unsigned int base, long *res)
{




 if (sizeof(long) == sizeof(long long) &&
     __alignof__(long) == __alignof__(long long))
  return kstrtoll(s, base, (long long *)res);
 else
  return _kstrtol(s, base, res);
}

int kstrtouint(const char *s, unsigned int base, unsigned int *res);
int kstrtoint(const char *s, unsigned int base, int *res);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtou64(const char *s, unsigned int base, u64 *res)
{
 return kstrtoull(s, base, res);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtos64(const char *s, unsigned int base, s64 *res)
{
 return kstrtoll(s, base, res);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtou32(const char *s, unsigned int base, u32 *res)
{
 return kstrtouint(s, base, res);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtos32(const char *s, unsigned int base, s32 *res)
{
 return kstrtoint(s, base, res);
}

int kstrtou16(const char *s, unsigned int base, u16 *res);
int kstrtos16(const char *s, unsigned int base, s16 *res);
int kstrtou8(const char *s, unsigned int base, u8 *res);
int kstrtos8(const char *s, unsigned int base, s8 *res);

int kstrtoull_from_user(const char *s, size_t count, unsigned int base, unsigned long long *res);
int kstrtoll_from_user(const char *s, size_t count, unsigned int base, long long *res);
int kstrtoul_from_user(const char *s, size_t count, unsigned int base, unsigned long *res);
int kstrtol_from_user(const char *s, size_t count, unsigned int base, long *res);
int kstrtouint_from_user(const char *s, size_t count, unsigned int base, unsigned int *res);
int kstrtoint_from_user(const char *s, size_t count, unsigned int base, int *res);
int kstrtou16_from_user(const char *s, size_t count, unsigned int base, u16 *res);
int kstrtos16_from_user(const char *s, size_t count, unsigned int base, s16 *res);
int kstrtou8_from_user(const char *s, size_t count, unsigned int base, u8 *res);
int kstrtos8_from_user(const char *s, size_t count, unsigned int base, s8 *res);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtou64_from_user(const char *s, size_t count, unsigned int base, u64 *res)
{
 return kstrtoull_from_user(s, count, base, res);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtos64_from_user(const char *s, size_t count, unsigned int base, s64 *res)
{
 return kstrtoll_from_user(s, count, base, res);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtou32_from_user(const char *s, size_t count, unsigned int base, u32 *res)
{
 return kstrtouint_from_user(s, count, base, res);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kstrtos32_from_user(const char *s, size_t count, unsigned int base, s32 *res)
{
 return kstrtoint_from_user(s, count, base, res);
}



extern unsigned long simple_strtoul(const char *,char **,unsigned int);
extern long simple_strtol(const char *,char **,unsigned int);
extern unsigned long long simple_strtoull(const char *,char **,unsigned int);
extern long long simple_strtoll(const char *,char **,unsigned int);

extern int num_to_str(char *buf, int size, unsigned long long num);



extern __attribute__((format(printf, 2, 3))) int sprintf(char *buf, const char * fmt, ...);
extern __attribute__((format(printf, 2, 0))) int vsprintf(char *buf, const char *, va_list);
extern __attribute__((format(printf, 3, 4)))
int snprintf(char *buf, size_t size, const char *fmt, ...);
extern __attribute__((format(printf, 3, 0)))
int vsnprintf(char *buf, size_t size, const char *fmt, va_list args);
extern __attribute__((format(printf, 3, 4)))
int scnprintf(char *buf, size_t size, const char *fmt, ...);
extern __attribute__((format(printf, 3, 0)))
int vscnprintf(char *buf, size_t size, const char *fmt, va_list args);
extern __attribute__((format(printf, 2, 3)))
char *kasprintf(gfp_t gfp, const char *fmt, ...);
extern char *kvasprintf(gfp_t gfp, const char *fmt, va_list args);

extern __attribute__((format(scanf, 2, 3)))
int sscanf(const char *, const char *, ...);
extern __attribute__((format(scanf, 2, 0)))
int vsscanf(const char *, const char *, va_list);

extern int get_option(char **str, int *pint);
extern char *get_options(const char *str, int nints, int *ints);
extern unsigned long long memparse(const char *ptr, char **retptr);
extern bool parse_option_str(const char *str, const char *option);

extern int core_kernel_text(unsigned long addr);
extern int core_kernel_data(unsigned long addr);
extern int __kernel_text_address(unsigned long addr);
extern int kernel_text_address(unsigned long addr);
extern int func_ptr_is_kernel_text(void *ptr);

struct pid;
extern struct pid *session_of_pgrp(struct pid *pgrp);

unsigned long int_sqrt(unsigned long);

extern void bust_spinlocks(int yes);
extern int oops_in_progress;
extern int panic_timeout;
extern int panic_on_oops;
extern int panic_on_unrecovered_nmi;
extern int panic_on_io_nmi;
extern int sysctl_panic_on_stackoverflow;




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_arch_panic_timeout(int timeout, int arch_default_timeout)
{
 if (panic_timeout == arch_default_timeout)
  panic_timeout = timeout;
}
extern const char *print_tainted(void);
enum lockdep_ok {
 LOCKDEP_STILL_OK,
 LOCKDEP_NOW_UNRELIABLE
};
extern void add_taint(unsigned flag, enum lockdep_ok);
extern int test_taint(unsigned flag);
extern unsigned long get_taint(void);
extern int root_mountflags;

extern bool early_boot_irqs_disabled;


extern enum system_states {
 SYSTEM_BOOTING,
 SYSTEM_RUNNING,
 SYSTEM_HALT,
 SYSTEM_POWER_OFF,
 SYSTEM_RESTART,
} system_state;
# 472 "include/linux/kernel.h"
extern const char hex_asc[];



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) char *hex_byte_pack(char *buf, u8 byte)
{
 *buf++ = hex_asc[((byte) & 0xf0) >> 4];
 *buf++ = hex_asc[((byte) & 0x0f)];
 return buf;
}

extern const char hex_asc_upper[];



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) char *hex_byte_pack_upper(char *buf, u8 byte)
{
 *buf++ = hex_asc_upper[((byte) & 0xf0) >> 4];
 *buf++ = hex_asc_upper[((byte) & 0x0f)];
 return buf;
}

extern int hex_to_bin(char ch);
extern int hex2bin(u8 *dst, const char *src, size_t count);
extern char *bin2hex(char *dst, const void *src, size_t count);

bool mac_pton(const char *s, u8 *mac);
# 523 "include/linux/kernel.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_off_permanent(void) { }


enum ftrace_dump_mode {
 DUMP_NONE,
 DUMP_ALL,
 DUMP_ORIG,
};
# 676 "include/linux/kernel.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_start(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_stop(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void trace_dump_stack(int skip) { }

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_on(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_off(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int tracing_is_on(void) { return 0; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_snapshot(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tracing_snapshot_alloc(void) { }

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((format(printf, 1, 2)))
int trace_printk(const char *fmt, ...)
{
 return 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
ftrace_vprintk(const char *fmt, va_list ap)
{
 return 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ftrace_dump(enum ftrace_dump_mode oops_dump_mode) { }
# 16 "arch/mips/ath79/setup.c" 2

# 1 "include/linux/bootmem.h" 1






# 1 "include/linux/mmzone.h" 1






# 1 "include/linux/spinlock.h" 1
# 50 "include/linux/spinlock.h"
# 1 "include/linux/preempt.h" 1
# 10 "include/linux/preempt.h"
# 1 "include/linux/list.h" 1





# 1 "include/linux/poison.h" 1
# 7 "include/linux/list.h" 2
# 25 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void INIT_LIST_HEAD(struct list_head *list)
{
 list->next = list;
 list->prev = list;
}
# 38 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __list_add(struct list_head *new,
         struct list_head *prev,
         struct list_head *next)
{
 next->prev = new;
 new->next = next;
 new->prev = prev;
 prev->next = new;
}
# 61 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_add(struct list_head *new, struct list_head *head)
{
 __list_add(new, head, head->next);
}
# 75 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_add_tail(struct list_head *new, struct list_head *head)
{
 __list_add(new, head->prev, head);
}
# 87 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __list_del(struct list_head * prev, struct list_head * next)
{
 next->prev = prev;
 prev->next = next;
}
# 100 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __list_del_entry(struct list_head *entry)
{
 __list_del(entry->prev, entry->next);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_del(struct list_head *entry)
{
 __list_del(entry->prev, entry->next);
 entry->next = ((void *) 0x00100100 + 0);
 entry->prev = ((void *) 0x00200200 + 0);
}
# 123 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_replace(struct list_head *old,
    struct list_head *new)
{
 new->next = old->next;
 new->next->prev = new;
 new->prev = old->prev;
 new->prev->next = new;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_replace_init(struct list_head *old,
     struct list_head *new)
{
 list_replace(old, new);
 INIT_LIST_HEAD(old);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_del_init(struct list_head *entry)
{
 __list_del_entry(entry);
 INIT_LIST_HEAD(entry);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_move(struct list_head *list, struct list_head *head)
{
 __list_del_entry(list);
 list_add(list, head);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_move_tail(struct list_head *list,
      struct list_head *head)
{
 __list_del_entry(list);
 list_add_tail(list, head);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int list_is_last(const struct list_head *list,
    const struct list_head *head)
{
 return list->next == head;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int list_empty(const struct list_head *head)
{
 return head->next == head;
}
# 205 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int list_empty_careful(const struct list_head *head)
{
 struct list_head *next = head->next;
 return (next == head) && (next == head->prev);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_rotate_left(struct list_head *head)
{
 struct list_head *first;

 if (!list_empty(head)) {
  first = head->next;
  list_move_tail(first, head);
 }
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int list_is_singular(const struct list_head *head)
{
 return !list_empty(head) && (head->next == head->prev);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __list_cut_position(struct list_head *list,
  struct list_head *head, struct list_head *entry)
{
 struct list_head *new_first = entry->next;
 list->next = head->next;
 list->next->prev = list;
 list->prev = entry;
 entry->next = list;
 head->next = new_first;
 new_first->prev = head;
}
# 260 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_cut_position(struct list_head *list,
  struct list_head *head, struct list_head *entry)
{
 if (list_empty(head))
  return;
 if (list_is_singular(head) &&
  (head->next != entry && head != entry))
  return;
 if (entry == head)
  INIT_LIST_HEAD(list);
 else
  __list_cut_position(list, head, entry);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __list_splice(const struct list_head *list,
     struct list_head *prev,
     struct list_head *next)
{
 struct list_head *first = list->next;
 struct list_head *last = list->prev;

 first->prev = prev;
 prev->next = first;

 last->next = next;
 next->prev = last;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_splice(const struct list_head *list,
    struct list_head *head)
{
 if (!list_empty(list))
  __list_splice(list, head, head->next);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_splice_tail(struct list_head *list,
    struct list_head *head)
{
 if (!list_empty(list))
  __list_splice(list, head->prev, head);
}
# 319 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_splice_init(struct list_head *list,
        struct list_head *head)
{
 if (!list_empty(list)) {
  __list_splice(list, head, head->next);
  INIT_LIST_HEAD(list);
 }
}
# 336 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_splice_tail_init(struct list_head *list,
      struct list_head *head)
{
 if (!list_empty(list)) {
  __list_splice(list, head->prev, head);
  INIT_LIST_HEAD(list);
 }
}
# 598 "include/linux/list.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void INIT_HLIST_NODE(struct hlist_node *h)
{
 h->next = ((void *)0);
 h->pprev = ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hlist_unhashed(const struct hlist_node *h)
{
 return !h->pprev;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hlist_empty(const struct hlist_head *h)
{
 return !h->first;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __hlist_del(struct hlist_node *n)
{
 struct hlist_node *next = n->next;
 struct hlist_node **pprev = n->pprev;
 *pprev = next;
 if (next)
  next->pprev = pprev;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_del(struct hlist_node *n)
{
 __hlist_del(n);
 n->next = ((void *) 0x00100100 + 0);
 n->pprev = ((void *) 0x00200200 + 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_del_init(struct hlist_node *n)
{
 if (!hlist_unhashed(n)) {
  __hlist_del(n);
  INIT_HLIST_NODE(n);
 }
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_head(struct hlist_node *n, struct hlist_head *h)
{
 struct hlist_node *first = h->first;
 n->next = first;
 if (first)
  first->pprev = &n->next;
 h->first = n;
 n->pprev = &h->first;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_before(struct hlist_node *n,
     struct hlist_node *next)
{
 n->pprev = next->pprev;
 n->next = next;
 next->pprev = &n->next;
 *(n->pprev) = n;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_behind(struct hlist_node *n,
        struct hlist_node *prev)
{
 n->next = prev->next;
 prev->next = n;
 n->pprev = &prev->next;

 if (n->next)
  n->next->pprev = &n->next;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_fake(struct hlist_node *n)
{
 n->pprev = &n->next;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_move_list(struct hlist_head *old,
       struct hlist_head *new)
{
 new->first = old->first;
 if (new->first)
  new->first->pprev = &new->first;
 old->first = ((void *)0);
}
# 11 "include/linux/preempt.h" 2







# 1 "arch/mips/include/generated/asm/preempt.h" 1
# 1 "include/asm-generic/preempt.h" 1



# 1 "include/linux/thread_info.h" 1
# 11 "include/linux/thread_info.h"
# 1 "include/linux/bug.h" 1



# 1 "./arch/mips/include/asm/bug.h" 1
# 9 "./arch/mips/include/asm/bug.h"
# 1 "./arch/mips/include/asm/break.h" 1
# 15 "./arch/mips/include/asm/break.h"
# 1 "./arch/mips/include/uapi/asm/break.h" 1
# 16 "./arch/mips/include/asm/break.h" 2
# 10 "./arch/mips/include/asm/bug.h" 2

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __attribute__((noreturn)) BUG(void)
{
 __asm__ __volatile__("break %0" : : "i" (12));
 __builtin_unreachable();
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __BUG_ON(unsigned long condition)
{
 if (__builtin_constant_p(condition)) {
  if (condition)
   BUG();
  else
   return;
 }
 __asm__ __volatile__("tne $0, %0, %1"
        : : "r" (condition), "i" (12));
}
# 41 "./arch/mips/include/asm/bug.h"
# 1 "include/asm-generic/bug.h" 1
# 65 "include/asm-generic/bug.h"
extern __attribute__((format(printf, 3, 4)))
void warn_slowpath_fmt(const char *file, const int line,
         const char *fmt, ...);
extern __attribute__((format(printf, 4, 5)))
void warn_slowpath_fmt_taint(const char *file, const int line, unsigned taint,
        const char *fmt, ...);
extern void warn_slowpath_null(const char *file, const int line);
# 42 "./arch/mips/include/asm/bug.h" 2
# 5 "include/linux/bug.h" 2


enum bug_trap_type {
 BUG_TRAP_TYPE_NONE = 0,
 BUG_TRAP_TYPE_WARN = 1,
 BUG_TRAP_TYPE_BUG = 2,
};

struct pt_regs;
# 105 "include/linux/bug.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) enum bug_trap_type report_bug(unsigned long bug_addr,
         struct pt_regs *regs)
{
 return BUG_TRAP_TYPE_BUG;
}
# 12 "include/linux/thread_info.h" 2

struct timespec;
struct compat_timespec;




struct restart_block {
 long (*fn)(struct restart_block *);
 union {

  struct {
   u32 *uaddr;
   u32 val;
   u32 flags;
   u32 bitset;
   u64 time;
   u32 *uaddr2;
  } futex;

  struct {
   clockid_t clockid;
   struct timespec *rmtp;



   u64 expires;
  } nanosleep;

  struct {
   struct pollfd *ufds;
   int nfds;
   int has_timeout;
   unsigned long tv_sec;
   unsigned long tv_nsec;
  } poll;
 };
};

extern long do_no_restart_syscall(struct restart_block *parm);


# 1 "./arch/mips/include/asm/thread_info.h" 1
# 15 "./arch/mips/include/asm/thread_info.h"
# 1 "./arch/mips/include/asm/processor.h" 1
# 14 "./arch/mips/include/asm/processor.h"
# 1 "include/linux/cpumask.h" 1
# 10 "include/linux/cpumask.h"
# 1 "include/linux/threads.h" 1
# 11 "include/linux/cpumask.h" 2
# 1 "include/linux/bitmap.h" 1
# 91 "include/linux/bitmap.h"
extern int __bitmap_empty(const unsigned long *bitmap, unsigned int nbits);
extern int __bitmap_full(const unsigned long *bitmap, unsigned int nbits);
extern int __bitmap_equal(const unsigned long *bitmap1,
     const unsigned long *bitmap2, unsigned int nbits);
extern void __bitmap_complement(unsigned long *dst, const unsigned long *src,
   unsigned int nbits);
extern void __bitmap_shift_right(unsigned long *dst,
                        const unsigned long *src, int shift, int bits);
extern void __bitmap_shift_left(unsigned long *dst,
                        const unsigned long *src, int shift, int bits);
extern int __bitmap_and(unsigned long *dst, const unsigned long *bitmap1,
   const unsigned long *bitmap2, unsigned int nbits);
extern void __bitmap_or(unsigned long *dst, const unsigned long *bitmap1,
   const unsigned long *bitmap2, unsigned int nbits);
extern void __bitmap_xor(unsigned long *dst, const unsigned long *bitmap1,
   const unsigned long *bitmap2, unsigned int nbits);
extern int __bitmap_andnot(unsigned long *dst, const unsigned long *bitmap1,
   const unsigned long *bitmap2, unsigned int nbits);
extern int __bitmap_intersects(const unsigned long *bitmap1,
   const unsigned long *bitmap2, unsigned int nbits);
extern int __bitmap_subset(const unsigned long *bitmap1,
   const unsigned long *bitmap2, unsigned int nbits);
extern int __bitmap_weight(const unsigned long *bitmap, unsigned int nbits);

extern void bitmap_set(unsigned long *map, unsigned int start, int len);
extern void bitmap_clear(unsigned long *map, unsigned int start, int len);
extern unsigned long bitmap_find_next_zero_area(unsigned long *map,
      unsigned long size,
      unsigned long start,
      unsigned int nr,
      unsigned long align_mask);

extern int bitmap_scnprintf(char *buf, unsigned int len,
   const unsigned long *src, int nbits);
extern int __bitmap_parse(const char *buf, unsigned int buflen, int is_user,
   unsigned long *dst, int nbits);
extern int bitmap_parse_user(const char *ubuf, unsigned int ulen,
   unsigned long *dst, int nbits);
extern int bitmap_scnlistprintf(char *buf, unsigned int len,
   const unsigned long *src, int nbits);
extern int bitmap_parselist(const char *buf, unsigned long *maskp,
   int nmaskbits);
extern int bitmap_parselist_user(const char *ubuf, unsigned int ulen,
   unsigned long *dst, int nbits);
extern void bitmap_remap(unsigned long *dst, const unsigned long *src,
  const unsigned long *old, const unsigned long *new, int bits);
extern int bitmap_bitremap(int oldbit,
  const unsigned long *old, const unsigned long *new, int bits);
extern void bitmap_onto(unsigned long *dst, const unsigned long *orig,
  const unsigned long *relmap, int bits);
extern void bitmap_fold(unsigned long *dst, const unsigned long *orig,
  int sz, int bits);
extern int bitmap_find_free_region(unsigned long *bitmap, unsigned int bits, int order);
extern void bitmap_release_region(unsigned long *bitmap, unsigned int pos, int order);
extern int bitmap_allocate_region(unsigned long *bitmap, unsigned int pos, int order);
extern void bitmap_copy_le(void *dst, const unsigned long *src, int nbits);
extern int bitmap_ord_to_pos(const unsigned long *bitmap, int n, int bits);
# 159 "include/linux/bitmap.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_zero(unsigned long *dst, int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = 0UL;
 else {
  int len = (((nbits) + (8 * sizeof(long)) - 1) / (8 * sizeof(long))) * sizeof(unsigned long);
  ({ size_t __len = (len); void *__ret; if (__builtin_constant_p(len) && __len >= 64) __ret = memset((dst), (0), __len); else __ret = __builtin_memset((dst), (0), __len); __ret; });
 }
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_fill(unsigned long *dst, int nbits)
{
 size_t nlongs = (((nbits) + (8 * sizeof(long)) - 1) / (8 * sizeof(long)));
 if (!(__builtin_constant_p(nbits) && (nbits) <= 32)) {
  int len = (nlongs - 1) * sizeof(unsigned long);
  ({ size_t __len = (len); void *__ret; if (__builtin_constant_p(len) && __len >= 64) __ret = memset((dst), (0xff), __len); else __ret = __builtin_memset((dst), (0xff), __len); __ret; });
 }
 dst[nlongs - 1] = ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL );
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_copy(unsigned long *dst, const unsigned long *src,
   int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = *src;
 else {
  int len = (((nbits) + (8 * sizeof(long)) - 1) / (8 * sizeof(long))) * sizeof(unsigned long);
  ({ size_t __len = (len); void *__ret; if (__builtin_constant_p(len) && __len >= 64) __ret = memcpy((dst), (src), __len); else __ret = __builtin_memcpy((dst), (src), __len); __ret; });
 }
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_and(unsigned long *dst, const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return (*dst = *src1 & *src2 & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL )) != 0;
 return __bitmap_and(dst, src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_or(unsigned long *dst, const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = *src1 | *src2;
 else
  __bitmap_or(dst, src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_xor(unsigned long *dst, const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = *src1 ^ *src2;
 else
  __bitmap_xor(dst, src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_andnot(unsigned long *dst, const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return (*dst = *src1 & ~(*src2) & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL )) != 0;
 return __bitmap_andnot(dst, src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_complement(unsigned long *dst, const unsigned long *src,
   unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = ~(*src);
 else
  __bitmap_complement(dst, src, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_equal(const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return ! ((*src1 ^ *src2) & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL ));
 else
  return __bitmap_equal(src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_intersects(const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return ((*src1 & *src2) & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL )) != 0;
 else
  return __bitmap_intersects(src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_subset(const unsigned long *src1,
   const unsigned long *src2, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return ! ((*src1 & ~(*src2)) & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL ));
 else
  return __bitmap_subset(src1, src2, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_empty(const unsigned long *src, unsigned nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return ! (*src & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL ));
 else
  return __bitmap_empty(src, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_full(const unsigned long *src, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return ! (~(*src) & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL ));
 else
  return __bitmap_full(src, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_weight(const unsigned long *src, unsigned int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  return hweight_long(*src & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL ));
 return __bitmap_weight(src, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_shift_right(unsigned long *dst,
   const unsigned long *src, int n, int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = (*src & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL )) >> n;
 else
  __bitmap_shift_right(dst, src, n, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bitmap_shift_left(unsigned long *dst,
   const unsigned long *src, int n, int nbits)
{
 if ((__builtin_constant_p(nbits) && (nbits) <= 32))
  *dst = (*src << n) & ( ((nbits) % 32) ? (1UL<<((nbits) % 32))-1 : ~0UL );
 else
  __bitmap_shift_left(dst, src, n, nbits);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bitmap_parse(const char *buf, unsigned int buflen,
   unsigned long *maskp, int nmaskbits)
{
 return __bitmap_parse(buf, buflen, 0, maskp, nmaskbits);
}
# 12 "include/linux/cpumask.h" 2


typedef struct cpumask { unsigned long bits[(((1) + (8 * sizeof(long)) - 1) / (8 * sizeof(long)))]; } cpumask_t;
# 79 "include/linux/cpumask.h"
extern const struct cpumask *const cpu_possible_mask;
extern const struct cpumask *const cpu_online_mask;
extern const struct cpumask *const cpu_present_mask;
extern const struct cpumask *const cpu_active_mask;
# 105 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_check(unsigned int cpu)
{



 return cpu;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_first(const struct cpumask *srcp)
{
 return 0;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_next(int n, const struct cpumask *srcp)
{
 return n+1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_next_zero(int n, const struct cpumask *srcp)
{
 return n+1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_next_and(int n,
         const struct cpumask *srcp,
         const struct cpumask *andp)
{
 return n+1;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_any_but(const struct cpumask *mask,
        unsigned int cpu)
{
 return 1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_set_cpu_local_first(int i, int numa_node, cpumask_t *dstp)
{
 set_bit(0, ((dstp)->bits));

 return 0;
}
# 263 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_set_cpu(unsigned int cpu, struct cpumask *dstp)
{
 set_bit(cpumask_check(cpu), ((dstp)->bits));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_clear_cpu(int cpu, struct cpumask *dstp)
{
 clear_bit(cpumask_check(cpu), ((dstp)->bits));
}
# 299 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_test_and_set_cpu(int cpu, struct cpumask *cpumask)
{
 return test_and_set_bit(cpumask_check(cpu), ((cpumask)->bits));
}
# 313 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_test_and_clear_cpu(int cpu, struct cpumask *cpumask)
{
 return test_and_clear_bit(cpumask_check(cpu), ((cpumask)->bits));
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_setall(struct cpumask *dstp)
{
 bitmap_fill(((dstp)->bits), 1);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_clear(struct cpumask *dstp)
{
 bitmap_zero(((dstp)->bits), 1);
}
# 344 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_and(struct cpumask *dstp,
          const struct cpumask *src1p,
          const struct cpumask *src2p)
{
 return bitmap_and(((dstp)->bits), ((src1p)->bits),
           ((src2p)->bits), 1);
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_or(struct cpumask *dstp, const struct cpumask *src1p,
         const struct cpumask *src2p)
{
 bitmap_or(((dstp)->bits), ((src1p)->bits),
          ((src2p)->bits), 1);
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_xor(struct cpumask *dstp,
          const struct cpumask *src1p,
          const struct cpumask *src2p)
{
 bitmap_xor(((dstp)->bits), ((src1p)->bits),
           ((src2p)->bits), 1);
}
# 387 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_andnot(struct cpumask *dstp,
      const struct cpumask *src1p,
      const struct cpumask *src2p)
{
 return bitmap_andnot(((dstp)->bits), ((src1p)->bits),
       ((src2p)->bits), 1);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_complement(struct cpumask *dstp,
          const struct cpumask *srcp)
{
 bitmap_complement(((dstp)->bits), ((srcp)->bits),
           1);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool cpumask_equal(const struct cpumask *src1p,
    const struct cpumask *src2p)
{
 return bitmap_equal(((src1p)->bits), ((src2p)->bits),
       1);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool cpumask_intersects(const struct cpumask *src1p,
         const struct cpumask *src2p)
{
 return bitmap_intersects(((src1p)->bits), ((src2p)->bits),
            1);
}
# 438 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_subset(const struct cpumask *src1p,
     const struct cpumask *src2p)
{
 return bitmap_subset(((src1p)->bits), ((src2p)->bits),
        1);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool cpumask_empty(const struct cpumask *srcp)
{
 return bitmap_empty(((srcp)->bits), 1);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool cpumask_full(const struct cpumask *srcp)
{
 return bitmap_full(((srcp)->bits), 1);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int cpumask_weight(const struct cpumask *srcp)
{
 return bitmap_weight(((srcp)->bits), 1);
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_shift_right(struct cpumask *dstp,
           const struct cpumask *srcp, int n)
{
 bitmap_shift_right(((dstp)->bits), ((srcp)->bits), n,
            1);
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_shift_left(struct cpumask *dstp,
          const struct cpumask *srcp, int n)
{
 bitmap_shift_left(((dstp)->bits), ((srcp)->bits), n,
           1);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpumask_copy(struct cpumask *dstp,
    const struct cpumask *srcp)
{
 bitmap_copy(((dstp)->bits), ((srcp)->bits), 1);
}
# 550 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_scnprintf(char *buf, int len,
        const struct cpumask *srcp)
{
 return bitmap_scnprintf(buf, len, ((srcp)->bits), 1);
}
# 564 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_parse_user(const char *buf, int len,
         struct cpumask *dstp)
{
 return bitmap_parse_user(buf, len, ((dstp)->bits), 1);
}
# 578 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_parselist_user(const char *buf, int len,
         struct cpumask *dstp)
{
 return bitmap_parselist_user(buf, len, ((dstp)->bits),
       1);
}
# 594 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpulist_scnprintf(char *buf, int len,
        const struct cpumask *srcp)
{
 return bitmap_scnlistprintf(buf, len, ((srcp)->bits),
        1);
}
# 608 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpumask_parse(const char *buf, struct cpumask *dstp)
{
 char *nl = strchr(buf, '\n');
 unsigned int len = nl ? (unsigned int)(nl - buf) : strlen(buf);

 return bitmap_parse(buf, len, ((dstp)->bits), 1);
}
# 623 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpulist_parse(const char *buf, struct cpumask *dstp)
{
 return bitmap_parselist(buf, ((dstp)->bits), 1);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) size_t cpumask_size(void)
{


 return (((1) + (8 * sizeof(long)) - 1) / (8 * sizeof(long))) * sizeof(long);
}
# 691 "include/linux/cpumask.h"
typedef struct cpumask cpumask_var_t[1];



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool alloc_cpumask_var(cpumask_var_t *mask, gfp_t flags)
{
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool alloc_cpumask_var_node(cpumask_var_t *mask, gfp_t flags,
       int node)
{
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool zalloc_cpumask_var(cpumask_var_t *mask, gfp_t flags)
{
 cpumask_clear(*mask);
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool zalloc_cpumask_var_node(cpumask_var_t *mask, gfp_t flags,
       int node)
{
 cpumask_clear(*mask);
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void alloc_bootmem_cpumask_var(cpumask_var_t *mask)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void free_cpumask_var(cpumask_var_t mask)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void free_bootmem_cpumask_var(cpumask_var_t mask)
{
}




extern const unsigned long cpu_all_bits[(((1) + (8 * sizeof(long)) - 1) / (8 * sizeof(long)))];
# 745 "include/linux/cpumask.h"
void set_cpu_possible(unsigned int cpu, bool possible);
void set_cpu_present(unsigned int cpu, bool present);
void set_cpu_online(unsigned int cpu, bool online);
void set_cpu_active(unsigned int cpu, bool active);
void init_cpu_present(const struct cpumask *src);
void init_cpu_possible(const struct cpumask *src);
void init_cpu_online(const struct cpumask *src);
# 767 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __check_is_bitmap(const unsigned long *bitmap)
{
 return 1;
}
# 779 "include/linux/cpumask.h"
extern const unsigned long
 cpu_bit_bitmap[32 +1][(((1) + (8 * sizeof(long)) - 1) / (8 * sizeof(long)))];

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) const struct cpumask *get_cpu_mask(unsigned int cpu)
{
 const unsigned long *p = cpu_bit_bitmap[1 + cpu % 32];
 p -= cpu / 32;
 return ((struct cpumask *)(1 ? (p) : (void *)sizeof(__check_is_bitmap(p))));
}
# 879 "include/linux/cpumask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpu_set(int cpu, volatile cpumask_t *dstp)
{
 set_bit(cpu, dstp->bits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpu_clear(int cpu, volatile cpumask_t *dstp)
{
 clear_bit(cpu, dstp->bits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpus_setall(cpumask_t *dstp, int nbits)
{
 bitmap_fill(dstp->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpus_clear(cpumask_t *dstp, int nbits)
{
 bitmap_zero(dstp->bits, nbits);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpu_test_and_set(int cpu, cpumask_t *addr)
{
 return test_and_set_bit(cpu, addr->bits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_and(cpumask_t *dstp, const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 return bitmap_and(dstp->bits, src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpus_or(cpumask_t *dstp, const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 bitmap_or(dstp->bits, src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpus_xor(cpumask_t *dstp, const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 bitmap_xor(dstp->bits, src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_andnot(cpumask_t *dstp, const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 return bitmap_andnot(dstp->bits, src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_equal(const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 return bitmap_equal(src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_intersects(const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 return bitmap_intersects(src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_subset(const cpumask_t *src1p,
     const cpumask_t *src2p, int nbits)
{
 return bitmap_subset(src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_empty(const cpumask_t *srcp, int nbits)
{
 return bitmap_empty(srcp->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __cpus_weight(const cpumask_t *srcp, int nbits)
{
 return bitmap_weight(srcp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __cpus_shift_left(cpumask_t *dstp,
     const cpumask_t *srcp, int n, int nbits)
{
 bitmap_shift_left(dstp->bits, srcp->bits, n, nbits);
}
# 15 "./arch/mips/include/asm/processor.h" 2


# 1 "./arch/mips/include/uapi/asm/cachectl.h" 1
# 18 "./arch/mips/include/asm/processor.h" 2


# 1 "./arch/mips/include/asm/mipsregs.h" 1
# 18 "./arch/mips/include/asm/mipsregs.h"
# 1 "./arch/mips/include/asm/hazards.h" 1
# 360 "./arch/mips/include/asm/hazards.h"
extern void mips_ihb(void);
# 19 "./arch/mips/include/asm/mipsregs.h" 2
# 769 "./arch/mips/include/asm/mipsregs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mm_insn_16bit(u16 insn)
{
 u16 opcode = (insn >> 10) & 0x7;

 return (opcode >= 1 && opcode <= 3) ? 1 : 0;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tlbinvf(void)
{
 __asm__ __volatile__(
  ".set push\n\t"
  ".set noreorder\n\t"
  ".word 0x42000004\n\t"
  ".set pop");
}
# 1760 "./arch/mips/include/asm/mipsregs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tlb_probe(void)
{
 __asm__ __volatile__(
  ".set noreorder\n\t"
  "tlbp\n\t"
  ".set reorder");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tlb_read(void)
{
# 1787 "./arch/mips/include/asm/mipsregs.h"
 __asm__ __volatile__(
  ".set noreorder\n\t"
  "tlbr\n\t"
  ".set reorder");
# 1803 "./arch/mips/include/asm/mipsregs.h"
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tlb_write_indexed(void)
{
 __asm__ __volatile__(
  ".set noreorder\n\t"
  "tlbwi\n\t"
  ".set reorder");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tlb_write_random(void)
{
 __asm__ __volatile__(
  ".set noreorder\n\t"
  "tlbwr\n\t"
  ".set reorder");
}
# 1862 "./arch/mips/include/asm/mipsregs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_status(unsigned int set) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_status(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_status(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_cause(unsigned int set) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$13" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$13" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$13" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$13" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_cause(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$13" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$13" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$13" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$13" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_cause(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$13" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$13" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$13" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$13" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_config(unsigned int set) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$16" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$16" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$16" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$16" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_config(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$16" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$16" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$16" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$16" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_config(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$16" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$16" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$16" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$16" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_config5(unsigned int set) { unsigned int res, new; res = ({ int __res; if (5 == 0) __asm__ __volatile__( "mfc0\t%0, " "$16" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$16" ", " "5" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (5 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$16" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$16" ", " "5" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_config5(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (5 == 0) __asm__ __volatile__( "mfc0\t%0, " "$16" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$16" ", " "5" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (5 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$16" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$16" ", " "5" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_config5(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (5 == 0) __asm__ __volatile__( "mfc0\t%0, " "$16" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$16" ", " "5" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (5 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$16" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$16" ", " "5" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_intcontrol(unsigned int set) { unsigned int res, new; res = ({ int __res; __asm__ __volatile__( "cfc0\t%0, " "$20" "\n\t" : "=r" (__res)); __res; }); new = res | set; do { __asm__ __volatile__( "ctc0\t%z0, " "$20" "\n\t" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_intcontrol(unsigned int clear) { unsigned int res, new; res = ({ int __res; __asm__ __volatile__( "cfc0\t%0, " "$20" "\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { __asm__ __volatile__( "ctc0\t%z0, " "$20" "\n\t" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_intcontrol(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; __asm__ __volatile__( "cfc0\t%0, " "$20" "\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { __asm__ __volatile__( "ctc0\t%z0, " "$20" "\n\t" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_intctl(unsigned int set) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_intctl(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_intctl(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_srsmap(unsigned int set) { unsigned int res, new; res = ({ int __res; if (3 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "3" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (3 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "3" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_srsmap(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (3 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "3" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (3 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "3" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_srsmap(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (3 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "3" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (3 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$12" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$12" ", " "3" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_config_0(unsigned int set) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_config_0(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_config_0(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_bus_pll(unsigned int set) { unsigned int res, new; res = ({ int __res; if (4 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "4" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (4 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "4" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_bus_pll(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (4 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "4" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (4 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "4" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_bus_pll(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (4 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "4" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (4 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "4" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_reset(unsigned int set) { unsigned int res, new; res = ({ int __res; if (5 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "5" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (5 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "5" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_reset(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (5 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "5" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (5 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "5" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_reset(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (5 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "5" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (5 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "5" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_cmt_intr(unsigned int set) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_cmt_intr(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_cmt_intr(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_cmt_ctrl(unsigned int set) { unsigned int res, new; res = ({ int __res; if (2 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "2" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (2 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "2" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_cmt_ctrl(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (2 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "2" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (2 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "2" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_cmt_ctrl(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (2 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "2" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (2 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "2" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_config(unsigned int set) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_config(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_config(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (0 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "0" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_brcm_mode(unsigned int set) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_brcm_mode(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_brcm_mode(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$22" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$22" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$22" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$22" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int get_ebase_cpunum(void)
{
 return ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$15" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$15" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }) & 0x3ff;
}
# 21 "./arch/mips/include/asm/processor.h" 2
# 1 "./arch/mips/include/asm/prefetch.h" 1
# 22 "./arch/mips/include/asm/processor.h" 2
# 32 "./arch/mips/include/asm/processor.h"
extern unsigned int vced_count, vcei_count;
# 106 "./arch/mips/include/asm/processor.h"
union fpureg {
 __u32 val32[64 / 32];
 __u64 val64[64 / 64];
};
# 129 "./arch/mips/include/asm/processor.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 get_fpr32(union fpureg *fpr, unsigned idx) { return fpr->val32[((64 / (32)) - 1 - (idx))]; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_fpr32(union fpureg *fpr, unsigned idx, u32 val) { fpr->val32[((64 / (32)) - 1 - (idx))] = val; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 get_fpr64(union fpureg *fpr, unsigned idx) { return fpr->val64[((64 / (64)) - 1 - (idx))]; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_fpr64(union fpureg *fpr, unsigned idx, u64 val) { fpr->val64[((64 / (64)) - 1 - (idx))] = val; }







struct mips_fpu_struct {
 union fpureg fpr[32];
 unsigned int fcr31;
 unsigned int msacsr;
};



typedef __u32 dspreg_t;

struct mips_dsp_state {
 dspreg_t dspr[6];
 unsigned int dspcontrol;
};





struct mips3264_watch_reg_state {



 unsigned long watchlo[4];

 u16 watchhi[4];
};

union mips_watch_reg_state {
 struct mips3264_watch_reg_state mips3264;
};
# 237 "./arch/mips/include/asm/processor.h"
typedef struct {
 unsigned long seg;
} mm_segment_t;
# 249 "./arch/mips/include/asm/processor.h"
struct mips_abi;




struct thread_struct {

 unsigned long reg16;
 unsigned long reg17, reg18, reg19, reg20, reg21, reg22, reg23;
 unsigned long reg29, reg30, reg31;


 unsigned long cp0_status;


 struct mips_fpu_struct fpu ;
# 273 "./arch/mips/include/asm/processor.h"
 struct mips_dsp_state dsp;


 union mips_watch_reg_state watch;


 unsigned long cp0_badvaddr;
 unsigned long cp0_baduaddr;
 unsigned long error_code;







 struct mips_abi *abi;
};
# 354 "./arch/mips/include/asm/processor.h"
struct task_struct;




extern unsigned long thread_saved_pc(struct task_struct *tsk);




extern void start_thread(struct pt_regs * regs, unsigned long pc, unsigned long sp);

unsigned long get_wchan(struct task_struct *p);
# 16 "./arch/mips/include/asm/thread_info.h" 2
# 24 "./arch/mips/include/asm/thread_info.h"
struct thread_info {
 struct task_struct *task;
 struct exec_domain *exec_domain;
 unsigned long flags;
 unsigned long tp_value;
 __u32 cpu;
 int preempt_count;

 mm_segment_t addr_limit;




 struct restart_block restart_block;
 struct pt_regs *regs;
};
# 61 "./arch/mips/include/asm/thread_info.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct thread_info *current_thread_info(void)
{
 register struct thread_info *__current_thread_info __asm__("$28");

 return __current_thread_info;
}
# 55 "include/linux/thread_info.h" 2
# 69 "include/linux/thread_info.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_ti_thread_flag(struct thread_info *ti, int flag)
{
 set_bit(flag, (unsigned long *)&ti->flags);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_ti_thread_flag(struct thread_info *ti, int flag)
{
 clear_bit(flag, (unsigned long *)&ti->flags);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_set_ti_thread_flag(struct thread_info *ti, int flag)
{
 return test_and_set_bit(flag, (unsigned long *)&ti->flags);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_and_clear_ti_thread_flag(struct thread_info *ti, int flag)
{
 return test_and_clear_bit(flag, (unsigned long *)&ti->flags);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int test_ti_thread_flag(struct thread_info *ti, int flag)
{
 return test_bit(flag, (unsigned long *)&ti->flags);
}
# 125 "include/linux/thread_info.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_restore_sigmask(void)
{
 set_ti_thread_flag(current_thread_info(), 9);
 ({ int __ret_warn_on = !!(!test_ti_thread_flag(current_thread_info(), 1)); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/thread_info.h", 128); __builtin_expect(!!(__ret_warn_on), 0); });
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_restore_sigmask(void)
{
 clear_ti_thread_flag(current_thread_info(), 9);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool test_restore_sigmask(void)
{
 return test_ti_thread_flag(current_thread_info(), 9);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool test_and_clear_restore_sigmask(void)
{
 return test_and_clear_ti_thread_flag(current_thread_info(), 9);
}
# 5 "include/asm-generic/preempt.h" 2



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) int preempt_count(void)
{
 return current_thread_info()->preempt_count;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) int *preempt_count_ptr(void)
{
 return &current_thread_info()->preempt_count;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void preempt_count_set(int pc)
{
 *preempt_count_ptr() = pc;
}
# 37 "include/asm-generic/preempt.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void set_preempt_need_resched(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void clear_preempt_need_resched(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) bool test_preempt_need_resched(void)
{
 return false;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void __preempt_count_add(int val)
{
 *preempt_count_ptr() += val;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void __preempt_count_sub(int val)
{
 *preempt_count_ptr() -= val;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) bool __preempt_count_dec_and_test(void)
{





 return !--*preempt_count_ptr() && test_ti_thread_flag(current_thread_info(), 2);
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) bool should_resched(void)
{
 return __builtin_expect(!!(!preempt_count() && test_ti_thread_flag(current_thread_info(), 2)), 0);
}
# 1 "arch/mips/include/generated/asm/preempt.h" 2
# 19 "include/linux/preempt.h" 2
# 51 "include/linux/spinlock.h" 2


# 1 "include/linux/irqflags.h" 1
# 15 "include/linux/irqflags.h"
# 1 "./arch/mips/include/asm/irqflags.h" 1
# 22 "./arch/mips/include/asm/irqflags.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void arch_local_irq_disable(void)
{
 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	noat						\n"
 "	di							\n"
 "	" "sll $0, $0, 3" "			\n"
 "	.set	pop						\n"
 :
 :
 : "memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long arch_local_irq_save(void)
{
 unsigned long flags;

 asm __volatile__(
 "	.set	push						\n"
 "	.set	reorder						\n"
 "	.set	noat						\n"
 "	di	%[flags]					\n"
 "	andi	%[flags], 1					\n"
 "	" "sll $0, $0, 3" "			\n"
 "	.set	pop						\n"
 : [flags] "=r" (flags)
 :
 : "memory");

 return flags;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void arch_local_irq_restore(unsigned long flags)
{
 unsigned long __tmp1;

 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	noreorder					\n"
 "	.set	noat						\n"





 "	beqz	%[flags], 1f					\n"
 "	di							\n"
 "	ei							\n"
 "1:								\n"
# 79 "./arch/mips/include/asm/irqflags.h"
 "	" "sll $0, $0, 3" "			\n"
 "	.set	pop						\n"
 : [flags] "=r" (__tmp1)
 : "0" (flags)
 : "memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __arch_local_irq_restore(unsigned long flags)
{
 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	noreorder					\n"
 "	.set	noat						\n"





 "	beqz	%[flags], 1f					\n"
 "	di							\n"
 "	ei							\n"
 "1:								\n"
# 109 "./arch/mips/include/asm/irqflags.h"
 "	" "sll $0, $0, 3" "			\n"
 "	.set	pop						\n"
 : [flags] "=r" (flags)
 : "0" (flags)
 : "memory");
}
# 123 "./arch/mips/include/asm/irqflags.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void arch_local_irq_enable(void)
{
 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	reorder						\n"
 "	.set	noat						\n"

 "	ei							\n"






 "	" "sll $0, $0, 3" "			\n"
 "	.set	pop						\n"
 :
 :
 : "memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long arch_local_save_flags(void)
{
 unsigned long flags;

 asm __volatile__(
 "	.set	push						\n"
 "	.set	reorder						\n"
 "	mfc0	%[flags], $12					\n"
 "	.set	pop						\n"
 : [flags] "=r" (flags));

 return flags;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int arch_irqs_disabled_flags(unsigned long flags)
{
 return !(flags & 1);
}
# 16 "include/linux/irqflags.h" 2
# 54 "include/linux/spinlock.h" 2



# 1 "include/linux/bottom_half.h" 1




# 1 "include/linux/preempt_mask.h" 1
# 6 "include/linux/bottom_half.h" 2




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void __local_bh_disable_ip(unsigned long ip, unsigned int cnt)
{
 __preempt_count_add(cnt);
 __asm__ __volatile__("": : :"memory");
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void local_bh_disable(void)
{
 __local_bh_disable_ip(({ __label__ __here; __here: (unsigned long)&&__here; }), (2 * (1UL << (0 + 8))));
}

extern void _local_bh_enable(void);
extern void __local_bh_enable_ip(unsigned long ip, unsigned int cnt);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void local_bh_enable_ip(unsigned long ip)
{
 __local_bh_enable_ip(ip, (2 * (1UL << (0 + 8))));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void local_bh_enable(void)
{
 __local_bh_enable_ip(({ __label__ __here; __here: (unsigned long)&&__here; }), (2 * (1UL << (0 + 8))));
}
# 58 "include/linux/spinlock.h" 2
# 81 "include/linux/spinlock.h"
# 1 "include/linux/spinlock_types.h" 1
# 15 "include/linux/spinlock_types.h"
# 1 "include/linux/spinlock_types_up.h" 1
# 25 "include/linux/spinlock_types_up.h"
typedef struct { } arch_spinlock_t;





typedef struct {

} arch_rwlock_t;
# 16 "include/linux/spinlock_types.h" 2


# 1 "include/linux/lockdep.h" 1
# 12 "include/linux/lockdep.h"
struct task_struct;
struct lockdep_map;


extern int prove_locking;
extern int lock_stat;
# 373 "include/linux/lockdep.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void lockdep_off(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void lockdep_on(void)
{
}
# 414 "include/linux/lockdep.h"
struct lock_class_key { };
# 469 "include/linux/lockdep.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void print_irqtrace_events(struct task_struct *curr)
{
}
# 19 "include/linux/spinlock_types.h" 2

typedef struct raw_spinlock {
 arch_spinlock_t raw_lock;
# 32 "include/linux/spinlock_types.h"
} raw_spinlock_t;
# 64 "include/linux/spinlock_types.h"
typedef struct spinlock {
 union {
  struct raw_spinlock rlock;
# 75 "include/linux/spinlock_types.h"
 };
} spinlock_t;
# 86 "include/linux/spinlock_types.h"
# 1 "include/linux/rwlock_types.h" 1
# 11 "include/linux/rwlock_types.h"
typedef struct {
 arch_rwlock_t raw_lock;
# 23 "include/linux/rwlock_types.h"
} rwlock_t;
# 87 "include/linux/spinlock_types.h" 2
# 82 "include/linux/spinlock.h" 2







# 1 "include/linux/spinlock_up.h" 1
# 90 "include/linux/spinlock.h" 2
# 155 "include/linux/spinlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void do_raw_spin_lock(raw_spinlock_t *lock)
{
 (void)0;
 do { __asm__ __volatile__("": : :"memory"); (void)(&lock->raw_lock); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
do_raw_spin_lock_flags(raw_spinlock_t *lock, unsigned long *flags)
{
 (void)0;
 do { __asm__ __volatile__("": : :"memory"); (void)(&lock->raw_lock); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int do_raw_spin_trylock(raw_spinlock_t *lock)
{
 return ({ __asm__ __volatile__("": : :"memory"); (void)(&(lock)->raw_lock); 1; });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void do_raw_spin_unlock(raw_spinlock_t *lock)
{
 do { __asm__ __volatile__("": : :"memory"); (void)(&lock->raw_lock); } while (0);
 (void)0;
}
# 281 "include/linux/spinlock.h"
# 1 "include/linux/rwlock.h" 1
# 282 "include/linux/spinlock.h" 2







# 1 "include/linux/spinlock_api_up.h" 1
# 290 "include/linux/spinlock.h" 2






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) raw_spinlock_t *spinlock_check(spinlock_t *lock)
{
 return &lock->rlock;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_lock(spinlock_t *lock)
{
 do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_lock_bh(spinlock_t *lock)
{
 do { __local_bh_disable_ip(({ __label__ __here; __here: (unsigned long)&&__here; }), ((2 * (1UL << (0 + 8))) + 0)); do { (void)0; (void)(&lock->rlock); } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int spin_trylock(spinlock_t *lock)
{
 return (({ do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0); 1; }));
}
# 332 "include/linux/spinlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_lock_irq(spinlock_t *lock)
{
 do { do { arch_local_irq_disable(); do { } while (0); } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0); } while (0);
}
# 347 "include/linux/spinlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_unlock(spinlock_t *lock)
{
 do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_unlock_bh(spinlock_t *lock)
{
 do { __local_bh_enable_ip(({ __label__ __here; __here: (unsigned long)&&__here; }), ((2 * (1UL << (0 + 8))) + 0)); do { (void)0; (void)(&lock->rlock); } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_unlock_irq(spinlock_t *lock)
{
 do { do { do { } while (0); arch_local_irq_enable(); } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_unlock_irqrestore(spinlock_t *lock, unsigned long flags)
{
 do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); do { do { if (({ ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(flags); })) { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); } } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0); } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int spin_trylock_bh(spinlock_t *lock)
{
 return (({ do { __local_bh_disable_ip(({ __label__ __here; __here: (unsigned long)&&__here; }), ((2 * (1UL << (0 + 8))) + 0)); do { (void)0; (void)(&lock->rlock); } while (0); } while (0); 1; }));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int spin_trylock_irq(spinlock_t *lock)
{
 return ({ do { arch_local_irq_disable(); do { } while (0); } while (0); (({ do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(&lock->rlock); } while (0); } while (0); 1; })) ? 1 : ({ do { do { } while (0); arch_local_irq_enable(); } while (0); 0; }); });
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void spin_unlock_wait(spinlock_t *lock)
{
 do { __asm__ __volatile__("": : :"memory"); } while (((void)(&(&lock->rlock)->raw_lock), 0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int spin_is_locked(spinlock_t *lock)
{
 return ((void)(&(&lock->rlock)->raw_lock), 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int spin_is_contended(spinlock_t *lock)
{
 return (((void)(&(&lock->rlock)->raw_lock), 0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int spin_can_lock(spinlock_t *lock)
{
 return (!((void)(&(&lock->rlock)->raw_lock), 0));
}







# 1 "include/linux/atomic.h" 1



# 1 "./arch/mips/include/asm/atomic.h" 1
# 21 "./arch/mips/include/asm/atomic.h"
# 1 "./arch/mips/include/asm/cmpxchg.h" 1
# 15 "./arch/mips/include/asm/cmpxchg.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __xchg_u32(volatile int * m, unsigned int val)
{
 __u32 retval;

 __asm__ __volatile__("		\n" : : :"memory");

 if (1 && 0) {
  unsigned long dummy;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	ll	%0, %3			# xchg_u32	\n"
  "	.set	mips0					\n"
  "	move	%2, %z4					\n"
  "	.set	arch=r4000				\n"
  "	sc	%2, %1					\n"
  "	beqzl	%2, 1b					\n"
  "	.set	mips0					\n"
  : "=&r" (retval), "=m" (*m), "=&r" (dummy)
  : "R" (*m), "Jr" (val)
  : "memory");
 } else if (1) {
  unsigned long dummy;

  do {
   __asm__ __volatile__(
   "	.set	arch=r4000			\n"
   "	ll	%0, %3		# xchg_u32	\n"
   "	.set	mips0				\n"
   "	move	%2, %z4				\n"
   "	.set	arch=r4000			\n"
   "	sc	%2, %1				\n"
   "	.set	mips0				\n"
   : "=&r" (retval), "=m" (*m), "=&r" (dummy)
   : "R" (*m), "Jr" (val)
   : "memory");
  } while (__builtin_expect(!!(!dummy), 0));
 } else {
  unsigned long flags;

  do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0);
  retval = *m;
  *m = val;
  do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0);
 }

 __asm__ __volatile__("		\n" : : :"memory");

 return retval;
}
# 114 "./arch/mips/include/asm/cmpxchg.h"
extern __u64 __xchg_u64_unsupported_on_32bit_kernels(volatile __u64 * m, __u64 val);



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __xchg(unsigned long x, volatile void * ptr, int size)
{
 switch (size) {
 case 4:
  return __xchg_u32(ptr, x);
 case 8:
  return __xchg_u64_unsupported_on_32bit_kernels(ptr, x);
 }

 return x;
}
# 195 "./arch/mips/include/asm/cmpxchg.h"
extern void __cmpxchg_called_with_bad_pointer(void);
# 242 "./arch/mips/include/asm/cmpxchg.h"
# 1 "include/asm-generic/cmpxchg-local.h" 1






extern unsigned long wrong_size_cmpxchg(volatile void *ptr)
 __attribute__((noreturn));





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __cmpxchg_local_generic(volatile void *ptr,
  unsigned long old, unsigned long new, int size)
{
 unsigned long flags, prev;




 if (size == 8 && sizeof(unsigned long) != 8)
  wrong_size_cmpxchg(ptr);

 do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0);
 switch (size) {
 case 1: prev = *(u8 *)ptr;
  if (prev == old)
   *(u8 *)ptr = (u8)new;
  break;
 case 2: prev = *(u16 *)ptr;
  if (prev == old)
   *(u16 *)ptr = (u16)new;
  break;
 case 4: prev = *(u32 *)ptr;
  if (prev == old)
   *(u32 *)ptr = (u32)new;
  break;
 case 8: prev = *(u64 *)ptr;
  if (prev == old)
   *(u64 *)ptr = (u64)new;
  break;
 default:
  wrong_size_cmpxchg(ptr);
 }
 do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0);
 return prev;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 __cmpxchg64_local_generic(volatile void *ptr,
  u64 old, u64 new)
{
 u64 prev;
 unsigned long flags;

 do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0);
 prev = *(u64 *)ptr;
 if (prev == old)
  *(u64 *)ptr = new;
 do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0);
 return prev;
}
# 243 "./arch/mips/include/asm/cmpxchg.h" 2
# 22 "./arch/mips/include/asm/atomic.h" 2
# 134 "./arch/mips/include/asm/atomic.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_add(int i, atomic_t * v) { if (1 && 0) { int temp; __asm__ __volatile__( "	.set	arch=r4000				\n" "1:	ll	%0, %1		# atomic_" "add" "	\n" "	" "addu" " %0, %2				\n" "	sc	%0, %1					\n" "	beqzl	%0, 1b					\n" "	.set	mips0					\n" : "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } else if (1) { int temp; do { __asm__ __volatile__( "	.set	arch=r4000			\n" "	ll	%0, %1		# atomic_" "add" "\n" "	" "addu" " %0, %2			\n" "	sc	%0, %1				\n" "	.set	mips0				\n" : "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } while (__builtin_expect(!!(!temp), 0)); } else { unsigned long flags; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); v->counter += i; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); } } static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_add_return(int i, atomic_t * v) { int result; __asm__ __volatile__("		\n" : : :"memory"); if (1 && 0) { int temp; __asm__ __volatile__( "	.set	arch=r4000				\n" "1:	ll	%1, %2		# atomic_" "add" "_return	\n" "	" "addu" " %0, %1, %3				\n" "	sc	%0, %2					\n" "	beqzl	%0, 1b					\n" "	" "addu" " %0, %1, %3				\n" "	.set	mips0					\n" : "=&r" (result), "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } else if (1) { int temp; do { __asm__ __volatile__( "	.set	arch=r4000			\n" "	ll	%1, %2	# atomic_" "add" "_return	\n" "	" "addu" " %0, %1, %3			\n" "	sc	%0, %2				\n" "	.set	mips0				\n" : "=&r" (result), "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } while (__builtin_expect(!!(!result), 0)); result = temp; result += i; } else { unsigned long flags; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); result = v->counter; result += i; v->counter = result; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); } __asm__ __volatile__("		\n" : : :"memory"); return result; }
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_sub(int i, atomic_t * v) { if (1 && 0) { int temp; __asm__ __volatile__( "	.set	arch=r4000				\n" "1:	ll	%0, %1		# atomic_" "sub" "	\n" "	" "subu" " %0, %2				\n" "	sc	%0, %1					\n" "	beqzl	%0, 1b					\n" "	.set	mips0					\n" : "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } else if (1) { int temp; do { __asm__ __volatile__( "	.set	arch=r4000			\n" "	ll	%0, %1		# atomic_" "sub" "\n" "	" "subu" " %0, %2			\n" "	sc	%0, %1				\n" "	.set	mips0				\n" : "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } while (__builtin_expect(!!(!temp), 0)); } else { unsigned long flags; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); v->counter -= i; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); } } static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_sub_return(int i, atomic_t * v) { int result; __asm__ __volatile__("		\n" : : :"memory"); if (1 && 0) { int temp; __asm__ __volatile__( "	.set	arch=r4000				\n" "1:	ll	%1, %2		# atomic_" "sub" "_return	\n" "	" "subu" " %0, %1, %3				\n" "	sc	%0, %2					\n" "	beqzl	%0, 1b					\n" "	" "subu" " %0, %1, %3				\n" "	.set	mips0					\n" : "=&r" (result), "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } else if (1) { int temp; do { __asm__ __volatile__( "	.set	arch=r4000			\n" "	ll	%1, %2	# atomic_" "sub" "_return	\n" "	" "subu" " %0, %1, %3			\n" "	sc	%0, %2				\n" "	.set	mips0				\n" : "=&r" (result), "=&r" (temp), "+m" (v->counter) : "Ir" (i)); } while (__builtin_expect(!!(!result), 0)); result = temp; result -= i; } else { unsigned long flags; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); result = v->counter; result -= i; v->counter = result; do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); } __asm__ __volatile__("		\n" : : :"memory"); return result; }
# 149 "./arch/mips/include/asm/atomic.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_sub_if_positive(int i, atomic_t * v)
{
 int result;

 __asm__ __volatile__("		\n" : : :"memory");

 if (1 && 0) {
  int temp;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	ll	%1, %2		# atomic_sub_if_positive\n"
  "	subu	%0, %1, %3				\n"
  "	bltz	%0, 1f					\n"
  "	sc	%0, %2					\n"
  "	.set	noreorder				\n"
  "	beqzl	%0, 1b					\n"
  "	 subu	%0, %1, %3				\n"
  "	.set	reorder					\n"
  "1:							\n"
  "	.set	mips0					\n"
  : "=&r" (result), "=&r" (temp), "+m" (v->counter)
  : "Ir" (i), "m" (v->counter)
  : "memory");
 } else if (1) {
  int temp;

  __asm__ __volatile__(
  "	.set	arch=r4000				\n"
  "1:	ll	%1, %2		# atomic_sub_if_positive\n"
  "	subu	%0, %1, %3				\n"
  "	bltz	%0, 1f					\n"
  "	sc	%0, %2					\n"
  "	.set	noreorder				\n"
  "	beqz	%0, 1b					\n"
  "	 subu	%0, %1, %3				\n"
  "	.set	reorder					\n"
  "1:							\n"
  "	.set	mips0					\n"
  : "=&r" (result), "=&r" (temp), "+m" (v->counter)
  : "Ir" (i));
 } else {
  unsigned long flags;

  do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0);
  result = v->counter;
  result -= i;
  if (result >= 0)
   v->counter = result;
  do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0);
 }

 __asm__ __volatile__("		\n" : : :"memory");

 return result;
}
# 218 "./arch/mips/include/asm/atomic.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int __atomic_add_unless(atomic_t *v, int a, int u)
{
 int c, old;
 c = (*(volatile typeof((v)->counter) *)&((v)->counter));
 for (;;) {
  if (__builtin_expect(!!(c == (u)), 0))
   break;
  old = (({ __typeof__(&(((v))->counter)) __ptr = (&(((v))->counter)); __typeof__(*(&(((v))->counter))) __old = ((c)); __typeof__(*(&(((v))->counter))) __new = ((c + (a))); __typeof__(*(&(((v))->counter))) __res = 0; __asm__ __volatile__("		\n" : : :"memory"); switch (sizeof(*(__ptr))) { case 4: __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; case 8: if (sizeof(long) == 8) { __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; } default: __cmpxchg_called_with_bad_pointer(); break; } __asm__ __volatile__("		\n" : : :"memory"); __res; }));
  if (__builtin_expect(!!(old == c), 1))
   break;
  c = old;
 }
 return c;
}
# 5 "include/linux/atomic.h" 2
# 15 "include/linux/atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_add_unless(atomic_t *v, int a, int u)
{
 return __atomic_add_unless(v, a, u) != u;
}
# 44 "include/linux/atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_inc_not_zero_hint(atomic_t *v, int hint)
{
 int val, c = hint;


 if (!hint)
  return atomic_add_unless((v), 1, 0);

 do {
  val = (({ __typeof__(&((v)->counter)) __ptr = (&((v)->counter)); __typeof__(*(&((v)->counter))) __old = ((c)); __typeof__(*(&((v)->counter))) __new = ((c + 1)); __typeof__(*(&((v)->counter))) __res = 0; __asm__ __volatile__("		\n" : : :"memory"); switch (sizeof(*(__ptr))) { case 4: __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; case 8: if (sizeof(long) == 8) { __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; } default: __cmpxchg_called_with_bad_pointer(); break; } __asm__ __volatile__("		\n" : : :"memory"); __res; }));
  if (val == c)
   return 1;
  c = val;
 } while (c);

 return 0;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_inc_unless_negative(atomic_t *p)
{
 int v, v1;
 for (v = 0; v >= 0; v = v1) {
  v1 = (({ __typeof__(&((p)->counter)) __ptr = (&((p)->counter)); __typeof__(*(&((p)->counter))) __old = ((v)); __typeof__(*(&((p)->counter))) __new = ((v + 1)); __typeof__(*(&((p)->counter))) __res = 0; __asm__ __volatile__("		\n" : : :"memory"); switch (sizeof(*(__ptr))) { case 4: __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; case 8: if (sizeof(long) == 8) { __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; } default: __cmpxchg_called_with_bad_pointer(); break; } __asm__ __volatile__("		\n" : : :"memory"); __res; }));
  if (__builtin_expect(!!(v1 == v), 1))
   return 1;
 }
 return 0;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_dec_unless_positive(atomic_t *p)
{
 int v, v1;
 for (v = 0; v <= 0; v = v1) {
  v1 = (({ __typeof__(&((p)->counter)) __ptr = (&((p)->counter)); __typeof__(*(&((p)->counter))) __old = ((v)); __typeof__(*(&((p)->counter))) __new = ((v - 1)); __typeof__(*(&((p)->counter))) __res = 0; __asm__ __volatile__("		\n" : : :"memory"); switch (sizeof(*(__ptr))) { case 4: __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; case 8: if (sizeof(long) == 8) { __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; } default: __cmpxchg_called_with_bad_pointer(); break; } __asm__ __volatile__("		\n" : : :"memory"); __res; }));
  if (__builtin_expect(!!(v1 == v), 1))
   return 1;
 }
 return 0;
}
# 115 "include/linux/atomic.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_or(int i, atomic_t *v)
{
 int old;
 int new;

 do {
  old = (*(volatile typeof((v)->counter) *)&((v)->counter));
  new = old | i;
 } while ((({ __typeof__(&((v)->counter)) __ptr = (&((v)->counter)); __typeof__(*(&((v)->counter))) __old = ((old)); __typeof__(*(&((v)->counter))) __new = ((new)); __typeof__(*(&((v)->counter))) __res = 0; __asm__ __volatile__("		\n" : : :"memory"); switch (sizeof(*(__ptr))) { case 4: __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "ll" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "sc" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; case 8: if (sizeof(long) == 8) { __res = ({ __typeof(*(__ptr)) __ret; if (1 && 0) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqzl	$1, 1b				\n" "2:						\n" "	.set	pop				\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else if (1) { __asm__ __volatile__( "	.set	push				\n" "	.set	noat				\n" "	.set	arch=r4000			\n" "1:	" "lld" "	%0, %2		# __cmpxchg_asm \n" "	bne	%0, %z3, 2f			\n" "	.set	mips0				\n" "	move	$1, %z4				\n" "	.set	arch=r4000			\n" "	" "scd" "	$1, %1				\n" "	beqz	$1, 1b				\n" "	.set	pop				\n" "2:						\n" : "=&r" (__ret), "=R" (*__ptr) : "R" (*__ptr), "Jr" (__old), "Jr" (__new) : "memory"); } else { unsigned long __flags; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); __ret = *__ptr; if (__ret == __old) *__ptr = __new; do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } __ret; }); break; } default: __cmpxchg_called_with_bad_pointer(); break; } __asm__ __volatile__("		\n" : : :"memory"); __res; })) != old);
}


# 1 "include/asm-generic/atomic-long.h" 1
# 141 "include/asm-generic/atomic-long.h"
typedef atomic_t atomic_long_t;


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long atomic_long_read(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (long)(*(volatile typeof((v)->counter) *)&((v)->counter));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_long_set(atomic_long_t *l, long i)
{
 atomic_t *v = (atomic_t *)l;

 ((v)->counter = (i));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_long_inc(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 atomic_add(1, (v));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_long_dec(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 atomic_sub(1, (v));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_long_add(long i, atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 atomic_add(i, v);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void atomic_long_sub(long i, atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 atomic_sub(i, v);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_long_sub_and_test(long i, atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (atomic_sub_return((i), (v)) == 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_long_dec_and_test(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (atomic_sub_return(1, (v)) == 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_long_inc_and_test(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (atomic_add_return(1, (v)) == 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int atomic_long_add_negative(long i, atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (atomic_add_return(i, (v)) < 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long atomic_long_add_return(long i, atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (long)atomic_add_return(i, v);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long atomic_long_sub_return(long i, atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (long)atomic_sub_return(i, v);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long atomic_long_inc_return(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (long)atomic_add_return(1, (v));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long atomic_long_dec_return(atomic_long_t *l)
{
 atomic_t *v = (atomic_t *)l;

 return (long)atomic_sub_return(1, (v));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long atomic_long_add_unless(atomic_long_t *l, long a, long u)
{
 atomic_t *v = (atomic_t *)l;

 return (long)atomic_add_unless(v, a, u);
}
# 128 "include/linux/atomic.h" 2

# 1 "include/asm-generic/atomic64.h" 1
# 15 "include/asm-generic/atomic64.h"
typedef struct {
 long long counter;
} atomic64_t;



extern long long atomic64_read(const atomic64_t *v);
extern void atomic64_set(atomic64_t *v, long long i);
# 32 "include/asm-generic/atomic64.h"
extern void atomic64_add(long long a, atomic64_t *v); extern long long atomic64_add_return(long long a, atomic64_t *v);
extern void atomic64_sub(long long a, atomic64_t *v); extern long long atomic64_sub_return(long long a, atomic64_t *v);





extern long long atomic64_dec_if_positive(atomic64_t *v);
extern long long atomic64_cmpxchg(atomic64_t *v, long long o, long long n);
extern long long atomic64_xchg(atomic64_t *v, long long new);
extern int atomic64_add_unless(atomic64_t *v, long long a, long long u);
# 130 "include/linux/atomic.h" 2
# 409 "include/linux/spinlock.h" 2
# 417 "include/linux/spinlock.h"
extern int _atomic_dec_and_lock(atomic_t *atomic, spinlock_t *lock);
# 8 "include/linux/mmzone.h" 2

# 1 "include/linux/wait.h" 1
# 9 "include/linux/wait.h"
# 1 "arch/mips/include/generated/asm/current.h" 1
# 1 "include/asm-generic/current.h" 1
# 1 "arch/mips/include/generated/asm/current.h" 2
# 10 "include/linux/wait.h" 2
# 1 "include/uapi/linux/wait.h" 1
# 11 "include/linux/wait.h" 2

typedef struct __wait_queue wait_queue_t;
typedef int (*wait_queue_func_t)(wait_queue_t *wait, unsigned mode, int flags, void *key);
int default_wake_function(wait_queue_t *wait, unsigned mode, int flags, void *key);





struct __wait_queue {
 unsigned int flags;
 void *private;
 wait_queue_func_t func;
 struct list_head task_list;
};

struct wait_bit_key {
 void *flags;
 int bit_nr;

 unsigned long timeout;
};

struct wait_bit_queue {
 struct wait_bit_key key;
 wait_queue_t wait;
};

struct __wait_queue_head {
 spinlock_t lock;
 struct list_head task_list;
};
typedef struct __wait_queue_head wait_queue_head_t;

struct task_struct;
# 72 "include/linux/wait.h"
extern void __init_waitqueue_head(wait_queue_head_t *q, const char *name, struct lock_class_key *);
# 90 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_waitqueue_entry(wait_queue_t *q, struct task_struct *p)
{
 q->flags = 0;
 q->private = p;
 q->func = default_wake_function;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
init_waitqueue_func_entry(wait_queue_t *q, wait_queue_func_t func)
{
 q->flags = 0;
 q->private = ((void *)0);
 q->func = func;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int waitqueue_active(wait_queue_head_t *q)
{
 return !list_empty(&q->task_list);
}

extern void add_wait_queue(wait_queue_head_t *q, wait_queue_t *wait);
extern void add_wait_queue_exclusive(wait_queue_head_t *q, wait_queue_t *wait);
extern void remove_wait_queue(wait_queue_head_t *q, wait_queue_t *wait);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __add_wait_queue(wait_queue_head_t *head, wait_queue_t *new)
{
 list_add(&new->task_list, &head->task_list);
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
__add_wait_queue_exclusive(wait_queue_head_t *q, wait_queue_t *wait)
{
 wait->flags |= 0x01;
 __add_wait_queue(q, wait);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __add_wait_queue_tail(wait_queue_head_t *head,
      wait_queue_t *new)
{
 list_add_tail(&new->task_list, &head->task_list);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
__add_wait_queue_tail_exclusive(wait_queue_head_t *q, wait_queue_t *wait)
{
 wait->flags |= 0x01;
 __add_wait_queue_tail(q, wait);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
__remove_wait_queue(wait_queue_head_t *head, wait_queue_t *old)
{
 list_del(&old->task_list);
}

typedef int wait_bit_action_f(struct wait_bit_key *);
void __wake_up(wait_queue_head_t *q, unsigned int mode, int nr, void *key);
void __wake_up_locked_key(wait_queue_head_t *q, unsigned int mode, void *key);
void __wake_up_sync_key(wait_queue_head_t *q, unsigned int mode, int nr, void *key);
void __wake_up_locked(wait_queue_head_t *q, unsigned int mode, int nr);
void __wake_up_sync(wait_queue_head_t *q, unsigned int mode, int nr);
void __wake_up_bit(wait_queue_head_t *, void *, int);
int __wait_on_bit(wait_queue_head_t *, struct wait_bit_queue *, wait_bit_action_f *, unsigned);
int __wait_on_bit_lock(wait_queue_head_t *, struct wait_bit_queue *, wait_bit_action_f *, unsigned);
void wake_up_bit(void *, int);
void wake_up_atomic_t(atomic_t *);
int out_of_line_wait_on_bit(void *, int, wait_bit_action_f *, unsigned);
int out_of_line_wait_on_bit_timeout(void *, int, wait_bit_action_f *, unsigned, unsigned long);
int out_of_line_wait_on_bit_lock(void *, int, wait_bit_action_f *, unsigned);
int out_of_line_wait_on_atomic_t(atomic_t *, int (*)(atomic_t *), unsigned);
wait_queue_head_t *bit_waitqueue(void *, int);
# 831 "include/linux/wait.h"
void prepare_to_wait(wait_queue_head_t *q, wait_queue_t *wait, int state);
void prepare_to_wait_exclusive(wait_queue_head_t *q, wait_queue_t *wait, int state);
long prepare_to_wait_event(wait_queue_head_t *q, wait_queue_t *wait, int state);
void finish_wait(wait_queue_head_t *q, wait_queue_t *wait);
void abort_exclusive_wait(wait_queue_head_t *q, wait_queue_t *wait, unsigned int mode, void *key);
long wait_woken(wait_queue_t *wait, unsigned mode, long timeout);
int woken_wake_function(wait_queue_t *wait, unsigned mode, int sync, void *key);
int autoremove_wake_function(wait_queue_t *wait, unsigned mode, int sync, void *key);
int wake_bit_function(wait_queue_t *wait, unsigned mode, int sync, void *key);
# 870 "include/linux/wait.h"
extern int bit_wait(struct wait_bit_key *);
extern int bit_wait_io(struct wait_bit_key *);
extern int bit_wait_timeout(struct wait_bit_key *);
extern int bit_wait_io_timeout(struct wait_bit_key *);
# 891 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
wait_on_bit(void *word, int bit, unsigned mode)
{
 if (!test_bit(bit, word))
  return 0;
 return out_of_line_wait_on_bit(word, bit,
           bit_wait,
           mode);
}
# 915 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
wait_on_bit_io(void *word, int bit, unsigned mode)
{
 if (!test_bit(bit, word))
  return 0;
 return out_of_line_wait_on_bit(word, bit,
           bit_wait_io,
           mode);
}
# 941 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
wait_on_bit_action(void *word, int bit, wait_bit_action_f *action, unsigned mode)
{
 if (!test_bit(bit, word))
  return 0;
 return out_of_line_wait_on_bit(word, bit, action, mode);
}
# 968 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
wait_on_bit_lock(void *word, int bit, unsigned mode)
{
 if (!test_and_set_bit(bit, word))
  return 0;
 return out_of_line_wait_on_bit_lock(word, bit, bit_wait, mode);
}
# 991 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
wait_on_bit_lock_io(void *word, int bit, unsigned mode)
{
 if (!test_and_set_bit(bit, word))
  return 0;
 return out_of_line_wait_on_bit_lock(word, bit, bit_wait_io, mode);
}
# 1016 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
wait_on_bit_lock_action(void *word, int bit, wait_bit_action_f *action, unsigned mode)
{
 if (!test_and_set_bit(bit, word))
  return 0;
 return out_of_line_wait_on_bit_lock(word, bit, action, mode);
}
# 1034 "include/linux/wait.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function))
int wait_on_atomic_t(atomic_t *val, int (*action)(atomic_t *), unsigned mode)
{
 if ((*(volatile typeof((val)->counter) *)&((val)->counter)) == 0)
  return 0;
 return out_of_line_wait_on_atomic_t(val, action, mode);
}
# 10 "include/linux/mmzone.h" 2



# 1 "include/linux/numa.h" 1
# 14 "include/linux/mmzone.h" 2

# 1 "include/linux/seqlock.h" 1
# 46 "include/linux/seqlock.h"
typedef struct seqcount {
 unsigned sequence;



} seqcount_t;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __seqcount_init(seqcount_t *s, const char *name,
       struct lock_class_key *key)
{



 do { (void)(name); (void)(key); } while (0);
 s->sequence = 0;
}
# 106 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned __read_seqcount_begin(const seqcount_t *s)
{
 unsigned ret;

repeat:
 ret = (*(volatile typeof(s->sequence) *)&(s->sequence));
 if (__builtin_expect(!!(ret & 1), 0)) {
  __asm__ __volatile__("": : :"memory");
  goto repeat;
 }
 return ret;
}
# 128 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned raw_read_seqcount(const seqcount_t *s)
{
 unsigned ret = (*(volatile typeof(s->sequence) *)&(s->sequence));
 __asm__ __volatile__("": : :"memory");
 return ret;
}
# 144 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned raw_read_seqcount_begin(const seqcount_t *s)
{
 unsigned ret = __read_seqcount_begin(s);
 __asm__ __volatile__("": : :"memory");
 return ret;
}
# 160 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned read_seqcount_begin(const seqcount_t *s)
{
 ;
 return raw_read_seqcount_begin(s);
}
# 180 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned raw_seqcount_begin(const seqcount_t *s)
{
 unsigned ret = (*(volatile typeof(s->sequence) *)&(s->sequence));
 __asm__ __volatile__("": : :"memory");
 return ret & ~1;
}
# 201 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __read_seqcount_retry(const seqcount_t *s, unsigned start)
{
 return __builtin_expect(!!(s->sequence != start), 0);
}
# 216 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int read_seqcount_retry(const seqcount_t *s, unsigned start)
{
 __asm__ __volatile__("": : :"memory");
 return __read_seqcount_retry(s, start);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void raw_write_seqcount_begin(seqcount_t *s)
{
 s->sequence++;
 __asm__ __volatile__("": : :"memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void raw_write_seqcount_end(seqcount_t *s)
{
 __asm__ __volatile__("": : :"memory");
 s->sequence++;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void raw_write_seqcount_latch(seqcount_t *s)
{
       __asm__ __volatile__("": : :"memory");
       s->sequence++;
       __asm__ __volatile__("": : :"memory");
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqcount_begin_nested(seqcount_t *s, int subclass)
{
 raw_write_seqcount_begin(s);
 do { } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqcount_begin(seqcount_t *s)
{
 write_seqcount_begin_nested(s, 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqcount_end(seqcount_t *s)
{
 do { } while (0);
 raw_write_seqcount_end(s);
}
# 275 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqcount_barrier(seqcount_t *s)
{
 __asm__ __volatile__("": : :"memory");
 s->sequence+=2;
}

typedef struct {
 struct seqcount seqcount;
 spinlock_t lock;
} seqlock_t;
# 308 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned read_seqbegin(const seqlock_t *sl)
{
 return read_seqcount_begin(&sl->seqcount);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned read_seqretry(const seqlock_t *sl, unsigned start)
{
 return read_seqcount_retry(&sl->seqcount, start);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqlock(seqlock_t *sl)
{
 spin_lock(&sl->lock);
 write_seqcount_begin(&sl->seqcount);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_sequnlock(seqlock_t *sl)
{
 write_seqcount_end(&sl->seqcount);
 spin_unlock(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqlock_bh(seqlock_t *sl)
{
 spin_lock_bh(&sl->lock);
 write_seqcount_begin(&sl->seqcount);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_sequnlock_bh(seqlock_t *sl)
{
 write_seqcount_end(&sl->seqcount);
 spin_unlock_bh(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_seqlock_irq(seqlock_t *sl)
{
 spin_lock_irq(&sl->lock);
 write_seqcount_begin(&sl->seqcount);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void write_sequnlock_irq(seqlock_t *sl)
{
 write_seqcount_end(&sl->seqcount);
 spin_unlock_irq(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __write_seqlock_irqsave(seqlock_t *sl)
{
 unsigned long flags;

 do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); do { do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(spinlock_check(&sl->lock)); } while (0); } while (0); } while (0); } while (0); } while (0);
 write_seqcount_begin(&sl->seqcount);
 return flags;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
write_sequnlock_irqrestore(seqlock_t *sl, unsigned long flags)
{
 write_seqcount_end(&sl->seqcount);
 spin_unlock_irqrestore(&sl->lock, flags);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_seqlock_excl(seqlock_t *sl)
{
 spin_lock(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_sequnlock_excl(seqlock_t *sl)
{
 spin_unlock(&sl->lock);
}
# 403 "include/linux/seqlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_seqbegin_or_lock(seqlock_t *lock, int *seq)
{
 if (!(*seq & 1))
  *seq = read_seqbegin(lock);
 else
  read_seqlock_excl(lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int need_seqretry(seqlock_t *lock, int seq)
{
 return !(seq & 1) && read_seqretry(lock, seq);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void done_seqretry(seqlock_t *lock, int seq)
{
 if (seq & 1)
  read_sequnlock_excl(lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_seqlock_excl_bh(seqlock_t *sl)
{
 spin_lock_bh(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_sequnlock_excl_bh(seqlock_t *sl)
{
 spin_unlock_bh(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_seqlock_excl_irq(seqlock_t *sl)
{
 spin_lock_irq(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void read_sequnlock_excl_irq(seqlock_t *sl)
{
 spin_unlock_irq(&sl->lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long __read_seqlock_excl_irqsave(seqlock_t *sl)
{
 unsigned long flags;

 do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); do { do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(spinlock_check(&sl->lock)); } while (0); } while (0); } while (0); } while (0); } while (0);
 return flags;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
read_sequnlock_excl_irqrestore(seqlock_t *sl, unsigned long flags)
{
 spin_unlock_irqrestore(&sl->lock, flags);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long
read_seqbegin_or_lock_irqsave(seqlock_t *lock, int *seq)
{
 unsigned long flags = 0;

 if (!(*seq & 1))
  *seq = read_seqbegin(lock);
 else
  do { flags = __read_seqlock_excl_irqsave(lock); } while (0);

 return flags;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
done_seqretry_irqrestore(seqlock_t *lock, int seq, unsigned long flags)
{
 if (seq & 1)
  read_sequnlock_excl_irqrestore(lock, flags);
}
# 16 "include/linux/mmzone.h" 2
# 1 "include/linux/nodemask.h" 1
# 98 "include/linux/nodemask.h"
typedef struct { unsigned long bits[((((1 << 0)) + (8 * sizeof(long)) - 1) / (8 * sizeof(long)))]; } nodemask_t;
extern nodemask_t _unused_nodemask_arg_;
# 111 "include/linux/nodemask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void __node_set(int node, volatile nodemask_t *dstp)
{
 set_bit(node, dstp->bits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __node_clear(int node, volatile nodemask_t *dstp)
{
 clear_bit(node, dstp->bits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_setall(nodemask_t *dstp, int nbits)
{
 bitmap_fill(dstp->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_clear(nodemask_t *dstp, int nbits)
{
 bitmap_zero(dstp->bits, nbits);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __node_test_and_set(int node, nodemask_t *addr)
{
 return test_and_set_bit(node, addr->bits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_and(nodemask_t *dstp, const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 bitmap_and(dstp->bits, src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_or(nodemask_t *dstp, const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 bitmap_or(dstp->bits, src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_xor(nodemask_t *dstp, const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 bitmap_xor(dstp->bits, src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_andnot(nodemask_t *dstp, const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 bitmap_andnot(dstp->bits, src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_complement(nodemask_t *dstp,
     const nodemask_t *srcp, int nbits)
{
 bitmap_complement(dstp->bits, srcp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodes_equal(const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 return bitmap_equal(src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodes_intersects(const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 return bitmap_intersects(src1p->bits, src2p->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodes_subset(const nodemask_t *src1p,
     const nodemask_t *src2p, int nbits)
{
 return bitmap_subset(src1p->bits, src2p->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodes_empty(const nodemask_t *srcp, int nbits)
{
 return bitmap_empty(srcp->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodes_full(const nodemask_t *srcp, int nbits)
{
 return bitmap_full(srcp->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodes_weight(const nodemask_t *srcp, int nbits)
{
 return bitmap_weight(srcp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_shift_right(nodemask_t *dstp,
     const nodemask_t *srcp, int n, int nbits)
{
 bitmap_shift_right(dstp->bits, srcp->bits, n, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_shift_left(nodemask_t *dstp,
     const nodemask_t *srcp, int n, int nbits)
{
 bitmap_shift_left(dstp->bits, srcp->bits, n, nbits);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __first_node(const nodemask_t *srcp)
{
 return ({ int __min1 = ((1 << 0)); int __min2 = (find_next_bit((srcp->bits), ((1 << 0)), 0)); __min1 < __min2 ? __min1: __min2; });
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __next_node(int n, const nodemask_t *srcp)
{
 return ({ int __min1 = ((1 << 0)); int __min2 = (find_next_bit(srcp->bits, (1 << 0), n+1)); __min1 < __min2 ? __min1: __min2; });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_nodemask_of_node(nodemask_t *mask, int node)
{
 __nodes_clear(&(*mask), (1 << 0));
 __node_set((node), &(*mask));
}
# 275 "include/linux/nodemask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __first_unset_node(const nodemask_t *maskp)
{
 return ({ int __min1 = ((1 << 0)); int __min2 = (find_next_zero_bit((maskp->bits), ((1 << 0)), 0)); __min1 < __min2 ? __min1: __min2; })
                                                  ;
}
# 309 "include/linux/nodemask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodemask_scnprintf(char *buf, int len,
     const nodemask_t *srcp, int nbits)
{
 return bitmap_scnprintf(buf, len, srcp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodemask_parse_user(const char *buf, int len,
     nodemask_t *dstp, int nbits)
{
 return bitmap_parse_user(buf, len, dstp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodelist_scnprintf(char *buf, int len,
     const nodemask_t *srcp, int nbits)
{
 return bitmap_scnlistprintf(buf, len, srcp->bits, nbits);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __nodelist_parse(const char *buf, nodemask_t *dstp, int nbits)
{
 return bitmap_parselist(buf, dstp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __node_remap(int oldbit,
  const nodemask_t *oldp, const nodemask_t *newp, int nbits)
{
 return bitmap_bitremap(oldbit, oldp->bits, newp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_remap(nodemask_t *dstp, const nodemask_t *srcp,
  const nodemask_t *oldp, const nodemask_t *newp, int nbits)
{
 bitmap_remap(dstp->bits, srcp->bits, oldp->bits, newp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_onto(nodemask_t *dstp, const nodemask_t *origp,
  const nodemask_t *relmapp, int nbits)
{
 bitmap_onto(dstp->bits, origp->bits, relmapp->bits, nbits);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __nodes_fold(nodemask_t *dstp, const nodemask_t *origp,
  int sz, int nbits)
{
 bitmap_fold(dstp->bits, origp->bits, sz, nbits);
}
# 383 "include/linux/nodemask.h"
enum node_states {
 N_POSSIBLE,
 N_ONLINE,
 N_NORMAL_MEMORY,



 N_HIGH_MEMORY = N_NORMAL_MEMORY,




 N_MEMORY = N_HIGH_MEMORY,

 N_CPU,
 NR_NODE_STATES
};






extern nodemask_t node_states[NR_NODE_STATES];
# 460 "include/linux/nodemask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int node_state(int node, enum node_states state)
{
 return node == 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void node_set_state(int node, enum node_states state)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void node_clear_state(int node, enum node_states state)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int num_node_state(enum node_states state)
{
 return 1;
}
# 495 "include/linux/nodemask.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int node_random(const nodemask_t *mask)
{
 return 0;
}
# 527 "include/linux/nodemask.h"
struct nodemask_scratch {
 nodemask_t mask1;
 nodemask_t mask2;
};
# 17 "include/linux/mmzone.h" 2
# 1 "include/linux/pageblock-flags.h" 1
# 29 "include/linux/pageblock-flags.h"
enum pageblock_bits {
 PB_migrate,
 PB_migrate_end = PB_migrate + 3 - 1,

 PB_migrate_skip,





 NR_PAGEBLOCK_BITS
};
# 66 "include/linux/pageblock-flags.h"
struct page;

unsigned long get_pfnblock_flags_mask(struct page *page,
    unsigned long pfn,
    unsigned long end_bitidx,
    unsigned long mask);

void set_pfnblock_flags_mask(struct page *page,
    unsigned long flags,
    unsigned long pfn,
    unsigned long end_bitidx,
    unsigned long mask);
# 18 "include/linux/mmzone.h" 2
# 1 "include/linux/page-flags-layout.h" 1




# 1 "include/generated/bounds.h" 1
# 6 "include/linux/page-flags-layout.h" 2
# 19 "include/linux/mmzone.h" 2

# 1 "./arch/mips/include/asm/page.h" 1
# 42 "./arch/mips/include/asm/page.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int page_size_ftlb(unsigned int mmuextdef)
{
 switch (mmuextdef) {
 case ((unsigned long)(2) << 14):
  if (((1UL) << 12) == (1 << 30))
   return 5;
  if (((1UL) << 12) == (1llu << 32))
   return 6;
  if (((1UL) << 12) > (256 << 10))
   return 7;

 case ((unsigned long)(3) << 14):
  return (12 - 10) / 2;
 default:
  panic("Invalid FTLB configuration with Conf4_mmuextdef=%d value\n",
        mmuextdef >> 14);
 }
}
# 73 "./arch/mips/include/asm/page.h"
# 1 "include/linux/pfn.h" 1
# 74 "./arch/mips/include/asm/page.h" 2

extern void build_clear_page(void);
extern void build_copy_page(void);
# 85 "./arch/mips/include/asm/page.h"
extern void clear_page(void * page);
extern void copy_page(void * to, void * from);

extern unsigned long shm_align_mask;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long pages_do_alias(unsigned long addr1,
 unsigned long addr2)
{
 return (addr1 ^ addr2) & shm_align_mask;
}

struct page;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_user_page(void *addr, unsigned long vaddr,
 struct page *page)
{
 extern void (*flush_data_cache_page)(unsigned long addr);

 clear_page(addr);
 if (pages_do_alias((unsigned long) addr, vaddr & (~((1 << 12) - 1))))
  flush_data_cache_page((unsigned long)addr);
}

extern void copy_user_page(void *vto, void *vfrom, unsigned long vaddr,
 struct page *to);
struct vm_area_struct;
extern void copy_user_highpage(struct page *to, struct page *from,
 unsigned long vaddr, struct vm_area_struct *vma);
# 130 "./arch/mips/include/asm/page.h"
typedef struct { unsigned long pte; } pte_t;



typedef struct page *pgtable_t;
# 144 "./arch/mips/include/asm/page.h"
typedef struct { unsigned long pgd; } pgd_t;






typedef struct { unsigned long pgprot; } pgprot_t;
# 178 "./arch/mips/include/asm/page.h"
# 1 "./arch/mips/include/asm/io.h" 1
# 25 "./arch/mips/include/asm/io.h"
# 1 "include/asm-generic/iomap.h" 1
# 28 "include/asm-generic/iomap.h"
extern unsigned int ioread8(void *);
extern unsigned int ioread16(void *);
extern unsigned int ioread16be(void *);
extern unsigned int ioread32(void *);
extern unsigned int ioread32be(void *);

extern void iowrite8(u8, void *);
extern void iowrite16(u16, void *);
extern void iowrite16be(u16, void *);
extern void iowrite32(u32, void *);
extern void iowrite32be(u32, void *);
# 51 "include/asm-generic/iomap.h"
extern void ioread8_rep(void *port, void *buf, unsigned long count);
extern void ioread16_rep(void *port, void *buf, unsigned long count);
extern void ioread32_rep(void *port, void *buf, unsigned long count);

extern void iowrite8_rep(void *port, const void *buf, unsigned long count);
extern void iowrite16_rep(void *port, const void *buf, unsigned long count);
extern void iowrite32_rep(void *port, const void *buf, unsigned long count);



extern void *ioport_map(unsigned long port, unsigned int nr);
extern void ioport_unmap(void *);
# 71 "include/asm-generic/iomap.h"
struct pci_dev;
extern void pci_iounmap(struct pci_dev *dev, void *);






# 1 "include/asm-generic/pci_iomap.h" 1
# 14 "include/asm-generic/pci_iomap.h"
struct pci_dev;


extern void *pci_iomap(struct pci_dev *dev, int bar, unsigned long max);




extern void *__pci_ioport_map(struct pci_dev *dev, unsigned long port,
          unsigned int nr);
# 80 "include/asm-generic/iomap.h" 2
# 26 "./arch/mips/include/asm/io.h" 2
# 1 "./arch/mips/include/asm/page.h" 1
# 27 "./arch/mips/include/asm/io.h" 2
# 1 "./arch/mips/include/asm/pgtable-bits.h" 1
# 199 "./arch/mips/include/asm/pgtable-bits.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) uint64_t pte_to_entrylo(unsigned long pte_val)
{
 if (0) {
  int sa;

  sa = 31 - (0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))));
# 213 "./arch/mips/include/asm/pgtable-bits.h"
  return (pte_val >> ((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1)) |
   ((pte_val & (({__BUG_ON((unsigned long)(!0)); 1 << (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))); }) | ({__BUG_ON((unsigned long)(!0)); 1 << (0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))); }))) << sa);
 }

 return pte_val >> ((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1);
}
# 28 "./arch/mips/include/asm/io.h" 2



# 1 "./arch/mips/include/asm/mach-generic/ioremap.h" 1
# 18 "./arch/mips/include/asm/mach-generic/ioremap.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) phys_t fixup_bigphys_addr(phys_t phys_addr, phys_t size)
{
 return phys_addr;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *plat_ioremap(phys_t offset, unsigned long size,
 unsigned long flags)
{
 return ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int plat_iounmap(const volatile void *addr)
{
 return 0;
}
# 32 "./arch/mips/include/asm/io.h" 2
# 1 "./arch/mips/include/asm/mach-ath79/mangle-port.h" 1
# 16 "./arch/mips/include/asm/mach-ath79/mangle-port.h"
extern unsigned long (ath79_pci_swizzle_b)(unsigned long port);
extern unsigned long (ath79_pci_swizzle_w)(unsigned long port);
# 33 "./arch/mips/include/asm/io.h" 2
# 63 "./arch/mips/include/asm/io.h"
extern const unsigned long mips_io_port_base;
# 74 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_io_port_base(unsigned long base)
{
 * (unsigned long *) &mips_io_port_base = base;
 __asm__ __volatile__("": : :"memory");
}
# 119 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long virt_to_phys(volatile const void *address)
{
 return ((unsigned long)(address) - ((0x80000000UL) + (0UL)) + (0UL));
}
# 136 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * phys_to_virt(unsigned long address)
{
 return (void *)(address + ((0x80000000UL) + (0UL)) - (0UL));
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long isa_virt_to_bus(volatile void * address)
{
 return (unsigned long)address - ((0x80000000UL) + (0UL));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * isa_bus_to_virt(unsigned long address)
{
 return (void *)(address + ((0x80000000UL) + (0UL)));
}
# 170 "./arch/mips/include/asm/io.h"
extern void * __ioremap(phys_t offset, phys_t size, unsigned long flags);
extern void __iounmap(const volatile void *addr);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __ioremap_mode(phys_t offset, unsigned long size,
 unsigned long flags)
{
 void *addr = plat_ioremap(offset, size, flags);

 if (addr)
  return addr;



 if (0) {
  u64 base = (0xa0000000UL);





  if (flags == (2<<(((((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1) + 1) + 1) + 1)))
   base = (u64) (0xa0000000UL);
  return (void *) (unsigned long) (base + offset);
 } else if (__builtin_constant_p(offset) &&
     __builtin_constant_p(size) && __builtin_constant_p(flags)) {
  phys_t phys_addr, last_addr;

  phys_addr = fixup_bigphys_addr(offset, size);


  last_addr = phys_addr + size - 1;
  if (!size || last_addr < phys_addr)
   return ((void *)0);





  if ((!((phys_t)(phys_addr) & (phys_t) ~0x1fffffffULL)) && (!((phys_t)(last_addr) & (phys_t) ~0x1fffffffULL)) &&
      flags == (2<<(((((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1) + 1) + 1) + 1)))
   return (void *)
    (unsigned long)((((int)(int)(phys_addr)) & 0x1fffffff) | 0xa0000000);
 }

 return __ioremap(offset, size, flags);


}
# 289 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void iounmap(const volatile void *addr)
{
 if (plat_iounmap(addr))
  return;



 if (0 ||
     (__builtin_constant_p(addr) && (((unsigned long)(addr) & ~0x1fffffffUL) == 0xa0000000)))
  return;

 __iounmap(addr);


}
# 426 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __raw_writeb(u8 val, volatile void *mem) { volatile u8 *__mem; u8 __val; do { } while (0); __mem = (void *)ath79_pci_swizzle_b((unsigned long)(mem)); __val = (val); if (sizeof(u8) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u8 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 __raw_readb(const volatile void *mem) { volatile u8 *__mem; u8 __val; __mem = (void *)ath79_pci_swizzle_b((unsigned long)(mem)); if (sizeof(u8) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writeb(u8 val, volatile void *mem) { volatile u8 *__mem; u8 __val; do { } while (0); __mem = (void *)ath79_pci_swizzle_b((unsigned long)(mem)); __val = (val); if (sizeof(u8) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u8 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 readb(const volatile void *mem) { volatile u8 *__mem; u8 __val; __mem = (void *)ath79_pci_swizzle_b((unsigned long)(mem)); if (sizeof(u8) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_writeb(u8 val, volatile void *mem) { volatile u8 *__mem; u8 __val; do { } while (0); __mem = (void *)ath79_pci_swizzle_b((unsigned long)(mem)); __val = (val); if (sizeof(u8) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u8 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 __mem_readb(const volatile void *mem) { volatile u8 *__mem; u8 __val; __mem = (void *)ath79_pci_swizzle_b((unsigned long)(mem)); if (sizeof(u8) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __raw_writew(u16 val, volatile void *mem) { volatile u16 *__mem; u16 __val; do { } while (0); __mem = (void *)ath79_pci_swizzle_w((unsigned long)(mem)); __val = (val); if (sizeof(u16) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u16 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 __raw_readw(const volatile void *mem) { volatile u16 *__mem; u16 __val; __mem = (void *)ath79_pci_swizzle_w((unsigned long)(mem)); if (sizeof(u16) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writew(u16 val, volatile void *mem) { volatile u16 *__mem; u16 __val; do { } while (0); __mem = (void *)ath79_pci_swizzle_w((unsigned long)(mem)); __val = (val); if (sizeof(u16) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u16 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 readw(const volatile void *mem) { volatile u16 *__mem; u16 __val; __mem = (void *)ath79_pci_swizzle_w((unsigned long)(mem)); if (sizeof(u16) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_writew(u16 val, volatile void *mem) { volatile u16 *__mem; u16 __val; do { } while (0); __mem = (void *)ath79_pci_swizzle_w((unsigned long)(mem)); __val = (( __le16)(__builtin_constant_p((__u16)((val))) ? ((__u16)( (((__u16)((val)) & (__u16)0x00ffU) << 8) | (((__u16)((val)) & (__u16)0xff00U) >> 8))) : __fswab16((val)))); if (sizeof(u16) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u16 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 __mem_readw(const volatile void *mem) { volatile u16 *__mem; u16 __val; __mem = (void *)ath79_pci_swizzle_w((unsigned long)(mem)); if (sizeof(u16) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (( __le16)(__builtin_constant_p((__u16)((__val))) ? ((__u16)( (((__u16)((__val)) & (__u16)0x00ffU) << 8) | (((__u16)((__val)) & (__u16)0xff00U) >> 8))) : __fswab16((__val)))); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __raw_writel(u32 val, volatile void *mem) { volatile u32 *__mem; u32 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (val); if (sizeof(u32) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u32 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 __raw_readl(const volatile void *mem) { volatile u32 *__mem; u32 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u32) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writel(u32 val, volatile void *mem) { volatile u32 *__mem; u32 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (val); if (sizeof(u32) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u32 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 readl(const volatile void *mem) { volatile u32 *__mem; u32 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u32) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_writel(u32 val, volatile void *mem) { volatile u32 *__mem; u32 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (( __le32)(__builtin_constant_p((__u32)((val))) ? ((__u32)( (((__u32)((val)) & (__u32)0x000000ffUL) << 24) | (((__u32)((val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)((val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)((val)) & (__u32)0xff000000UL) >> 24))) : __fswab32((val)))); if (sizeof(u32) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u32 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 __mem_readl(const volatile void *mem) { volatile u32 *__mem; u32 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u32) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (( __le32)(__builtin_constant_p((__u32)((__val))) ? ((__u32)( (((__u32)((__val)) & (__u32)0x000000ffUL) << 24) | (((__u32)((__val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)((__val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)((__val)) & (__u32)0xff000000UL) >> 24))) : __fswab32((__val)))); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __raw_writeq(u64 val, volatile void *mem) { volatile u64 *__mem; u64 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (val); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u64 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 __raw_readq(const volatile void *mem) { volatile u64 *__mem; u64 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writeq(u64 val, volatile void *mem) { volatile u64 *__mem; u64 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (val); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u64 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 readq(const volatile void *mem) { volatile u64 *__mem; u64 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_writeq(u64 val, volatile void *mem) { volatile u64 *__mem; u64 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (( __le64)(__builtin_constant_p((__u64)((val))) ? ((__u64)( (((__u64)((val)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)((val)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)((val)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)((val)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)((val)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)((val)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)((val)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)((val)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64((val)))); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u64 __tmp; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 __mem_readq(const volatile void *mem) { volatile u64 *__mem; u64 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (1) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (1) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (( __le64)(__builtin_constant_p((__u64)((__val))) ? ((__u64)( (((__u64)((__val)) & (__u64)0x00000000000000ffULL) << 56) | (((__u64)((__val)) & (__u64)0x000000000000ff00ULL) << 40) | (((__u64)((__val)) & (__u64)0x0000000000ff0000ULL) << 24) | (((__u64)((__val)) & (__u64)0x00000000ff000000ULL) << 8) | (((__u64)((__val)) & (__u64)0x000000ff00000000ULL) >> 8) | (((__u64)((__val)) & (__u64)0x0000ff0000000000ULL) >> 24) | (((__u64)((__val)) & (__u64)0x00ff000000000000ULL) >> 40) | (((__u64)((__val)) & (__u64)0xff00000000000000ULL) >> 56))) : __fswab64((__val)))); }
# 439 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outb(u8 val, unsigned long port) { volatile u8 *__addr; u8 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 inb(unsigned long port) { volatile u8 *__addr; u8 __val; __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outb_p(u8 val, unsigned long port) { volatile u8 *__addr; u8 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 inb_p(unsigned long port) { volatile u8 *__addr; u8 __val; __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_outb(u8 val, unsigned long port) { volatile u8 *__addr; u8 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 __mem_inb(unsigned long port) { volatile u8 *__addr; u8 __val; __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_outb_p(u8 val, unsigned long port) { volatile u8 *__addr; u8 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u8 __mem_inb_p(unsigned long port) { volatile u8 *__addr; u8 __val; __addr = (void *)ath79_pci_swizzle_b(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u8) > sizeof(unsigned long))); extern void __compiletime_assert_439(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u8) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_439(); do { } while (0); } while (0); __val = *__addr; ; return (__val); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outw(u16 val, unsigned long port) { volatile u16 *__addr; u16 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 inw(unsigned long port) { volatile u16 *__addr; u16 __val; __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outw_p(u16 val, unsigned long port) { volatile u16 *__addr; u16 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 inw_p(unsigned long port) { volatile u16 *__addr; u16 __val; __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_outw(u16 val, unsigned long port) { volatile u16 *__addr; u16 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); __val = (( __le16)(__builtin_constant_p((__u16)((val))) ? ((__u16)( (((__u16)((val)) & (__u16)0x00ffU) << 8) | (((__u16)((val)) & (__u16)0xff00U) >> 8))) : __fswab16((val)))); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 __mem_inw(unsigned long port) { volatile u16 *__addr; u16 __val; __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); __val = *__addr; ; return (( __le16)(__builtin_constant_p((__u16)((__val))) ? ((__u16)( (((__u16)((__val)) & (__u16)0x00ffU) << 8) | (((__u16)((__val)) & (__u16)0xff00U) >> 8))) : __fswab16((__val)))); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_outw_p(u16 val, unsigned long port) { volatile u16 *__addr; u16 __val; do { } while (0); __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); __val = (( __le16)(__builtin_constant_p((__u16)((val))) ? ((__u16)( (((__u16)((val)) & (__u16)0x00ffU) << 8) | (((__u16)((val)) & (__u16)0xff00U) >> 8))) : __fswab16((val)))); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 __mem_inw_p(unsigned long port) { volatile u16 *__addr; u16 __val; __addr = (void *)ath79_pci_swizzle_w(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u16) > sizeof(unsigned long))); extern void __compiletime_assert_440(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u16) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_440(); do { } while (0); } while (0); __val = *__addr; ; return (( __le16)(__builtin_constant_p((__u16)((__val))) ? ((__u16)( (((__u16)((__val)) & (__u16)0x00ffU) << 8) | (((__u16)((__val)) & (__u16)0xff00U) >> 8))) : __fswab16((__val)))); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outl(u32 val, unsigned long port) { volatile u32 *__addr; u32 __val; do { } while (0); __addr = (void *)(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 inl(unsigned long port) { volatile u32 *__addr; u32 __val; __addr = (void *)(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outl_p(u32 val, unsigned long port) { volatile u32 *__addr; u32 __val; do { } while (0); __addr = (void *)(mips_io_port_base + port); __val = (val); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 inl_p(unsigned long port) { volatile u32 *__addr; u32 __val; __addr = (void *)(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); __val = *__addr; ; return (__val); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_outl(u32 val, unsigned long port) { volatile u32 *__addr; u32 __val; do { } while (0); __addr = (void *)(mips_io_port_base + port); __val = (( __le32)(__builtin_constant_p((__u32)((val))) ? ((__u32)( (((__u32)((val)) & (__u32)0x000000ffUL) << 24) | (((__u32)((val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)((val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)((val)) & (__u32)0xff000000UL) >> 24))) : __fswab32((val)))); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 __mem_inl(unsigned long port) { volatile u32 *__addr; u32 __val; __addr = (void *)(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); __val = *__addr; ; return (( __le32)(__builtin_constant_p((__u32)((__val))) ? ((__u32)( (((__u32)((__val)) & (__u32)0x000000ffUL) << 24) | (((__u32)((__val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)((__val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)((__val)) & (__u32)0xff000000UL) >> 24))) : __fswab32((__val)))); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __mem_outl_p(u32 val, unsigned long port) { volatile u32 *__addr; u32 __val; do { } while (0); __addr = (void *)(mips_io_port_base + port); __val = (( __le32)(__builtin_constant_p((__u32)((val))) ? ((__u32)( (((__u32)((val)) & (__u32)0x000000ffUL) << 24) | (((__u32)((val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)((val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)((val)) & (__u32)0xff000000UL) >> 24))) : __fswab32((val)))); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); *__addr = __val; ; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 __mem_inl_p(unsigned long port) { volatile u32 *__addr; u32 __val; __addr = (void *)(mips_io_port_base + port); do { bool __cond = !(!(sizeof(u32) > sizeof(unsigned long))); extern void __compiletime_assert_441(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(u32) > sizeof(unsigned long)"))); if (__cond) __compiletime_assert_441(); do { } while (0); } while (0); __val = *__addr; ; return (( __le32)(__builtin_constant_p((__u32)((__val))) ? ((__u32)( (((__u32)((__val)) & (__u32)0x000000ffUL) << 24) | (((__u32)((__val)) & (__u32)0x0000ff00UL) << 8) | (((__u32)((__val)) & (__u32)0x00ff0000UL) >> 8) | (((__u32)((__val)) & (__u32)0xff000000UL) >> 24))) : __fswab32((__val)))); }
# 450 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ____raw_writeq(u64 val, volatile void *mem) { volatile u64 *__mem; u64 __val; do { } while (0); __mem = (void *)((unsigned long)(mem)); __val = (val); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) *__mem = __val; else if (0) { unsigned long __flags; u64 __tmp; if (0) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __writeq""\n\t" "dsll32 %L0, %L0, 0" "\n\t" "dsrl32 %L0, %L0, 0" "\n\t" "dsll32 %M0, %M0, 0" "\n\t" "or	%L0, %L0, %M0" "\n\t" "sd	%L0, %2" "\n\t" ".set	mips0" "\n" : "=r" (__tmp) : "0" (__val), "m" (*__mem)); if (0) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else BUG(); } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 ____raw_readq(const volatile void *mem) { volatile u64 *__mem; u64 __val; __mem = (void *)((unsigned long)(mem)); if (sizeof(u64) != sizeof(u64) || sizeof(u64) == sizeof(long)) __val = *__mem; else if (0) { unsigned long __flags; if (0) do { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); __flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); __asm__ __volatile__( ".set	arch=r4000" "\t\t# __readq" "\n\t" "ld	%L0, %1" "\n\t" "dsra32 %M0, %L0, 0" "\n\t" "sll	%L0, %L0, 0" "\n\t" ".set	mips0" "\n" : "=r" (__val) : "m" (*__mem)); if (0) do { if (({ ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(__flags); })) { do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(__flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(__flags); } while (0); } } while (0); } else { __val = 0; BUG(); } return (__val); }
# 539 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writesb(volatile void *mem, const void *addr, unsigned int count) { const volatile u8 *__addr = addr; while (count--) { __mem_writeb(*__addr, mem); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void readsb(volatile void *mem, void *addr, unsigned int count) { volatile u8 *__addr = addr; while (count--) { *__addr = __mem_readb(mem); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outsb(unsigned long port, const void *addr, unsigned int count) { const volatile u8 *__addr = addr; while (count--) { __mem_outb(*__addr, port); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void insb(unsigned long port, void *addr, unsigned int count) { volatile u8 *__addr = addr; while (count--) { *__addr = __mem_inb(port); __addr++; } }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writesw(volatile void *mem, const void *addr, unsigned int count) { const volatile u16 *__addr = addr; while (count--) { __mem_writew(*__addr, mem); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void readsw(volatile void *mem, void *addr, unsigned int count) { volatile u16 *__addr = addr; while (count--) { *__addr = __mem_readw(mem); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outsw(unsigned long port, const void *addr, unsigned int count) { const volatile u16 *__addr = addr; while (count--) { __mem_outw(*__addr, port); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void insw(unsigned long port, void *addr, unsigned int count) { volatile u16 *__addr = addr; while (count--) { *__addr = __mem_inw(port); __addr++; } }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void writesl(volatile void *mem, const void *addr, unsigned int count) { const volatile u32 *__addr = addr; while (count--) { __mem_writel(*__addr, mem); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void readsl(volatile void *mem, void *addr, unsigned int count) { volatile u32 *__addr = addr; while (count--) { *__addr = __mem_readl(mem); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void outsl(unsigned long port, const void *addr, unsigned int count) { const volatile u32 *__addr = addr; while (count--) { __mem_outl(*__addr, port); __addr++; } } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void insl(unsigned long port, void *addr, unsigned int count) { volatile u32 *__addr = addr; while (count--) { *__addr = __mem_inl(port); __addr++; } }
# 554 "./arch/mips/include/asm/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void memset_io(volatile void *addr, unsigned char val, int count)
{
 ({ size_t __len = (count); void *__ret; if (__builtin_constant_p(count) && __len >= 64) __ret = memset(((void *) addr), (val), __len); else __ret = __builtin_memset(((void *) addr), (val), __len); __ret; });
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void memcpy_fromio(void *dst, const volatile void *src, int count)
{
 ({ size_t __len = (count); void *__ret; if (__builtin_constant_p(count) && __len >= 64) __ret = memcpy((dst), ((void *) src), __len); else __ret = __builtin_memcpy((dst), ((void *) src), __len); __ret; });
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void memcpy_toio(volatile void *dst, const void *src, int count)
{
 ({ size_t __len = (count); void *__ret; if (__builtin_constant_p(count) && __len >= 64) __ret = memcpy(((void *) dst), (src), __len); else __ret = __builtin_memcpy(((void *) dst), (src), __len); __ret; });
}
# 589 "./arch/mips/include/asm/io.h"
extern void (*_dma_cache_wback_inv)(unsigned long start, unsigned long size);
extern void (*_dma_cache_wback)(unsigned long start, unsigned long size);
extern void (*_dma_cache_inv)(unsigned long start, unsigned long size);
# 179 "./arch/mips/include/asm/page.h" 2
# 201 "./arch/mips/include/asm/page.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int pfn_valid(unsigned long pfn)
{

 extern unsigned long max_mapnr;

 return pfn >= ((((0UL)) + ((1UL) << 12)-1) >> 12) && pfn < max_mapnr;
}
# 229 "./arch/mips/include/asm/page.h"
extern int __virt_addr_valid(const volatile void *kaddr);
# 239 "./arch/mips/include/asm/page.h"
# 1 "include/asm-generic/memory_model.h" 1
# 240 "./arch/mips/include/asm/page.h" 2
# 1 "include/asm-generic/getorder.h" 1
# 12 "include/asm-generic/getorder.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((__const__))
int __get_order(unsigned long size)
{
 int order;

 size--;
 size >>= 12;

 order = fls(size);



 return order;
}
# 241 "./arch/mips/include/asm/page.h" 2
# 21 "include/linux/mmzone.h" 2
# 38 "include/linux/mmzone.h"
enum {
 MIGRATE_UNMOVABLE,
 MIGRATE_RECLAIMABLE,
 MIGRATE_MOVABLE,
 MIGRATE_PCPTYPES,
 MIGRATE_RESERVE = MIGRATE_PCPTYPES,
# 63 "include/linux/mmzone.h"
 MIGRATE_TYPES
};
# 76 "include/linux/mmzone.h"
extern int page_group_by_mobility_disabled;
# 85 "include/linux/mmzone.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int get_pfnblock_migratetype(struct page *page, unsigned long pfn)
{
 do { bool __cond = !(!(PB_migrate_end - PB_migrate != 2)); extern void __compiletime_assert_87(void) __attribute__((error("BUILD_BUG_ON failed: " "PB_migrate_end - PB_migrate != 2"))); if (__cond) __compiletime_assert_87(); do { } while (0); } while (0);
 return get_pfnblock_flags_mask(page, pfn, PB_migrate_end,
     ((1UL << (PB_migrate_end - PB_migrate + 1)) - 1));
}

struct free_area {
 struct list_head free_list[MIGRATE_TYPES];
 unsigned long nr_free;
};

struct pglist_data;
# 114 "include/linux/mmzone.h"
enum zone_stat_item {

 NR_FREE_PAGES,
 NR_ALLOC_BATCH,
 NR_LRU_BASE,
 NR_INACTIVE_ANON = NR_LRU_BASE,
 NR_ACTIVE_ANON,
 NR_INACTIVE_FILE,
 NR_ACTIVE_FILE,
 NR_UNEVICTABLE,
 NR_MLOCK,
 NR_ANON_PAGES,
 NR_FILE_MAPPED,

 NR_FILE_PAGES,
 NR_FILE_DIRTY,
 NR_WRITEBACK,
 NR_SLAB_RECLAIMABLE,
 NR_SLAB_UNRECLAIMABLE,
 NR_PAGETABLE,
 NR_KERNEL_STACK,

 NR_UNSTABLE_NFS,
 NR_BOUNCE,
 NR_VMSCAN_WRITE,
 NR_VMSCAN_IMMEDIATE,
 NR_WRITEBACK_TEMP,
 NR_ISOLATED_ANON,
 NR_ISOLATED_FILE,
 NR_SHMEM,
 NR_DIRTIED,
 NR_WRITTEN,
 NR_PAGES_SCANNED,
# 155 "include/linux/mmzone.h"
 WORKINGSET_REFAULT,
 WORKINGSET_ACTIVATE,
 WORKINGSET_NODERECLAIM,
 NR_ANON_TRANSPARENT_HUGEPAGES,
 NR_FREE_CMA_PAGES,
 NR_VM_ZONE_STAT_ITEMS };
# 175 "include/linux/mmzone.h"
enum lru_list {
 LRU_INACTIVE_ANON = 0,
 LRU_ACTIVE_ANON = 0 + 1,
 LRU_INACTIVE_FILE = 0 + 2,
 LRU_ACTIVE_FILE = 0 + 2 + 1,
 LRU_UNEVICTABLE,
 NR_LRU_LISTS
};





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_file_lru(enum lru_list lru)
{
 return (lru == LRU_INACTIVE_FILE || lru == LRU_ACTIVE_FILE);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_active_lru(enum lru_list lru)
{
 return (lru == LRU_ACTIVE_ANON || lru == LRU_ACTIVE_FILE);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_unevictable_lru(enum lru_list lru)
{
 return (lru == LRU_UNEVICTABLE);
}

struct zone_reclaim_stat {
# 212 "include/linux/mmzone.h"
 unsigned long recent_rotated[2];
 unsigned long recent_scanned[2];
};

struct lruvec {
 struct list_head lists[NR_LRU_LISTS];
 struct zone_reclaim_stat reclaim_stat;



};
# 239 "include/linux/mmzone.h"
typedef unsigned isolate_mode_t;

enum zone_watermarks {
 WMARK_MIN,
 WMARK_LOW,
 WMARK_HIGH,
 NR_WMARK
};





struct per_cpu_pages {
 int count;
 int high;
 int batch;


 struct list_head lists[MIGRATE_PCPTYPES];
};

struct per_cpu_pageset {
 struct per_cpu_pages pcp;







};



enum zone_type {
# 309 "include/linux/mmzone.h"
 ZONE_NORMAL,
# 321 "include/linux/mmzone.h"
 ZONE_MOVABLE,
 __MAX_NR_ZONES
};



struct zone {



 unsigned long watermark[NR_WMARK];
# 341 "include/linux/mmzone.h"
 long lowmem_reserve[2];
# 351 "include/linux/mmzone.h"
 unsigned int inactive_ratio;

 struct pglist_data *zone_pgdat;
 struct per_cpu_pageset *pageset;





 unsigned long dirty_balance_reserve;






 unsigned long *pageblock_flags;
# 379 "include/linux/mmzone.h"
 unsigned long zone_start_pfn;
# 422 "include/linux/mmzone.h"
 unsigned long managed_pages;
 unsigned long spanned_pages;
 unsigned long present_pages;

 const char *name;





 int nr_migrate_reserve_block;
# 472 "include/linux/mmzone.h"
 wait_queue_head_t *wait_table;
 unsigned long wait_table_hash_nr_entries;
 unsigned long wait_table_bits;




 spinlock_t lock;


 struct free_area free_area[11];


 unsigned long flags;






 spinlock_t lru_lock;
 struct lruvec lruvec;


 atomic_long_t inactive_age;






 unsigned long percpu_drift_mark;
# 528 "include/linux/mmzone.h"


 atomic_long_t vm_stat[NR_VM_ZONE_STAT_ITEMS];
} ;

enum zone_flags {
 ZONE_RECLAIM_LOCKED,
 ZONE_OOM_LOCKED,
 ZONE_CONGESTED,


 ZONE_DIRTY,



 ZONE_WRITEBACK,


 ZONE_FAIR_DEPLETED,
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long zone_end_pfn(const struct zone *zone)
{
 return zone->zone_start_pfn + zone->spanned_pages;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool zone_spans_pfn(const struct zone *zone, unsigned long pfn)
{
 return zone->zone_start_pfn <= pfn && pfn < zone_end_pfn(zone);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool zone_is_initialized(struct zone *zone)
{
 return !!zone->wait_table;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool zone_is_empty(struct zone *zone)
{
 return zone->spanned_pages == 0;
}
# 657 "include/linux/mmzone.h"
struct zonelist_cache;






struct zoneref {
 struct zone *zone;
 int zone_idx;
};
# 686 "include/linux/mmzone.h"
struct zonelist {
 struct zonelist_cache *zlcache_ptr;
 struct zoneref _zonerefs[((1 << 0) * 2) + 1];



};


struct node_active_region {
 unsigned long start_pfn;
 unsigned long end_pfn;
 int nid;
};




extern struct page *mem_map;
# 718 "include/linux/mmzone.h"
struct bootmem_data;
typedef struct pglist_data {
 struct zone node_zones[2];
 struct zonelist node_zonelists[1];
 int nr_zones;

 struct page *node_mem_map;





 struct bootmem_data *bdata;
# 745 "include/linux/mmzone.h"
 unsigned long node_start_pfn;
 unsigned long node_present_pages;
 unsigned long node_spanned_pages;

 int node_id;
 wait_queue_head_t kswapd_wait;
 wait_queue_head_t pfmemalloc_wait;
 struct task_struct *kswapd;

 int kswapd_max_order;
 enum zone_type classzone_idx;
# 766 "include/linux/mmzone.h"
} pg_data_t;
# 780 "include/linux/mmzone.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long pgdat_end_pfn(pg_data_t *pgdat)
{
 return pgdat->node_start_pfn + pgdat->node_spanned_pages;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool pgdat_is_empty(pg_data_t *pgdat)
{
 return !pgdat->node_start_pfn && !pgdat->node_spanned_pages;
}

# 1 "include/linux/memory_hotplug.h" 1



# 1 "include/linux/mmzone.h" 1
# 5 "include/linux/memory_hotplug.h" 2

# 1 "include/linux/notifier.h" 1
# 13 "include/linux/notifier.h"
# 1 "include/linux/mutex.h" 1
# 13 "include/linux/mutex.h"
# 1 "arch/mips/include/generated/asm/current.h" 1
# 14 "include/linux/mutex.h" 2






# 1 "include/linux/osq_lock.h" 1
# 11 "include/linux/osq_lock.h"
struct optimistic_spin_queue {




 atomic_t tail;
};




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void osq_lock_init(struct optimistic_spin_queue *lock)
{
 ((&lock->tail)->counter = ((0)));
}
# 21 "include/linux/mutex.h" 2
# 50 "include/linux/mutex.h"
struct mutex {

 atomic_t count;
 spinlock_t wait_lock;
 struct list_head wait_list;
# 68 "include/linux/mutex.h"
};





struct mutex_waiter {
 struct list_head list;
 struct task_struct *task;



};
# 100 "include/linux/mutex.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void mutex_destroy(struct mutex *lock) {}
# 120 "include/linux/mutex.h"
extern void __mutex_init(struct mutex *lock, const char *name,
    struct lock_class_key *key);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mutex_is_locked(struct mutex *lock)
{
 return (*(volatile typeof((&lock->count)->counter) *)&((&lock->count)->counter)) != 1;
}
# 158 "include/linux/mutex.h"
extern void mutex_lock(struct mutex *lock);
extern int mutex_lock_interruptible(struct mutex *lock);
extern int mutex_lock_killable(struct mutex *lock);
# 174 "include/linux/mutex.h"
extern int mutex_trylock(struct mutex *lock);
extern void mutex_unlock(struct mutex *lock);

extern int atomic_dec_and_mutex_lock(atomic_t *cnt, struct mutex *lock);
# 14 "include/linux/notifier.h" 2
# 1 "include/linux/rwsem.h" 1
# 21 "include/linux/rwsem.h"
struct rw_semaphore;


# 1 "include/linux/rwsem-spinlock.h" 1
# 23 "include/linux/rwsem-spinlock.h"
struct rw_semaphore {
 __s32 count;
 raw_spinlock_t wait_lock;
 struct list_head wait_list;



};



extern void __down_read(struct rw_semaphore *sem);
extern int __down_read_trylock(struct rw_semaphore *sem);
extern void __down_write(struct rw_semaphore *sem);
extern void __down_write_nested(struct rw_semaphore *sem, int subclass);
extern int __down_write_trylock(struct rw_semaphore *sem);
extern void __up_read(struct rw_semaphore *sem);
extern void __up_write(struct rw_semaphore *sem);
extern void __downgrade_write(struct rw_semaphore *sem);
extern int rwsem_is_locked(struct rw_semaphore *sem);
# 25 "include/linux/rwsem.h" 2
# 84 "include/linux/rwsem.h"
extern void __init_rwsem(struct rw_semaphore *sem, const char *name,
    struct lock_class_key *key);
# 100 "include/linux/rwsem.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int rwsem_is_contended(struct rw_semaphore *sem)
{
 return !list_empty(&sem->wait_list);
}




extern void down_read(struct rw_semaphore *sem);




extern int down_read_trylock(struct rw_semaphore *sem);




extern void down_write(struct rw_semaphore *sem);




extern int down_write_trylock(struct rw_semaphore *sem);




extern void up_read(struct rw_semaphore *sem);




extern void up_write(struct rw_semaphore *sem);




extern void downgrade_write(struct rw_semaphore *sem);
# 15 "include/linux/notifier.h" 2
# 1 "include/linux/srcu.h" 1
# 33 "include/linux/srcu.h"
# 1 "include/linux/rcupdate.h" 1
# 43 "include/linux/rcupdate.h"
# 1 "include/linux/completion.h" 1
# 25 "include/linux/completion.h"
struct completion {
 unsigned int done;
 wait_queue_head_t wait;
};
# 73 "include/linux/completion.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_completion(struct completion *x)
{
 x->done = 0;
 do { static struct lock_class_key __key; __init_waitqueue_head((&x->wait), "&x->wait", &__key); } while (0);
}
# 86 "include/linux/completion.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void reinit_completion(struct completion *x)
{
 x->done = 0;
}

extern void wait_for_completion(struct completion *);
extern void wait_for_completion_io(struct completion *);
extern int wait_for_completion_interruptible(struct completion *x);
extern int wait_for_completion_killable(struct completion *x);
extern unsigned long wait_for_completion_timeout(struct completion *x,
         unsigned long timeout);
extern unsigned long wait_for_completion_io_timeout(struct completion *x,
          unsigned long timeout);
extern long wait_for_completion_interruptible_timeout(
 struct completion *x, unsigned long timeout);
extern long wait_for_completion_killable_timeout(
 struct completion *x, unsigned long timeout);
extern bool try_wait_for_completion(struct completion *x);
extern bool completion_done(struct completion *x);

extern void complete(struct completion *);
extern void complete_all(struct completion *);
# 44 "include/linux/rcupdate.h" 2
# 1 "include/linux/debugobjects.h" 1






enum debug_obj_state {
 ODEBUG_STATE_NONE,
 ODEBUG_STATE_INIT,
 ODEBUG_STATE_INACTIVE,
 ODEBUG_STATE_ACTIVE,
 ODEBUG_STATE_DESTROYED,
 ODEBUG_STATE_NOTAVAILABLE,
 ODEBUG_STATE_MAX,
};

struct debug_obj_descr;
# 27 "include/linux/debugobjects.h"
struct debug_obj {
 struct hlist_node node;
 enum debug_obj_state state;
 unsigned int astate;
 void *object;
 struct debug_obj_descr *descr;
};
# 52 "include/linux/debugobjects.h"
struct debug_obj_descr {
 const char *name;
 void *(*debug_hint) (void *addr);
 int (*fixup_init) (void *addr, enum debug_obj_state state);
 int (*fixup_activate) (void *addr, enum debug_obj_state state);
 int (*fixup_destroy) (void *addr, enum debug_obj_state state);
 int (*fixup_free) (void *addr, enum debug_obj_state state);
 int (*fixup_assert_init)(void *addr, enum debug_obj_state state);
};
# 84 "include/linux/debugobjects.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_object_init (void *addr, struct debug_obj_descr *descr) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_object_init_on_stack(void *addr, struct debug_obj_descr *descr) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
debug_object_activate (void *addr, struct debug_obj_descr *descr) { return 0; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_object_deactivate(void *addr, struct debug_obj_descr *descr) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_object_destroy (void *addr, struct debug_obj_descr *descr) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_object_free (void *addr, struct debug_obj_descr *descr) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_object_assert_init(void *addr, struct debug_obj_descr *descr) { }

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void debug_objects_early_init(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void debug_objects_mem_init(void) { }





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
debug_check_no_obj_freed(const void *address, unsigned long size) { }
# 45 "include/linux/rcupdate.h" 2




extern int rcu_expedited;

enum rcutorture_type {
 RCU_FLAVOR,
 RCU_BH_FLAVOR,
 RCU_SCHED_FLAVOR,
 RCU_TASKS_FLAVOR,
 SRCU_FLAVOR,
 INVALID_RCU_FLAVOR
};
# 71 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcutorture_get_gp_data(enum rcutorture_type test_type,
       int *flags,
       unsigned long *gpnum,
       unsigned long *completed)
{
 *flags = 0;
 *gpnum = 0;
 *completed = 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcutorture_record_test_transition(void)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcutorture_record_progress(unsigned long vernum)
{
}
# 171 "include/linux/rcupdate.h"
void call_rcu_bh(struct callback_head *head,
   void (*func)(struct callback_head *head));
# 193 "include/linux/rcupdate.h"
void call_rcu_sched(struct callback_head *head,
      void (*func)(struct callback_head *rcu));

void synchronize_sched(void);
# 216 "include/linux/rcupdate.h"
void call_rcu_tasks(struct callback_head *head, void (*func)(struct callback_head *head));
void synchronize_rcu_tasks(void);
void rcu_barrier_tasks(void);
# 237 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __rcu_read_lock(void)
{
 __asm__ __volatile__("": : :"memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __rcu_read_unlock(void)
{
 __asm__ __volatile__("": : :"memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void synchronize_rcu(void)
{
 synchronize_sched();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int rcu_preempt_depth(void)
{
 return 0;
}




void rcu_init(void);
void rcu_sched_qs(void);
void rcu_bh_qs(void);
void rcu_check_callbacks(int cpu, int user);
struct notifier_block;
void rcu_idle_enter(void);
void rcu_idle_exit(void);
void rcu_irq_enter(void);
void rcu_irq_exit(void);





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_sysrq_start(void)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_sysrq_end(void)
{
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_user_enter(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_user_exit(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_user_hooks_switch(struct task_struct *prev,
      struct task_struct *next) { }





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_init_nohz(void)
{
}
# 364 "include/linux/rcupdate.h"
typedef void call_rcu_func_t(struct callback_head *head,
        void (*func)(struct callback_head *head));
void wait_rcu_gp(call_rcu_func_t crf);




# 1 "include/linux/rcutiny.h" 1
# 30 "include/linux/rcutiny.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long get_state_synchronize_rcu(void)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cond_synchronize_rcu(unsigned long oldstate)
{
 do { do { } while (0); } while (0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_barrier_bh(void)
{
 wait_rcu_gp(call_rcu_bh);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_barrier_sched(void)
{
 wait_rcu_gp(call_rcu_sched);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void synchronize_rcu_expedited(void)
{
 synchronize_sched();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_barrier(void)
{
 rcu_barrier_sched();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void synchronize_rcu_bh(void)
{
 synchronize_sched();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void synchronize_rcu_bh_expedited(void)
{
 synchronize_sched();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void synchronize_sched_expedited(void)
{
 synchronize_sched();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void kfree_call_rcu(struct callback_head *head,
      void (*func)(struct callback_head *rcu))
{
 call_rcu_sched(head, func);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_note_context_switch(int cpu)
{
 rcu_sched_qs();
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_virt_note_context_switch(int cpu)
{
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long rcu_batches_completed(void)
{
 return 0;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long rcu_batches_completed_bh(void)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_force_quiescent_state(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_bh_force_quiescent_state(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_sched_force_quiescent_state(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void show_rcu_gp_kthreads(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_cpu_stall_reset(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void exit_rcu(void)
{
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_scheduler_starting(void)
{
}
# 152 "include/linux/rcutiny.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool rcu_is_watching(void)
{
 return true;
}
# 372 "include/linux/rcupdate.h" 2
# 388 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_rcu_head(struct callback_head *head)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void destroy_rcu_head(struct callback_head *head)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_rcu_head_on_stack(struct callback_head *head)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void destroy_rcu_head_on_stack(struct callback_head *head)
{
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool rcu_lockdep_current_cpu_online(void)
{
 return true;
}
# 493 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int rcu_read_lock_held(void)
{
 return 1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int rcu_read_lock_bh_held(void)
{
 return 1;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int rcu_read_lock_sched_held(void)
{
 return 1;
}
# 877 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_read_lock(void)
{
 __rcu_read_lock();
 (void)0;
 do { } while (0);
 do { } while (0)
                                                  ;
}
# 929 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_read_unlock(void)
{
 do { } while (0)
                                                    ;
 do { } while (0);
 (void)0;
 __rcu_read_unlock();
}
# 955 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_read_lock_bh(void)
{
 local_bh_disable();
 (void)0;
 do { } while (0);
 do { } while (0)
                                                     ;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_read_unlock_bh(void)
{
 do { } while (0)
                                                       ;
 do { } while (0);
 (void)0;
 local_bh_enable();
}
# 991 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_read_lock_sched(void)
{
 __asm__ __volatile__("": : :"memory");
 (void)0;
 do { } while (0);
 do { } while (0)
                                                        ;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((no_instrument_function)) void rcu_read_lock_sched_notrace(void)
{
 __asm__ __volatile__("": : :"memory");
 (void)0;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_read_unlock_sched(void)
{
 do { } while (0)
                                                          ;
 do { } while (0);
 (void)0;
 __asm__ __volatile__("": : :"memory");
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((no_instrument_function)) void rcu_read_unlock_sched_notrace(void)
{
 (void)0;
 __asm__ __volatile__("": : :"memory");
}
# 1121 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int rcu_needs_cpu(int cpu, unsigned long *delta_jiffies)
{
 *delta_jiffies = (~0UL);
 return 0;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool rcu_is_nocb_cpu(int cpu) { return false; }
# 1143 "include/linux/rcupdate.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool rcu_sys_is_idle(void)
{
 return false;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_sysidle_force_exit(void)
{
}
# 34 "include/linux/srcu.h" 2
# 1 "include/linux/workqueue.h" 1







# 1 "include/linux/timer.h" 1




# 1 "include/linux/ktime.h" 1
# 24 "include/linux/ktime.h"
# 1 "include/linux/time.h" 1





# 1 "include/linux/math64.h" 1
# 64 "include/linux/math64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 div_u64_rem(u64 dividend, u32 divisor, u32 *remainder)
{
 *remainder = ({ uint32_t __base = (divisor); uint32_t __rem; (void)(((typeof((dividend)) *)0) == ((uint64_t *)0)); if (__builtin_expect(!!(((dividend) >> 32) == 0), 1)) { __rem = (uint32_t)(dividend) % __base; (dividend) = (uint32_t)(dividend) / __base; } else __rem = __div64_32(&(dividend), __base); __rem; });
 return dividend;
}



extern s64 div_s64_rem(s64 dividend, s32 divisor, s32 *remainder);



extern u64 div64_u64_rem(u64 dividend, u64 divisor, u64 *remainder);



extern u64 div64_u64(u64 dividend, u64 divisor);



extern s64 div64_s64(s64 dividend, s64 divisor);
# 97 "include/linux/math64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 div_u64(u64 dividend, u32 divisor)
{
 u32 remainder;
 return div_u64_rem(dividend, divisor, &remainder);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 div_s64(s64 dividend, s32 divisor)
{
 s32 remainder;
 return div_s64_rem(dividend, divisor, &remainder);
}


u32 iter_div_u64_rem(u64 dividend, u32 divisor, u64 *remainder);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) u32
__iter_div_u64_rem(u64 dividend, u32 divisor, u64 *remainder)
{
 u32 ret = 0;

 while (dividend >= divisor) {


  asm("" : "+rm"(dividend));

  dividend -= divisor;
  ret++;
 }

 *remainder = dividend;

 return ret;
}
# 148 "include/linux/math64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 mul_u64_u32_shr(u64 a, u32 mul, unsigned int shift)
{
 u32 ah, al;
 u64 ret;

 al = a;
 ah = a >> 32;

 ret = ((u64)al * mul) >> shift;
 if (ah)
  ret += ((u64)ah * mul) << (32 - shift);

 return ret;
}
# 7 "include/linux/time.h" 2
# 1 "include/linux/time64.h" 1



# 1 "include/uapi/linux/time.h" 1
# 9 "include/uapi/linux/time.h"
struct timespec {
 __kernel_time_t tv_sec;
 long tv_nsec;
};


struct timeval {
 __kernel_time_t tv_sec;
 __kernel_suseconds_t tv_usec;
};

struct timezone {
 int tz_minuteswest;
 int tz_dsttime;
};
# 34 "include/uapi/linux/time.h"
struct itimerspec {
 struct timespec it_interval;
 struct timespec it_value;
};

struct itimerval {
 struct timeval it_interval;
 struct timeval it_value;
};
# 5 "include/linux/time64.h" 2

typedef __s64 time64_t;
# 15 "include/linux/time64.h"
struct timespec64 {
 time64_t tv_sec;
 long tv_nsec;
};
# 60 "include/linux/time64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct timespec timespec64_to_timespec(const struct timespec64 ts64)
{
 struct timespec ret;

 ret.tv_sec = (time_t)ts64.tv_sec;
 ret.tv_nsec = ts64.tv_nsec;
 return ret;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct timespec64 timespec_to_timespec64(const struct timespec ts)
{
 struct timespec64 ret;

 ret.tv_sec = ts.tv_sec;
 ret.tv_nsec = ts.tv_nsec;
 return ret;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int timespec64_equal(const struct timespec64 *a,
       const struct timespec64 *b)
{
 return (a->tv_sec == b->tv_sec) && (a->tv_nsec == b->tv_nsec);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int timespec64_compare(const struct timespec64 *lhs, const struct timespec64 *rhs)
{
 if (lhs->tv_sec < rhs->tv_sec)
  return -1;
 if (lhs->tv_sec > rhs->tv_sec)
  return 1;
 return lhs->tv_nsec - rhs->tv_nsec;
}

extern void set_normalized_timespec64(struct timespec64 *ts, time64_t sec, s64 nsec);






extern struct timespec64 timespec64_add_safe(const struct timespec64 lhs,
      const struct timespec64 rhs);


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct timespec64 timespec64_add(struct timespec64 lhs,
      struct timespec64 rhs)
{
 struct timespec64 ts_delta;
 set_normalized_timespec64(&ts_delta, lhs.tv_sec + rhs.tv_sec,
    lhs.tv_nsec + rhs.tv_nsec);
 return ts_delta;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct timespec64 timespec64_sub(struct timespec64 lhs,
      struct timespec64 rhs)
{
 struct timespec64 ts_delta;
 set_normalized_timespec64(&ts_delta, lhs.tv_sec - rhs.tv_sec,
    lhs.tv_nsec - rhs.tv_nsec);
 return ts_delta;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool timespec64_valid(const struct timespec64 *ts)
{

 if (ts->tv_sec < 0)
  return false;

 if ((unsigned long)ts->tv_nsec >= 1000000000L)
  return false;
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool timespec64_valid_strict(const struct timespec64 *ts)
{
 if (!timespec64_valid(ts))
  return false;

 if ((unsigned long long)ts->tv_sec >= (((s64)~((u64)1 << 63)) / 1000000000L))
  return false;
 return true;
}
# 161 "include/linux/time64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 timespec64_to_ns(const struct timespec64 *ts)
{
 return ((s64) ts->tv_sec * 1000000000L) + ts->tv_nsec;
}







extern struct timespec64 ns_to_timespec64(const s64 nsec);
# 182 "include/linux/time64.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void timespec64_add_ns(struct timespec64 *a, u64 ns)
{
 a->tv_sec += __iter_div_u64_rem(a->tv_nsec + ns, 1000000000L, &ns);
 a->tv_nsec = ns;
}
# 8 "include/linux/time.h" 2

extern struct timezone sys_tz;



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int timespec_equal(const struct timespec *a,
                                 const struct timespec *b)
{
 return (a->tv_sec == b->tv_sec) && (a->tv_nsec == b->tv_nsec);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int timespec_compare(const struct timespec *lhs, const struct timespec *rhs)
{
 if (lhs->tv_sec < rhs->tv_sec)
  return -1;
 if (lhs->tv_sec > rhs->tv_sec)
  return 1;
 return lhs->tv_nsec - rhs->tv_nsec;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int timeval_compare(const struct timeval *lhs, const struct timeval *rhs)
{
 if (lhs->tv_sec < rhs->tv_sec)
  return -1;
 if (lhs->tv_sec > rhs->tv_sec)
  return 1;
 return lhs->tv_usec - rhs->tv_usec;
}

extern unsigned long mktime(const unsigned int year, const unsigned int mon,
       const unsigned int day, const unsigned int hour,
       const unsigned int min, const unsigned int sec);

extern void set_normalized_timespec(struct timespec *ts, time_t sec, s64 nsec);






extern struct timespec timespec_add_safe(const struct timespec lhs,
      const struct timespec rhs);


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct timespec timespec_add(struct timespec lhs,
      struct timespec rhs)
{
 struct timespec ts_delta;
 set_normalized_timespec(&ts_delta, lhs.tv_sec + rhs.tv_sec,
    lhs.tv_nsec + rhs.tv_nsec);
 return ts_delta;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct timespec timespec_sub(struct timespec lhs,
      struct timespec rhs)
{
 struct timespec ts_delta;
 set_normalized_timespec(&ts_delta, lhs.tv_sec - rhs.tv_sec,
    lhs.tv_nsec - rhs.tv_nsec);
 return ts_delta;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool timespec_valid(const struct timespec *ts)
{

 if (ts->tv_sec < 0)
  return false;

 if ((unsigned long)ts->tv_nsec >= 1000000000L)
  return false;
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool timespec_valid_strict(const struct timespec *ts)
{
 if (!timespec_valid(ts))
  return false;

 if ((unsigned long long)ts->tv_sec >= (((s64)~((u64)1 << 63)) / 1000000000L))
  return false;
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool timeval_valid(const struct timeval *tv)
{

 if (tv->tv_sec < 0)
  return false;


 if (tv->tv_usec < 0 || tv->tv_usec >= 1000000L)
  return false;

 return true;
}

extern struct timespec timespec_trunc(struct timespec t, unsigned gran);
# 133 "include/linux/time.h"
struct itimerval;
extern int do_setitimer(int which, struct itimerval *value,
   struct itimerval *ovalue);
extern int do_getitimer(int which, struct itimerval *value);

extern unsigned int alarm_setitimer(unsigned int seconds);

extern long do_utimes(int dfd, const char *filename, struct timespec *times, int flags);

struct tms;
extern void do_sys_times(struct tms *);





struct tm {




 int tm_sec;

 int tm_min;

 int tm_hour;

 int tm_mday;

 int tm_mon;

 long tm_year;

 int tm_wday;

 int tm_yday;
};

void time_to_tm(time_t totalsecs, int offset, struct tm *result);
# 180 "include/linux/time.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 timespec_to_ns(const struct timespec *ts)
{
 return ((s64) ts->tv_sec * 1000000000L) + ts->tv_nsec;
}
# 192 "include/linux/time.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 timeval_to_ns(const struct timeval *tv)
{
 return ((s64) tv->tv_sec * 1000000000L) +
  tv->tv_usec * 1000L;
}







extern struct timespec ns_to_timespec(const s64 nsec);







extern struct timeval ns_to_timeval(const s64 nsec);
# 222 "include/linux/time.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void timespec_add_ns(struct timespec *a, u64 ns)
{
 a->tv_sec += __iter_div_u64_rem(a->tv_nsec + ns, 1000000000L, &ns);
 a->tv_nsec = ns;
}
# 25 "include/linux/ktime.h" 2
# 1 "include/linux/jiffies.h" 1







# 1 "include/linux/timex.h" 1
# 56 "include/linux/timex.h"
# 1 "include/uapi/linux/timex.h" 1
# 64 "include/uapi/linux/timex.h"
struct timex {
 unsigned int modes;
 __kernel_long_t offset;
 __kernel_long_t freq;
 __kernel_long_t maxerror;
 __kernel_long_t esterror;
 int status;
 __kernel_long_t constant;
 __kernel_long_t precision;
 __kernel_long_t tolerance;


 struct timeval time;
 __kernel_long_t tick;

 __kernel_long_t ppsfreq;
 __kernel_long_t jitter;
 int shift;
 __kernel_long_t stabil;
 __kernel_long_t jitcnt;
 __kernel_long_t calcnt;
 __kernel_long_t errcnt;
 __kernel_long_t stbcnt;

 int tai;

 int :32; int :32; int :32; int :32;
 int :32; int :32; int :32; int :32;
 int :32; int :32; int :32;
};
# 57 "include/linux/timex.h" 2






# 1 "./include/uapi/linux/param.h" 1



# 1 "./arch/mips/include/uapi/asm/param.h" 1
# 14 "./arch/mips/include/uapi/asm/param.h"
# 1 "include/asm-generic/param.h" 1



# 1 "include/uapi/asm-generic/param.h" 1
# 5 "include/asm-generic/param.h" 2
# 15 "./arch/mips/include/uapi/asm/param.h" 2
# 5 "./include/uapi/linux/param.h" 2
# 64 "include/linux/timex.h" 2

# 1 "./arch/mips/include/asm/timex.h" 1
# 19 "./arch/mips/include/asm/timex.h"
# 1 "./arch/mips/include/asm/cpu-type.h" 1
# 12 "./arch/mips/include/asm/cpu-type.h"
# 1 "include/linux/smp.h" 1
# 14 "include/linux/smp.h"
# 1 "include/linux/llist.h" 1
# 61 "include/linux/llist.h"
struct llist_head {
 struct llist_node *first;
};

struct llist_node {
 struct llist_node *next;
};
# 76 "include/linux/llist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_llist_head(struct llist_head *list)
{
 list->first = ((void *)0);
}
# 158 "include/linux/llist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool llist_empty(const struct llist_head *head)
{
 return (*(volatile typeof(head->first) *)&(head->first)) == ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct llist_node *llist_next(struct llist_node *node)
{
 return node->next;
}

extern bool llist_add_batch(struct llist_node *new_first,
       struct llist_node *new_last,
       struct llist_head *head);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool llist_add(struct llist_node *new, struct llist_head *head)
{
 return llist_add_batch(new, new, head);
}
# 191 "include/linux/llist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct llist_node *llist_del_all(struct llist_head *head)
{
 return ({ do { bool __cond = !(!(sizeof(*(&head->first)) & ~0xc)); extern void __compiletime_assert_193(void) __attribute__((error("BUILD_BUG_ON failed: " "sizeof(*(&head->first)) & ~0xc"))); if (__cond) __compiletime_assert_193(); do { } while (0); } while (0); ((__typeof__(*(&head->first))) __xchg((unsigned long)(((void *)0)), (&head->first), sizeof(*(&head->first)))); });
}

extern struct llist_node *llist_del_first(struct llist_head *head);

struct llist_node *llist_reverse_order(struct llist_node *head);
# 15 "include/linux/smp.h" 2

typedef void (*smp_call_func_t)(void *info);
struct call_single_data {
 struct llist_node llist;
 smp_call_func_t func;
 void *info;
 u16 flags;
};


extern unsigned int total_cpus;

int smp_call_function_single(int cpuid, smp_call_func_t func, void *info,
        int wait);




int on_each_cpu(smp_call_func_t func, void *info, int wait);





void on_each_cpu_mask(const struct cpumask *mask, smp_call_func_t func,
  void *info, bool wait);






void on_each_cpu_cond(bool (*cond_func)(int cpu, void *info),
  smp_call_func_t func, void *info, bool wait,
  gfp_t gfp_flags);

int smp_call_function_single_async(int cpu, struct call_single_data *csd);
# 125 "include/linux/smp.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void smp_send_stop(void) { }





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int up_smp_call_function(smp_call_func_t func, void *info)
{
 return 0;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void smp_send_reschedule(int cpu) { }



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void call_function_init(void) { }

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
smp_call_function_any(const struct cpumask *mask, smp_call_func_t func,
        void *info, int wait)
{
 return smp_call_function_single(0, func, info, wait);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void kick_all_cpus_sync(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wake_up_all_idle_cpus(void) { }
# 185 "include/linux/smp.h"
extern void arch_disable_smp_support(void);

extern void arch_enable_nonboot_cpus_begin(void);
extern void arch_enable_nonboot_cpus_end(void);

void smp_setup_processor_id(void);
# 13 "./arch/mips/include/asm/cpu-type.h" 2


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __attribute__((pure)) __get_cpu_type(const int cpu_type)
{
 switch (cpu_type) {
# 40 "./arch/mips/include/asm/cpu-type.h"
 case CPU_4KEC:



 case CPU_4KSC:
 case CPU_24K:
 case CPU_34K:
 case CPU_1004K:
 case CPU_74K:
 case CPU_M14KC:
 case CPU_M14KEC:
 case CPU_INTERAPTIV:
 case CPU_PROAPTIV:
 case CPU_P5600:
 case CPU_M5150:
# 194 "./arch/mips/include/asm/cpu-type.h"
  break;
 default:
  __builtin_unreachable();
 }

 return cpu_type;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __attribute__((pure)) current_cpu_type(void)
{
 const int cpu_type = cpu_data[0].cputype;

 return __get_cpu_type(cpu_type);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __attribute__((pure)) boot_cpu_type(void)
{
 const int cpu_type = cpu_data[0].cputype;

 return __get_cpu_type(cpu_type);
}
# 20 "./arch/mips/include/asm/timex.h" 2
# 40 "./arch/mips/include/asm/timex.h"
typedef unsigned int cycles_t;
# 52 "./arch/mips/include/asm/timex.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int can_use_mips_counter(unsigned int prid)
{
 int comp = (prid & 0xff0000) != 0x000000;

 if (__builtin_constant_p(1) && !1)
  return 0;
 else if (__builtin_constant_p((1 | 1 | 0 | 0)) && (1 | 1 | 0 | 0))
  return 1;
 else if (__builtin_expect(!!(!__builtin_constant_p((1 | 1 | 0 | 0)) && comp), 1))
  return 1;

 if (!__builtin_constant_p(1))
  asm volatile("" : "=m" (cpu_data[0].options));
 if (__builtin_expect(!!(1 && prid >= (0x0400 | ((5) << 4 | (0)))), 1)
                                                         )
  return 1;
 else
  return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) cycles_t get_cycles(void)
{
 if (can_use_mips_counter(({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$15" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$15" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; })))
  return ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$9" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$9" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; });
 else
  return 0;
}
# 87 "./arch/mips/include/asm/timex.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long random_get_entropy(void)
{
 unsigned int prid = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$15" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$15" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; });
 unsigned int imp = prid & 0xff00;

 if (can_use_mips_counter(prid))
  return ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$9" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$9" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; });
 else if (__builtin_expect(!!(imp != 0x0300 && imp != 0x0600), 1))
  return ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$1" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$1" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; });
 else
  return 0;
}
# 66 "include/linux/timex.h" 2
# 139 "include/linux/timex.h"
extern unsigned long tick_usec;
extern unsigned long tick_nsec;
# 154 "include/linux/timex.h"
extern int do_adjtimex(struct timex *);
extern void hardpps(const struct timespec *, const struct timespec *);

int read_current_timer(unsigned long *timer_val);
void ntp_notify_cmos_timer(void);
# 9 "include/linux/jiffies.h" 2
# 57 "include/linux/jiffies.h"
extern int register_refined_jiffies(long clock_tick_rate);
# 76 "include/linux/jiffies.h"
extern u64 __attribute__((section(".data"))) jiffies_64;
extern unsigned long volatile __attribute__((section(".data"))) jiffies;


u64 get_jiffies_64(void);
# 182 "include/linux/jiffies.h"
extern unsigned long preset_lpj;
# 283 "include/linux/jiffies.h"
extern unsigned int jiffies_to_msecs(const unsigned long j);
extern unsigned int jiffies_to_usecs(const unsigned long j);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 jiffies_to_nsecs(const unsigned long j)
{
 return (u64)jiffies_to_usecs(j) * 1000L;
}

extern unsigned long msecs_to_jiffies(const unsigned int m);
extern unsigned long usecs_to_jiffies(const unsigned int u);
extern unsigned long timespec_to_jiffies(const struct timespec *value);
extern void jiffies_to_timespec(const unsigned long jiffies,
    struct timespec *value);
extern unsigned long timeval_to_jiffies(const struct timeval *value);
extern void jiffies_to_timeval(const unsigned long jiffies,
          struct timeval *value);

extern clock_t jiffies_to_clock_t(unsigned long x);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) clock_t jiffies_delta_to_clock_t(long delta)
{
 return jiffies_to_clock_t(({ typeof(0L) _max1 = (0L); typeof(delta) _max2 = (delta); (void) (&_max1 == &_max2); _max1 > _max2 ? _max1 : _max2; }));
}

extern unsigned long clock_t_to_jiffies(unsigned long x);
extern u64 jiffies_64_to_clock_t(u64 x);
extern u64 nsec_to_clock_t(u64 x);
extern u64 nsecs_to_jiffies64(u64 n);
extern unsigned long nsecs_to_jiffies(u64 n);
# 26 "include/linux/ktime.h" 2
# 37 "include/linux/ktime.h"
union ktime {
 s64 tv64;
};

typedef union ktime ktime_t;
# 50 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_set(const s64 secs, const unsigned long nsecs)
{
 if (__builtin_expect(!!(secs >= (((s64)~((u64)1 << 63)) / 1000000000L)), 0))
  return (ktime_t){ .tv64 = ((s64)~((u64)1 << 63)) };

 return (ktime_t) { .tv64 = secs * 1000000000L + (s64)nsecs };
}
# 81 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t timespec_to_ktime(struct timespec ts)
{
 return ktime_set(ts.tv_sec, ts.tv_nsec);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t timespec64_to_ktime(struct timespec64 ts)
{
 return ktime_set(ts.tv_sec, ts.tv_nsec);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t timeval_to_ktime(struct timeval tv)
{
 return ktime_set(tv.tv_sec, tv.tv_usec * 1000L);
}
# 120 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ktime_equal(const ktime_t cmp1, const ktime_t cmp2)
{
 return cmp1.tv64 == cmp2.tv64;
}
# 135 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ktime_compare(const ktime_t cmp1, const ktime_t cmp2)
{
 if (cmp1.tv64 < cmp2.tv64)
  return -1;
 if (cmp1.tv64 > cmp2.tv64)
  return 1;
 return 0;
}
# 151 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool ktime_after(const ktime_t cmp1, const ktime_t cmp2)
{
 return ktime_compare(cmp1, cmp2) > 0;
}
# 163 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool ktime_before(const ktime_t cmp1, const ktime_t cmp2)
{
 return ktime_compare(cmp1, cmp2) < 0;
}


extern s64 __ktime_divns(const ktime_t kt, s64 div);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 ktime_divns(const ktime_t kt, s64 div)
{




 __BUG_ON((unsigned long)(div < 0));
 if (__builtin_constant_p(div) && !(div >> 32)) {
  s64 ns = kt.tv64;
  u64 tmp = ns < 0 ? -ns : ns;

  ({ uint32_t __base = (div); uint32_t __rem; (void)(((typeof((tmp)) *)0) == ((uint64_t *)0)); if (__builtin_expect(!!(((tmp) >> 32) == 0), 1)) { __rem = (uint32_t)(tmp) % __base; (tmp) = (uint32_t)(tmp) / __base; } else __rem = __div64_32(&(tmp), __base); __rem; });
  return ns < 0 ? -tmp : tmp;
 } else {
  return __ktime_divns(kt, div);
 }
}
# 199 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 ktime_to_us(const ktime_t kt)
{
 return ktime_divns(kt, 1000L);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 ktime_to_ms(const ktime_t kt)
{
 return ktime_divns(kt, 1000000L);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 ktime_us_delta(const ktime_t later, const ktime_t earlier)
{
       return ktime_to_us(({ (ktime_t){ .tv64 = (later).tv64 - (earlier).tv64 }; }));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_add_us(const ktime_t kt, const u64 usec)
{
 return ({ (ktime_t){ .tv64 = (kt).tv64 + (usec * 1000L) }; });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_add_ms(const ktime_t kt, const u64 msec)
{
 return ({ (ktime_t){ .tv64 = (kt).tv64 + (msec * 1000000L) }; });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_sub_us(const ktime_t kt, const u64 usec)
{
 return ({ (ktime_t){ .tv64 = (kt).tv64 - (usec * 1000L) }; });
}

extern ktime_t ktime_add_safe(const ktime_t lhs, const ktime_t rhs);
# 239 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool ktime_to_timespec_cond(const ktime_t kt,
             struct timespec *ts)
{
 if (kt.tv64) {
  *ts = ns_to_timespec((kt).tv64);
  return true;
 } else {
  return false;
 }
}
# 258 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool ktime_to_timespec64_cond(const ktime_t kt,
             struct timespec64 *ts)
{
 if (kt.tv64) {
  *ts = ns_to_timespec64((kt).tv64);
  return true;
 } else {
  return false;
 }
}
# 278 "include/linux/ktime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ns_to_ktime(u64 ns)
{
 static const ktime_t ktime_zero = { .tv64 = 0 };

 return ({ (ktime_t){ .tv64 = (ktime_zero).tv64 + (ns) }; });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ms_to_ktime(u64 ms)
{
 static const ktime_t ktime_zero = { .tv64 = 0 };

 return ktime_add_ms(ktime_zero, ms);
}

# 1 "include/linux/timekeeping.h" 1





void timekeeping_init(void);
extern int timekeeping_suspended;




extern void do_gettimeofday(struct timeval *tv);
extern int do_settimeofday(const struct timespec *tv);
extern int do_sys_settimeofday(const struct timespec *tv,
          const struct timezone *tz);




unsigned long get_seconds(void);
struct timespec current_kernel_time(void);

struct timespec __current_kernel_time(void);




struct timespec get_monotonic_coarse(void);
extern void getrawmonotonic(struct timespec *ts);
extern void ktime_get_ts64(struct timespec64 *ts);

extern int __getnstimeofday64(struct timespec64 *tv);
extern void getnstimeofday64(struct timespec64 *tv);
# 57 "include/linux/timekeeping.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __getnstimeofday(struct timespec *ts)
{
 struct timespec64 ts64;
 int ret = __getnstimeofday64(&ts64);

 *ts = timespec64_to_timespec(ts64);
 return ret;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void getnstimeofday(struct timespec *ts)
{
 struct timespec64 ts64;

 getnstimeofday64(&ts64);
 *ts = timespec64_to_timespec(ts64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ktime_get_ts(struct timespec *ts)
{
 struct timespec64 ts64;

 ktime_get_ts64(&ts64);
 *ts = timespec64_to_timespec(ts64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ktime_get_real_ts(struct timespec *ts)
{
 struct timespec64 ts64;

 getnstimeofday64(&ts64);
 *ts = timespec64_to_timespec(ts64);
}


extern void getboottime(struct timespec *ts);
# 100 "include/linux/timekeeping.h"
enum tk_offsets {
 TK_OFFS_REAL,
 TK_OFFS_BOOT,
 TK_OFFS_TAI,
 TK_OFFS_MAX,
};

extern ktime_t ktime_get(void);
extern ktime_t ktime_get_with_offset(enum tk_offsets offs);
extern ktime_t ktime_mono_to_any(ktime_t tmono, enum tk_offsets offs);
extern ktime_t ktime_get_raw(void);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_get_real(void)
{
 return ktime_get_with_offset(TK_OFFS_REAL);
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_get_boottime(void)
{
 return ktime_get_with_offset(TK_OFFS_BOOT);
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_get_clocktai(void)
{
 return ktime_get_with_offset(TK_OFFS_TAI);
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t ktime_mono_to_real(ktime_t mono)
{
 return ktime_mono_to_any(mono, TK_OFFS_REAL);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 ktime_get_ns(void)
{
 return ((ktime_get()).tv64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 ktime_get_real_ns(void)
{
 return ((ktime_get_real()).tv64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 ktime_get_boot_ns(void)
{
 return ((ktime_get_boottime()).tv64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 ktime_get_raw_ns(void)
{
 return ((ktime_get_raw()).tv64);
}

extern u64 ktime_get_mono_fast_ns(void);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void get_monotonic_boottime(struct timespec *ts)
{
 *ts = ns_to_timespec((ktime_get_boottime()).tv64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void timekeeping_clocktai(struct timespec *ts)
{
 *ts = ns_to_timespec((ktime_get_clocktai()).tv64);
}




extern void timekeeping_inject_sleeptime(struct timespec *delta);




extern void getnstime_raw_and_real(struct timespec *ts_raw,
       struct timespec *ts_real);




extern bool persistent_clock_exist;
extern int persistent_clock_is_local;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool has_persistent_clock(void)
{
 return persistent_clock_exist;
}

extern void read_persistent_clock(struct timespec *ts);
extern void read_boot_clock(struct timespec *ts);
extern int update_persistent_clock(struct timespec now);
# 293 "include/linux/ktime.h" 2
# 6 "include/linux/timer.h" 2




struct tvec_base;

struct timer_list {




 struct list_head entry;
 unsigned long expires;
 struct tvec_base *base;

 void (*function)(unsigned long);
 unsigned long data;

 int slack;


 int start_pid;
 void *start_site;
 char start_comm[16];




};

extern struct tvec_base boot_tvec_bases;
# 94 "include/linux/timer.h"
void init_timer_key(struct timer_list *timer, unsigned int flags,
      const char *name, struct lock_class_key *key);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void destroy_timer_on_stack(struct timer_list *timer) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_timer_on_stack_key(struct timer_list *timer,
        unsigned int flags, const char *name,
        struct lock_class_key *key)
{
 init_timer_key(timer, flags, name, key);
}
# 169 "include/linux/timer.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int timer_pending(const struct timer_list * timer)
{
 return timer->entry.next != ((void *)0);
}

extern void add_timer_on(struct timer_list *timer, int cpu);
extern int del_timer(struct timer_list * timer);
extern int mod_timer(struct timer_list *timer, unsigned long expires);
extern int mod_timer_pending(struct timer_list *timer, unsigned long expires);
extern int mod_timer_pinned(struct timer_list *timer, unsigned long expires);

extern void set_timer_slack(struct timer_list *time, int slack_hz);
# 195 "include/linux/timer.h"
extern unsigned long get_next_timer_interrupt(unsigned long now);






extern int timer_stats_active;



extern void init_timer_stats(void);

extern void timer_stats_update_stats(void *timer, pid_t pid, void *startf,
         void *timerf, char *comm,
         unsigned int timer_flag);

extern void __timer_stats_timer_set_start_info(struct timer_list *timer,
            void *addr);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void timer_stats_timer_set_start_info(struct timer_list *timer)
{
 if (__builtin_expect(!!(!timer_stats_active), 1))
  return;
 __timer_stats_timer_set_start_info(timer, __builtin_return_address(0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void timer_stats_timer_clear_start_info(struct timer_list *timer)
{
 timer->start_site = ((void *)0);
}
# 240 "include/linux/timer.h"
extern void add_timer(struct timer_list *timer);

extern int try_to_del_timer_sync(struct timer_list *timer);
# 252 "include/linux/timer.h"
extern void init_timers(void);
extern void run_local_timers(void);
struct hrtimer;
extern enum hrtimer_restart it_real_fn(struct hrtimer *);

unsigned long __round_jiffies(unsigned long j, int cpu);
unsigned long __round_jiffies_relative(unsigned long j, int cpu);
unsigned long round_jiffies(unsigned long j);
unsigned long round_jiffies_relative(unsigned long j);

unsigned long __round_jiffies_up(unsigned long j, int cpu);
unsigned long __round_jiffies_up_relative(unsigned long j, int cpu);
unsigned long round_jiffies_up(unsigned long j);
unsigned long round_jiffies_up_relative(unsigned long j);
# 9 "include/linux/workqueue.h" 2







struct workqueue_struct;

struct work_struct;
typedef void (*work_func_t)(struct work_struct *work);
void delayed_work_timer_fn(unsigned long __data);







enum {
 WORK_STRUCT_PENDING_BIT = 0,
 WORK_STRUCT_DELAYED_BIT = 1,
 WORK_STRUCT_PWQ_BIT = 2,
 WORK_STRUCT_LINKED_BIT = 3,




 WORK_STRUCT_COLOR_SHIFT = 4,


 WORK_STRUCT_COLOR_BITS = 4,

 WORK_STRUCT_PENDING = 1 << WORK_STRUCT_PENDING_BIT,
 WORK_STRUCT_DELAYED = 1 << WORK_STRUCT_DELAYED_BIT,
 WORK_STRUCT_PWQ = 1 << WORK_STRUCT_PWQ_BIT,
 WORK_STRUCT_LINKED = 1 << WORK_STRUCT_LINKED_BIT,



 WORK_STRUCT_STATIC = 0,






 WORK_NR_COLORS = (1 << WORK_STRUCT_COLOR_BITS) - 1,
 WORK_NO_COLOR = WORK_NR_COLORS,


 WORK_CPU_UNBOUND = 1,






 WORK_STRUCT_FLAG_BITS = WORK_STRUCT_COLOR_SHIFT +
      WORK_STRUCT_COLOR_BITS,


 WORK_OFFQ_FLAG_BASE = WORK_STRUCT_COLOR_SHIFT,

 __WORK_OFFQ_CANCELING = WORK_OFFQ_FLAG_BASE,
 WORK_OFFQ_CANCELING = (1 << __WORK_OFFQ_CANCELING),






 WORK_OFFQ_FLAG_BITS = 1,
 WORK_OFFQ_POOL_SHIFT = WORK_OFFQ_FLAG_BASE + WORK_OFFQ_FLAG_BITS,
 WORK_OFFQ_LEFT = 32 - WORK_OFFQ_POOL_SHIFT,
 WORK_OFFQ_POOL_BITS = WORK_OFFQ_LEFT <= 31 ? WORK_OFFQ_LEFT : 31,
 WORK_OFFQ_POOL_NONE = (1LU << WORK_OFFQ_POOL_BITS) - 1,


 WORK_STRUCT_FLAG_MASK = (1UL << WORK_STRUCT_FLAG_BITS) - 1,
 WORK_STRUCT_WQ_DATA_MASK = ~WORK_STRUCT_FLAG_MASK,
 WORK_STRUCT_NO_POOL = (unsigned long)WORK_OFFQ_POOL_NONE << WORK_OFFQ_POOL_SHIFT,


 WORK_BUSY_PENDING = 1 << 0,
 WORK_BUSY_RUNNING = 1 << 1,


 WORKER_DESC_LEN = 24,
};

struct work_struct {
 atomic_long_t data;
 struct list_head entry;
 work_func_t func;



};





struct delayed_work {
 struct work_struct work;
 struct timer_list timer;


 struct workqueue_struct *wq;
 int cpu;
};
# 130 "include/linux/workqueue.h"
struct workqueue_attrs {
 int nice;
 cpumask_var_t cpumask;
 bool no_numa;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct delayed_work *to_delayed_work(struct work_struct *work)
{
 return ({ const typeof( ((struct delayed_work *)0)->work ) *__mptr = (work); (struct delayed_work *)( (char *)__mptr - __builtin_offsetof(struct delayed_work,work) );});
}

struct execute_work {
 struct work_struct work;
};
# 189 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __init_work(struct work_struct *work, int onstack) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void destroy_work_on_stack(struct work_struct *work) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void destroy_delayed_work_on_stack(struct delayed_work *work) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int work_static(struct work_struct *work) { return 0; }
# 281 "include/linux/workqueue.h"
enum {
 WQ_UNBOUND = 1 << 1,
 WQ_FREEZABLE = 1 << 2,
 WQ_MEM_RECLAIM = 1 << 3,
 WQ_HIGHPRI = 1 << 4,
 WQ_CPU_INTENSIVE = 1 << 5,
 WQ_SYSFS = 1 << 6,
# 314 "include/linux/workqueue.h"
 WQ_POWER_EFFICIENT = 1 << 7,

 __WQ_DRAINING = 1 << 16,
 __WQ_ORDERED = 1 << 17,

 WQ_MAX_ACTIVE = 512,
 WQ_MAX_UNBOUND_PER_CPU = 4,
 WQ_DFL_ACTIVE = WQ_MAX_ACTIVE / 2,
};
# 356 "include/linux/workqueue.h"
extern struct workqueue_struct *system_wq;
extern struct workqueue_struct *system_highpri_wq;
extern struct workqueue_struct *system_long_wq;
extern struct workqueue_struct *system_unbound_wq;
extern struct workqueue_struct *system_freezable_wq;
extern struct workqueue_struct *system_power_efficient_wq;
extern struct workqueue_struct *system_freezable_power_efficient_wq;

extern struct workqueue_struct *
__alloc_workqueue_key(const char *fmt, unsigned int flags, int max_active,
 struct lock_class_key *key, const char *lock_name, ...) __attribute__((format(printf, 1, 6)));
# 425 "include/linux/workqueue.h"
extern void destroy_workqueue(struct workqueue_struct *wq);

struct workqueue_attrs *alloc_workqueue_attrs(gfp_t gfp_mask);
void free_workqueue_attrs(struct workqueue_attrs *attrs);
int apply_workqueue_attrs(struct workqueue_struct *wq,
     const struct workqueue_attrs *attrs);

extern bool queue_work_on(int cpu, struct workqueue_struct *wq,
   struct work_struct *work);
extern bool queue_delayed_work_on(int cpu, struct workqueue_struct *wq,
   struct delayed_work *work, unsigned long delay);
extern bool mod_delayed_work_on(int cpu, struct workqueue_struct *wq,
   struct delayed_work *dwork, unsigned long delay);

extern void flush_workqueue(struct workqueue_struct *wq);
extern void drain_workqueue(struct workqueue_struct *wq);
extern void flush_scheduled_work(void);

extern int schedule_on_each_cpu(work_func_t func);

int execute_in_process_context(work_func_t fn, struct execute_work *);

extern bool flush_work(struct work_struct *work);
extern bool cancel_work_sync(struct work_struct *work);

extern bool flush_delayed_work(struct delayed_work *dwork);
extern bool cancel_delayed_work(struct delayed_work *dwork);
extern bool cancel_delayed_work_sync(struct delayed_work *dwork);

extern void workqueue_set_max_active(struct workqueue_struct *wq,
         int max_active);
extern bool current_is_workqueue_rescuer(void);
extern bool workqueue_congested(int cpu, struct workqueue_struct *wq);
extern unsigned int work_busy(struct work_struct *work);
extern __attribute__((format(printf, 1, 2))) void set_worker_desc(const char *fmt, ...);
extern void print_worker_info(const char *log_lvl, struct task_struct *task);
# 472 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool queue_work(struct workqueue_struct *wq,
         struct work_struct *work)
{
 return queue_work_on(WORK_CPU_UNBOUND, wq, work);
}
# 486 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool queue_delayed_work(struct workqueue_struct *wq,
          struct delayed_work *dwork,
          unsigned long delay)
{
 return queue_delayed_work_on(WORK_CPU_UNBOUND, wq, dwork, delay);
}
# 501 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool mod_delayed_work(struct workqueue_struct *wq,
        struct delayed_work *dwork,
        unsigned long delay)
{
 return mod_delayed_work_on(WORK_CPU_UNBOUND, wq, dwork, delay);
}
# 515 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool schedule_work_on(int cpu, struct work_struct *work)
{
 return queue_work_on(cpu, system_wq, work);
}
# 531 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool schedule_work(struct work_struct *work)
{
 return queue_work(system_wq, work);
}
# 545 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool schedule_delayed_work_on(int cpu, struct delayed_work *dwork,
         unsigned long delay)
{
 return queue_delayed_work_on(cpu, system_wq, dwork, delay);
}
# 559 "include/linux/workqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool schedule_delayed_work(struct delayed_work *dwork,
      unsigned long delay)
{
 return queue_delayed_work(system_wq, dwork, delay);
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool keventd_up(void)
{
 return system_wq != ((void *)0);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long work_on_cpu(int cpu, long (*fn)(void *), void *arg)
{
 return fn(arg);
}
# 589 "include/linux/workqueue.h"
int workqueue_sysfs_register(struct workqueue_struct *wq);
# 35 "include/linux/srcu.h" 2

struct srcu_struct_array {
 unsigned long c[2];
 unsigned long seq[2];
};

struct rcu_batch {
 struct callback_head *head, **tail;
};



struct srcu_struct {
 unsigned completed;
 struct srcu_struct_array *per_cpu_ref;
 spinlock_t queue_lock;
 bool running;

 struct rcu_batch batch_queue;

 struct rcu_batch batch_check0;

 struct rcu_batch batch_check1;
 struct rcu_batch batch_done;
 struct delayed_work work;



};
# 80 "include/linux/srcu.h"
int init_srcu_struct(struct srcu_struct *sp);




void process_srcu(struct work_struct *work);
# 130 "include/linux/srcu.h"
void call_srcu(struct srcu_struct *sp, struct callback_head *head,
  void (*func)(struct callback_head *head));

void cleanup_srcu_struct(struct srcu_struct *sp);
int __srcu_read_lock(struct srcu_struct *sp) ;
void __srcu_read_unlock(struct srcu_struct *sp, int idx) ;
void synchronize_srcu(struct srcu_struct *sp);
void synchronize_srcu_expedited(struct srcu_struct *sp);
long srcu_batches_completed(struct srcu_struct *sp);
void srcu_barrier(struct srcu_struct *sp);
# 167 "include/linux/srcu.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int srcu_read_lock_held(struct srcu_struct *sp)
{
 return 1;
}
# 218 "include/linux/srcu.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int srcu_read_lock(struct srcu_struct *sp)
{
 int retval = __srcu_read_lock(sp);

 do { } while (0);
 return retval;
}
# 233 "include/linux/srcu.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void srcu_read_unlock(struct srcu_struct *sp, int idx)

{
 do { } while (0);
 __srcu_read_unlock(sp, idx);
}
# 249 "include/linux/srcu.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void smp_mb__after_srcu_read_unlock(void)
{

}
# 16 "include/linux/notifier.h" 2
# 50 "include/linux/notifier.h"
typedef int (*notifier_fn_t)(struct notifier_block *nb,
   unsigned long action, void *data);

struct notifier_block {
 notifier_fn_t notifier_call;
 struct notifier_block *next;
 int priority;
};

struct atomic_notifier_head {
 spinlock_t lock;
 struct notifier_block *head;
};

struct blocking_notifier_head {
 struct rw_semaphore rwsem;
 struct notifier_block *head;
};

struct raw_notifier_head {
 struct notifier_block *head;
};

struct srcu_notifier_head {
 struct mutex mutex;
 struct srcu_struct srcu;
 struct notifier_block *head;
};
# 92 "include/linux/notifier.h"
extern void srcu_init_notifier_head(struct srcu_notifier_head *nh);
# 118 "include/linux/notifier.h"
extern int atomic_notifier_chain_register(struct atomic_notifier_head *nh,
  struct notifier_block *nb);
extern int blocking_notifier_chain_register(struct blocking_notifier_head *nh,
  struct notifier_block *nb);
extern int raw_notifier_chain_register(struct raw_notifier_head *nh,
  struct notifier_block *nb);
extern int srcu_notifier_chain_register(struct srcu_notifier_head *nh,
  struct notifier_block *nb);

extern int blocking_notifier_chain_cond_register(
  struct blocking_notifier_head *nh,
  struct notifier_block *nb);

extern int atomic_notifier_chain_unregister(struct atomic_notifier_head *nh,
  struct notifier_block *nb);
extern int blocking_notifier_chain_unregister(struct blocking_notifier_head *nh,
  struct notifier_block *nb);
extern int raw_notifier_chain_unregister(struct raw_notifier_head *nh,
  struct notifier_block *nb);
extern int srcu_notifier_chain_unregister(struct srcu_notifier_head *nh,
  struct notifier_block *nb);

extern int atomic_notifier_call_chain(struct atomic_notifier_head *nh,
  unsigned long val, void *v);
extern int __atomic_notifier_call_chain(struct atomic_notifier_head *nh,
 unsigned long val, void *v, int nr_to_call, int *nr_calls);
extern int blocking_notifier_call_chain(struct blocking_notifier_head *nh,
  unsigned long val, void *v);
extern int __blocking_notifier_call_chain(struct blocking_notifier_head *nh,
 unsigned long val, void *v, int nr_to_call, int *nr_calls);
extern int raw_notifier_call_chain(struct raw_notifier_head *nh,
  unsigned long val, void *v);
extern int __raw_notifier_call_chain(struct raw_notifier_head *nh,
 unsigned long val, void *v, int nr_to_call, int *nr_calls);
extern int srcu_notifier_call_chain(struct srcu_notifier_head *nh,
  unsigned long val, void *v);
extern int __srcu_notifier_call_chain(struct srcu_notifier_head *nh,
 unsigned long val, void *v, int nr_to_call, int *nr_calls);
# 168 "include/linux/notifier.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int notifier_from_errno(int err)
{
 if (err)
  return 0x8000 | (0x0001 - err);

 return 0x0001;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int notifier_to_errno(int ret)
{
 ret &= ~0x8000;
 return ret > 0x0001 ? 0x0001 - ret : 0;
}
# 212 "include/linux/notifier.h"
extern struct blocking_notifier_head reboot_notifier_list;
# 7 "include/linux/memory_hotplug.h" 2


struct page;
struct zone;
struct pglist_data;
struct mem_section;
struct memory_block;
# 199 "include/linux/memory_hotplug.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pgdat_resize_lock(struct pglist_data *p, unsigned long *f) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pgdat_resize_unlock(struct pglist_data *p, unsigned long *f) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pgdat_resize_init(struct pglist_data *pgdat) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned zone_span_seqbegin(struct zone *zone)
{
 return 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int zone_span_seqretry(struct zone *zone, unsigned iv)
{
 return 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void zone_span_writelock(struct zone *zone) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void zone_span_writeunlock(struct zone *zone) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void zone_seqlock_init(struct zone *zone) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mhp_notimplemented(const char *func)
{
 printk("\001" "4" "%s() called, with CONFIG_MEMORY_HOTPLUG disabled\n", func);
 dump_stack();
 return -89;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void register_page_bootmem_info_node(struct pglist_data *pgdat)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int try_online_node(int nid)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void get_online_mems(void) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void put_online_mems(void) {}
# 244 "include/linux/memory_hotplug.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_mem_section_removable(unsigned long pfn,
     unsigned long nr_pages)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void try_offline_node(int nid) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int offline_pages(unsigned long start_pfn, unsigned long nr_pages)
{
 return -22;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void remove_memory(int nid, u64 start, u64 size) {}


extern int walk_memory_range(unsigned long start_pfn, unsigned long end_pfn,
  void *arg, int (*func)(struct memory_block *, void *));
extern int add_memory(int nid, u64 start, u64 size);
extern int zone_for_memory(int nid, u64 start, u64 size, int zone_default);
extern int arch_add_memory(int nid, u64 start, u64 size);
extern int offline_pages(unsigned long start_pfn, unsigned long nr_pages);
extern bool is_memblock_offlined(struct memory_block *mem);
extern void remove_memory(int nid, u64 start, u64 size);
extern int sparse_add_one_section(struct zone *zone, unsigned long start_pfn);
extern void sparse_remove_one_section(struct zone *zone, struct mem_section *ms);
extern struct page *sparse_decode_mem_map(unsigned long coded_mem_map,
       unsigned long pnum);
# 791 "include/linux/mmzone.h" 2

extern struct mutex zonelists_mutex;
void build_all_zonelists(pg_data_t *pgdat, struct zone *zone);
void wakeup_kswapd(struct zone *zone, int order, enum zone_type classzone_idx);
bool zone_watermark_ok(struct zone *z, unsigned int order,
  unsigned long mark, int classzone_idx, int alloc_flags);
bool zone_watermark_ok_safe(struct zone *z, unsigned int order,
  unsigned long mark, int classzone_idx, int alloc_flags);
enum memmap_context {
 MEMMAP_EARLY,
 MEMMAP_HOTPLUG,
};
extern int init_currently_empty_zone(struct zone *zone, unsigned long start_pfn,
         unsigned long size,
         enum memmap_context context);

extern void lruvec_init(struct lruvec *lruvec);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct zone *lruvec_zone(struct lruvec *lruvec)
{



 return ({ const typeof( ((struct zone *)0)->lruvec ) *__mptr = (lruvec); (struct zone *)( (char *)__mptr - __builtin_offsetof(struct zone,lruvec) );});

}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void memory_present(int nid, unsigned long start, unsigned long end) {}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int local_memory_node(int node_id) { return node_id; };
# 839 "include/linux/mmzone.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int populated_zone(struct zone *zone)
{
 return (!!zone->present_pages);
}

extern int movable_zone;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int zone_movable_is_highmem(void)
{





 return 0;

}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_highmem_idx(enum zone_type idx)
{




 return 0;

}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_highmem(struct zone *zone)
{






 return 0;

}


struct ctl_table;
int min_free_kbytes_sysctl_handler(struct ctl_table *, int,
     void *, size_t *, loff_t *);
extern int sysctl_lowmem_reserve_ratio[2 -1];
int lowmem_reserve_ratio_sysctl_handler(struct ctl_table *, int,
     void *, size_t *, loff_t *);
int percpu_pagelist_fraction_sysctl_handler(struct ctl_table *, int,
     void *, size_t *, loff_t *);
int sysctl_min_unmapped_ratio_sysctl_handler(struct ctl_table *, int,
   void *, size_t *, loff_t *);
int sysctl_min_slab_ratio_sysctl_handler(struct ctl_table *, int,
   void *, size_t *, loff_t *);

extern int numa_zonelist_order_handler(struct ctl_table *, int,
   void *, size_t *, loff_t *);
extern char numa_zonelist_order[];




extern struct pglist_data contig_page_data;
# 916 "include/linux/mmzone.h"
extern struct pglist_data *first_online_pgdat(void);
extern struct pglist_data *next_online_pgdat(struct pglist_data *pgdat);
extern struct zone *next_zone(struct zone *zone);
# 948 "include/linux/mmzone.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct zone *zonelist_zone(struct zoneref *zoneref)
{
 return zoneref->zone;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int zonelist_zone_idx(struct zoneref *zoneref)
{
 return zoneref->zone_idx;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int zonelist_node_idx(struct zoneref *zoneref)
{




 return 0;

}
# 981 "include/linux/mmzone.h"
struct zoneref *next_zones_zonelist(struct zoneref *z,
     enum zone_type highest_zoneidx,
     nodemask_t *nodes,
     struct zone **zone);
# 998 "include/linux/mmzone.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct zoneref *first_zones_zonelist(struct zonelist *zonelist,
     enum zone_type highest_zoneidx,
     nodemask_t *nodes,
     struct zone **zone)
{
 return next_zones_zonelist(zonelist->_zonerefs, highest_zoneidx, nodes,
        zone);
}
# 1229 "include/linux/mmzone.h"
void memory_present(int nid, unsigned long start, unsigned long end);
unsigned long __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) node_memmap_size_bytes(int, unsigned long, unsigned long);
# 1263 "include/linux/mmzone.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int memmap_valid_within(unsigned long pfn,
     struct page *page, struct zone *zone)
{
 return 1;
}
# 8 "include/linux/bootmem.h" 2
# 1 "include/linux/mm_types.h" 1



# 1 "include/linux/auxvec.h" 1



# 1 "include/uapi/linux/auxvec.h" 1



# 1 "arch/mips/include/generated/uapi/asm/auxvec.h" 1
# 1 "./include/uapi/asm-generic/auxvec.h" 1
# 1 "arch/mips/include/generated/uapi/asm/auxvec.h" 2
# 5 "include/uapi/linux/auxvec.h" 2
# 5 "include/linux/auxvec.h" 2
# 5 "include/linux/mm_types.h" 2




# 1 "include/linux/rbtree.h" 1
# 35 "include/linux/rbtree.h"
struct rb_node {
 unsigned long __rb_parent_color;
 struct rb_node *rb_right;
 struct rb_node *rb_left;
} __attribute__((aligned(sizeof(long))));


struct rb_root {
 struct rb_node *rb_node;
};
# 61 "include/linux/rbtree.h"
extern void rb_insert_color(struct rb_node *, struct rb_root *);
extern void rb_erase(struct rb_node *, struct rb_root *);



extern struct rb_node *rb_next(const struct rb_node *);
extern struct rb_node *rb_prev(const struct rb_node *);
extern struct rb_node *rb_first(const struct rb_root *);
extern struct rb_node *rb_last(const struct rb_root *);


extern struct rb_node *rb_first_postorder(const struct rb_root *);
extern struct rb_node *rb_next_postorder(const struct rb_node *);


extern void rb_replace_node(struct rb_node *victim, struct rb_node *new,
       struct rb_root *root);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rb_link_node(struct rb_node * node, struct rb_node * parent,
    struct rb_node ** rb_link)
{
 node->__rb_parent_color = (unsigned long)parent;
 node->rb_left = node->rb_right = ((void *)0);

 *rb_link = node;
}
# 10 "include/linux/mm_types.h" 2



# 1 "include/linux/page-debug-flags.h" 1
# 14 "include/linux/page-debug-flags.h"
enum page_debug_flags {
 PAGE_DEBUG_FLAG_POISON,
 PAGE_DEBUG_FLAG_GUARD,
};
# 14 "include/linux/mm_types.h" 2
# 1 "include/linux/uprobes.h" 1
# 31 "include/linux/uprobes.h"
struct vm_area_struct;
struct mm_struct;
struct inode;
struct notifier_block;
struct page;






enum uprobe_filter_ctx {
 UPROBE_FILTER_REGISTER,
 UPROBE_FILTER_UNREGISTER,
 UPROBE_FILTER_MMAP,
};

struct uprobe_consumer {
 int (*handler)(struct uprobe_consumer *self, struct pt_regs *regs);
 int (*ret_handler)(struct uprobe_consumer *self,
    unsigned long func,
    struct pt_regs *regs);
 bool (*filter)(struct uprobe_consumer *self,
    enum uprobe_filter_ctx ctx,
    struct mm_struct *mm);

 struct uprobe_consumer *next;
};
# 135 "include/linux/uprobes.h"
struct uprobes_state {
};



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
uprobe_register(struct inode *inode, loff_t offset, struct uprobe_consumer *uc)
{
 return -89;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
uprobe_apply(struct inode *inode, loff_t offset, struct uprobe_consumer *uc, bool add)
{
 return -89;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
uprobe_unregister(struct inode *inode, loff_t offset, struct uprobe_consumer *uc)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int uprobe_mmap(struct vm_area_struct *vma)
{
 return 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
uprobe_munmap(struct vm_area_struct *vma, unsigned long start, unsigned long end)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void uprobe_start_dup_mmap(void)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void uprobe_end_dup_mmap(void)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
uprobe_dup_mmap(struct mm_struct *oldmm, struct mm_struct *newmm)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void uprobe_notify_resume(struct pt_regs *regs)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uprobe_deny_signal(void)
{
 return false;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void uprobe_free_utask(struct task_struct *t)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void uprobe_copy_process(struct task_struct *t, unsigned long flags)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void uprobe_clear_state(struct mm_struct *mm)
{
}
# 15 "include/linux/mm_types.h" 2


# 1 "./arch/mips/include/asm/mmu.h" 1



typedef struct {
 unsigned long asid[1];
 void *vdso;
} mm_context_t;
# 18 "include/linux/mm_types.h" 2






struct address_space;
# 44 "include/linux/mm_types.h"
struct page {

 unsigned long flags;

 union {
  struct address_space *mapping;






  void *s_mem;
 };


 struct {
  union {
   unsigned long index;
   void *freelist;
   bool pfmemalloc;
# 73 "include/linux/mm_types.h"
  };

  union {
# 86 "include/linux/mm_types.h"
   unsigned counters;


   struct {

    union {
# 108 "include/linux/mm_types.h"
     atomic_t _mapcount;

     struct {
      unsigned inuse:16;
      unsigned objects:15;
      unsigned frozen:1;
     };
     int units;
    };
    atomic_t _count;
   };
   unsigned int active;
  };
 };


 union {
  struct list_head lru;




  struct {
   struct page *next;




   short int pages;
   short int pobjects;

  };

  struct slab *slab_page;
  struct callback_head callback_head;





 };


 union {
  unsigned long private;
# 166 "include/linux/mm_types.h"
  struct kmem_cache *slab_cache;
  struct page *first_page;
 };
# 199 "include/linux/mm_types.h"
}







;

struct page_frag {
 struct page *page;




 __u16 offset;
 __u16 size;

};

typedef unsigned long vm_flags_t;






struct vm_region {
 struct rb_node vm_rb;
 vm_flags_t vm_flags;
 unsigned long vm_start;
 unsigned long vm_end;
 unsigned long vm_top;
 unsigned long vm_pgoff;
 struct file *vm_file;

 int vm_usage;
 bool vm_icache_flushed : 1;

};







struct vm_area_struct {


 unsigned long vm_start;
 unsigned long vm_end;



 struct vm_area_struct *vm_next, *vm_prev;

 struct rb_node vm_rb;







 unsigned long rb_subtree_gap;



 struct mm_struct *vm_mm;
 pgprot_t vm_page_prot;
 unsigned long vm_flags;






 union {
  struct {
   struct rb_node rb;
   unsigned long rb_subtree_last;
  } linear;
  struct list_head nonlinear;
 } shared;







 struct list_head anon_vma_chain;

 struct anon_vma *anon_vma;


 const struct vm_operations_struct *vm_ops;


 unsigned long vm_pgoff;

 struct file * vm_file;
 void * vm_private_data;







};

struct core_thread {
 struct task_struct *task;
 struct core_thread *next;
};

struct core_state {
 atomic_t nr_threads;
 struct core_thread dumper;
 struct completion startup;
};

enum {
 MM_FILEPAGES,
 MM_ANONPAGES,
 MM_SWAPENTS,
 NR_MM_COUNTERS
};
# 340 "include/linux/mm_types.h"
struct mm_rss_stat {
 atomic_long_t count[NR_MM_COUNTERS];
};

struct kioctx_table;
struct mm_struct {
 struct vm_area_struct *mmap;
 struct rb_root mm_rb;
 u32 vmacache_seqnum;

 unsigned long (*get_unmapped_area) (struct file *filp,
    unsigned long addr, unsigned long len,
    unsigned long pgoff, unsigned long flags);

 unsigned long mmap_base;
 unsigned long mmap_legacy_base;
 unsigned long task_size;
 unsigned long highest_vm_end;
 pgd_t * pgd;
 atomic_t mm_users;
 atomic_t mm_count;
 atomic_long_t nr_ptes;
 int map_count;

 spinlock_t page_table_lock;
 struct rw_semaphore mmap_sem;

 struct list_head mmlist;





 unsigned long hiwater_rss;
 unsigned long hiwater_vm;

 unsigned long total_vm;
 unsigned long locked_vm;
 unsigned long pinned_vm;
 unsigned long shared_vm;
 unsigned long exec_vm;
 unsigned long stack_vm;
 unsigned long def_flags;
 unsigned long start_code, end_code, start_data, end_data;
 unsigned long start_brk, brk, start_stack;
 unsigned long arg_start, arg_end, env_start, env_end;

 unsigned long saved_auxv[(2*(0 + 20 + 1))];





 struct mm_rss_stat rss_stat;

 struct linux_binfmt *binfmt;

 cpumask_var_t cpu_vm_mask_var;


 mm_context_t context;

 unsigned long flags;

 struct core_state *core_state;
# 424 "include/linux/mm_types.h"
 struct file *exe_file;
# 456 "include/linux/mm_types.h"
 struct uprobes_state uprobes_state;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void mm_init_cpumask(struct mm_struct *mm)
{



 cpumask_clear(mm->cpu_vm_mask_var);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) cpumask_t *mm_cpumask(struct mm_struct *mm)
{
 return mm->cpu_vm_mask_var;
}
# 502 "include/linux/mm_types.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool mm_tlb_flush_pending(struct mm_struct *mm)
{
 return false;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_tlb_flush_pending(struct mm_struct *mm)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_tlb_flush_pending(struct mm_struct *mm)
{
}


struct vm_special_mapping
{
 const char *name;
 struct page **pages;
};

enum tlb_flush_reason {
 TLB_FLUSH_ON_TASK_SWITCH,
 TLB_REMOTE_SHOOTDOWN,
 TLB_LOCAL_SHOOTDOWN,
 TLB_LOCAL_MM_SHOOTDOWN,
 NR_TLB_FLUSH_REASONS,
};
# 9 "include/linux/bootmem.h" 2
# 1 "./arch/mips/include/asm/dma.h" 1
# 17 "./arch/mips/include/asm/dma.h"
# 1 "include/linux/delay.h" 1
# 12 "include/linux/delay.h"
extern unsigned long loops_per_jiffy;

# 1 "./arch/mips/include/asm/delay.h" 1
# 16 "./arch/mips/include/asm/delay.h"
extern void __delay(unsigned long loops);
extern void __ndelay(unsigned long ns);
extern void __udelay(unsigned long us);
# 15 "include/linux/delay.h" 2
# 44 "include/linux/delay.h"
extern unsigned long lpj_fine;
void calibrate_delay(void);
void msleep(unsigned int msecs);
unsigned long msleep_interruptible(unsigned int msecs);
void usleep_range(unsigned long min, unsigned long max);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ssleep(unsigned int seconds)
{
 msleep(seconds * 1000);
}
# 18 "./arch/mips/include/asm/dma.h" 2
# 157 "./arch/mips/include/asm/dma.h"
extern spinlock_t dma_spin_lock;

static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long claim_dma_lock(void)
{
 unsigned long flags;
 do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); do { do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(spinlock_check(&dma_spin_lock)); } while (0); } while (0); } while (0); } while (0); } while (0);
 return flags;
}

static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void release_dma_lock(unsigned long flags)
{
 spin_unlock_irqrestore(&dma_spin_lock, flags);
}


static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void enable_dma(unsigned int dmanr)
{
 if (dmanr<=3)
  outb(dmanr, 0x0A);
 else
  outb(dmanr & 3, 0xD4);
}

static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void disable_dma(unsigned int dmanr)
{
 if (dmanr<=3)
  outb(dmanr | 4, 0x0A);
 else
  outb((dmanr & 3) | 4, 0xD4);
}
# 195 "./arch/mips/include/asm/dma.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void clear_dma_ff(unsigned int dmanr)
{
 if (dmanr<=3)
  outb(0, 0x0C);
 else
  outb(0, 0xD8);
}


static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_dma_mode(unsigned int dmanr, char mode)
{
 if (dmanr<=3)
  outb(mode | dmanr, 0x0B);
 else
  outb(mode | (dmanr&3), 0xD6);
}






static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_dma_page(unsigned int dmanr, char pagenr)
{
 switch(dmanr) {
  case 0:
   outb(pagenr, 0x87);
   break;
  case 1:
   outb(pagenr, 0x83);
   break;
  case 2:
   outb(pagenr, 0x81);
   break;
  case 3:
   outb(pagenr, 0x82);
   break;
  case 5:
   outb(pagenr & 0xfe, 0x8B);
   break;
  case 6:
   outb(pagenr & 0xfe, 0x89);
   break;
  case 7:
   outb(pagenr & 0xfe, 0x8A);
   break;
 }
}





static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_dma_addr(unsigned int dmanr, unsigned int a)
{
 set_dma_page(dmanr, a>>16);
 if (dmanr <= 3) {
     outb( a & 0xff, ((dmanr&3)<<1) + 0x00 );
     outb( (a>>8) & 0xff, ((dmanr&3)<<1) + 0x00 );
 } else {
     outb( (a>>1) & 0xff, ((dmanr&3)<<2) + 0xC0 );
     outb( (a>>9) & 0xff, ((dmanr&3)<<2) + 0xC0 );
 }
}
# 269 "./arch/mips/include/asm/dma.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_dma_count(unsigned int dmanr, unsigned int count)
{
 count--;
 if (dmanr <= 3) {
     outb( count & 0xff, ((dmanr&3)<<1) + 1 + 0x00 );
     outb( (count>>8) & 0xff, ((dmanr&3)<<1) + 1 + 0x00 );
 } else {
     outb( (count>>1) & 0xff, ((dmanr&3)<<2) + 2 + 0xC0 );
     outb( (count>>9) & 0xff, ((dmanr&3)<<2) + 2 + 0xC0 );
 }
}
# 290 "./arch/mips/include/asm/dma.h"
static __inline__ __attribute__((always_inline)) __attribute__((no_instrument_function)) int get_dma_residue(unsigned int dmanr)
{
 unsigned int io_port = (dmanr<=3)? ((dmanr&3)<<1) + 1 + 0x00
      : ((dmanr&3)<<2) + 2 + 0xC0;


 unsigned short count;

 count = 1 + inb(io_port);
 count += inb(io_port) << 8;

 return (dmanr<=3)? count : (count<<1);
}



extern int request_dma(unsigned int dmanr, const char * device_id);
extern void free_dma(unsigned int dmanr);




extern int isa_dma_bridge_buggy;
# 10 "include/linux/bootmem.h" 2





extern unsigned long max_low_pfn;
extern unsigned long min_low_pfn;




extern unsigned long max_pfn;






typedef struct bootmem_data {
 unsigned long node_min_pfn;
 unsigned long node_low_pfn;
 void *node_bootmem_map;
 unsigned long last_end_off;
 unsigned long hint_idx;
 struct list_head list;
} bootmem_data_t;

extern bootmem_data_t bootmem_node_data[];


extern unsigned long bootmem_bootmap_pages(unsigned long);

extern unsigned long init_bootmem_node(pg_data_t *pgdat,
           unsigned long freepfn,
           unsigned long startpfn,
           unsigned long endpfn);
extern unsigned long init_bootmem(unsigned long addr, unsigned long memend);

extern unsigned long free_all_bootmem(void);
extern void reset_node_managed_pages(pg_data_t *pgdat);
extern void reset_all_zones_managed_pages(void);

extern void free_bootmem_node(pg_data_t *pgdat,
         unsigned long addr,
         unsigned long size);
extern void free_bootmem(unsigned long physaddr, unsigned long size);
extern void free_bootmem_late(unsigned long physaddr, unsigned long size);
# 69 "include/linux/bootmem.h"
extern int reserve_bootmem(unsigned long addr,
      unsigned long size,
      int flags);
extern int reserve_bootmem_node(pg_data_t *pgdat,
    unsigned long physaddr,
    unsigned long size,
    int flags);

extern void *__alloc_bootmem(unsigned long size,
        unsigned long align,
        unsigned long goal);
extern void *__alloc_bootmem_nopanic(unsigned long size,
         unsigned long align,
         unsigned long goal);
extern void *__alloc_bootmem_node(pg_data_t *pgdat,
      unsigned long size,
      unsigned long align,
      unsigned long goal);
void *__alloc_bootmem_node_high(pg_data_t *pgdat,
      unsigned long size,
      unsigned long align,
      unsigned long goal);
extern void *__alloc_bootmem_node_nopanic(pg_data_t *pgdat,
      unsigned long size,
      unsigned long align,
      unsigned long goal);
void *___alloc_bootmem_node_nopanic(pg_data_t *pgdat,
      unsigned long size,
      unsigned long align,
      unsigned long goal,
      unsigned long limit);
extern void *__alloc_bootmem_low(unsigned long size,
     unsigned long align,
     unsigned long goal);
void *__alloc_bootmem_low_nopanic(unsigned long size,
     unsigned long align,
     unsigned long goal);
extern void *__alloc_bootmem_low_node(pg_data_t *pgdat,
          unsigned long size,
          unsigned long align,
          unsigned long goal);
# 247 "include/linux/bootmem.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc(
     phys_addr_t size, phys_addr_t align)
{
 if (!align)
  align = (1 << 5);
 return __alloc_bootmem(size, align, ((unsigned long)((((0x80000000UL) + (0UL)) + 0x01000000)) - ((0x80000000UL) + (0UL)) + (0UL)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_nopanic(
     phys_addr_t size, phys_addr_t align)
{
 if (!align)
  align = (1 << 5);
 return __alloc_bootmem_nopanic(size, align, ((unsigned long)((((0x80000000UL) + (0UL)) + 0x01000000)) - ((0x80000000UL) + (0UL)) + (0UL)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_low(
     phys_addr_t size, phys_addr_t align)
{
 if (!align)
  align = (1 << 5);
 return __alloc_bootmem_low(size, align, 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_low_nopanic(
     phys_addr_t size, phys_addr_t align)
{
 if (!align)
  align = (1 << 5);
 return __alloc_bootmem_low_nopanic(size, align, 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_from_nopanic(
  phys_addr_t size, phys_addr_t align, phys_addr_t min_addr)
{
 return __alloc_bootmem_nopanic(size, align, min_addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_node(
      phys_addr_t size, int nid)
{
 return __alloc_bootmem_node((&contig_page_data), size, (1 << 5),
         ((unsigned long)((((0x80000000UL) + (0UL)) + 0x01000000)) - ((0x80000000UL) + (0UL)) + (0UL)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_node_nopanic(
      phys_addr_t size, int nid)
{
 return __alloc_bootmem_node_nopanic((&contig_page_data), size,
          (1 << 5),
          ((unsigned long)((((0x80000000UL) + (0UL)) + 0x01000000)) - ((0x80000000UL) + (0UL)) + (0UL)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_try_nid(phys_addr_t size,
 phys_addr_t align, phys_addr_t min_addr, phys_addr_t max_addr, int nid)
{
 return __alloc_bootmem_node_high((&contig_page_data), size, align,
       min_addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_virt_alloc_try_nid_nopanic(
   phys_addr_t size, phys_addr_t align,
   phys_addr_t min_addr, phys_addr_t max_addr, int nid)
{
 return ___alloc_bootmem_node_nopanic((&contig_page_data), size, align,
    min_addr, max_addr);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_free_early(
     phys_addr_t base, phys_addr_t size)
{
 free_bootmem(base, size);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_free_early_nid(
    phys_addr_t base, phys_addr_t size, int nid)
{
 free_bootmem_node((&contig_page_data), base, size);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) memblock_free_late(
     phys_addr_t base, phys_addr_t size)
{
 free_bootmem_late(base, size);
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *alloc_remap(int nid, unsigned long size)
{
 return ((void *)0);
}


extern void *alloc_large_system_hash(const char *tablename,
         unsigned long bucketsize,
         unsigned long numentries,
         int scale,
         int flags,
         unsigned int *_hash_shift,
         unsigned int *_hash_mask,
         unsigned long low_limit,
         unsigned long high_limit);
# 365 "include/linux/bootmem.h"
extern int hashdist;
# 18 "arch/mips/ath79/setup.c" 2
# 1 "include/linux/err.h" 1
# 23 "include/linux/err.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * ERR_PTR(long error)
{
 return (void *) error;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long PTR_ERR( const void *ptr)
{
 return (long) ptr;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool IS_ERR( const void *ptr)
{
 return __builtin_expect(!!(((unsigned long)ptr) >= (unsigned long)-4095), 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool IS_ERR_OR_NULL( const void *ptr)
{
 return !ptr || __builtin_expect(!!(((unsigned long)ptr) >= (unsigned long)-4095), 0);
}
# 50 "include/linux/err.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void * ERR_CAST( const void *ptr)
{

 return (void *) ptr;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int PTR_ERR_OR_ZERO( const void *ptr)
{
 if (IS_ERR(ptr))
  return PTR_ERR(ptr);
 else
  return 0;
}
# 19 "arch/mips/ath79/setup.c" 2
# 1 "include/linux/clk.h" 1
# 19 "include/linux/clk.h"
struct device;

struct clk;
# 130 "include/linux/clk.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long clk_get_accuracy(struct clk *clk)
{
 return -524;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long clk_set_phase(struct clk *clk, int phase)
{
 return -524;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long clk_get_phase(struct clk *clk)
{
 return -524;
}
# 158 "include/linux/clk.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int clk_prepare(struct clk *clk)
{
 do { do { } while (0); } while (0);
 return 0;
}
# 177 "include/linux/clk.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clk_unprepare(struct clk *clk)
{
 do { do { } while (0); } while (0);
}
# 199 "include/linux/clk.h"
struct clk *clk_get(struct device *dev, const char *id);
# 219 "include/linux/clk.h"
struct clk *devm_clk_get(struct device *dev, const char *id);
# 231 "include/linux/clk.h"
int clk_enable(struct clk *clk);
# 247 "include/linux/clk.h"
void clk_disable(struct clk *clk);






unsigned long clk_get_rate(struct clk *clk);
# 266 "include/linux/clk.h"
void clk_put(struct clk *clk);
# 279 "include/linux/clk.h"
void devm_clk_put(struct device *dev, struct clk *clk);
# 293 "include/linux/clk.h"
long clk_round_rate(struct clk *clk, unsigned long rate);
# 302 "include/linux/clk.h"
int clk_set_rate(struct clk *clk, unsigned long rate);
# 311 "include/linux/clk.h"
int clk_set_parent(struct clk *clk, struct clk *parent);
# 320 "include/linux/clk.h"
struct clk *clk_get_parent(struct clk *clk);
# 337 "include/linux/clk.h"
struct clk *clk_get_sys(const char *dev_id, const char *con_id);
# 390 "include/linux/clk.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int clk_prepare_enable(struct clk *clk)
{
 int ret;

 ret = clk_prepare(clk);
 if (ret)
  return ret;
 ret = clk_enable(clk);
 if (ret)
  clk_unprepare(clk);

 return ret;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clk_disable_unprepare(struct clk *clk)
{
 clk_disable(clk);
 clk_unprepare(clk);
}
# 421 "include/linux/clk.h"
int clk_add_alias(const char *alias, const char *alias_dev_name, char *id,
   struct device *dev);

struct device_node;
struct of_phandle_args;






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct clk *of_clk_get(struct device_node *np, int index)
{
 return ERR_PTR(-2);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct clk *of_clk_get_by_name(struct device_node *np,
          const char *name)
{
 return ERR_PTR(-2);
}
# 20 "arch/mips/ath79/setup.c" 2

# 1 "./arch/mips/include/asm/bootinfo.h" 1
# 16 "./arch/mips/include/asm/bootinfo.h"
# 1 "./arch/mips/include/asm/setup.h" 1



# 1 "./arch/mips/include/uapi/asm/setup.h" 1
# 5 "./arch/mips/include/asm/setup.h" 2

extern void setup_early_printk(void);





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void setup_8250_early_printk_port(unsigned long base,
 unsigned int reg_shift, unsigned int timeout) {}


extern void set_handler(unsigned long offset, void *addr, unsigned long len);
extern void set_uncached_handler(unsigned long offset, void *addr, unsigned long len);

typedef void (*vi_handler_t)(void);
extern void *set_vi_handler(int n, vi_handler_t addr);

extern void *set_except_vector(int n, void *addr);
extern unsigned long ebase;
extern void per_cpu_trap_init(bool);
extern void cpu_cache_init(void);
# 17 "./arch/mips/include/asm/bootinfo.h" 2
# 64 "./arch/mips/include/asm/bootinfo.h"
enum loongson_machine_type {
 MACH_LOONGSON_UNKNOWN,
 MACH_LEMOTE_FL2E,
 MACH_LEMOTE_FL2F,
 MACH_LEMOTE_ML2F7,
 MACH_LEMOTE_YL2F89,
 MACH_DEXXON_GDIUM2F10,
 MACH_LEMOTE_NAS,
 MACH_LEMOTE_LL2F,
 MACH_LEMOTE_A1004,
 MACH_LEMOTE_A1101,
 MACH_LEMOTE_A1201,
 MACH_LEMOTE_A1205,
 MACH_LOONGSON_END
};







extern char *system_type;
const char *get_system_type(void);

extern unsigned long mips_machtype;
# 101 "./arch/mips/include/asm/bootinfo.h"
struct boot_mem_map {
 int nr_map;
 struct boot_mem_map_entry {
  phys_t addr;
  phys_t size;
  long type;
 } map[32];
};

extern struct boot_mem_map boot_mem_map;

extern void add_memory_region(phys_t start, phys_t size, long type);
extern void detect_memory_region(phys_t start, phys_t sz_min, phys_t sz_max);

extern void prom_init(void);
extern void prom_free_prom_memory(void);

extern void free_init_pages(const char *what,
       unsigned long begin, unsigned long end);

extern void (*free_init_pages_eva)(void *begin, void *end);




extern char arcs_cmdline[4096];




extern unsigned long fw_arg0, fw_arg1, fw_arg2, fw_arg3;




extern void plat_mem_setup(void);
# 146 "./arch/mips/include/asm/bootinfo.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void plat_swiotlb_setup(void) {}
# 22 "arch/mips/ath79/setup.c" 2
# 1 "./arch/mips/include/asm/idle.h" 1



# 1 "include/linux/cpuidle.h" 1
# 14 "include/linux/cpuidle.h"
# 1 "include/linux/percpu.h" 1



# 1 "include/linux/mmdebug.h" 1





struct page;
struct vm_area_struct;
struct mm_struct;

extern void dump_page(struct page *page, const char *reason);
extern void dump_page_badflags(struct page *page, const char *reason,
          unsigned long badflags);
void dump_vma(const struct vm_area_struct *vma);
void dump_mm(const struct mm_struct *mm);
# 5 "include/linux/percpu.h" 2






# 1 "arch/mips/include/generated/asm/percpu.h" 1
# 1 "include/asm-generic/percpu.h" 1





# 1 "include/linux/percpu-defs.h" 1
# 297 "include/linux/percpu-defs.h"
extern void __bad_size_call_parameter(void);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __this_cpu_preempt_check(const char *op) { }
# 7 "include/asm-generic/percpu.h" 2
# 1 "arch/mips/include/generated/asm/percpu.h" 2
# 12 "include/linux/percpu.h" 2
# 56 "include/linux/percpu.h"
extern void *pcpu_base_addr;
extern const unsigned long *pcpu_unit_offsets;

struct pcpu_group_info {
 int nr_units;
 unsigned long base_offset;
 unsigned int *cpu_map;

};

struct pcpu_alloc_info {
 size_t static_size;
 size_t reserved_size;
 size_t dyn_size;
 size_t unit_size;
 size_t atom_size;
 size_t alloc_size;
 size_t __ai_size;
 int nr_groups;
 struct pcpu_group_info groups[];
};

enum pcpu_fc {
 PCPU_FC_AUTO,
 PCPU_FC_EMBED,
 PCPU_FC_PAGE,

 PCPU_FC_NR,
};
extern const char * const pcpu_fc_names[PCPU_FC_NR];

extern enum pcpu_fc pcpu_chosen_fc;

typedef void * (*pcpu_fc_alloc_fn_t)(unsigned int cpu, size_t size,
         size_t align);
typedef void (*pcpu_fc_free_fn_t)(void *ptr, size_t size);
typedef void (*pcpu_fc_populate_pte_fn_t)(unsigned long addr);
typedef int (pcpu_fc_cpu_distance_fn_t)(unsigned int from, unsigned int to);

extern struct pcpu_alloc_info * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) pcpu_alloc_alloc_info(int nr_groups,
            int nr_units);
extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) pcpu_free_alloc_info(struct pcpu_alloc_info *ai);

extern int __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) pcpu_setup_first_chunk(const struct pcpu_alloc_info *ai,
      void *base_addr);
# 117 "include/linux/percpu.h"
extern void *__alloc_reserved_percpu(size_t size, size_t align);
extern bool is_kernel_percpu_address(unsigned long addr);


extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) setup_per_cpu_areas(void);

extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) percpu_init_late(void);

extern void *__alloc_percpu_gfp(size_t size, size_t align, gfp_t gfp);
extern void *__alloc_percpu(size_t size, size_t align);
extern void free_percpu(void *__pdata);
extern phys_addr_t per_cpu_ptr_to_phys(void *addr);
# 15 "include/linux/cpuidle.h" 2

# 1 "include/linux/hrtimer.h" 1
# 25 "include/linux/hrtimer.h"
# 1 "include/linux/timerqueue.h" 1







struct timerqueue_node {
 struct rb_node node;
 ktime_t expires;
};

struct timerqueue_head {
 struct rb_root head;
 struct timerqueue_node *next;
};


extern void timerqueue_add(struct timerqueue_head *head,
    struct timerqueue_node *node);
extern void timerqueue_del(struct timerqueue_head *head,
    struct timerqueue_node *node);
extern struct timerqueue_node *timerqueue_iterate_next(
      struct timerqueue_node *node);
# 34 "include/linux/timerqueue.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function))
struct timerqueue_node *timerqueue_getnext(struct timerqueue_head *head)
{
 return head->next;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void timerqueue_init(struct timerqueue_node *node)
{
 ((&node->node)->__rb_parent_color = (unsigned long)(&node->node));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void timerqueue_init_head(struct timerqueue_head *head)
{
 head->head = (struct rb_root) { ((void *)0), };
 head->next = ((void *)0);
}
# 26 "include/linux/hrtimer.h" 2

struct hrtimer_clock_base;
struct hrtimer_cpu_base;




enum hrtimer_mode {
 HRTIMER_MODE_ABS = 0x0,
 HRTIMER_MODE_REL = 0x1,
 HRTIMER_MODE_PINNED = 0x02,
 HRTIMER_MODE_ABS_PINNED = 0x02,
 HRTIMER_MODE_REL_PINNED = 0x03,
};




enum hrtimer_restart {
 HRTIMER_NORESTART,
 HRTIMER_RESTART,
};
# 108 "include/linux/hrtimer.h"
struct hrtimer {
 struct timerqueue_node node;
 ktime_t _softexpires;
 enum hrtimer_restart (*function)(struct hrtimer *);
 struct hrtimer_clock_base *base;
 unsigned long state;

 int start_pid;
 void *start_site;
 char start_comm[16];

};
# 128 "include/linux/hrtimer.h"
struct hrtimer_sleeper {
 struct hrtimer timer;
 struct task_struct *task;
};
# 145 "include/linux/hrtimer.h"
struct hrtimer_clock_base {
 struct hrtimer_cpu_base *cpu_base;
 int index;
 clockid_t clockid;
 struct timerqueue_head active;
 ktime_t resolution;
 ktime_t (*get_time)(void);
 ktime_t softirq_time;
 ktime_t offset;
};

enum hrtimer_base_type {
 HRTIMER_BASE_MONOTONIC,
 HRTIMER_BASE_REALTIME,
 HRTIMER_BASE_BOOTTIME,
 HRTIMER_BASE_TAI,
 HRTIMER_MAX_CLOCK_BASES,
};
# 181 "include/linux/hrtimer.h"
struct hrtimer_cpu_base {
 raw_spinlock_t lock;
 unsigned int cpu;
 unsigned int active_bases;
 unsigned int clock_was_set;

 ktime_t expires_next;
 int hres_active;
 int hang_detected;
 unsigned long nr_events;
 unsigned long nr_retries;
 unsigned long nr_hangs;
 ktime_t max_hang_time;

 struct hrtimer_clock_base clock_base[HRTIMER_MAX_CLOCK_BASES];
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_set_expires(struct hrtimer *timer, ktime_t time)
{
 timer->node.expires = time;
 timer->_softexpires = time;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_set_expires_range(struct hrtimer *timer, ktime_t time, ktime_t delta)
{
 timer->_softexpires = time;
 timer->node.expires = ktime_add_safe(time, delta);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_set_expires_range_ns(struct hrtimer *timer, ktime_t time, unsigned long delta)
{
 timer->_softexpires = time;
 timer->node.expires = ktime_add_safe(time, ns_to_ktime(delta));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_set_expires_tv64(struct hrtimer *timer, s64 tv64)
{
 timer->node.expires.tv64 = tv64;
 timer->_softexpires.tv64 = tv64;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_add_expires(struct hrtimer *timer, ktime_t time)
{
 timer->node.expires = ktime_add_safe(timer->node.expires, time);
 timer->_softexpires = ktime_add_safe(timer->_softexpires, time);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_add_expires_ns(struct hrtimer *timer, u64 ns)
{
 timer->node.expires = ({ (ktime_t){ .tv64 = (timer->node.expires).tv64 + (ns) }; });
 timer->_softexpires = ({ (ktime_t){ .tv64 = (timer->_softexpires).tv64 + (ns) }; });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t hrtimer_get_expires(const struct hrtimer *timer)
{
 return timer->node.expires;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t hrtimer_get_softexpires(const struct hrtimer *timer)
{
 return timer->_softexpires;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 hrtimer_get_expires_tv64(const struct hrtimer *timer)
{
 return timer->node.expires.tv64;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 hrtimer_get_softexpires_tv64(const struct hrtimer *timer)
{
 return timer->_softexpires.tv64;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 hrtimer_get_expires_ns(const struct hrtimer *timer)
{
 return ((timer->node.expires).tv64);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t hrtimer_expires_remaining(const struct hrtimer *timer)
{
 return ({ (ktime_t){ .tv64 = (timer->node.expires).tv64 - (timer->base->get_time()).tv64 }; });
}


struct clock_event_device;

extern void hrtimer_interrupt(struct clock_event_device *dev);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ktime_t hrtimer_cb_get_time(struct hrtimer *timer)
{
 return timer->base->get_time();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hrtimer_is_hres_active(struct hrtimer *timer)
{
 return timer->base->cpu_base->hres_active;
}

extern void hrtimer_peek_ahead_timers(void);
# 294 "include/linux/hrtimer.h"
extern void clock_was_set_delayed(void);
# 321 "include/linux/hrtimer.h"
extern void clock_was_set(void);

extern void timerfd_clock_was_set(void);



extern void hrtimers_resume(void);

extern __attribute__((section(".data" ""))) __typeof__(struct tick_device) tick_cpu_device;





extern void hrtimer_init(struct hrtimer *timer, clockid_t which_clock,
    enum hrtimer_mode mode);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hrtimer_init_on_stack(struct hrtimer *timer,
      clockid_t which_clock,
      enum hrtimer_mode mode)
{
 hrtimer_init(timer, which_clock, mode);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void destroy_hrtimer_on_stack(struct hrtimer *timer) { }



extern int hrtimer_start(struct hrtimer *timer, ktime_t tim,
    const enum hrtimer_mode mode);
extern int hrtimer_start_range_ns(struct hrtimer *timer, ktime_t tim,
   unsigned long range_ns, const enum hrtimer_mode mode);
extern int
__hrtimer_start_range_ns(struct hrtimer *timer, ktime_t tim,
    unsigned long delta_ns,
    const enum hrtimer_mode mode, int wakeup);

extern int hrtimer_cancel(struct hrtimer *timer);
extern int hrtimer_try_to_cancel(struct hrtimer *timer);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hrtimer_start_expires(struct hrtimer *timer,
      enum hrtimer_mode mode)
{
 unsigned long delta;
 ktime_t soft, hard;
 soft = hrtimer_get_softexpires(timer);
 hard = hrtimer_get_expires(timer);
 delta = ((({ (ktime_t){ .tv64 = (hard).tv64 - (soft).tv64 }; })).tv64);
 return hrtimer_start_range_ns(timer, soft, delta, mode);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hrtimer_restart(struct hrtimer *timer)
{
 return hrtimer_start_expires(timer, HRTIMER_MODE_ABS);
}


extern ktime_t hrtimer_get_remaining(const struct hrtimer *timer);
extern int hrtimer_get_res(const clockid_t which_clock, struct timespec *tp);

extern ktime_t hrtimer_get_next_event(void);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hrtimer_active(const struct hrtimer *timer)
{
 return timer->state != 0x00;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hrtimer_is_queued(struct hrtimer *timer)
{
 return timer->state & 0x01;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hrtimer_callback_running(struct hrtimer *timer)
{
 return timer->state & 0x02;
}


extern u64
hrtimer_forward(struct hrtimer *timer, ktime_t now, ktime_t interval);


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 hrtimer_forward_now(struct hrtimer *timer,
          ktime_t interval)
{
 return hrtimer_forward(timer, timer->base->get_time(), interval);
}


extern long hrtimer_nanosleep(struct timespec *rqtp,
         struct timespec *rmtp,
         const enum hrtimer_mode mode,
         const clockid_t clockid);
extern long hrtimer_nanosleep_restart(struct restart_block *restart_block);

extern void hrtimer_init_sleeper(struct hrtimer_sleeper *sl,
     struct task_struct *tsk);

extern int schedule_hrtimeout_range(ktime_t *expires, unsigned long delta,
      const enum hrtimer_mode mode);
extern int schedule_hrtimeout_range_clock(ktime_t *expires,
  unsigned long delta, const enum hrtimer_mode mode, int clock);
extern int schedule_hrtimeout(ktime_t *expires, const enum hrtimer_mode mode);


extern void hrtimer_run_queues(void);
extern void hrtimer_run_pending(void);


extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) hrtimers_init(void);


extern void sysrq_timer_list_show(void);
# 17 "include/linux/cpuidle.h" 2





struct module;

struct cpuidle_device;
struct cpuidle_driver;






struct cpuidle_state_usage {
 unsigned long long disable;
 unsigned long long usage;
 unsigned long long time;
};

struct cpuidle_state {
 char name[16];
 char desc[32];

 unsigned int flags;
 unsigned int exit_latency;
 int power_usage;
 unsigned int target_residency;
 bool disabled;

 int (*enter) (struct cpuidle_device *dev,
   struct cpuidle_driver *drv,
   int index);

 int (*enter_dead) (struct cpuidle_device *dev, int index);
};
# 62 "include/linux/cpuidle.h"
struct cpuidle_device_kobj;
struct cpuidle_state_kobj;
struct cpuidle_driver_kobj;

struct cpuidle_device {
 unsigned int registered:1;
 unsigned int enabled:1;
 unsigned int cpu;

 int last_residency;
 struct cpuidle_state_usage states_usage[10];
 struct cpuidle_state_kobj *kobjs[10];
 struct cpuidle_driver_kobj *kobj_driver;
 struct cpuidle_device_kobj *kobj_dev;
 struct list_head device_list;






};

extern __attribute__((section(".data" ""))) __typeof__(struct cpuidle_device *) cpuidle_devices;
extern __attribute__((section(".data" ""))) __typeof__(struct cpuidle_device) cpuidle_dev;







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_get_last_residency(struct cpuidle_device *dev)
{
 return dev->last_residency;
}






struct cpuidle_driver {
 const char *name;
 struct module *owner;
 int refcnt;


 unsigned int bctimer:1;

 struct cpuidle_state states[10];
 int state_count;
 int safe_state_index;


 struct cpumask *cpumask;
};
# 150 "include/linux/cpuidle.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void disable_cpuidle(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_select(struct cpuidle_driver *drv,
     struct cpuidle_device *dev)
{return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_enter(struct cpuidle_driver *drv,
    struct cpuidle_device *dev, int index)
{return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_reflect(struct cpuidle_device *dev, int index) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_register_driver(struct cpuidle_driver *drv)
{return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct cpuidle_driver *cpuidle_get_driver(void) {return ((void *)0); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct cpuidle_driver *cpuidle_driver_ref(void) {return ((void *)0); }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_driver_unref(void) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_unregister_driver(struct cpuidle_driver *drv) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_register_device(struct cpuidle_device *dev)
{return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_unregister_device(struct cpuidle_device *dev) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_register(struct cpuidle_driver *drv,
       const struct cpumask *const coupled_cpus)
{return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_unregister(struct cpuidle_driver *drv) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_pause_and_lock(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_resume_and_unlock(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_pause(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_resume(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_enable_device(struct cpuidle_device *dev)
{return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_disable_device(struct cpuidle_device *dev) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_play_dead(void) {return -19; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_use_deepest_state(bool enable) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct cpuidle_driver *cpuidle_get_cpu_driver(
 struct cpuidle_device *dev) {return ((void *)0); }





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void cpuidle_coupled_parallel_barrier(struct cpuidle_device *dev, atomic_t *a)
{
}






struct cpuidle_governor {
 char name[16];
 struct list_head governor_list;
 unsigned int rating;

 int (*enable) (struct cpuidle_driver *drv,
     struct cpuidle_device *dev);
 void (*disable) (struct cpuidle_driver *drv,
     struct cpuidle_device *dev);

 int (*select) (struct cpuidle_driver *drv,
     struct cpuidle_device *dev);
 void (*reflect) (struct cpuidle_device *dev, int index);

 struct module *owner;
};




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cpuidle_register_governor(struct cpuidle_governor *gov)
{return 0;}
# 5 "./arch/mips/include/asm/idle.h" 2


extern void (*cpu_wait)(void);
extern void r4k_wait(void);
extern void __r4k_wait(void);
extern void r4k_wait_irqoff(void);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int using_rollback_handler(void)
{
 return cpu_wait == r4k_wait;
}

extern int mips_cpuidle_wait_enter(struct cpuidle_device *dev,
       struct cpuidle_driver *drv, int index);
# 23 "arch/mips/ath79/setup.c" 2
# 1 "./arch/mips/include/asm/time.h" 1
# 17 "./arch/mips/include/asm/time.h"
# 1 "include/linux/rtc.h" 1
# 16 "include/linux/rtc.h"
# 1 "include/linux/interrupt.h" 1
# 10 "include/linux/interrupt.h"
# 1 "include/linux/irqreturn.h" 1
# 10 "include/linux/irqreturn.h"
enum irqreturn {
 IRQ_NONE = (0 << 0),
 IRQ_HANDLED = (1 << 0),
 IRQ_WAKE_THREAD = (1 << 1),
};

typedef enum irqreturn irqreturn_t;
# 11 "include/linux/interrupt.h" 2
# 1 "include/linux/irqnr.h" 1



# 1 "include/uapi/linux/irqnr.h" 1
# 5 "include/linux/irqnr.h" 2


extern int nr_irqs;
extern struct irq_desc *irq_to_desc(unsigned int irq);
unsigned int irq_get_next_irq(unsigned int offset);
# 12 "include/linux/interrupt.h" 2
# 1 "include/linux/hardirq.h" 1





# 1 "include/linux/ftrace_irq.h" 1
# 9 "include/linux/ftrace_irq.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ftrace_nmi_enter(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ftrace_nmi_exit(void) { }
# 7 "include/linux/hardirq.h" 2
# 1 "include/linux/vtime.h" 1



# 1 "include/linux/context_tracking_state.h" 1




# 1 "include/linux/static_key.h" 1
# 1 "include/linux/jump_label.h" 1
# 52 "include/linux/jump_label.h"
extern bool static_key_initialized;
# 72 "include/linux/jump_label.h"
struct static_key {
 atomic_t enabled;
};


enum jump_label_type {
 JUMP_LABEL_DISABLE = 0,
 JUMP_LABEL_ENABLE,
};

struct module;



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int static_key_count(struct static_key *key)
{
 return (*(volatile typeof((&key->enabled)->counter) *)&((&key->enabled)->counter));
}
# 146 "include/linux/jump_label.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void jump_label_init(void)
{
 static_key_initialized = true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) bool static_key_false(struct static_key *key)
{
 if (__builtin_expect(!!(static_key_count(key) > 0), 0))
  return true;
 return false;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) bool static_key_true(struct static_key *key)
{
 if (__builtin_expect(!!(static_key_count(key) > 0), 1))
  return true;
 return false;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void static_key_slow_inc(struct static_key *key)
{
 ({ int __ret_warn_on = !!(!static_key_initialized); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_fmt("include/linux/jump_label.h", 167, "%s used before call to jump_label_init", __func__); __builtin_expect(!!(__ret_warn_on), 0); });
 atomic_add(1, (&key->enabled));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void static_key_slow_dec(struct static_key *key)
{
 ({ int __ret_warn_on = !!(!static_key_initialized); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_fmt("include/linux/jump_label.h", 173, "%s used before call to jump_label_init", __func__); __builtin_expect(!!(__ret_warn_on), 0); });
 atomic_sub(1, (&key->enabled));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int jump_label_text_reserved(void *start, void *end)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void jump_label_lock(void) {}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void jump_label_unlock(void) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int jump_label_apply_nops(struct module *mod)
{
 return 0;
}
# 200 "include/linux/jump_label.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool static_key_enabled(struct static_key *key)
{
 return static_key_count(key) > 0;
}
# 1 "include/linux/static_key.h" 2
# 6 "include/linux/context_tracking_state.h" 2

struct context_tracking {






 bool active;
 enum ctx_state {
  IN_KERNEL = 0,
  IN_USER,
 } state;
};
# 40 "include/linux/context_tracking_state.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool context_tracking_in_user(void) { return false; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool context_tracking_active(void) { return false; }
# 5 "include/linux/vtime.h" 2





struct task_struct;
# 32 "include/linux/vtime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool vtime_accounting_enabled(void) { return false; }
# 69 "include/linux/vtime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_task_switch(struct task_struct *prev) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_account_system(struct task_struct *tsk) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_account_user(struct task_struct *tsk) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_account_irq_enter(struct task_struct *tsk) { }
# 95 "include/linux/vtime.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_account_irq_exit(struct task_struct *tsk)
{

 vtime_account_system(tsk);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_user_enter(struct task_struct *tsk) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_user_exit(struct task_struct *tsk) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_guest_enter(struct task_struct *tsk) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_guest_exit(struct task_struct *tsk) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void vtime_init_idle(struct task_struct *tsk, int cpu) { }





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irqtime_account_irq(struct task_struct *tsk) { }


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void account_irq_enter_time(struct task_struct *tsk)
{
 vtime_account_irq_enter(tsk);
 irqtime_account_irq(tsk);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void account_irq_exit_time(struct task_struct *tsk)
{
 vtime_account_irq_exit(tsk);
 irqtime_account_irq(tsk);
}
# 8 "include/linux/hardirq.h" 2
# 1 "./arch/mips/include/asm/hardirq.h" 1
# 13 "./arch/mips/include/asm/hardirq.h"
extern void ack_bad_irq(unsigned int irq);


# 1 "include/asm-generic/hardirq.h" 1






typedef struct {
 unsigned int __softirq_pending;
} __attribute__((__aligned__((1 << 5)))) irq_cpustat_t;

# 1 "include/linux/irq_cpustat.h" 1
# 20 "include/linux/irq_cpustat.h"
extern irq_cpustat_t irq_stat[];
# 12 "include/asm-generic/hardirq.h" 2
# 1 "include/linux/irq.h" 1
# 17 "include/linux/irq.h"
# 1 "include/linux/gfp.h" 1







# 1 "include/linux/topology.h" 1
# 35 "include/linux/topology.h"
# 1 "./arch/mips/include/asm/topology.h" 1
# 11 "./arch/mips/include/asm/topology.h"
# 1 "./arch/mips/include/asm/mach-generic/topology.h" 1
# 1 "include/asm-generic/topology.h" 1
# 1 "./arch/mips/include/asm/mach-generic/topology.h" 2
# 12 "./arch/mips/include/asm/topology.h" 2
# 36 "include/linux/topology.h" 2
# 49 "include/linux/topology.h"
int arch_update_cpu_topology(void);
# 106 "include/linux/topology.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int numa_node_id(void)
{
 return ((void)(0),0);
}
# 166 "include/linux/topology.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int numa_mem_id(void)
{
 return numa_node_id();
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int node_to_mem_node(int node)
{
 return node;
}
# 208 "include/linux/topology.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) const struct cpumask *cpu_cpu_mask(int cpu)
{
 return ((void)((void)(cpu),0), cpu_online_mask);
}
# 9 "include/linux/gfp.h" 2

struct vm_area_struct;
# 159 "include/linux/gfp.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int gfpflags_to_migratetype(const gfp_t gfp_flags)
{
 ({ int __ret_warn_on = !!((gfp_flags & ((( gfp_t)0x80000u)|(( gfp_t)0x08u))) == ((( gfp_t)0x80000u)|(( gfp_t)0x08u))); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/gfp.h", 161); __builtin_expect(!!(__ret_warn_on), 0); });

 if (__builtin_expect(!!(page_group_by_mobility_disabled), 0))
  return MIGRATE_UNMOVABLE;


 return (((gfp_flags & (( gfp_t)0x08u)) != 0) << 1) |
  ((gfp_flags & (( gfp_t)0x80000u)) != 0);
}
# 254 "include/linux/gfp.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) enum zone_type gfp_zone(gfp_t flags)
{
 enum zone_type z;
 int bit = ( int) (flags & ((( gfp_t)0x01u)|(( gfp_t)0x02u)|(( gfp_t)0x04u)|(( gfp_t)0x08u)));

 z = (( (ZONE_NORMAL << 0 * 1) | (ZONE_NORMAL << 0x01u * 1) | (ZONE_NORMAL << 0x02u * 1) | (ZONE_NORMAL << 0x04u * 1) | (ZONE_NORMAL << 0x08u * 1) | (ZONE_NORMAL << (0x08u | 0x01u) * 1) | (ZONE_MOVABLE << (0x08u | 0x02u) * 1) | (ZONE_NORMAL << (0x08u | 0x04u) * 1) ) >> (bit * 1)) &
      ((1 << 1) - 1);
 ((void)(sizeof(( long)((( 1 << (0x01u | 0x02u) | 1 << (0x01u | 0x04u) | 1 << (0x04u | 0x02u) | 1 << (0x01u | 0x04u | 0x02u) | 1 << (0x08u | 0x02u | 0x01u) | 1 << (0x08u | 0x04u | 0x01u) | 1 << (0x08u | 0x04u | 0x02u) | 1 << (0x08u | 0x04u | 0x01u | 0x02u) ) >> bit) & 1))));
 return z;
}
# 272 "include/linux/gfp.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int gfp_zonelist(gfp_t flags)
{
 if ((0 || 0) && __builtin_expect(!!(flags & (( gfp_t)0x40000u)), 0))
  return 1;

 return 0;
}
# 289 "include/linux/gfp.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct zonelist *node_zonelist(int nid, gfp_t flags)
{
 return (&contig_page_data)->node_zonelists + gfp_zonelist(flags);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void arch_free_page(struct page *page, int order) { }


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void arch_alloc_page(struct page *page, int order) { }


struct page *
__alloc_pages_nodemask(gfp_t gfp_mask, unsigned int order,
         struct zonelist *zonelist, nodemask_t *nodemask);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct page *
__alloc_pages(gfp_t gfp_mask, unsigned int order,
  struct zonelist *zonelist)
{
 return __alloc_pages_nodemask(gfp_mask, order, zonelist, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct page *alloc_pages_node(int nid, gfp_t gfp_mask,
      unsigned int order)
{

 if (nid < 0)
  nid = numa_node_id();

 return __alloc_pages(gfp_mask, order, node_zonelist(nid, gfp_mask));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct page *alloc_pages_exact_node(int nid, gfp_t gfp_mask,
      unsigned int order)
{
 ((void)(sizeof(( long)(nid < 0 || nid >= (1 << 0) || !node_state((nid), N_ONLINE)))));

 return __alloc_pages(gfp_mask, order, node_zonelist(nid, gfp_mask));
}
# 353 "include/linux/gfp.h"
extern struct page *alloc_kmem_pages(gfp_t gfp_mask, unsigned int order);
extern struct page *alloc_kmem_pages_node(int nid, gfp_t gfp_mask,
       unsigned int order);

extern unsigned long __get_free_pages(gfp_t gfp_mask, unsigned int order);
extern unsigned long get_zeroed_page(gfp_t gfp_mask);

void *alloc_pages_exact(size_t size, gfp_t gfp_mask);
void free_pages_exact(void *virt, size_t size);

void * __attribute__ ((__section__(".meminit.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) alloc_pages_exact_nid(int nid, size_t size, gfp_t gfp_mask);







extern void __free_pages(struct page *page, unsigned int order);
extern void free_pages(unsigned long addr, unsigned int order);
extern void free_hot_cold_page(struct page *page, bool cold);
extern void free_hot_cold_page_list(struct list_head *list, bool cold);

extern void __free_kmem_pages(struct page *page, unsigned int order);
extern void free_kmem_pages(unsigned long addr, unsigned int order);




void page_alloc_init(void);
void drain_zone_pages(struct zone *zone, struct per_cpu_pages *pcp);
void drain_all_pages(void);
void drain_local_pages(void *dummy);
# 394 "include/linux/gfp.h"
extern gfp_t gfp_allowed_mask;


bool gfp_pfmemalloc_allowed(gfp_t gfp_mask);

extern void pm_restrict_gfp_mask(void);
extern void pm_restore_gfp_mask(void);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool pm_suspended_storage(void)
{
 return false;
}
# 18 "include/linux/irq.h" 2






# 1 "./arch/mips/include/asm/irq.h" 1
# 14 "./arch/mips/include/asm/irq.h"
# 1 "include/linux/irqdomain.h" 1
# 36 "include/linux/irqdomain.h"
# 1 "include/linux/radix-tree.h" 1
# 54 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int radix_tree_is_indirect_ptr(void *ptr)
{
 return (int)((unsigned long)ptr & 1);
}
# 87 "include/linux/radix-tree.h"
struct radix_tree_node {
 unsigned int path;
 unsigned int count;
 union {
  struct {

   struct radix_tree_node *parent;

   void *private_data;
  };

  struct callback_head callback_head;
 };

 struct list_head private_list;
 void *slots[(1UL << (0 ? 4 : 6))];
 unsigned long tags[3][(((1UL << (0 ? 4 : 6)) + 32 - 1) / 32)];
};


struct radix_tree_root {
 unsigned int height;
 gfp_t gfp_mask;
 struct radix_tree_node *rnode;
};
# 194 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *radix_tree_deref_slot(void **pslot)
{
 return ({ typeof(*(*pslot)) *_________p1 = (typeof(*(*pslot)) *)(*(volatile typeof((*pslot)) *)&((*pslot))); do { } while (0); ; do { } while(0); ((typeof(*(*pslot)) *)(_________p1)); });
}
# 209 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *radix_tree_deref_slot_protected(void **pslot,
       spinlock_t *treelock)
{
 return ({ do { } while (0); ; ((typeof(*(*pslot)) *)((*pslot))); });
}
# 222 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int radix_tree_deref_retry(void *arg)
{
 return __builtin_expect(!!((unsigned long)arg & 1), 0);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int radix_tree_exceptional_entry(void *arg)
{

 return (unsigned long)arg & 2;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int radix_tree_exception(void *arg)
{
 return __builtin_expect(!!((unsigned long)arg & (1 | 2)), 0)
                                                           ;
}
# 257 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void radix_tree_replace_slot(void **pslot, void *item)
{
 __BUG_ON((unsigned long)(radix_tree_is_indirect_ptr(item)));
 do { do { bool __cond = !((sizeof(*&*pslot) == sizeof(int) || sizeof(*&*pslot) == sizeof(long))); extern void __compiletime_assert_260(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_260(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&*pslot) *)&(*&*pslot)) = ((typeof(*(item)) *)(item)); } while (0);
}

int __radix_tree_create(struct radix_tree_root *root, unsigned long index,
   struct radix_tree_node **nodep, void ***slotp);
int radix_tree_insert(struct radix_tree_root *, unsigned long, void *);
void *__radix_tree_lookup(struct radix_tree_root *root, unsigned long index,
     struct radix_tree_node **nodep, void ***slotp);
void *radix_tree_lookup(struct radix_tree_root *, unsigned long);
void **radix_tree_lookup_slot(struct radix_tree_root *, unsigned long);
bool __radix_tree_delete_node(struct radix_tree_root *root,
         struct radix_tree_node *node);
void *radix_tree_delete_item(struct radix_tree_root *, unsigned long, void *);
void *radix_tree_delete(struct radix_tree_root *, unsigned long);
unsigned int
radix_tree_gang_lookup(struct radix_tree_root *root, void **results,
   unsigned long first_index, unsigned int max_items);
unsigned int radix_tree_gang_lookup_slot(struct radix_tree_root *root,
   void ***results, unsigned long *indices,
   unsigned long first_index, unsigned int max_items);
int radix_tree_preload(gfp_t gfp_mask);
int radix_tree_maybe_preload(gfp_t gfp_mask);
void radix_tree_init(void);
void *radix_tree_tag_set(struct radix_tree_root *root,
   unsigned long index, unsigned int tag);
void *radix_tree_tag_clear(struct radix_tree_root *root,
   unsigned long index, unsigned int tag);
int radix_tree_tag_get(struct radix_tree_root *root,
   unsigned long index, unsigned int tag);
unsigned int
radix_tree_gang_lookup_tag(struct radix_tree_root *root, void **results,
  unsigned long first_index, unsigned int max_items,
  unsigned int tag);
unsigned int
radix_tree_gang_lookup_tag_slot(struct radix_tree_root *root, void ***results,
  unsigned long first_index, unsigned int max_items,
  unsigned int tag);
unsigned long radix_tree_range_tag_if_tagged(struct radix_tree_root *root,
  unsigned long *first_indexp, unsigned long last_index,
  unsigned long nr_to_tag,
  unsigned int fromtag, unsigned int totag);
int radix_tree_tagged(struct radix_tree_root *root, unsigned int tag);
unsigned long radix_tree_locate_item(struct radix_tree_root *root, void *item);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void radix_tree_preload_end(void)
{
 __asm__ __volatile__("": : :"memory");
}
# 323 "include/linux/radix-tree.h"
struct radix_tree_iter {
 unsigned long index;
 unsigned long next_index;
 unsigned long tags;
};
# 340 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void **
radix_tree_iter_init(struct radix_tree_iter *iter, unsigned long start)
{
# 351 "include/linux/radix-tree.h"
 iter->index = 0;
 iter->next_index = start;
 return ((void *)0);
}
# 369 "include/linux/radix-tree.h"
void **radix_tree_next_chunk(struct radix_tree_root *root,
        struct radix_tree_iter *iter, unsigned flags);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) unsigned
radix_tree_chunk_size(struct radix_tree_iter *iter)
{
 return iter->next_index - iter->index;
}
# 395 "include/linux/radix-tree.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((always_inline)) void **
radix_tree_next_slot(void **slot, struct radix_tree_iter *iter, unsigned flags)
{
 if (flags & 0x0100) {
  iter->tags >>= 1;
  if (__builtin_expect(!!(iter->tags & 1ul), 1)) {
   iter->index++;
   return slot + 1;
  }
  if (!(flags & 0x0200) && __builtin_expect(!!(iter->tags), 1)) {
   unsigned offset = __ffs(iter->tags);

   iter->tags >>= offset;
   iter->index += offset + 1;
   return slot + offset + 1;
  }
 } else {
  unsigned size = radix_tree_chunk_size(iter) - 1;

  while (size--) {
   slot++;
   iter->index++;
   if (__builtin_expect(!!(*slot), 1))
    return slot;
   if (flags & 0x0200) {

    iter->next_index = 0;
    break;
   }
  }
 }
 return ((void *)0);
}
# 37 "include/linux/irqdomain.h" 2

struct device_node;
struct irq_domain;
struct of_device_id;
# 60 "include/linux/irqdomain.h"
struct irq_domain_ops {
 int (*match)(struct irq_domain *d, struct device_node *node);
 int (*map)(struct irq_domain *d, unsigned int virq, irq_hw_number_t hw);
 void (*unmap)(struct irq_domain *d, unsigned int virq);
 int (*xlate)(struct irq_domain *d, struct device_node *node,
       const u32 *intspec, unsigned int intsize,
       unsigned long *out_hwirq, unsigned int *out_type);
};

extern struct irq_domain_ops irq_generic_chip_ops;

struct irq_domain_chip_generic;
# 95 "include/linux/irqdomain.h"
struct irq_domain {
 struct list_head link;
 const char *name;
 const struct irq_domain_ops *ops;
 void *host_data;


 struct device_node *of_node;
 struct irq_domain_chip_generic *gc;


 irq_hw_number_t hwirq_max;
 unsigned int revmap_direct_max_irq;
 unsigned int revmap_size;
 struct radix_tree_root revmap_tree;
 unsigned int linear_revmap[];
};


struct irq_domain *__irq_domain_add(struct device_node *of_node, int size,
        irq_hw_number_t hwirq_max, int direct_max,
        const struct irq_domain_ops *ops,
        void *host_data);
struct irq_domain *irq_domain_add_simple(struct device_node *of_node,
      unsigned int size,
      unsigned int first_irq,
      const struct irq_domain_ops *ops,
      void *host_data);
struct irq_domain *irq_domain_add_legacy(struct device_node *of_node,
      unsigned int size,
      unsigned int first_irq,
      irq_hw_number_t first_hwirq,
      const struct irq_domain_ops *ops,
      void *host_data);
extern struct irq_domain *irq_find_host(struct device_node *node);
extern void irq_set_default_host(struct irq_domain *host);
# 139 "include/linux/irqdomain.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_domain *irq_domain_add_linear(struct device_node *of_node,
      unsigned int size,
      const struct irq_domain_ops *ops,
      void *host_data)
{
 return __irq_domain_add(of_node, size, size, 0, ops, host_data);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_domain *irq_domain_add_nomap(struct device_node *of_node,
      unsigned int max_irq,
      const struct irq_domain_ops *ops,
      void *host_data)
{
 return __irq_domain_add(of_node, 0, max_irq, max_irq, ops, host_data);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_domain *irq_domain_add_legacy_isa(
    struct device_node *of_node,
    const struct irq_domain_ops *ops,
    void *host_data)
{
 return irq_domain_add_legacy(of_node, 16, 0, 0, ops,
         host_data);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_domain *irq_domain_add_tree(struct device_node *of_node,
      const struct irq_domain_ops *ops,
      void *host_data)
{
 return __irq_domain_add(of_node, 0, ~0, 0, ops, host_data);
}

extern void irq_domain_remove(struct irq_domain *host);

extern int irq_domain_associate(struct irq_domain *domain, unsigned int irq,
     irq_hw_number_t hwirq);
extern void irq_domain_associate_many(struct irq_domain *domain,
          unsigned int irq_base,
          irq_hw_number_t hwirq_base, int count);
extern void irq_domain_disassociate(struct irq_domain *domain,
        unsigned int irq);

extern unsigned int irq_create_mapping(struct irq_domain *host,
           irq_hw_number_t hwirq);
extern void irq_dispose_mapping(unsigned int virq);
# 192 "include/linux/irqdomain.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int irq_linear_revmap(struct irq_domain *domain,
          irq_hw_number_t hwirq)
{
 return hwirq < domain->revmap_size ? domain->linear_revmap[hwirq] : 0;
}
extern unsigned int irq_find_mapping(struct irq_domain *host,
         irq_hw_number_t hwirq);
extern unsigned int irq_create_direct_mapping(struct irq_domain *host);
extern int irq_create_strict_mappings(struct irq_domain *domain,
          unsigned int irq_base,
          irq_hw_number_t hwirq_base, int count);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_create_identity_mapping(struct irq_domain *host,
           irq_hw_number_t hwirq)
{
 return irq_create_strict_mappings(host, hwirq, hwirq, 1);
}

extern const struct irq_domain_ops irq_domain_simple_ops;


int irq_domain_xlate_onecell(struct irq_domain *d, struct device_node *ctrlr,
   const u32 *intspec, unsigned int intsize,
   irq_hw_number_t *out_hwirq, unsigned int *out_type);
int irq_domain_xlate_twocell(struct irq_domain *d, struct device_node *ctrlr,
   const u32 *intspec, unsigned int intsize,
   irq_hw_number_t *out_hwirq, unsigned int *out_type);
int irq_domain_xlate_onetwocell(struct irq_domain *d, struct device_node *ctrlr,
   const u32 *intspec, unsigned int intsize,
   irq_hw_number_t *out_hwirq, unsigned int *out_type);
# 15 "./arch/mips/include/asm/irq.h" 2

# 1 "./arch/mips/include/asm/mipsmtregs.h" 1
# 181 "./arch/mips/include/asm/mipsmtregs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned core_nvpes(void)
{
 unsigned conf0;

 if (!0)
  return 1;

 conf0 = ({ int __res; if (2 == 0) __asm__ __volatile__( "mfc0\t%0, " "$0" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$0" ", " "2" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; });
 return ((conf0 & ( (unsigned long)(0xf) << 10)) >> 10) + 1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int dvpe(void)
{
 int res = 0;

 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	noreorder					\n"
 "	.set	noat						\n"
 "	.set	mips32r2					\n"
 "	.word	0x41610001		# dvpe $1		\n"
 "	move	%0, $1						\n"
 "	ehb							\n"
 "	.set	pop						\n"
 : "=r" (res));

 do { unsigned long tmp; __asm__ __volatile__( "	.set	mips64r2				\n" "	dla	%0, 1f					\n" "	jr.hb	%0					\n" "	.set	mips0					\n" "1:							\n" : "=r" (tmp)); } while (0);

 return res;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __raw_evpe(void)
{
 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	noreorder					\n"
 "	.set	noat						\n"
 "	.set	mips32r2					\n"
 "	.word	0x41600021		# evpe			\n"
 "	ehb							\n"
 "	.set	pop						\n");
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void evpe(int previous)
{
 if ((previous & ((unsigned long)(1))))
  __raw_evpe();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int dmt(void)
{
 int res;

 __asm__ __volatile__(
 "	.set	push						\n"
 "	.set	mips32r2					\n"
 "	.set	noat						\n"
 "	.word	0x41610BC1			# dmt $1	\n"
 "	ehb							\n"
 "	move	%0, $1						\n"
 "	.set	pop						\n"
 : "=r" (res));

 do { unsigned long tmp; __asm__ __volatile__( "	.set	mips64r2				\n" "	dla	%0, 1f					\n" "	jr.hb	%0					\n" "	.set	mips0					\n" "1:							\n" : "=r" (tmp)); } while (0);

 return res;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __raw_emt(void)
{
 __asm__ __volatile__(
 "	.set	noreorder					\n"
 "	.set	mips32r2					\n"
 "	.word	0x41600be1			# emt		\n"
 "	ehb							\n"
 "	.set	mips0						\n"
 "	.set	reorder");
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void emt(int previous)
{
 if ((previous & ((unsigned long)(1) << 15)))
  __raw_emt();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ehb(void)
{
 __asm__ __volatile__(
 "	.set	mips32r2				\n"
 "	ehb						\n"
 "	.set	mips0					\n");
}
# 417 "./arch/mips/include/asm/mipsmtregs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int set_c0_mvpcontrol(unsigned int set) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$0" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$0" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res | set; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$0" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$0" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int clear_c0_mvpcontrol(unsigned int clear) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$0" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$0" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~clear; do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$0" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$0" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; } static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int change_c0_mvpcontrol(unsigned int change, unsigned int val) { unsigned int res, new; res = ({ int __res; if (1 == 0) __asm__ __volatile__( "mfc0\t%0, " "$0" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$0" ", " "1" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }); new = res & ~change; new |= (val & change); do { if (1 == 0) __asm__ __volatile__( "mtc0\t%z0, " "$0" "\n\t" : : "Jr" ((unsigned int)(new))); else __asm__ __volatile__( ".set\tmips32\n\t" "mtc0\t%z0, " "$0" ", " "1" "\n\t" ".set\tmips0" : : "Jr" ((unsigned int)(new))); } while (0); return res; }
# 17 "./arch/mips/include/asm/irq.h" 2

# 1 "./arch/mips/include/asm/mach-ath79/irq.h" 1
# 33 "./arch/mips/include/asm/mach-ath79/irq.h"
# 1 "./arch/mips/include/asm/mach-generic/irq.h" 1
# 34 "./arch/mips/include/asm/mach-ath79/irq.h" 2
# 19 "./arch/mips/include/asm/irq.h" 2
# 29 "./arch/mips/include/asm/irq.h"
 void plat_irq_dispatch(void);

extern void do_IRQ(unsigned int irq);

extern void arch_init_irq(void);
extern void spurious_interrupt(void);

extern int allocate_irqno(void);
extern void alloc_legacy_irqno(void);
extern void free_irqno(unsigned int irq);
# 47 "./arch/mips/include/asm/irq.h"
extern int cp0_compare_irq;
extern int cp0_compare_irq_shift;
extern int cp0_perfcount_irq;
# 25 "include/linux/irq.h" 2
# 1 "./arch/mips/include/asm/ptrace.h" 1
# 16 "./arch/mips/include/asm/ptrace.h"
# 1 "./arch/mips/include/asm/isadep.h" 1
# 17 "./arch/mips/include/asm/ptrace.h" 2
# 1 "./arch/mips/include/uapi/asm/ptrace.h" 1
# 33 "./arch/mips/include/uapi/asm/ptrace.h"
struct user_pt_regs {




 __u64 regs[32];


 __u64 lo;
 __u64 hi;
 __u64 cp0_epc;
 __u64 cp0_badvaddr;
 __u64 cp0_status;
 __u64 cp0_cause;
} __attribute__ ((aligned (8)));
# 70 "./arch/mips/include/uapi/asm/ptrace.h"
enum pt_watch_style {
 pt_watch_style_mips32,
 pt_watch_style_mips64
};
struct mips32_watch_regs {
 unsigned int watchlo[8];

 unsigned short watchhi[8];






 unsigned short watch_masks[8];

 unsigned int num_valid;
} __attribute__((aligned(8)));

struct mips64_watch_regs {
 unsigned long long watchlo[8];
 unsigned short watchhi[8];
 unsigned short watch_masks[8];
 unsigned int num_valid;
} __attribute__((aligned(8)));

struct pt_watch_regs {
 enum pt_watch_style style;
 union {
  struct mips32_watch_regs mips32;
  struct mips64_watch_regs mips64;
 };
};
# 18 "./arch/mips/include/asm/ptrace.h" 2





struct pt_regs {


 unsigned long pad0[8];



 unsigned long regs[32];


 unsigned long cp0_status;
 unsigned long hi;
 unsigned long lo;



 unsigned long cp0_badvaddr;
 unsigned long cp0_cause;
 unsigned long cp0_epc;




} __attribute__((aligned(8)));

struct task_struct;

extern int ptrace_getregs(struct task_struct *child,
 struct user_pt_regs *data);
extern int ptrace_setregs(struct task_struct *child,
 struct user_pt_regs *data);

extern int ptrace_getfpregs(struct task_struct *child, __u32 *data);
extern int ptrace_setfpregs(struct task_struct *child, __u32 *data);

extern int ptrace_get_watch_regs(struct task_struct *child,
 struct pt_watch_regs *addr);
extern int ptrace_set_watch_regs(struct task_struct *child,
 struct pt_watch_regs *addr);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_syscall_success(struct pt_regs *regs)
{
 return !regs->regs[7];
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long regs_return_value(struct pt_regs *regs)
{
 if (is_syscall_success(regs))
  return regs->regs[2];
 else
  return -regs->regs[2];
}




extern long syscall_trace_enter(struct pt_regs *regs, long syscall);
extern void syscall_trace_leave(struct pt_regs *regs);

extern void die(const char *, struct pt_regs *) __attribute__((noreturn));

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void die_if_kernel(const char *str, struct pt_regs *regs)
{
 if (__builtin_expect(!!(!(((regs)->cp0_status & 0x18) == 0x10)), 0))
  die(str, regs);
}
# 103 "./arch/mips/include/asm/ptrace.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long user_stack_pointer(struct pt_regs *regs)
{
 return regs->regs[29];
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void user_stack_pointer_set(struct pt_regs *regs,
 unsigned long val)
{
 regs->regs[29] = val;
}
# 26 "include/linux/irq.h" 2
# 1 "./arch/mips/include/asm/irq_regs.h" 1
# 16 "./arch/mips/include/asm/irq_regs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct pt_regs *get_irq_regs(void)
{
 return current_thread_info()->regs;
}
# 27 "include/linux/irq.h" 2

struct seq_file;
struct module;
struct irq_desc;
struct irq_data;
typedef void (*irq_flow_handler_t)(unsigned int irq,
         struct irq_desc *desc);
typedef void (*irq_preflow_handler_t)(struct irq_data *data);
# 77 "include/linux/irq.h"
enum {
 IRQ_TYPE_NONE = 0x00000000,
 IRQ_TYPE_EDGE_RISING = 0x00000001,
 IRQ_TYPE_EDGE_FALLING = 0x00000002,
 IRQ_TYPE_EDGE_BOTH = (IRQ_TYPE_EDGE_FALLING | IRQ_TYPE_EDGE_RISING),
 IRQ_TYPE_LEVEL_HIGH = 0x00000004,
 IRQ_TYPE_LEVEL_LOW = 0x00000008,
 IRQ_TYPE_LEVEL_MASK = (IRQ_TYPE_LEVEL_LOW | IRQ_TYPE_LEVEL_HIGH),
 IRQ_TYPE_SENSE_MASK = 0x0000000f,
 IRQ_TYPE_DEFAULT = IRQ_TYPE_SENSE_MASK,

 IRQ_TYPE_PROBE = 0x00000010,

 IRQ_LEVEL = (1 << 8),
 IRQ_PER_CPU = (1 << 9),
 IRQ_NOPROBE = (1 << 10),
 IRQ_NOREQUEST = (1 << 11),
 IRQ_NOAUTOEN = (1 << 12),
 IRQ_NO_BALANCING = (1 << 13),
 IRQ_MOVE_PCNTXT = (1 << 14),
 IRQ_NESTED_THREAD = (1 << 15),
 IRQ_NOTHREAD = (1 << 16),
 IRQ_PER_CPU_DEVID = (1 << 17),
 IRQ_IS_POLLED = (1 << 18),
};
# 117 "include/linux/irq.h"
enum {
 IRQ_SET_MASK_OK = 0,
 IRQ_SET_MASK_OK_NOCOPY,
};

struct msi_desc;
struct irq_domain;
# 146 "include/linux/irq.h"
struct irq_data {
 u32 mask;
 unsigned int irq;
 unsigned long hwirq;
 unsigned int node;
 unsigned int state_use_accessors;
 struct irq_chip *chip;
 struct irq_domain *domain;
 void *handler_data;
 void *chip_data;
 struct msi_desc *msi_desc;
 cpumask_var_t affinity;
};
# 178 "include/linux/irq.h"
enum {
 IRQD_TRIGGER_MASK = 0xf,
 IRQD_SETAFFINITY_PENDING = (1 << 8),
 IRQD_NO_BALANCING = (1 << 10),
 IRQD_PER_CPU = (1 << 11),
 IRQD_AFFINITY_SET = (1 << 12),
 IRQD_LEVEL = (1 << 13),
 IRQD_WAKEUP_STATE = (1 << 14),
 IRQD_MOVE_PCNTXT = (1 << 15),
 IRQD_IRQ_DISABLED = (1 << 16),
 IRQD_IRQ_MASKED = (1 << 17),
 IRQD_IRQ_INPROGRESS = (1 << 18),
 IRQD_WAKEUP_ARMED = (1 << 19),
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_is_setaffinity_pending(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_SETAFFINITY_PENDING;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_is_per_cpu(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_PER_CPU;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_can_balance(struct irq_data *d)
{
 return !(d->state_use_accessors & (IRQD_PER_CPU | IRQD_NO_BALANCING));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_affinity_was_set(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_AFFINITY_SET;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irqd_mark_affinity_was_set(struct irq_data *d)
{
 d->state_use_accessors |= IRQD_AFFINITY_SET;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 irqd_get_trigger_type(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_TRIGGER_MASK;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irqd_set_trigger_type(struct irq_data *d, u32 type)
{
 d->state_use_accessors &= ~IRQD_TRIGGER_MASK;
 d->state_use_accessors |= type & IRQD_TRIGGER_MASK;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_is_level_type(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_LEVEL;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_is_wakeup_set(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_WAKEUP_STATE;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_can_move_in_process_context(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_MOVE_PCNTXT;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_irq_disabled(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_IRQ_DISABLED;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_irq_masked(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_IRQ_MASKED;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_irq_inprogress(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_IRQ_INPROGRESS;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool irqd_is_wakeup_armed(struct irq_data *d)
{
 return d->state_use_accessors & IRQD_WAKEUP_ARMED;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irqd_set_chained_irq_inprogress(struct irq_data *d)
{
 d->state_use_accessors |= IRQD_IRQ_INPROGRESS;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irqd_clr_chained_irq_inprogress(struct irq_data *d)
{
 d->state_use_accessors &= ~IRQD_IRQ_INPROGRESS;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) irq_hw_number_t irqd_to_hwirq(struct irq_data *d)
{
 return d->hwirq;
}
# 320 "include/linux/irq.h"
struct irq_chip {
 const char *name;
 unsigned int (*irq_startup)(struct irq_data *data);
 void (*irq_shutdown)(struct irq_data *data);
 void (*irq_enable)(struct irq_data *data);
 void (*irq_disable)(struct irq_data *data);

 void (*irq_ack)(struct irq_data *data);
 void (*irq_mask)(struct irq_data *data);
 void (*irq_mask_ack)(struct irq_data *data);
 void (*irq_unmask)(struct irq_data *data);
 void (*irq_eoi)(struct irq_data *data);

 int (*irq_set_affinity)(struct irq_data *data, const struct cpumask *dest, bool force);
 int (*irq_retrigger)(struct irq_data *data);
 int (*irq_set_type)(struct irq_data *data, unsigned int flow_type);
 int (*irq_set_wake)(struct irq_data *data, unsigned int on);

 void (*irq_bus_lock)(struct irq_data *data);
 void (*irq_bus_sync_unlock)(struct irq_data *data);

 void (*irq_cpu_online)(struct irq_data *data);
 void (*irq_cpu_offline)(struct irq_data *data);

 void (*irq_suspend)(struct irq_data *data);
 void (*irq_resume)(struct irq_data *data);
 void (*irq_pm_shutdown)(struct irq_data *data);

 void (*irq_calc_mask)(struct irq_data *data);

 void (*irq_print_chip)(struct irq_data *data, struct seq_file *p);
 int (*irq_request_resources)(struct irq_data *data);
 void (*irq_release_resources)(struct irq_data *data);

 unsigned long flags;
};
# 369 "include/linux/irq.h"
enum {
 IRQCHIP_SET_TYPE_MASKED = (1 << 0),
 IRQCHIP_EOI_IF_HANDLED = (1 << 1),
 IRQCHIP_MASK_ON_SUSPEND = (1 << 2),
 IRQCHIP_ONOFFLINE_ENABLED = (1 << 3),
 IRQCHIP_SKIP_SET_WAKE = (1 << 4),
 IRQCHIP_ONESHOT_SAFE = (1 << 5),
 IRQCHIP_EOI_THREADED = (1 << 6),
};


# 1 "include/linux/irqdesc.h" 1
# 11 "include/linux/irqdesc.h"
struct irq_affinity_notify;
struct proc_dir_entry;
struct module;
struct irq_desc;
struct irq_domain;
struct pt_regs;
# 49 "include/linux/irqdesc.h"
struct irq_desc {
 struct irq_data irq_data;
 unsigned int *kstat_irqs;
 irq_flow_handler_t handle_irq;



 struct irqaction *action;
 unsigned int status_use_accessors;
 unsigned int core_internal_state__do_not_mess_with_it;
 unsigned int depth;
 unsigned int wake_depth;
 unsigned int irq_count;
 unsigned long last_unhandled;
 unsigned int irqs_unhandled;
 atomic_t threads_handled;
 int threads_handled_last;
 raw_spinlock_t lock;
 struct cpumask *percpu_enabled;







 unsigned long threads_oneshot;
 atomic_t threads_active;
 wait_queue_head_t wait_for_threads;






 struct proc_dir_entry *dir;

 int parent_irq;
 struct module *owner;
 const char *name;
} ;


extern struct irq_desc irq_desc[51];


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_data *irq_desc_get_irq_data(struct irq_desc *desc)
{
 return &desc->irq_data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_chip *irq_desc_get_chip(struct irq_desc *desc)
{
 return desc->irq_data.chip;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *irq_desc_get_chip_data(struct irq_desc *desc)
{
 return desc->irq_data.chip_data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *irq_desc_get_handler_data(struct irq_desc *desc)
{
 return desc->irq_data.handler_data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct msi_desc *irq_desc_get_msi_desc(struct irq_desc *desc)
{
 return desc->irq_data.msi_desc;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void generic_handle_irq_desc(unsigned int irq, struct irq_desc *desc)
{
 desc->handle_irq(irq, desc);
}

int generic_handle_irq(unsigned int irq);
# 151 "include/linux/irqdesc.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_has_action(unsigned int irq)
{
 struct irq_desc *desc = irq_to_desc(irq);
 return desc->action != ((void *)0);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __irq_set_handler_locked(unsigned int irq,
         irq_flow_handler_t handler)
{
 struct irq_desc *desc;

 desc = irq_to_desc(irq);
 desc->handle_irq = handler;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
__irq_set_chip_handler_name_locked(unsigned int irq, struct irq_chip *chip,
       irq_flow_handler_t handler, const char *name)
{
 struct irq_desc *desc;

 desc = irq_to_desc(irq);
 irq_desc_get_irq_data(desc)->chip = chip;
 desc->handle_irq = handler;
 desc->name = name;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_balancing_disabled(unsigned int irq)
{
 struct irq_desc *desc;

 desc = irq_to_desc(irq);
 return desc->status_use_accessors & (IRQ_PER_CPU | IRQ_NO_BALANCING);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_is_percpu(unsigned int irq)
{
 struct irq_desc *desc;

 desc = irq_to_desc(irq);
 return desc->status_use_accessors & IRQ_PER_CPU;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
irq_set_lockdep_class(unsigned int irq, struct lock_class_key *class)
{
 struct irq_desc *desc = irq_to_desc(irq);

 if (desc)
  do { (void)(class); } while (0);
}
# 381 "include/linux/irq.h" 2




# 1 "./arch/mips/include/asm/hw_irq.h" 1
# 13 "./arch/mips/include/asm/hw_irq.h"
extern atomic_t irq_err_count;
# 386 "include/linux/irq.h" 2
# 397 "include/linux/irq.h"
struct irqaction;
extern int setup_irq(unsigned int irq, struct irqaction *new);
extern void remove_irq(unsigned int irq, struct irqaction *act);
extern int setup_percpu_irq(unsigned int irq, struct irqaction *new);
extern void remove_percpu_irq(unsigned int irq, struct irqaction *act);

extern void irq_cpu_online(void);
extern void irq_cpu_offline(void);
extern int irq_set_affinity_locked(struct irq_data *data,
       const struct cpumask *cpumask, bool force);





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_move_irq(struct irq_data *data) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_move_masked_irq(struct irq_data *data) { }


extern int no_irq_affinity;




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_set_parent(int irq, int parent_irq)
{
 return 0;
}






extern void handle_level_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_fasteoi_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_edge_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_edge_eoi_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_simple_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_percpu_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_percpu_devid_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_bad_irq(unsigned int irq, struct irq_desc *desc);
extern void handle_nested_irq(unsigned int irq);


extern void note_interrupt(unsigned int irq, struct irq_desc *desc,
      irqreturn_t action_ret);



extern int noirqdebug_setup(char *str);


extern int can_request_irq(unsigned int irq, unsigned long irqflags);


extern struct irq_chip no_irq_chip;
extern struct irq_chip dummy_irq_chip;

extern void
irq_set_chip_and_handler_name(unsigned int irq, struct irq_chip *chip,
         irq_flow_handler_t handle, const char *name);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_chip_and_handler(unsigned int irq, struct irq_chip *chip,
         irq_flow_handler_t handle)
{
 irq_set_chip_and_handler_name(irq, chip, handle, ((void *)0));
}

extern int irq_set_percpu_devid(unsigned int irq);

extern void
__irq_set_handler(unsigned int irq, irq_flow_handler_t handle, int is_chained,
    const char *name);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
irq_set_handler(unsigned int irq, irq_flow_handler_t handle)
{
 __irq_set_handler(irq, handle, 0, ((void *)0));
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
irq_set_chained_handler(unsigned int irq, irq_flow_handler_t handle)
{
 __irq_set_handler(irq, handle, 1, ((void *)0));
}

void irq_modify_status(unsigned int irq, unsigned long clr, unsigned long set);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_status_flags(unsigned int irq, unsigned long set)
{
 irq_modify_status(irq, 0, set);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_clear_status_flags(unsigned int irq, unsigned long clr)
{
 irq_modify_status(irq, clr, 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_noprobe(unsigned int irq)
{
 irq_modify_status(irq, 0, IRQ_NOPROBE);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_probe(unsigned int irq)
{
 irq_modify_status(irq, IRQ_NOPROBE, 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_nothread(unsigned int irq)
{
 irq_modify_status(irq, 0, IRQ_NOTHREAD);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_thread(unsigned int irq)
{
 irq_modify_status(irq, IRQ_NOTHREAD, 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_nested_thread(unsigned int irq, bool nest)
{
 if (nest)
  irq_set_status_flags(irq, IRQ_NESTED_THREAD);
 else
  irq_clear_status_flags(irq, IRQ_NESTED_THREAD);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_set_percpu_devid_flags(unsigned int irq)
{
 irq_set_status_flags(irq,
        IRQ_NOAUTOEN | IRQ_PER_CPU | IRQ_NOTHREAD |
        IRQ_NOPROBE | IRQ_PER_CPU_DEVID);
}


extern int irq_set_chip(unsigned int irq, struct irq_chip *chip);
extern int irq_set_handler_data(unsigned int irq, void *data);
extern int irq_set_chip_data(unsigned int irq, void *data);
extern int irq_set_irq_type(unsigned int irq, unsigned int type);
extern int irq_set_msi_desc(unsigned int irq, struct msi_desc *entry);
extern int irq_set_msi_desc_off(unsigned int irq_base, unsigned int irq_offset,
    struct msi_desc *entry);
extern struct irq_data *irq_get_irq_data(unsigned int irq);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_chip *irq_get_chip(unsigned int irq)
{
 struct irq_data *d = irq_get_irq_data(irq);
 return d ? d->chip : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_chip *irq_data_get_irq_chip(struct irq_data *d)
{
 return d->chip;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *irq_get_chip_data(unsigned int irq)
{
 struct irq_data *d = irq_get_irq_data(irq);
 return d ? d->chip_data : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *irq_data_get_irq_chip_data(struct irq_data *d)
{
 return d->chip_data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *irq_get_handler_data(unsigned int irq)
{
 struct irq_data *d = irq_get_irq_data(irq);
 return d ? d->handler_data : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *irq_data_get_irq_handler_data(struct irq_data *d)
{
 return d->handler_data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct msi_desc *irq_get_msi_desc(unsigned int irq)
{
 struct irq_data *d = irq_get_irq_data(irq);
 return d ? d->msi_desc : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct msi_desc *irq_data_get_msi(struct irq_data *d)
{
 return d->msi_desc;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 irq_get_trigger_type(unsigned int irq)
{
 struct irq_data *d = irq_get_irq_data(irq);
 return d ? irqd_get_trigger_type(d) : 0;
}

unsigned int arch_dynirq_lower_bound(unsigned int from);

int __irq_alloc_descs(int irq, unsigned int from, unsigned int cnt, int node,
  struct module *owner);
# 617 "include/linux/irq.h"
void irq_free_descs(unsigned int irq, unsigned int cnt);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_free_desc(unsigned int irq)
{
 irq_free_descs(irq, 1);
}
# 659 "include/linux/irq.h"
struct irq_chip_regs {
 unsigned long enable;
 unsigned long disable;
 unsigned long mask;
 unsigned long ack;
 unsigned long eoi;
 unsigned long type;
 unsigned long polarity;
};
# 682 "include/linux/irq.h"
struct irq_chip_type {
 struct irq_chip chip;
 struct irq_chip_regs regs;
 irq_flow_handler_t handler;
 u32 type;
 u32 mask_cache_priv;
 u32 *mask_cache;
};
# 716 "include/linux/irq.h"
struct irq_chip_generic {
 raw_spinlock_t lock;
 void *reg_base;
 unsigned int irq_base;
 unsigned int irq_cnt;
 u32 mask_cache;
 u32 type_cache;
 u32 polarity_cache;
 u32 wake_enabled;
 u32 wake_active;
 unsigned int num_ct;
 void *private;
 unsigned long installed;
 unsigned long unused;
 struct irq_domain *domain;
 struct list_head list;
 struct irq_chip_type chip_types[0];
};
# 744 "include/linux/irq.h"
enum irq_gc_flags {
 IRQ_GC_INIT_MASK_CACHE = 1 << 0,
 IRQ_GC_INIT_NESTED_LOCK = 1 << 1,
 IRQ_GC_MASK_CACHE_PER_TYPE = 1 << 2,
 IRQ_GC_NO_MASK = 1 << 3,
};
# 760 "include/linux/irq.h"
struct irq_domain_chip_generic {
 unsigned int irqs_per_chip;
 unsigned int num_chips;
 unsigned int irq_flags_to_clear;
 unsigned int irq_flags_to_set;
 enum irq_gc_flags gc_flags;
 struct irq_chip_generic *gc[0];
};


void irq_gc_noop(struct irq_data *d);
void irq_gc_mask_disable_reg(struct irq_data *d);
void irq_gc_mask_set_bit(struct irq_data *d);
void irq_gc_mask_clr_bit(struct irq_data *d);
void irq_gc_unmask_enable_reg(struct irq_data *d);
void irq_gc_ack_set_bit(struct irq_data *d);
void irq_gc_ack_clr_bit(struct irq_data *d);
void irq_gc_mask_disable_reg_and_ack(struct irq_data *d);
void irq_gc_eoi(struct irq_data *d);
int irq_gc_set_wake(struct irq_data *d, unsigned int on);


int irq_map_generic_chip(struct irq_domain *d, unsigned int virq,
    irq_hw_number_t hw_irq);
struct irq_chip_generic *
irq_alloc_generic_chip(const char *name, int nr_ct, unsigned int irq_base,
         void *reg_base, irq_flow_handler_t handler);
void irq_setup_generic_chip(struct irq_chip_generic *gc, u32 msk,
       enum irq_gc_flags flags, unsigned int clr,
       unsigned int set);
int irq_setup_alt_chip(struct irq_data *d, unsigned int type);
void irq_remove_generic_chip(struct irq_chip_generic *gc, u32 msk,
        unsigned int clr, unsigned int set);

struct irq_chip_generic *irq_get_domain_generic_chip(struct irq_domain *d, unsigned int hw_irq);
int irq_alloc_domain_generic_chips(struct irq_domain *d, int irqs_per_chip,
       int num_ct, const char *name,
       irq_flow_handler_t handler,
       unsigned int clr, unsigned int set,
       enum irq_gc_flags flags);


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct irq_chip_type *irq_data_get_chip_type(struct irq_data *d)
{
 return ({ const typeof( ((struct irq_chip_type *)0)->chip ) *__mptr = (d->chip); (struct irq_chip_type *)( (char *)__mptr - __builtin_offsetof(struct irq_chip_type,chip) );});
}
# 820 "include/linux/irq.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_gc_lock(struct irq_chip_generic *gc) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void irq_gc_unlock(struct irq_chip_generic *gc) { }
# 13 "include/asm-generic/hardirq.h" 2
# 17 "./arch/mips/include/asm/hardirq.h" 2
# 9 "include/linux/hardirq.h" 2


extern void synchronize_irq(unsigned int irq);
extern void synchronize_hardirq(unsigned int irq);



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_nmi_enter(void)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void rcu_nmi_exit(void)
{
}
# 45 "include/linux/hardirq.h"
extern void irq_enter(void);
# 60 "include/linux/hardirq.h"
extern void irq_exit(void);
# 13 "include/linux/interrupt.h" 2


# 1 "include/linux/kref.h" 1
# 24 "include/linux/kref.h"
struct kref {
 atomic_t refcount;
};





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void kref_init(struct kref *kref)
{
 ((&kref->refcount)->counter = (1));
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void kref_get(struct kref *kref)
{




 ({ static bool __attribute__ ((__section__(".data.unlikely"))) __warned; int __ret_warn_once = !!(atomic_add_return(1, (&kref->refcount)) < 2); if (__builtin_expect(!!(__ret_warn_once), 0)) if (({ int __ret_warn_on = !!(!__warned); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/kref.h", 47); __builtin_expect(!!(__ret_warn_on), 0); })) __warned = true; __builtin_expect(!!(__ret_warn_once), 0); });
}
# 68 "include/linux/kref.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kref_sub(struct kref *kref, unsigned int count,
      void (*release)(struct kref *kref))
{
 ({ int __ret_warn_on = !!(release == ((void *)0)); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/kref.h", 71); __builtin_expect(!!(__ret_warn_on), 0); });

 if ((atomic_sub_return(((int) count), (&kref->refcount)) == 0)) {
  release(kref);
  return 1;
 }
 return 0;
}
# 97 "include/linux/kref.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kref_put(struct kref *kref, void (*release)(struct kref *kref))
{
 return kref_sub(kref, 1, release);
}
# 115 "include/linux/kref.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kref_put_spinlock_irqsave(struct kref *kref,
  void (*release)(struct kref *kref),
  spinlock_t *lock)
{
 unsigned long flags;

 ({ int __ret_warn_on = !!(release == ((void *)0)); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/kref.h", 121); __builtin_expect(!!(__ret_warn_on), 0); });
 if (atomic_add_unless(&kref->refcount, -1, 1))
  return 0;
 do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); do { do { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); flags = arch_local_irq_save(); } while (0); do { } while (0); } while (0); do { __asm__ __volatile__("": : :"memory"); do { (void)0; (void)(spinlock_check(lock)); } while (0); } while (0); } while (0); } while (0); } while (0);
 if ((atomic_sub_return(1, (&kref->refcount)) == 0)) {
  release(kref);
  do { if (({ ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_irqs_disabled_flags(flags); })) { do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); do { } while (0); } else { do { } while (0); do { ({ unsigned long __dummy; typeof(flags) __dummy2; (void)(&__dummy == &__dummy2); 1; }); arch_local_irq_restore(flags); } while (0); } } while (0);
  return 1;
 }
 spin_unlock_irqrestore(lock, flags);
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kref_put_mutex(struct kref *kref,
     void (*release)(struct kref *kref),
     struct mutex *lock)
{
 ({ int __ret_warn_on = !!(release == ((void *)0)); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/kref.h", 138); __builtin_expect(!!(__ret_warn_on), 0); });
 if (__builtin_expect(!!(!atomic_add_unless(&kref->refcount, -1, 1)), 0)) {
  mutex_lock(lock);
  if (__builtin_expect(!!(!(atomic_sub_return(1, (&kref->refcount)) == 0)), 0)) {
   mutex_unlock(lock);
   return 0;
  }
  release(kref);
  return 1;
 }
 return 0;
}
# 167 "include/linux/kref.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kref_get_unless_zero(struct kref *kref)
{
 return atomic_add_unless(&kref->refcount, 1, 0);
}
# 16 "include/linux/interrupt.h" 2
# 83 "include/linux/interrupt.h"
enum {
 IRQC_IS_HARDIRQ = 0,
 IRQC_IS_NESTED,
};

typedef irqreturn_t (*irq_handler_t)(int, void *);
# 105 "include/linux/interrupt.h"
struct irqaction {
 irq_handler_t handler;
 void *dev_id;
 void *percpu_dev_id;
 struct irqaction *next;
 irq_handler_t thread_fn;
 struct task_struct *thread;
 unsigned int irq;
 unsigned int flags;
 unsigned long thread_flags;
 unsigned long thread_mask;
 const char *name;
 struct proc_dir_entry *dir;
} ;

extern irqreturn_t no_action(int cpl, void *dev_id);

extern int
request_threaded_irq(unsigned int irq, irq_handler_t handler,
       irq_handler_t thread_fn,
       unsigned long flags, const char *name, void *dev);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
request_irq(unsigned int irq, irq_handler_t handler, unsigned long flags,
     const char *name, void *dev)
{
 return request_threaded_irq(irq, handler, ((void *)0), flags, name, dev);
}

extern int
request_any_context_irq(unsigned int irq, irq_handler_t handler,
   unsigned long flags, const char *name, void *dev_id);

extern int
request_percpu_irq(unsigned int irq, irq_handler_t handler,
     const char *devname, void *percpu_dev_id);

extern void free_irq(unsigned int, void *);
extern void free_percpu_irq(unsigned int, void *);

struct device;

extern int
devm_request_threaded_irq(struct device *dev, unsigned int irq,
     irq_handler_t handler, irq_handler_t thread_fn,
     unsigned long irqflags, const char *devname,
     void *dev_id);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
devm_request_irq(struct device *dev, unsigned int irq, irq_handler_t handler,
   unsigned long irqflags, const char *devname, void *dev_id)
{
 return devm_request_threaded_irq(dev, irq, handler, ((void *)0), irqflags,
      devname, dev_id);
}

extern int
devm_request_any_context_irq(struct device *dev, unsigned int irq,
   irq_handler_t handler, unsigned long irqflags,
   const char *devname, void *dev_id);

extern void devm_free_irq(struct device *dev, unsigned int irq, void *dev_id);
# 186 "include/linux/interrupt.h"
extern void disable_irq_nosync(unsigned int irq);
extern void disable_irq(unsigned int irq);
extern void disable_percpu_irq(unsigned int irq);
extern void enable_irq(unsigned int irq);
extern void enable_percpu_irq(unsigned int irq, unsigned int type);
extern void irq_wake_thread(unsigned int irq, void *dev_id);


extern void suspend_device_irqs(void);
extern void resume_device_irqs(void);
# 209 "include/linux/interrupt.h"
struct irq_affinity_notify {
 unsigned int irq;
 struct kref kref;
 struct work_struct work;
 void (*notify)(struct irq_affinity_notify *, const cpumask_t *mask);
 void (*release)(struct kref *ref);
};
# 265 "include/linux/interrupt.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_set_affinity(unsigned int irq, const struct cpumask *m)
{
 return -22;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_force_affinity(unsigned int irq, const struct cpumask *cpumask)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_can_set_affinity(unsigned int irq)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_select_affinity(unsigned int irq) { return 0; }

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int irq_set_affinity_hint(unsigned int irq,
     const struct cpumask *m)
{
 return -22;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int
irq_set_affinity_notifier(unsigned int irq, struct irq_affinity_notify *notify)
{
 return 0;
}
# 306 "include/linux/interrupt.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void disable_irq_nosync_lockdep(unsigned int irq)
{
 disable_irq_nosync(irq);



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void disable_irq_nosync_lockdep_irqsave(unsigned int irq, unsigned long *flags)
{
 disable_irq_nosync(irq);



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void disable_irq_lockdep(unsigned int irq)
{
 disable_irq(irq);



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void enable_irq_lockdep(unsigned int irq)
{



 enable_irq(irq);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void enable_irq_lockdep_irqrestore(unsigned int irq, unsigned long *flags)
{



 enable_irq(irq);
}


extern int irq_set_irq_wake(unsigned int irq, unsigned int on);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int enable_irq_wake(unsigned int irq)
{
 return irq_set_irq_wake(irq, 1);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int disable_irq_wake(unsigned int irq)
{
 return irq_set_irq_wake(irq, 0);
}



extern bool force_irqthreads;
# 387 "include/linux/interrupt.h"
enum
{
 HI_SOFTIRQ=0,
 TIMER_SOFTIRQ,
 NET_TX_SOFTIRQ,
 NET_RX_SOFTIRQ,
 BLOCK_SOFTIRQ,
 BLOCK_IOPOLL_SOFTIRQ,
 TASKLET_SOFTIRQ,
 SCHED_SOFTIRQ,
 HRTIMER_SOFTIRQ,
 RCU_SOFTIRQ,

 NR_SOFTIRQS
};






extern const char * const softirq_to_name[NR_SOFTIRQS];





struct softirq_action
{
 void (*action)(struct softirq_action *);
};

 void do_softirq(void);
 void __do_softirq(void);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void do_softirq_own_stack(void)
{
 __do_softirq();
}


extern void open_softirq(int nr, void (*action)(struct softirq_action *));
extern void softirq_init(void);
extern void __raise_softirq_irqoff(unsigned int nr);

extern void raise_softirq_irqoff(unsigned int nr);
extern void raise_softirq(unsigned int nr);

extern __attribute__((section(".data" ""))) __typeof__(struct task_struct *) ksoftirqd;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct task_struct *this_cpu_ksoftirqd(void)
{
 return ({ typeof(ksoftirqd) pscr_ret__; do { const void *__vpp_verify = (typeof((&(ksoftirqd)) + 0))((void *)0); (void)__vpp_verify; } while (0); switch(sizeof(ksoftirqd)) { case 1: pscr_ret__ = ({ typeof(ksoftirqd) __ret; __asm__ __volatile__("": : :"memory"); __ret = *({ (void)(0); ({ do { const void *__vpp_verify = (typeof((&(ksoftirqd)) + 0))((void *)0); (void)__vpp_verify; } while (0); (typeof(*(&(ksoftirqd))) *)(&(ksoftirqd)); }); }); __asm__ __volatile__("": : :"memory"); __ret; }); break; case 2: pscr_ret__ = ({ typeof(ksoftirqd) __ret; __asm__ __volatile__("": : :"memory"); __ret = *({ (void)(0); ({ do { const void *__vpp_verify = (typeof((&(ksoftirqd)) + 0))((void *)0); (void)__vpp_verify; } while (0); (typeof(*(&(ksoftirqd))) *)(&(ksoftirqd)); }); }); __asm__ __volatile__("": : :"memory"); __ret; }); break; case 4: pscr_ret__ = ({ typeof(ksoftirqd) __ret; __asm__ __volatile__("": : :"memory"); __ret = *({ (void)(0); ({ do { const void *__vpp_verify = (typeof((&(ksoftirqd)) + 0))((void *)0); (void)__vpp_verify; } while (0); (typeof(*(&(ksoftirqd))) *)(&(ksoftirqd)); }); }); __asm__ __volatile__("": : :"memory"); __ret; }); break; case 8: pscr_ret__ = ({ typeof(ksoftirqd) __ret; __asm__ __volatile__("": : :"memory"); __ret = *({ (void)(0); ({ do { const void *__vpp_verify = (typeof((&(ksoftirqd)) + 0))((void *)0); (void)__vpp_verify; } while (0); (typeof(*(&(ksoftirqd))) *)(&(ksoftirqd)); }); }); __asm__ __volatile__("": : :"memory"); __ret; }); break; default: __bad_size_call_parameter(); break; } pscr_ret__; });
}
# 465 "include/linux/interrupt.h"
struct tasklet_struct
{
 struct tasklet_struct *next;
 unsigned long state;
 atomic_t count;
 void (*func)(unsigned long);
 unsigned long data;
};
# 481 "include/linux/interrupt.h"
enum
{
 TASKLET_STATE_SCHED,
 TASKLET_STATE_RUN
};
# 509 "include/linux/interrupt.h"
extern void __tasklet_schedule(struct tasklet_struct *t);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_schedule(struct tasklet_struct *t)
{
 if (!test_and_set_bit(TASKLET_STATE_SCHED, &t->state))
  __tasklet_schedule(t);
}

extern void __tasklet_hi_schedule(struct tasklet_struct *t);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_hi_schedule(struct tasklet_struct *t)
{
 if (!test_and_set_bit(TASKLET_STATE_SCHED, &t->state))
  __tasklet_hi_schedule(t);
}

extern void __tasklet_hi_schedule_first(struct tasklet_struct *t);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_hi_schedule_first(struct tasklet_struct *t)
{
 if (!test_and_set_bit(TASKLET_STATE_SCHED, &t->state))
  __tasklet_hi_schedule_first(t);
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_disable_nosync(struct tasklet_struct *t)
{
 atomic_add(1, (&t->count));
 __asm__ __volatile__("		\n" : : :"memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_disable(struct tasklet_struct *t)
{
 tasklet_disable_nosync(t);
 do { } while (0);
 __asm__ __volatile__("": : :"memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_enable(struct tasklet_struct *t)
{
 __asm__ __volatile__("		\n" : : :"memory");
 atomic_sub(1, (&t->count));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tasklet_hi_enable(struct tasklet_struct *t)
{
 __asm__ __volatile__("		\n" : : :"memory");
 atomic_sub(1, (&t->count));
}

extern void tasklet_kill(struct tasklet_struct *t);
extern void tasklet_kill_immediate(struct tasklet_struct *t, unsigned int cpu);
extern void tasklet_init(struct tasklet_struct *t,
    void (*func)(unsigned long), unsigned long data);

struct tasklet_hrtimer {
 struct hrtimer timer;
 struct tasklet_struct tasklet;
 enum hrtimer_restart (*function)(struct hrtimer *);
};

extern void
tasklet_hrtimer_init(struct tasklet_hrtimer *ttimer,
       enum hrtimer_restart (*function)(struct hrtimer *),
       clockid_t which_clock, enum hrtimer_mode mode);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function))
int tasklet_hrtimer_start(struct tasklet_hrtimer *ttimer, ktime_t time,
     const enum hrtimer_mode mode)
{
 return hrtimer_start(&ttimer->timer, time, mode);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function))
void tasklet_hrtimer_cancel(struct tasklet_hrtimer *ttimer)
{
 hrtimer_cancel(&ttimer->timer);
 tasklet_kill(&ttimer->tasklet);
}
# 637 "include/linux/interrupt.h"
extern unsigned long probe_irq_on(void);
extern int probe_irq_off(unsigned long);
extern unsigned int probe_irq_mask(unsigned long);




extern void init_irq_proc(void);






struct seq_file;
int show_interrupts(struct seq_file *p, void *v);
int arch_show_interrupts(struct seq_file *p, int prec);

extern int early_irq_init(void);
extern int arch_probe_nr_irqs(void);
extern int arch_early_irq_init(void);
# 17 "include/linux/rtc.h" 2
# 1 "include/uapi/linux/rtc.h" 1
# 20 "include/uapi/linux/rtc.h"
struct rtc_time {
 int tm_sec;
 int tm_min;
 int tm_hour;
 int tm_mday;
 int tm_mon;
 int tm_year;
 int tm_wday;
 int tm_yday;
 int tm_isdst;
};





struct rtc_wkalrm {
 unsigned char enabled;
 unsigned char pending;
 struct rtc_time time;
};
# 55 "include/uapi/linux/rtc.h"
struct rtc_pll_info {
 int pll_ctrl;
 int pll_value;
 int pll_max;
 int pll_min;
 int pll_posmult;
 int pll_negmult;
 long pll_clock;
};
# 18 "include/linux/rtc.h" 2

extern int rtc_month_days(unsigned int month, unsigned int year);
extern int rtc_year_days(unsigned int day, unsigned int month, unsigned int year);
extern int rtc_valid_tm(struct rtc_time *tm);
extern int rtc_tm_to_time(struct rtc_time *tm, unsigned long *time);
extern void rtc_time_to_tm(unsigned long time, struct rtc_time *tm);
ktime_t rtc_tm_to_ktime(struct rtc_time tm);
struct rtc_time rtc_ktime_to_tm(ktime_t kt);


# 1 "include/linux/device.h" 1
# 16 "include/linux/device.h"
# 1 "include/linux/ioport.h" 1
# 18 "include/linux/ioport.h"
struct resource {
 resource_size_t start;
 resource_size_t end;
 const char *name;
 unsigned long flags;
 struct resource *parent, *sibling, *child;
};
# 138 "include/linux/ioport.h"
extern struct resource ioport_resource;
extern struct resource iomem_resource;

extern struct resource *request_resource_conflict(struct resource *root, struct resource *new);
extern int request_resource(struct resource *root, struct resource *new);
extern int release_resource(struct resource *new);
void release_child_resources(struct resource *new);
extern void reserve_region_with_split(struct resource *root,
        resource_size_t start, resource_size_t end,
        const char *name);
extern struct resource *insert_resource_conflict(struct resource *parent, struct resource *new);
extern int insert_resource(struct resource *parent, struct resource *new);
extern void insert_resource_expand_to_fit(struct resource *root, struct resource *new);
extern void arch_remove_reservations(struct resource *avail);
extern int allocate_resource(struct resource *root, struct resource *new,
        resource_size_t size, resource_size_t min,
        resource_size_t max, resource_size_t align,
        resource_size_t (*alignf)(void *,
             const struct resource *,
             resource_size_t,
             resource_size_t),
        void *alignf_data);
struct resource *lookup_resource(struct resource *root, resource_size_t start);
int adjust_resource(struct resource *res, resource_size_t start,
      resource_size_t size);
resource_size_t resource_alignment(struct resource *res);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) resource_size_t resource_size(const struct resource *res)
{
 return res->end - res->start + 1;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long resource_type(const struct resource *res)
{
 return res->flags & 0x00001f00;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool resource_contains(struct resource *r1, struct resource *r2)
{
 if (resource_type(r1) != resource_type(r2))
  return false;
 if (r1->flags & 0x20000000 || r2->flags & 0x20000000)
  return false;
 return r1->start <= r2->start && r1->end >= r2->end;
}
# 192 "include/linux/ioport.h"
extern struct resource * __request_region(struct resource *,
     resource_size_t start,
     resource_size_t n,
     const char *name, int flags);






extern int __check_region(struct resource *, resource_size_t, resource_size_t);
extern void __release_region(struct resource *, resource_size_t,
    resource_size_t);





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __attribute__((deprecated)) check_region(resource_size_t s,
      resource_size_t n)
{
 return __check_region(&ioport_resource, s, n);
}


struct device;

extern int devm_request_resource(struct device *dev, struct resource *root,
     struct resource *new);
extern void devm_release_resource(struct device *dev, struct resource *new);






extern struct resource * __devm_request_region(struct device *dev,
    struct resource *parent, resource_size_t start,
    resource_size_t n, const char *name);






extern void __devm_release_region(struct device *dev, struct resource *parent,
      resource_size_t start, resource_size_t n);
extern int iomem_map_sanity_check(resource_size_t addr, unsigned long size);
extern int iomem_is_exclusive(u64 addr);

extern int
walk_system_ram_range(unsigned long start_pfn, unsigned long nr_pages,
  void *arg, int (*func)(unsigned long, unsigned long, void *));
extern int
walk_system_ram_res(u64 start, u64 end, void *arg,
      int (*func)(u64, u64, void *));
extern int
walk_iomem_res(char *name, unsigned long flags, u64 start, u64 end, void *arg,
        int (*func)(u64, u64, void *));


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool resource_overlaps(struct resource *r1, struct resource *r2)
{
       return (r1->start <= r2->end && r1->end >= r2->start);
}
# 17 "include/linux/device.h" 2
# 1 "include/linux/kobject.h" 1
# 21 "include/linux/kobject.h"
# 1 "include/linux/sysfs.h" 1
# 15 "include/linux/sysfs.h"
# 1 "include/linux/kernfs.h" 1
# 14 "include/linux/kernfs.h"
# 1 "include/linux/idr.h" 1
# 30 "include/linux/idr.h"
struct idr_layer {
 int prefix;
 int layer;
 struct idr_layer *ary[1<<8];
 int count;
 union {

  unsigned long bitmap[((((1 << 8)) + (8 * sizeof(long)) - 1) / (8 * sizeof(long)))];
  struct callback_head callback_head;
 };
};

struct idr {
 struct idr_layer *hint;
 struct idr_layer *top;
 int layers;
 int cur;
 spinlock_t lock;
 int id_free_cnt;
 struct idr_layer *id_free;
};
# 79 "include/linux/idr.h"
void *idr_find_slowpath(struct idr *idp, int id);
void idr_preload(gfp_t gfp_mask);
int idr_alloc(struct idr *idp, void *ptr, int start, int end, gfp_t gfp_mask);
int idr_alloc_cyclic(struct idr *idr, void *ptr, int start, int end, gfp_t gfp_mask);
int idr_for_each(struct idr *idp,
   int (*fn)(int id, void *p, void *data), void *data);
void *idr_get_next(struct idr *idp, int *nextid);
void *idr_replace(struct idr *idp, void *ptr, int id);
void idr_remove(struct idr *idp, int id);
void idr_destroy(struct idr *idp);
void idr_init(struct idr *idp);
bool idr_is_empty(struct idr *idp);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void idr_preload_end(void)
{
 __asm__ __volatile__("": : :"memory");
}
# 115 "include/linux/idr.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *idr_find(struct idr *idr, int id)
{
 struct idr_layer *hint = ({ typeof(*(idr->hint)) *_________p1 = (typeof(*(idr->hint)) *)(*(volatile typeof((idr->hint)) *)&((idr->hint))); do { } while (0); ; do { } while(0); ((typeof(*(idr->hint)) *)(_________p1)); });

 if (hint && (id & ~((1 << 8)-1)) == hint->prefix)
  return ({ typeof(*(hint->ary[id & ((1 << 8)-1)])) *_________p1 = (typeof(*(hint->ary[id & ((1 << 8)-1)])) *)(*(volatile typeof((hint->ary[id & ((1 << 8)-1)])) *)&((hint->ary[id & ((1 << 8)-1)]))); do { } while (0); ; do { } while(0); ((typeof(*(hint->ary[id & ((1 << 8)-1)])) *)(_________p1)); });

 return idr_find_slowpath(idr, id);
}
# 149 "include/linux/idr.h"
struct ida_bitmap {
 long nr_busy;
 unsigned long bitmap[(128 / sizeof(long) - 1)];
};

struct ida {
 struct idr idr;
 struct ida_bitmap *free_bitmap;
};




int ida_pre_get(struct ida *ida, gfp_t gfp_mask);
int ida_get_new_above(struct ida *ida, int starting_id, int *p_id);
void ida_remove(struct ida *ida, int id);
void ida_destroy(struct ida *ida);
void ida_init(struct ida *ida);

int ida_simple_get(struct ida *ida, unsigned int start, unsigned int end,
     gfp_t gfp_mask);
void ida_simple_remove(struct ida *ida, unsigned int id);
# 179 "include/linux/idr.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ida_get_new(struct ida *ida, int *p_id)
{
 return ida_get_new_above(ida, 0, p_id);
}

void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) idr_init_cache(void);
# 15 "include/linux/kernfs.h" 2





struct file;
struct dentry;
struct iattr;
struct seq_file;
struct vm_area_struct;
struct super_block;
struct file_system_type;

struct kernfs_open_node;
struct kernfs_iattrs;

enum kernfs_node_type {
 KERNFS_DIR = 0x0001,
 KERNFS_FILE = 0x0002,
 KERNFS_LINK = 0x0004,
};




enum kernfs_node_flag {
 KERNFS_ACTIVATED = 0x0010,
 KERNFS_NS = 0x0020,
 KERNFS_HAS_SEQ_SHOW = 0x0040,
 KERNFS_HAS_MMAP = 0x0080,
 KERNFS_LOCKDEP = 0x0100,
 KERNFS_STATIC_NAME = 0x0200,
 KERNFS_SUICIDAL = 0x0400,
 KERNFS_SUICIDED = 0x0800,
};


enum kernfs_root_flag {






 KERNFS_ROOT_CREATE_DEACTIVATED = 0x0001,
# 70 "include/linux/kernfs.h"
 KERNFS_ROOT_EXTRA_OPEN_PERM_CHECK = 0x0002,
};


struct kernfs_elem_dir {
 unsigned long subdirs;

 struct rb_root children;





 struct kernfs_root *root;
};

struct kernfs_elem_symlink {
 struct kernfs_node *target_kn;
};

struct kernfs_elem_attr {
 const struct kernfs_ops *ops;
 struct kernfs_open_node *open;
 loff_t size;
 struct kernfs_node *notify_next;
};
# 106 "include/linux/kernfs.h"
struct kernfs_node {
 atomic_t count;
 atomic_t active;
# 118 "include/linux/kernfs.h"
 struct kernfs_node *parent;
 const char *name;

 struct rb_node rb;

 const void *ns;
 unsigned int hash;
 union {
  struct kernfs_elem_dir dir;
  struct kernfs_elem_symlink symlink;
  struct kernfs_elem_attr attr;
 };

 void *priv;

 unsigned short flags;
 umode_t mode;
 unsigned int ino;
 struct kernfs_iattrs *iattr;
};
# 146 "include/linux/kernfs.h"
struct kernfs_syscall_ops {
 int (*remount_fs)(struct kernfs_root *root, int *flags, char *data);
 int (*show_options)(struct seq_file *sf, struct kernfs_root *root);

 int (*mkdir)(struct kernfs_node *parent, const char *name,
       umode_t mode);
 int (*rmdir)(struct kernfs_node *kn);
 int (*rename)(struct kernfs_node *kn, struct kernfs_node *new_parent,
        const char *new_name);
};

struct kernfs_root {

 struct kernfs_node *kn;
 unsigned int flags;


 struct ida ino_ida;
 struct kernfs_syscall_ops *syscall_ops;


 struct list_head supers;

 wait_queue_head_t deactivate_waitq;
};

struct kernfs_open_file {

 struct kernfs_node *kn;
 struct file *file;
 void *priv;


 struct mutex mutex;
 int event;
 struct list_head list;

 size_t atomic_write_len;
 bool mmapped;
 const struct vm_operations_struct *vm_ops;
};

struct kernfs_ops {
# 200 "include/linux/kernfs.h"
 int (*seq_show)(struct seq_file *sf, void *v);

 void *(*seq_start)(struct seq_file *sf, loff_t *ppos);
 void *(*seq_next)(struct seq_file *sf, void *v, loff_t *ppos);
 void (*seq_stop)(struct seq_file *sf, void *v);

 ssize_t (*read)(struct kernfs_open_file *of, char *buf, size_t bytes,
   loff_t off);
# 216 "include/linux/kernfs.h"
 size_t atomic_write_len;
 ssize_t (*write)(struct kernfs_open_file *of, char *buf, size_t bytes,
    loff_t off);

 int (*mmap)(struct kernfs_open_file *of, struct vm_area_struct *vma);




};



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) enum kernfs_node_type kernfs_type(struct kernfs_node *kn)
{
 return kn->flags & 0x000f;
}
# 242 "include/linux/kernfs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void kernfs_enable_ns(struct kernfs_node *kn)
{
 ({ static bool __attribute__ ((__section__(".data.unlikely"))) __warned; int __ret_warn_once = !!(kernfs_type(kn) != KERNFS_DIR); if (__builtin_expect(!!(__ret_warn_once), 0)) if (({ int __ret_warn_on = !!(!__warned); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/kernfs.h", 244); __builtin_expect(!!(__ret_warn_on), 0); })) __warned = true; __builtin_expect(!!(__ret_warn_once), 0); });
 ({ static bool __attribute__ ((__section__(".data.unlikely"))) __warned; int __ret_warn_once = !!(!((&kn->dir.children)->rb_node == ((void *)0))); if (__builtin_expect(!!(__ret_warn_once), 0)) if (({ int __ret_warn_on = !!(!__warned); if (__builtin_expect(!!(__ret_warn_on), 0)) warn_slowpath_null("include/linux/kernfs.h", 245); __builtin_expect(!!(__ret_warn_on), 0); })) __warned = true; __builtin_expect(!!(__ret_warn_once), 0); });
 kn->flags |= KERNFS_NS;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool kernfs_ns_enabled(struct kernfs_node *kn)
{
 return kn->flags & KERNFS_NS;
}

int kernfs_name(struct kernfs_node *kn, char *buf, size_t buflen);
char * kernfs_path(struct kernfs_node *kn, char *buf,
    size_t buflen);
void pr_cont_kernfs_name(struct kernfs_node *kn);
void pr_cont_kernfs_path(struct kernfs_node *kn);
struct kernfs_node *kernfs_get_parent(struct kernfs_node *kn);
struct kernfs_node *kernfs_find_and_get_ns(struct kernfs_node *parent,
        const char *name, const void *ns);
void kernfs_get(struct kernfs_node *kn);
void kernfs_put(struct kernfs_node *kn);

struct kernfs_node *kernfs_node_from_dentry(struct dentry *dentry);
struct kernfs_root *kernfs_root_from_sb(struct super_block *sb);

struct kernfs_root *kernfs_create_root(struct kernfs_syscall_ops *scops,
           unsigned int flags, void *priv);
void kernfs_destroy_root(struct kernfs_root *root);

struct kernfs_node *kernfs_create_dir_ns(struct kernfs_node *parent,
      const char *name, umode_t mode,
      void *priv, const void *ns);
struct kernfs_node *__kernfs_create_file(struct kernfs_node *parent,
      const char *name,
      umode_t mode, loff_t size,
      const struct kernfs_ops *ops,
      void *priv, const void *ns,
      bool name_is_static,
      struct lock_class_key *key);
struct kernfs_node *kernfs_create_link(struct kernfs_node *parent,
           const char *name,
           struct kernfs_node *target);
void kernfs_activate(struct kernfs_node *kn);
void kernfs_remove(struct kernfs_node *kn);
void kernfs_break_active_protection(struct kernfs_node *kn);
void kernfs_unbreak_active_protection(struct kernfs_node *kn);
bool kernfs_remove_self(struct kernfs_node *kn);
int kernfs_remove_by_name_ns(struct kernfs_node *parent, const char *name,
        const void *ns);
int kernfs_rename_ns(struct kernfs_node *kn, struct kernfs_node *new_parent,
       const char *new_name, const void *new_ns);
int kernfs_setattr(struct kernfs_node *kn, const struct iattr *iattr);
void kernfs_notify(struct kernfs_node *kn);

const void *kernfs_super_ns(struct super_block *sb);
struct dentry *kernfs_mount_ns(struct file_system_type *fs_type, int flags,
          struct kernfs_root *root, unsigned long magic,
          bool *new_sb_created, const void *ns);
void kernfs_kill_sb(struct super_block *sb);
struct super_block *kernfs_pin_sb(struct kernfs_root *root, const void *ns);

void kernfs_init(void);
# 410 "include/linux/kernfs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kernfs_node *
kernfs_find_and_get(struct kernfs_node *kn, const char *name)
{
 return kernfs_find_and_get_ns(kn, name, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kernfs_node *
kernfs_create_dir(struct kernfs_node *parent, const char *name, umode_t mode,
    void *priv)
{
 return kernfs_create_dir_ns(parent, name, mode, priv, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kernfs_node *
kernfs_create_file_ns(struct kernfs_node *parent, const char *name,
        umode_t mode, loff_t size, const struct kernfs_ops *ops,
        void *priv, const void *ns)
{
 struct lock_class_key *key = ((void *)0);




 return __kernfs_create_file(parent, name, mode, size, ops, priv, ns,
        false, key);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kernfs_node *
kernfs_create_file(struct kernfs_node *parent, const char *name, umode_t mode,
     loff_t size, const struct kernfs_ops *ops, void *priv)
{
 return kernfs_create_file_ns(parent, name, mode, size, ops, priv, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kernfs_remove_by_name(struct kernfs_node *parent,
     const char *name)
{
 return kernfs_remove_by_name_ns(parent, name, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int kernfs_rename(struct kernfs_node *kn,
    struct kernfs_node *new_parent,
    const char *new_name)
{
 return kernfs_rename_ns(kn, new_parent, new_name, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct dentry *
kernfs_mount(struct file_system_type *fs_type, int flags,
  struct kernfs_root *root, unsigned long magic,
  bool *new_sb_created)
{
 return kernfs_mount_ns(fs_type, flags, root,
    magic, new_sb_created, ((void *)0));
}
# 16 "include/linux/sysfs.h" 2




# 1 "include/linux/kobject_ns.h" 1
# 20 "include/linux/kobject_ns.h"
struct sock;
struct kobject;





enum kobj_ns_type {
 KOBJ_NS_TYPE_NONE = 0,
 KOBJ_NS_TYPE_NET,
 KOBJ_NS_TYPES
};
# 40 "include/linux/kobject_ns.h"
struct kobj_ns_type_operations {
 enum kobj_ns_type type;
 bool (*current_may_mount)(void);
 void *(*grab_current_ns)(void);
 const void *(*netlink_ns)(struct sock *sk);
 const void *(*initial_ns)(void);
 void (*drop_ns)(void *);
};

int kobj_ns_type_register(const struct kobj_ns_type_operations *ops);
int kobj_ns_type_registered(enum kobj_ns_type type);
const struct kobj_ns_type_operations *kobj_child_ns_ops(struct kobject *parent);
const struct kobj_ns_type_operations *kobj_ns_ops(struct kobject *kobj);

bool kobj_ns_current_may_mount(enum kobj_ns_type type);
void *kobj_ns_grab_current(enum kobj_ns_type type);
const void *kobj_ns_netlink(enum kobj_ns_type type, struct sock *sk);
const void *kobj_ns_initial(enum kobj_ns_type type);
void kobj_ns_drop(enum kobj_ns_type type, void *ns);
# 21 "include/linux/sysfs.h" 2
# 1 "include/linux/stat.h" 1




# 1 "./arch/mips/include/uapi/asm/stat.h" 1
# 18 "./arch/mips/include/uapi/asm/stat.h"
struct stat {
 unsigned st_dev;
 long st_pad1[3];
 ino_t st_ino;
 mode_t st_mode;
 __u32 st_nlink;
 uid_t st_uid;
 gid_t st_gid;
 unsigned st_rdev;
 long st_pad2[2];
 off_t st_size;
 long st_pad3;




 time_t st_atime;
 long st_atime_nsec;
 time_t st_mtime;
 long st_mtime_nsec;
 time_t st_ctime;
 long st_ctime_nsec;
 long st_blksize;
 long st_blocks;
 long st_pad4[14];
};







struct stat64 {
 unsigned long st_dev;
 unsigned long st_pad0[3];

 unsigned long long st_ino;

 mode_t st_mode;
 __u32 st_nlink;

 uid_t st_uid;
 gid_t st_gid;

 unsigned long st_rdev;
 unsigned long st_pad1[3];

 long long st_size;





 time_t st_atime;
 unsigned long st_atime_nsec;

 time_t st_mtime;
 unsigned long st_mtime_nsec;

 time_t st_ctime;
 unsigned long st_ctime_nsec;

 unsigned long st_blksize;
 unsigned long st_pad2;

 long long st_blocks;
};
# 6 "include/linux/stat.h" 2
# 1 "include/uapi/linux/stat.h" 1
# 7 "include/linux/stat.h" 2
# 19 "include/linux/stat.h"
# 1 "include/linux/uidgid.h" 1
# 15 "include/linux/uidgid.h"
# 1 "include/linux/highuid.h" 1
# 34 "include/linux/highuid.h"
extern int overflowuid;
extern int overflowgid;

extern void __bad_uid(void);
extern void __bad_gid(void);
# 81 "include/linux/highuid.h"
extern int fs_overflowuid;
extern int fs_overflowgid;
# 16 "include/linux/uidgid.h" 2

struct user_namespace;
extern struct user_namespace init_user_ns;

typedef struct {
 uid_t val;
} kuid_t;


typedef struct {
 gid_t val;
} kgid_t;




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) uid_t __kuid_val(kuid_t uid)
{
 return uid.val;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) gid_t __kgid_val(kgid_t gid)
{
 return gid.val;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uid_eq(kuid_t left, kuid_t right)
{
 return __kuid_val(left) == __kuid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool gid_eq(kgid_t left, kgid_t right)
{
 return __kgid_val(left) == __kgid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uid_gt(kuid_t left, kuid_t right)
{
 return __kuid_val(left) > __kuid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool gid_gt(kgid_t left, kgid_t right)
{
 return __kgid_val(left) > __kgid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uid_gte(kuid_t left, kuid_t right)
{
 return __kuid_val(left) >= __kuid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool gid_gte(kgid_t left, kgid_t right)
{
 return __kgid_val(left) >= __kgid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uid_lt(kuid_t left, kuid_t right)
{
 return __kuid_val(left) < __kuid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool gid_lt(kgid_t left, kgid_t right)
{
 return __kgid_val(left) < __kgid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uid_lte(kuid_t left, kuid_t right)
{
 return __kuid_val(left) <= __kuid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool gid_lte(kgid_t left, kgid_t right)
{
 return __kgid_val(left) <= __kgid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool uid_valid(kuid_t uid)
{
 return !uid_eq(uid, (kuid_t){ -1 });
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool gid_valid(kgid_t gid)
{
 return !gid_eq(gid, (kgid_t){ -1 });
}
# 130 "include/linux/uidgid.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kuid_t make_kuid(struct user_namespace *from, uid_t uid)
{
 return (kuid_t){ uid };
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kgid_t make_kgid(struct user_namespace *from, gid_t gid)
{
 return (kgid_t){ gid };
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) uid_t from_kuid(struct user_namespace *to, kuid_t kuid)
{
 return __kuid_val(kuid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) gid_t from_kgid(struct user_namespace *to, kgid_t kgid)
{
 return __kgid_val(kgid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) uid_t from_kuid_munged(struct user_namespace *to, kuid_t kuid)
{
 uid_t uid = from_kuid(to, kuid);
 if (uid == (uid_t)-1)
  uid = overflowuid;
 return uid;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) gid_t from_kgid_munged(struct user_namespace *to, kgid_t kgid)
{
 gid_t gid = from_kgid(to, kgid);
 if (gid == (gid_t)-1)
  gid = overflowgid;
 return gid;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool kuid_has_mapping(struct user_namespace *ns, kuid_t uid)
{
 return true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool kgid_has_mapping(struct user_namespace *ns, kgid_t gid)
{
 return true;
}
# 20 "include/linux/stat.h" 2

struct kstat {
 u64 ino;
 dev_t dev;
 umode_t mode;
 unsigned int nlink;
 kuid_t uid;
 kgid_t gid;
 dev_t rdev;
 loff_t size;
 struct timespec atime;
 struct timespec mtime;
 struct timespec ctime;
 unsigned long blksize;
 unsigned long long blocks;
};
# 22 "include/linux/sysfs.h" 2


struct kobject;
struct module;
struct bin_attribute;
enum kobj_ns_type;

struct attribute {
 const char *name;
 umode_t mode;





};
# 60 "include/linux/sysfs.h"
struct attribute_group {
 const char *name;
 umode_t (*is_visible)(struct kobject *,
           struct attribute *, int);
 struct attribute **attrs;
 struct bin_attribute **bin_attrs;
};
# 118 "include/linux/sysfs.h"
struct file;
struct vm_area_struct;

struct bin_attribute {
 struct attribute attr;
 size_t size;
 void *private;
 ssize_t (*read)(struct file *, struct kobject *, struct bin_attribute *,
   char *, loff_t, size_t);
 ssize_t (*write)(struct file *, struct kobject *, struct bin_attribute *,
    char *, loff_t, size_t);
 int (*mmap)(struct file *, struct kobject *, struct bin_attribute *attr,
      struct vm_area_struct *vma);
};
# 175 "include/linux/sysfs.h"
struct sysfs_ops {
 ssize_t (*show)(struct kobject *, struct attribute *, char *);
 ssize_t (*store)(struct kobject *, struct attribute *, const char *, size_t);
};



int sysfs_create_dir_ns(struct kobject *kobj, const void *ns);
void sysfs_remove_dir(struct kobject *kobj);
int sysfs_rename_dir_ns(struct kobject *kobj, const char *new_name,
         const void *new_ns);
int sysfs_move_dir_ns(struct kobject *kobj,
       struct kobject *new_parent_kobj,
       const void *new_ns);

int sysfs_create_file_ns(struct kobject *kobj,
          const struct attribute *attr,
          const void *ns);
int sysfs_create_files(struct kobject *kobj,
       const struct attribute **attr);
int sysfs_chmod_file(struct kobject *kobj,
      const struct attribute *attr, umode_t mode);
void sysfs_remove_file_ns(struct kobject *kobj, const struct attribute *attr,
     const void *ns);
bool sysfs_remove_file_self(struct kobject *kobj, const struct attribute *attr);
void sysfs_remove_files(struct kobject *kobj, const struct attribute **attr);

int sysfs_create_bin_file(struct kobject *kobj,
           const struct bin_attribute *attr);
void sysfs_remove_bin_file(struct kobject *kobj,
      const struct bin_attribute *attr);

int sysfs_create_link(struct kobject *kobj, struct kobject *target,
       const char *name);
int sysfs_create_link_nowarn(struct kobject *kobj,
       struct kobject *target,
       const char *name);
void sysfs_remove_link(struct kobject *kobj, const char *name);

int sysfs_rename_link_ns(struct kobject *kobj, struct kobject *target,
    const char *old_name, const char *new_name,
    const void *new_ns);

void sysfs_delete_link(struct kobject *dir, struct kobject *targ,
   const char *name);

int sysfs_create_group(struct kobject *kobj,
        const struct attribute_group *grp);
int sysfs_create_groups(struct kobject *kobj,
         const struct attribute_group **groups);
int sysfs_update_group(struct kobject *kobj,
         const struct attribute_group *grp);
void sysfs_remove_group(struct kobject *kobj,
   const struct attribute_group *grp);
void sysfs_remove_groups(struct kobject *kobj,
    const struct attribute_group **groups);
int sysfs_add_file_to_group(struct kobject *kobj,
   const struct attribute *attr, const char *group);
void sysfs_remove_file_from_group(struct kobject *kobj,
   const struct attribute *attr, const char *group);
int sysfs_merge_group(struct kobject *kobj,
         const struct attribute_group *grp);
void sysfs_unmerge_group(struct kobject *kobj,
         const struct attribute_group *grp);
int sysfs_add_link_to_group(struct kobject *kobj, const char *group_name,
       struct kobject *target, const char *link_name);
void sysfs_remove_link_from_group(struct kobject *kobj, const char *group_name,
      const char *link_name);

void sysfs_notify(struct kobject *kobj, const char *dir, const char *attr);

int sysfs_init(void);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sysfs_enable_ns(struct kernfs_node *kn)
{
 return kernfs_enable_ns(kn);
}
# 431 "include/linux/sysfs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int sysfs_create_file(struct kobject *kobj,
       const struct attribute *attr)
{
 return sysfs_create_file_ns(kobj, attr, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sysfs_remove_file(struct kobject *kobj,
         const struct attribute *attr)
{
 sysfs_remove_file_ns(kobj, attr, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int sysfs_rename_link(struct kobject *kobj, struct kobject *target,
        const char *old_name, const char *new_name)
{
 return sysfs_rename_link_ns(kobj, target, old_name, new_name, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sysfs_notify_dirent(struct kernfs_node *kn)
{
 kernfs_notify(kn);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kernfs_node *sysfs_get_dirent(struct kernfs_node *parent,
         const unsigned char *name)
{
 return kernfs_find_and_get(parent, name);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kernfs_node *sysfs_get(struct kernfs_node *kn)
{
 kernfs_get(kn);
 return kn;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sysfs_put(struct kernfs_node *kn)
{
 kernfs_put(kn);
}
# 22 "include/linux/kobject.h" 2
# 35 "include/linux/kobject.h"
struct sk_buff;



extern char uevent_helper[];



extern u64 uevent_seqnum;
# 55 "include/linux/kobject.h"
enum kobject_action {
 KOBJ_ADD,
 KOBJ_REMOVE,
 KOBJ_CHANGE,
 KOBJ_MOVE,
 KOBJ_ONLINE,
 KOBJ_OFFLINE,
 KOBJ_MAX
};

struct kobject {
 const char *name;
 struct list_head entry;
 struct kobject *parent;
 struct kset *kset;
 struct kobj_type *ktype;
 struct kernfs_node *sd;
 struct kref kref;



 unsigned int state_initialized:1;
 unsigned int state_in_sysfs:1;
 unsigned int state_add_uevent_sent:1;
 unsigned int state_remove_uevent_sent:1;
 unsigned int uevent_suppress:1;
};

extern __attribute__((format(printf, 2, 3)))
int kobject_set_name(struct kobject *kobj, const char *name, ...);
extern int kobject_set_name_vargs(struct kobject *kobj, const char *fmt,
      va_list vargs);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) const char *kobject_name(const struct kobject *kobj)
{
 return kobj->name;
}

extern void kobject_init(struct kobject *kobj, struct kobj_type *ktype);
extern __attribute__((format(printf, 3, 4)))
int kobject_add(struct kobject *kobj, struct kobject *parent,
  const char *fmt, ...);
extern __attribute__((format(printf, 4, 5)))
int kobject_init_and_add(struct kobject *kobj,
    struct kobj_type *ktype, struct kobject *parent,
    const char *fmt, ...);

extern void kobject_del(struct kobject *kobj);

extern struct kobject * kobject_create(void);
extern struct kobject * kobject_create_and_add(const char *name,
      struct kobject *parent);

extern int kobject_rename(struct kobject *, const char *new_name);
extern int kobject_move(struct kobject *, struct kobject *);

extern struct kobject *kobject_get(struct kobject *kobj);
extern void kobject_put(struct kobject *kobj);

extern const void *kobject_namespace(struct kobject *kobj);
extern char *kobject_get_path(struct kobject *kobj, gfp_t flag);

struct kobj_type {
 void (*release)(struct kobject *kobj);
 const struct sysfs_ops *sysfs_ops;
 struct attribute **default_attrs;
 const struct kobj_ns_type_operations *(*child_ns_type)(struct kobject *kobj);
 const void *(*namespace)(struct kobject *kobj);
};

struct kobj_uevent_env {
 char *argv[3];
 char *envp[32];
 int envp_idx;
 char buf[2048];
 int buflen;
};

struct kset_uevent_ops {
 int (* const filter)(struct kset *kset, struct kobject *kobj);
 const char *(* const name)(struct kset *kset, struct kobject *kobj);
 int (* const uevent)(struct kset *kset, struct kobject *kobj,
        struct kobj_uevent_env *env);
};

struct kobj_attribute {
 struct attribute attr;
 ssize_t (*show)(struct kobject *kobj, struct kobj_attribute *attr,
   char *buf);
 ssize_t (*store)(struct kobject *kobj, struct kobj_attribute *attr,
    const char *buf, size_t count);
};

extern const struct sysfs_ops kobj_sysfs_ops;

struct sock;
# 169 "include/linux/kobject.h"
struct kset {
 struct list_head list;
 spinlock_t list_lock;
 struct kobject kobj;
 const struct kset_uevent_ops *uevent_ops;
};

extern void kset_init(struct kset *kset);
extern int kset_register(struct kset *kset);
extern void kset_unregister(struct kset *kset);
extern struct kset * kset_create_and_add(const char *name,
      const struct kset_uevent_ops *u,
      struct kobject *parent_kobj);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kset *to_kset(struct kobject *kobj)
{
 return kobj ? ({ const typeof( ((struct kset *)0)->kobj ) *__mptr = (kobj); (struct kset *)( (char *)__mptr - __builtin_offsetof(struct kset,kobj) );}) : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kset *kset_get(struct kset *k)
{
 return k ? to_kset(kobject_get(&k->kobj)) : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void kset_put(struct kset *k)
{
 kobject_put(&k->kobj);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kobj_type *get_ktype(struct kobject *kobj)
{
 return kobj->ktype;
}

extern struct kobject *kset_find_obj(struct kset *, const char *);


extern struct kobject *kernel_kobj;

extern struct kobject *mm_kobj;

extern struct kobject *hypervisor_kobj;

extern struct kobject *power_kobj;

extern struct kobject *firmware_kobj;

int kobject_uevent(struct kobject *kobj, enum kobject_action action);
int kobject_uevent_env(struct kobject *kobj, enum kobject_action action,
   char *envp[]);

__attribute__((format(printf, 2, 3)))
int add_uevent_var(struct kobj_uevent_env *env, const char *format, ...);

int kobject_action_type(const char *buf, size_t count,
   enum kobject_action *type);

int broadcast_uevent(struct sk_buff *skb, __u32 pid, __u32 group,
       gfp_t allocation);
# 18 "include/linux/device.h" 2
# 1 "include/linux/klist.h" 1
# 19 "include/linux/klist.h"
struct klist_node;
struct klist {
 spinlock_t k_lock;
 struct list_head k_list;
 void (*get)(struct klist_node *);
 void (*put)(struct klist_node *);
} __attribute__ ((aligned (sizeof(void *))));
# 36 "include/linux/klist.h"
extern void klist_init(struct klist *k, void (*get)(struct klist_node *),
         void (*put)(struct klist_node *));

struct klist_node {
 void *n_klist;
 struct list_head n_node;
 struct kref n_ref;
};

extern void klist_add_tail(struct klist_node *n, struct klist *k);
extern void klist_add_head(struct klist_node *n, struct klist *k);
extern void klist_add_behind(struct klist_node *n, struct klist_node *pos);
extern void klist_add_before(struct klist_node *n, struct klist_node *pos);

extern void klist_del(struct klist_node *n);
extern void klist_remove(struct klist_node *n);

extern int klist_node_attached(struct klist_node *n);


struct klist_iter {
 struct klist *i_klist;
 struct klist_node *i_cur;
};


extern void klist_iter_init(struct klist *k, struct klist_iter *i);
extern void klist_iter_init_node(struct klist *k, struct klist_iter *i,
     struct klist_node *n);
extern void klist_iter_exit(struct klist_iter *i);
extern struct klist_node *klist_next(struct klist_iter *i);
# 19 "include/linux/device.h" 2





# 1 "include/linux/pinctrl/devinfo.h" 1
# 43 "include/linux/pinctrl/devinfo.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int pinctrl_bind_pins(struct device *dev)
{
 return 0;
}
# 25 "include/linux/device.h" 2
# 1 "include/linux/pm.h" 1
# 34 "include/linux/pm.h"
extern void (*pm_power_off)(void);
extern void (*pm_power_off_prepare)(void);

struct device;




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pm_vt_switch_required(struct device *dev, bool required)
{
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pm_vt_switch_unregister(struct device *dev)
{
}






struct device;







typedef struct pm_message {
 int event;
} pm_message_t;
# 295 "include/linux/pm.h"
struct dev_pm_ops {
 int (*prepare)(struct device *dev);
 void (*complete)(struct device *dev);
 int (*suspend)(struct device *dev);
 int (*resume)(struct device *dev);
 int (*freeze)(struct device *dev);
 int (*thaw)(struct device *dev);
 int (*poweroff)(struct device *dev);
 int (*restore)(struct device *dev);
 int (*suspend_late)(struct device *dev);
 int (*resume_early)(struct device *dev);
 int (*freeze_late)(struct device *dev);
 int (*thaw_early)(struct device *dev);
 int (*poweroff_late)(struct device *dev);
 int (*restore_early)(struct device *dev);
 int (*suspend_noirq)(struct device *dev);
 int (*resume_noirq)(struct device *dev);
 int (*freeze_noirq)(struct device *dev);
 int (*thaw_noirq)(struct device *dev);
 int (*poweroff_noirq)(struct device *dev);
 int (*restore_noirq)(struct device *dev);
 int (*runtime_suspend)(struct device *dev);
 int (*runtime_resume)(struct device *dev);
 int (*runtime_idle)(struct device *dev);
};
# 510 "include/linux/pm.h"
enum rpm_status {
 RPM_ACTIVE = 0,
 RPM_RESUMING,
 RPM_SUSPENDED,
 RPM_SUSPENDING,
};
# 532 "include/linux/pm.h"
enum rpm_request {
 RPM_REQ_NONE = 0,
 RPM_REQ_IDLE,
 RPM_REQ_SUSPEND,
 RPM_REQ_AUTOSUSPEND,
 RPM_REQ_RESUME,
};

struct wakeup_source;

struct pm_domain_data {
 struct list_head list_node;
 struct device *dev;
};

struct pm_subsys_data {
 spinlock_t lock;
 unsigned int refcount;






};

struct dev_pm_info {
 pm_message_t power_state;
 unsigned int can_wakeup:1;
 unsigned int async_suspend:1;
 bool is_prepared:1;
 bool is_suspended:1;
 bool is_noirq_suspended:1;
 bool is_late_suspended:1;
 bool ignore_children:1;
 bool early_init:1;
 bool direct_complete:1;
 spinlock_t lock;







 unsigned int should_wakeup:1;
# 606 "include/linux/pm.h"
 struct pm_subsys_data *subsys_data;
 void (*set_latency_tolerance)(struct device *, s32);
 struct dev_pm_qos *qos;
};

extern void update_pm_runtime_accounting(struct device *dev);
extern int dev_pm_get_subsys_data(struct device *dev);
extern int dev_pm_put_subsys_data(struct device *dev);






struct dev_pm_domain {
 struct dev_pm_ops ops;
 void (*detach)(struct device *dev, bool power_off);
};
# 732 "include/linux/pm.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int dpm_suspend_start(pm_message_t state)
{
 return 0;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_pm_wait_for_dev(struct device *a, struct device *b)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dpm_for_each_dev(void *data, void (*fn)(struct device *, void *))
{
}
# 771 "include/linux/pm.h"
enum dpm_order {
 DPM_ORDER_NONE,
 DPM_ORDER_DEV_AFTER_PARENT,
 DPM_ORDER_PARENT_BEFORE_DEV,
 DPM_ORDER_DEV_LAST,
};
# 26 "include/linux/device.h" 2

# 1 "include/linux/ratelimit.h" 1
# 10 "include/linux/ratelimit.h"
struct ratelimit_state {
 raw_spinlock_t lock;

 int interval;
 int burst;
 int printed;
 int missed;
 unsigned long begin;
};
# 28 "include/linux/ratelimit.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ratelimit_state_init(struct ratelimit_state *rs,
     int interval, int burst)
{
 do { *(&rs->lock) = (raw_spinlock_t) { .raw_lock = { }, }; } while (0);
 rs->interval = interval;
 rs->burst = burst;
 rs->printed = 0;
 rs->missed = 0;
 rs->begin = 0;
}

extern struct ratelimit_state printk_ratelimit_state;

extern int ___ratelimit(struct ratelimit_state *rs, const char *func);
# 28 "include/linux/device.h" 2


# 1 "./arch/mips/include/asm/device.h" 1
# 9 "./arch/mips/include/asm/device.h"
struct dma_map_ops;

struct dev_archdata {

 struct dma_map_ops *dma_ops;
};

struct pdev_archdata {
};
# 31 "include/linux/device.h" 2

struct device;
struct device_private;
struct device_driver;
struct driver_private;
struct module;
struct class;
struct subsys_private;
struct bus_type;
struct device_node;
struct iommu_ops;
struct iommu_group;

struct bus_attribute {
 struct attribute attr;
 ssize_t (*show)(struct bus_type *bus, char *buf);
 ssize_t (*store)(struct bus_type *bus, const char *buf, size_t count);
};
# 57 "include/linux/device.h"
extern int bus_create_file(struct bus_type *,
     struct bus_attribute *);
extern void bus_remove_file(struct bus_type *, struct bus_attribute *);
# 104 "include/linux/device.h"
struct bus_type {
 const char *name;
 const char *dev_name;
 struct device *dev_root;
 struct device_attribute *dev_attrs;
 const struct attribute_group **bus_groups;
 const struct attribute_group **dev_groups;
 const struct attribute_group **drv_groups;

 int (*match)(struct device *dev, struct device_driver *drv);
 int (*uevent)(struct device *dev, struct kobj_uevent_env *env);
 int (*probe)(struct device *dev);
 int (*remove)(struct device *dev);
 void (*shutdown)(struct device *dev);

 int (*online)(struct device *dev);
 int (*offline)(struct device *dev);

 int (*suspend)(struct device *dev, pm_message_t state);
 int (*resume)(struct device *dev);

 const struct dev_pm_ops *pm;

 const struct iommu_ops *iommu_ops;

 struct subsys_private *p;
 struct lock_class_key lock_key;
};

extern int bus_register(struct bus_type *bus);

extern void bus_unregister(struct bus_type *bus);

extern int bus_rescan_devices(struct bus_type *bus);


struct subsys_dev_iter {
 struct klist_iter ki;
 const struct device_type *type;
};
void subsys_dev_iter_init(struct subsys_dev_iter *iter,
    struct bus_type *subsys,
    struct device *start,
    const struct device_type *type);
struct device *subsys_dev_iter_next(struct subsys_dev_iter *iter);
void subsys_dev_iter_exit(struct subsys_dev_iter *iter);

int bus_for_each_dev(struct bus_type *bus, struct device *start, void *data,
       int (*fn)(struct device *dev, void *data));
struct device *bus_find_device(struct bus_type *bus, struct device *start,
          void *data,
          int (*match)(struct device *dev, void *data));
struct device *bus_find_device_by_name(struct bus_type *bus,
           struct device *start,
           const char *name);
struct device *subsys_find_device_by_id(struct bus_type *bus, unsigned int id,
     struct device *hint);
int bus_for_each_drv(struct bus_type *bus, struct device_driver *start,
       void *data, int (*fn)(struct device_driver *, void *));
void bus_sort_breadthfirst(struct bus_type *bus,
      int (*compare)(const struct device *a,
       const struct device *b));






struct notifier_block;

extern int bus_register_notifier(struct bus_type *bus,
     struct notifier_block *nb);
extern int bus_unregister_notifier(struct bus_type *bus,
       struct notifier_block *nb);
# 194 "include/linux/device.h"
extern struct kset *bus_get_kset(struct bus_type *bus);
extern struct klist *bus_get_device_klist(struct bus_type *bus);
# 229 "include/linux/device.h"
struct device_driver {
 const char *name;
 struct bus_type *bus;

 struct module *owner;
 const char *mod_name;

 bool suppress_bind_attrs;

 const struct of_device_id *of_match_table;
 const struct acpi_device_id *acpi_match_table;

 int (*probe) (struct device *dev);
 int (*remove) (struct device *dev);
 void (*shutdown) (struct device *dev);
 int (*suspend) (struct device *dev, pm_message_t state);
 int (*resume) (struct device *dev);
 const struct attribute_group **groups;

 const struct dev_pm_ops *pm;

 struct driver_private *p;
};


extern int driver_register(struct device_driver *drv);
extern void driver_unregister(struct device_driver *drv);

extern struct device_driver *driver_find(const char *name,
      struct bus_type *bus);
extern int driver_probe_done(void);
extern void wait_for_device_probe(void);




struct driver_attribute {
 struct attribute attr;
 ssize_t (*show)(struct device_driver *driver, char *buf);
 ssize_t (*store)(struct device_driver *driver, const char *buf,
    size_t count);
};
# 281 "include/linux/device.h"
extern int driver_create_file(struct device_driver *driver,
     const struct driver_attribute *attr);
extern void driver_remove_file(struct device_driver *driver,
          const struct driver_attribute *attr);

extern int driver_for_each_device(struct device_driver *drv,
            struct device *start,
            void *data,
            int (*fn)(struct device *dev,
        void *));
struct device *driver_find_device(struct device_driver *drv,
      struct device *start, void *data,
      int (*match)(struct device *dev, void *data));
# 308 "include/linux/device.h"
struct subsys_interface {
 const char *name;
 struct bus_type *subsys;
 struct list_head node;
 int (*add_dev)(struct device *dev, struct subsys_interface *sif);
 int (*remove_dev)(struct device *dev, struct subsys_interface *sif);
};

int subsys_interface_register(struct subsys_interface *sif);
void subsys_interface_unregister(struct subsys_interface *sif);

int subsys_system_register(struct bus_type *subsys,
      const struct attribute_group **groups);
int subsys_virtual_register(struct bus_type *subsys,
       const struct attribute_group **groups);
# 352 "include/linux/device.h"
struct class {
 const char *name;
 struct module *owner;

 struct class_attribute *class_attrs;
 const struct attribute_group **dev_groups;
 struct kobject *dev_kobj;

 int (*dev_uevent)(struct device *dev, struct kobj_uevent_env *env);
 char *(*devnode)(struct device *dev, umode_t *mode);

 void (*class_release)(struct class *class);
 void (*dev_release)(struct device *dev);

 int (*suspend)(struct device *dev, pm_message_t state);
 int (*resume)(struct device *dev);

 const struct kobj_ns_type_operations *ns_type;
 const void *(*namespace)(struct device *dev);

 const struct dev_pm_ops *pm;

 struct subsys_private *p;
};

struct class_dev_iter {
 struct klist_iter ki;
 const struct device_type *type;
};

extern struct kobject *sysfs_dev_block_kobj;
extern struct kobject *sysfs_dev_char_kobj;
extern int __class_register(struct class *class,
      struct lock_class_key *key);
extern void class_unregister(struct class *class);
# 396 "include/linux/device.h"
struct class_compat;
struct class_compat *class_compat_register(const char *name);
void class_compat_unregister(struct class_compat *cls);
int class_compat_create_link(struct class_compat *cls, struct device *dev,
        struct device *device_link);
void class_compat_remove_link(struct class_compat *cls, struct device *dev,
         struct device *device_link);

extern void class_dev_iter_init(struct class_dev_iter *iter,
    struct class *class,
    struct device *start,
    const struct device_type *type);
extern struct device *class_dev_iter_next(struct class_dev_iter *iter);
extern void class_dev_iter_exit(struct class_dev_iter *iter);

extern int class_for_each_device(struct class *class, struct device *start,
     void *data,
     int (*fn)(struct device *dev, void *data));
extern struct device *class_find_device(struct class *class,
     struct device *start, const void *data,
     int (*match)(struct device *, const void *));

struct class_attribute {
 struct attribute attr;
 ssize_t (*show)(struct class *class, struct class_attribute *attr,
   char *buf);
 ssize_t (*store)(struct class *class, struct class_attribute *attr,
   const char *buf, size_t count);
};
# 433 "include/linux/device.h"
extern int class_create_file_ns(struct class *class,
          const struct class_attribute *attr,
          const void *ns);
extern void class_remove_file_ns(struct class *class,
     const struct class_attribute *attr,
     const void *ns);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int class_create_file(struct class *class,
     const struct class_attribute *attr)
{
 return class_create_file_ns(class, attr, ((void *)0));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void class_remove_file(struct class *class,
         const struct class_attribute *attr)
{
 return class_remove_file_ns(class, attr, ((void *)0));
}


struct class_attribute_string {
 struct class_attribute attr;
 char *str;
};
# 465 "include/linux/device.h"
extern ssize_t show_class_attr_string(struct class *class, struct class_attribute *attr,
                        char *buf);

struct class_interface {
 struct list_head node;
 struct class *class;

 int (*add_dev) (struct device *, struct class_interface *);
 void (*remove_dev) (struct device *, struct class_interface *);
};

extern int class_interface_register(struct class_interface *);
extern void class_interface_unregister(struct class_interface *);

extern struct class * __class_create(struct module *owner,
        const char *name,
        struct lock_class_key *key);
extern void class_destroy(struct class *cls);
# 501 "include/linux/device.h"
struct device_type {
 const char *name;
 const struct attribute_group **groups;
 int (*uevent)(struct device *dev, struct kobj_uevent_env *env);
 char *(*devnode)(struct device *dev, umode_t *mode,
    kuid_t *uid, kgid_t *gid);
 void (*release)(struct device *dev);

 const struct dev_pm_ops *pm;
};


struct device_attribute {
 struct attribute attr;
 ssize_t (*show)(struct device *dev, struct device_attribute *attr,
   char *buf);
 ssize_t (*store)(struct device *dev, struct device_attribute *attr,
    const char *buf, size_t count);
};

struct dev_ext_attribute {
 struct device_attribute attr;
 void *var;
};

ssize_t device_show_ulong(struct device *dev, struct device_attribute *attr,
     char *buf);
ssize_t device_store_ulong(struct device *dev, struct device_attribute *attr,
      const char *buf, size_t count);
ssize_t device_show_int(struct device *dev, struct device_attribute *attr,
   char *buf);
ssize_t device_store_int(struct device *dev, struct device_attribute *attr,
    const char *buf, size_t count);
ssize_t device_show_bool(struct device *dev, struct device_attribute *attr,
   char *buf);
ssize_t device_store_bool(struct device *dev, struct device_attribute *attr,
    const char *buf, size_t count);
# 560 "include/linux/device.h"
extern int device_create_file(struct device *device,
         const struct device_attribute *entry);
extern void device_remove_file(struct device *dev,
          const struct device_attribute *attr);
extern bool device_remove_file_self(struct device *dev,
        const struct device_attribute *attr);
extern int device_create_bin_file(struct device *dev,
     const struct bin_attribute *attr);
extern void device_remove_bin_file(struct device *dev,
       const struct bin_attribute *attr);


typedef void (*dr_release_t)(struct device *dev, void *res);
typedef int (*dr_match_t)(struct device *dev, void *res, void *match_data);







extern void *devres_alloc(dr_release_t release, size_t size, gfp_t gfp);

extern void devres_for_each_res(struct device *dev, dr_release_t release,
    dr_match_t match, void *match_data,
    void (*fn)(struct device *, void *, void *),
    void *data);
extern void devres_free(void *res);
extern void devres_add(struct device *dev, void *res);
extern void *devres_find(struct device *dev, dr_release_t release,
    dr_match_t match, void *match_data);
extern void *devres_get(struct device *dev, void *new_res,
   dr_match_t match, void *match_data);
extern void *devres_remove(struct device *dev, dr_release_t release,
      dr_match_t match, void *match_data);
extern int devres_destroy(struct device *dev, dr_release_t release,
     dr_match_t match, void *match_data);
extern int devres_release(struct device *dev, dr_release_t release,
     dr_match_t match, void *match_data);


extern void * devres_open_group(struct device *dev, void *id,
          gfp_t gfp);
extern void devres_close_group(struct device *dev, void *id);
extern void devres_remove_group(struct device *dev, void *id);
extern int devres_release_group(struct device *dev, void *id);


extern void *devm_kmalloc(struct device *dev, size_t size, gfp_t gfp);
extern char *devm_kvasprintf(struct device *dev, gfp_t gfp, const char *fmt,
        va_list ap);
extern __attribute__((format(printf, 3, 4)))
char *devm_kasprintf(struct device *dev, gfp_t gfp, const char *fmt, ...);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *devm_kzalloc(struct device *dev, size_t size, gfp_t gfp)
{
 return devm_kmalloc(dev, size, gfp | (( gfp_t)0x8000u));
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *devm_kmalloc_array(struct device *dev,
           size_t n, size_t size, gfp_t flags)
{
 if (size != 0 && n > (~(size_t)0) / size)
  return ((void *)0);
 return devm_kmalloc(dev, n * size, flags);
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *devm_kcalloc(struct device *dev,
     size_t n, size_t size, gfp_t flags)
{
 return devm_kmalloc_array(dev, n, size, flags | (( gfp_t)0x8000u));
}
extern void devm_kfree(struct device *dev, void *p);
extern char *devm_kstrdup(struct device *dev, const char *s, gfp_t gfp);
extern void *devm_kmemdup(struct device *dev, const void *src, size_t len,
     gfp_t gfp);

extern unsigned long devm_get_free_pages(struct device *dev,
      gfp_t gfp_mask, unsigned int order);
extern void devm_free_pages(struct device *dev, unsigned long addr);

void *devm_ioremap_resource(struct device *dev, struct resource *res);


int devm_add_action(struct device *dev, void (*action)(void *), void *data);
void devm_remove_action(struct device *dev, void (*action)(void *), void *data);

struct device_dma_parameters {




 unsigned int max_segment_size;
 unsigned long segment_boundary_mask;
};

struct acpi_device;

struct acpi_dev_node {



};
# 730 "include/linux/device.h"
struct device {
 struct device *parent;

 struct device_private *p;

 struct kobject kobj;
 const char *init_name;
 const struct device_type *type;

 struct mutex mutex;



 struct bus_type *bus;
 struct device_driver *driver;

 void *platform_data;

 void *driver_data;

 struct dev_pm_info power;
 struct dev_pm_domain *pm_domain;
# 760 "include/linux/device.h"
 u64 *dma_mask;
 u64 coherent_dma_mask;




 unsigned long dma_pfn_offset;

 struct device_dma_parameters *dma_parms;

 struct list_head dma_pools;

 struct dma_coherent_mem *dma_mem;






 struct dev_archdata archdata;

 struct device_node *of_node;
 struct acpi_dev_node acpi_node;

 dev_t devt;
 u32 id;

 spinlock_t devres_lock;
 struct list_head devres_head;

 struct klist_node knode_class;
 struct class *class;
 const struct attribute_group **groups;

 void (*release)(struct device *dev);
 struct iommu_group *iommu_group;

 bool offline_disabled:1;
 bool offline:1;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct device *kobj_to_dev(struct kobject *kobj)
{
 return ({ const typeof( ((struct device *)0)->kobj ) *__mptr = (kobj); (struct device *)( (char *)__mptr - __builtin_offsetof(struct device,kobj) );});
}


# 1 "include/linux/pm_wakeup.h" 1
# 46 "include/linux/pm_wakeup.h"
struct wakeup_source {
 const char *name;
 struct list_head entry;
 spinlock_t lock;
 struct timer_list timer;
 unsigned long timer_expires;
 ktime_t total_time;
 ktime_t max_time;
 ktime_t last_time;
 ktime_t start_prevent_time;
 ktime_t prevent_sleep_time;
 unsigned long event_count;
 unsigned long active_count;
 unsigned long relax_count;
 unsigned long expire_count;
 unsigned long wakeup_count;
 bool active:1;
 bool autosleep_enabled:1;
};
# 105 "include/linux/pm_wakeup.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void device_set_wakeup_capable(struct device *dev, bool capable)
{
 dev->power.can_wakeup = capable;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool device_can_wakeup(struct device *dev)
{
 return dev->power.can_wakeup;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_prepare(struct wakeup_source *ws,
      const char *name) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct wakeup_source *wakeup_source_create(const char *name)
{
 return ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_drop(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_destroy(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_add(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_remove(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct wakeup_source *wakeup_source_register(const char *name)
{
 return ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_unregister(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_wakeup_enable(struct device *dev)
{
 dev->power.should_wakeup = true;
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_wakeup_disable(struct device *dev)
{
 dev->power.should_wakeup = false;
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_set_wakeup_enable(struct device *dev, bool enable)
{
 dev->power.should_wakeup = enable;
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_init_wakeup(struct device *dev, bool val)
{
 device_set_wakeup_capable(dev, val);
 device_set_wakeup_enable(dev, val);
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool device_may_wakeup(struct device *dev)
{
 return dev->power.can_wakeup && dev->power.should_wakeup;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __pm_stay_awake(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pm_stay_awake(struct device *dev) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __pm_relax(struct wakeup_source *ws) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pm_relax(struct device *dev) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __pm_wakeup_event(struct wakeup_source *ws, unsigned int msec) {}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pm_wakeup_event(struct device *dev, unsigned int msec) {}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_init(struct wakeup_source *ws,
          const char *name)
{
 wakeup_source_prepare(ws, name);
 wakeup_source_add(ws);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void wakeup_source_trash(struct wakeup_source *ws)
{
 wakeup_source_remove(ws);
 wakeup_source_drop(ws);
}
# 808 "include/linux/device.h" 2

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) const char *dev_name(const struct device *dev)
{

 if (dev->init_name)
  return dev->init_name;

 return kobject_name(&dev->kobj);
}

extern __attribute__((format(printf, 2, 3)))
int dev_set_name(struct device *dev, const char *name, ...);
# 831 "include/linux/device.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int dev_to_node(struct device *dev)
{
 return -1;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void set_dev_node(struct device *dev, int node)
{
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *dev_get_drvdata(const struct device *dev)
{
 return dev->driver_data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dev_set_drvdata(struct device *dev, void *data)
{
 dev->driver_data = data;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct pm_subsys_data *dev_to_psd(struct device *dev)
{
 return dev ? dev->power.subsys_data : ((void *)0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int dev_get_uevent_suppress(const struct device *dev)
{
 return dev->kobj.uevent_suppress;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dev_set_uevent_suppress(struct device *dev, int val)
{
 dev->kobj.uevent_suppress = val;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_is_registered(struct device *dev)
{
 return dev->kobj.state_in_sysfs;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void device_enable_async_suspend(struct device *dev)
{
 if (!dev->power.is_prepared)
  dev->power.async_suspend = true;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void device_disable_async_suspend(struct device *dev)
{
 if (!dev->power.is_prepared)
  dev->power.async_suspend = false;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool device_async_suspend_enabled(struct device *dev)
{
 return !!dev->power.async_suspend;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void pm_suspend_ignore_children(struct device *dev, bool enable)
{
 dev->power.ignore_children = enable;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dev_pm_syscore_device(struct device *dev, bool val)
{



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void device_lock(struct device *dev)
{
 mutex_lock(&dev->mutex);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int device_trylock(struct device *dev)
{
 return mutex_trylock(&dev->mutex);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void device_unlock(struct device *dev)
{
 mutex_unlock(&dev->mutex);
}

void driver_init(void);




extern int device_register(struct device *dev);
extern void device_unregister(struct device *dev);
extern void device_initialize(struct device *dev);
extern int device_add(struct device *dev);
extern void device_del(struct device *dev);
extern int device_for_each_child(struct device *dev, void *data,
       int (*fn)(struct device *dev, void *data));
extern struct device *device_find_child(struct device *dev, void *data,
    int (*match)(struct device *dev, void *data));
extern int device_rename(struct device *dev, const char *new_name);
extern int device_move(struct device *dev, struct device *new_parent,
         enum dpm_order dpm_order);
extern const char *device_get_devnode(struct device *dev,
          umode_t *mode, kuid_t *uid, kgid_t *gid,
          const char **tmp);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool device_supports_offline(struct device *dev)
{
 return dev->bus && dev->bus->offline && dev->bus->online;
}

extern void lock_device_hotplug(void);
extern void unlock_device_hotplug(void);
extern int lock_device_hotplug_sysfs(void);
extern int device_offline(struct device *dev);
extern int device_online(struct device *dev);



extern struct device *__root_device_register(const char *name,
          struct module *owner);





extern void root_device_unregister(struct device *root);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *dev_get_platdata(const struct device *dev)
{
 return dev->platform_data;
}





extern int device_bind_driver(struct device *dev);
extern void device_release_driver(struct device *dev);
extern int device_attach(struct device *dev);
extern int driver_attach(struct device_driver *drv);
extern int device_reprobe(struct device *dev);




extern struct device *device_create_vargs(struct class *cls,
       struct device *parent,
       dev_t devt,
       void *drvdata,
       const char *fmt,
       va_list vargs);
extern __attribute__((format(printf, 5, 6)))
struct device *device_create(struct class *cls, struct device *parent,
        dev_t devt, void *drvdata,
        const char *fmt, ...);
extern __attribute__((format(printf, 6, 7)))
struct device *device_create_with_groups(struct class *cls,
        struct device *parent, dev_t devt, void *drvdata,
        const struct attribute_group **groups,
        const char *fmt, ...);
extern void device_destroy(struct class *cls, dev_t devt);







extern int (*platform_notify)(struct device *dev);

extern int (*platform_notify_remove)(struct device *dev);






extern struct device *get_device(struct device *dev);
extern void put_device(struct device *dev);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int devtmpfs_create_node(struct device *dev) { return 0; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int devtmpfs_delete_node(struct device *dev) { return 0; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int devtmpfs_mount(const char *mountpoint) { return 0; }



extern void device_shutdown(void);


extern const char *dev_driver_string(const struct device *dev);




extern __attribute__((format(printf, 3, 0)))
int dev_vprintk_emit(int level, const struct device *dev,
       const char *fmt, va_list args);
extern __attribute__((format(printf, 3, 4)))
int dev_printk_emit(int level, const struct device *dev, const char *fmt, ...);

extern __attribute__((format(printf, 3, 4)))
int dev_printk(const char *level, const struct device *dev,
        const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int dev_emerg(const struct device *dev, const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int dev_alert(const struct device *dev, const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int dev_crit(const struct device *dev, const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int dev_err(const struct device *dev, const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int dev_warn(const struct device *dev, const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int dev_notice(const struct device *dev, const char *fmt, ...);
extern __attribute__((format(printf, 2, 3)))
int _dev_info(const struct device *dev, const char *fmt, ...);
# 29 "include/linux/rtc.h" 2
# 1 "include/linux/seq_file.h" 1
# 11 "include/linux/seq_file.h"
struct seq_operations;
struct file;
struct path;
struct inode;
struct dentry;
struct user_namespace;

struct seq_file {
 char *buf;
 size_t size;
 size_t from;
 size_t count;
 size_t pad_until;
 loff_t index;
 loff_t read_pos;
 u64 version;
 struct mutex lock;
 const struct seq_operations *op;
 int poll_event;



 void *private;
};

struct seq_operations {
 void * (*start) (struct seq_file *m, loff_t *pos);
 void (*stop) (struct seq_file *m, void *v);
 void * (*next) (struct seq_file *m, void *v, loff_t *pos);
 int (*show) (struct seq_file *m, void *v);
};
# 53 "include/linux/seq_file.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) size_t seq_get_buf(struct seq_file *m, char **bufp)
{
 __BUG_ON((unsigned long)(m->count > m->size));
 if (m->count < m->size)
  *bufp = m->buf + m->count;
 else
  *bufp = ((void *)0);

 return m->size - m->count;
}
# 73 "include/linux/seq_file.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void seq_commit(struct seq_file *m, int num)
{
 if (num < 0) {
  m->count = m->size;
 } else {
  __BUG_ON((unsigned long)(m->count + num > m->size));
  m->count += num;
 }
}
# 91 "include/linux/seq_file.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void seq_setwidth(struct seq_file *m, size_t size)
{
 m->pad_until = m->count + size;
}
void seq_pad(struct seq_file *m, char c);

char *mangle_path(char *s, const char *p, const char *esc);
int seq_open(struct file *, const struct seq_operations *);
ssize_t seq_read(struct file *, char *, size_t, loff_t *);
loff_t seq_lseek(struct file *, loff_t, int);
int seq_release(struct inode *, struct file *);
int seq_escape(struct seq_file *, const char *, const char *);
int seq_putc(struct seq_file *m, char c);
int seq_puts(struct seq_file *m, const char *s);
int seq_write(struct seq_file *seq, const void *data, size_t len);

__attribute__((format(printf, 2, 3))) int seq_printf(struct seq_file *, const char *, ...);
__attribute__((format(printf, 2, 0))) int seq_vprintf(struct seq_file *, const char *, va_list args);

int seq_path(struct seq_file *, const struct path *, const char *);
int seq_dentry(struct seq_file *, struct dentry *, const char *);
int seq_path_root(struct seq_file *m, const struct path *path,
    const struct path *root, const char *esc);
int seq_bitmap(struct seq_file *m, const unsigned long *bits,
       unsigned int nr_bits);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int seq_cpumask(struct seq_file *m, const struct cpumask *mask)
{
 return seq_bitmap(m, ((mask)->bits), 1);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int seq_nodemask(struct seq_file *m, nodemask_t *mask)
{
 return seq_bitmap(m, mask->bits, (1 << 0));
}

int seq_bitmap_list(struct seq_file *m, const unsigned long *bits,
  unsigned int nr_bits);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int seq_cpumask_list(struct seq_file *m,
       const struct cpumask *mask)
{
 return seq_bitmap_list(m, ((mask)->bits), 1);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int seq_nodemask_list(struct seq_file *m, nodemask_t *mask)
{
 return seq_bitmap_list(m, mask->bits, (1 << 0));
}

int single_open(struct file *, int (*)(struct seq_file *, void *), void *);
int single_open_size(struct file *, int (*)(struct seq_file *, void *), void *, size_t);
int single_release(struct inode *, struct file *);
void *__seq_open_private(struct file *, const struct seq_operations *, int);
int seq_open_private(struct file *, const struct seq_operations *, int);
int seq_release_private(struct inode *, struct file *);
int seq_put_decimal_ull(struct seq_file *m, char delimiter,
   unsigned long long num);
int seq_put_decimal_ll(struct seq_file *m, char delimiter,
   long long num);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct user_namespace *seq_user_ns(struct seq_file *seq)
{



 extern struct user_namespace init_user_ns;
 return &init_user_ns;

}






extern struct list_head *seq_list_start(struct list_head *head,
  loff_t pos);
extern struct list_head *seq_list_start_head(struct list_head *head,
  loff_t pos);
extern struct list_head *seq_list_next(void *v, struct list_head *head,
  loff_t *ppos);





extern struct hlist_node *seq_hlist_start(struct hlist_head *head,
       loff_t pos);
extern struct hlist_node *seq_hlist_start_head(struct hlist_head *head,
            loff_t pos);
extern struct hlist_node *seq_hlist_next(void *v, struct hlist_head *head,
      loff_t *ppos);

extern struct hlist_node *seq_hlist_start_rcu(struct hlist_head *head,
           loff_t pos);
extern struct hlist_node *seq_hlist_start_head_rcu(struct hlist_head *head,
         loff_t pos);
extern struct hlist_node *seq_hlist_next_rcu(void *v,
         struct hlist_head *head,
         loff_t *ppos);


extern struct hlist_node *seq_hlist_start_percpu(struct hlist_head *head, int *cpu, loff_t pos);

extern struct hlist_node *seq_hlist_next_percpu(void *v, struct hlist_head *head, int *cpu, loff_t *pos);
# 30 "include/linux/rtc.h" 2
# 1 "include/linux/cdev.h" 1




# 1 "include/linux/kdev_t.h" 1



# 1 "include/uapi/linux/kdev_t.h" 1
# 5 "include/linux/kdev_t.h" 2
# 23 "include/linux/kdev_t.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int old_valid_dev(dev_t dev)
{
 return ((unsigned int) ((dev) >> 20)) < 256 && ((unsigned int) ((dev) & ((1U << 20) - 1))) < 256;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u16 old_encode_dev(dev_t dev)
{
 return (((unsigned int) ((dev) >> 20)) << 8) | ((unsigned int) ((dev) & ((1U << 20) - 1)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) dev_t old_decode_dev(u16 val)
{
 return ((((val >> 8) & 255) << 20) | (val & 255));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int new_valid_dev(dev_t dev)
{
 return 1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 new_encode_dev(dev_t dev)
{
 unsigned major = ((unsigned int) ((dev) >> 20));
 unsigned minor = ((unsigned int) ((dev) & ((1U << 20) - 1)));
 return (minor & 0xff) | (major << 8) | ((minor & ~0xff) << 12);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) dev_t new_decode_dev(u32 dev)
{
 unsigned major = (dev & 0xfff00) >> 8;
 unsigned minor = (dev & 0xff) | ((dev >> 12) & 0xfff00);
 return (((major) << 20) | (minor));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int huge_valid_dev(dev_t dev)
{
 return 1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 huge_encode_dev(dev_t dev)
{
 return new_encode_dev(dev);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) dev_t huge_decode_dev(u64 dev)
{
 return new_decode_dev(dev);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int sysv_valid_dev(dev_t dev)
{
 return ((unsigned int) ((dev) >> 20)) < (1<<14) && ((unsigned int) ((dev) & ((1U << 20) - 1))) < (1<<18);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 sysv_encode_dev(dev_t dev)
{
 return ((unsigned int) ((dev) & ((1U << 20) - 1))) | (((unsigned int) ((dev) >> 20)) << 18);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned sysv_major(u32 dev)
{
 return (dev >> 18) & 0x3fff;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned sysv_minor(u32 dev)
{
 return dev & 0x3ffff;
}
# 6 "include/linux/cdev.h" 2


struct file_operations;
struct inode;
struct module;

struct cdev {
 struct kobject kobj;
 struct module *owner;
 const struct file_operations *ops;
 struct list_head list;
 dev_t dev;
 unsigned int count;
};

void cdev_init(struct cdev *, const struct file_operations *);

struct cdev *cdev_alloc(void);

void cdev_put(struct cdev *p);

int cdev_add(struct cdev *, dev_t, unsigned);

void cdev_del(struct cdev *);

void cd_forget(struct inode *);

extern struct backing_dev_info directly_mappable_cdev_bdi;
# 31 "include/linux/rtc.h" 2
# 1 "include/linux/poll.h" 1
# 9 "include/linux/poll.h"
# 1 "include/linux/fs.h" 1







# 1 "include/linux/dcache.h" 1





# 1 "include/linux/rculist.h" 1
# 30 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void INIT_LIST_HEAD_RCU(struct list_head *list)
{
 (*(volatile typeof(list->next) *)&(list->next)) = list;
 (*(volatile typeof(list->prev) *)&(list->prev)) = list;
}
# 49 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __list_add_rcu(struct list_head *new,
  struct list_head *prev, struct list_head *next)
{
 new->next = next;
 new->prev = prev;
 do { do { bool __cond = !((sizeof(*&(*((struct list_head **)(&(prev)->next)))) == sizeof(int) || sizeof(*&(*((struct list_head **)(&(prev)->next)))) == sizeof(long))); extern void __compiletime_assert_54(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_54(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&(*((struct list_head **)(&(prev)->next)))) *)&(*&(*((struct list_head **)(&(prev)->next))))) = ((typeof(*(new)) *)(new)); } while (0);
 next->prev = new;
}
# 78 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_add_rcu(struct list_head *new, struct list_head *head)
{
 __list_add_rcu(new, head, head->next);
}
# 99 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_add_tail_rcu(struct list_head *new,
     struct list_head *head)
{
 __list_add_rcu(new, head->prev, head);
}
# 129 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_del_rcu(struct list_head *entry)
{
 __list_del_entry(entry);
 entry->prev = ((void *) 0x00200200 + 0);
}
# 155 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_del_init_rcu(struct hlist_node *n)
{
 if (!hlist_unhashed(n)) {
  __hlist_del(n);
  n->pprev = ((void *)0);
 }
}
# 171 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_replace_rcu(struct list_head *old,
    struct list_head *new)
{
 new->next = old->next;
 new->prev = old->prev;
 do { do { bool __cond = !((sizeof(*&(*((struct list_head **)(&(new->prev)->next)))) == sizeof(int) || sizeof(*&(*((struct list_head **)(&(new->prev)->next)))) == sizeof(long))); extern void __compiletime_assert_176(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_176(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&(*((struct list_head **)(&(new->prev)->next)))) *)&(*&(*((struct list_head **)(&(new->prev)->next))))) = ((typeof(*(new)) *)(new)); } while (0);
 new->next->prev = new;
 old->prev = ((void *) 0x00200200 + 0);
}
# 198 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void list_splice_init_rcu(struct list_head *list,
     struct list_head *head,
     void (*sync)(void))
{
 struct list_head *first = list->next;
 struct list_head *last = list->prev;
 struct list_head *at = head->next;

 if (list_empty(list))
  return;







 INIT_LIST_HEAD_RCU(list);
# 224 "include/linux/rculist.h"
 sync();
# 234 "include/linux/rculist.h"
 last->next = at;
 do { do { bool __cond = !((sizeof(*&(*((struct list_head **)(&(head)->next)))) == sizeof(int) || sizeof(*&(*((struct list_head **)(&(head)->next)))) == sizeof(long))); extern void __compiletime_assert_235(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_235(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&(*((struct list_head **)(&(head)->next)))) *)&(*&(*((struct list_head **)(&(head)->next))))) = ((typeof(*(first)) *)(first)); } while (0);
 first->prev = head;
 at->prev = last;
}
# 343 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_del_rcu(struct hlist_node *n)
{
 __hlist_del(n);
 n->pprev = ((void *) 0x00200200 + 0);
}
# 356 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_replace_rcu(struct hlist_node *old,
     struct hlist_node *new)
{
 struct hlist_node *next = old->next;

 new->next = next;
 new->pprev = old->pprev;
 do { do { bool __cond = !((sizeof(*&*(struct hlist_node **)new->pprev) == sizeof(int) || sizeof(*&*(struct hlist_node **)new->pprev) == sizeof(long))); extern void __compiletime_assert_363(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_363(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&*(struct hlist_node **)new->pprev) *)&(*&*(struct hlist_node **)new->pprev)) = ((typeof(*(new)) *)(new)); } while (0);
 if (next)
  new->next->pprev = &new->next;
 old->pprev = ((void *) 0x00200200 + 0);
}
# 395 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_head_rcu(struct hlist_node *n,
     struct hlist_head *h)
{
 struct hlist_node *first = h->first;

 n->next = first;
 n->pprev = &h->first;
 do { do { bool __cond = !((sizeof(*&(*((struct hlist_node **)(&(h)->first)))) == sizeof(int) || sizeof(*&(*((struct hlist_node **)(&(h)->first)))) == sizeof(long))); extern void __compiletime_assert_402(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_402(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&(*((struct hlist_node **)(&(h)->first)))) *)&(*&(*((struct hlist_node **)(&(h)->first))))) = ((typeof(*(n)) *)(n)); } while (0);
 if (first)
  first->pprev = &n->next;
}
# 425 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_before_rcu(struct hlist_node *n,
     struct hlist_node *next)
{
 n->pprev = next->pprev;
 n->next = next;
 do { do { bool __cond = !((sizeof(*&(*((struct hlist_node **)((n)->pprev)))) == sizeof(int) || sizeof(*&(*((struct hlist_node **)((n)->pprev)))) == sizeof(long))); extern void __compiletime_assert_430(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_430(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&(*((struct hlist_node **)((n)->pprev)))) *)&(*&(*((struct hlist_node **)((n)->pprev))))) = ((typeof(*(n)) *)(n)); } while (0);
 next->pprev = &n->next;
}
# 452 "include/linux/rculist.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_add_behind_rcu(struct hlist_node *n,
     struct hlist_node *prev)
{
 n->next = prev->next;
 n->pprev = &prev->next;
 do { do { bool __cond = !((sizeof(*&(*((struct hlist_node **)(&(prev)->next)))) == sizeof(int) || sizeof(*&(*((struct hlist_node **)(&(prev)->next)))) == sizeof(long))); extern void __compiletime_assert_457(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_457(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&(*((struct hlist_node **)(&(prev)->next)))) *)&(*&(*((struct hlist_node **)(&(prev)->next))))) = ((typeof(*(n)) *)(n)); } while (0);
 if (n->next)
  n->next->pprev = &n->next;
}
# 7 "include/linux/dcache.h" 2
# 1 "include/linux/rculist_bl.h" 1






# 1 "include/linux/list_bl.h" 1




# 1 "include/linux/bit_spinlock.h" 1
# 15 "include/linux/bit_spinlock.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bit_spin_lock(int bitnum, unsigned long *addr)
{







 __asm__ __volatile__("": : :"memory");
# 34 "include/linux/bit_spinlock.h"
 (void)0;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bit_spin_trylock(int bitnum, unsigned long *addr)
{
 __asm__ __volatile__("": : :"memory");






 (void)0;
 return 1;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void bit_spin_unlock(int bitnum, unsigned long *addr)
{






 __asm__ __volatile__("": : :"memory");
 (void)0;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __bit_spin_unlock(int bitnum, unsigned long *addr)
{






 __asm__ __volatile__("": : :"memory");
 (void)0;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int bit_spin_is_locked(int bitnum, unsigned long *addr)
{





 return 1;

}
# 6 "include/linux/list_bl.h" 2
# 33 "include/linux/list_bl.h"
struct hlist_bl_head {
 struct hlist_bl_node *first;
};

struct hlist_bl_node {
 struct hlist_bl_node *next, **pprev;
};



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void INIT_HLIST_BL_NODE(struct hlist_bl_node *h)
{
 h->next = ((void *)0);
 h->pprev = ((void *)0);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hlist_bl_unhashed(const struct hlist_bl_node *h)
{
 return !h->pprev;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct hlist_bl_node *hlist_bl_first(struct hlist_bl_head *h)
{
 return (struct hlist_bl_node *)
  ((unsigned long)h->first & ~0UL);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_set_first(struct hlist_bl_head *h,
     struct hlist_bl_node *n)
{
 ;

                        ;
 h->first = (struct hlist_bl_node *)((unsigned long)n | 0UL);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int hlist_bl_empty(const struct hlist_bl_head *h)
{
 return !((unsigned long)h->first & ~0UL);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_add_head(struct hlist_bl_node *n,
     struct hlist_bl_head *h)
{
 struct hlist_bl_node *first = hlist_bl_first(h);

 n->next = first;
 if (first)
  first->pprev = &n->next;
 n->pprev = &h->first;
 hlist_bl_set_first(h, n);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __hlist_bl_del(struct hlist_bl_node *n)
{
 struct hlist_bl_node *next = n->next;
 struct hlist_bl_node **pprev = n->pprev;

 ;


 *pprev = (struct hlist_bl_node *)
   ((unsigned long)next |
    ((unsigned long)*pprev & 0UL));
 if (next)
  next->pprev = pprev;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_del(struct hlist_bl_node *n)
{
 __hlist_bl_del(n);
 n->next = ((void *) 0x00100100 + 0);
 n->pprev = ((void *) 0x00200200 + 0);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_del_init(struct hlist_bl_node *n)
{
 if (!hlist_bl_unhashed(n)) {
  __hlist_bl_del(n);
  INIT_HLIST_BL_NODE(n);
 }
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_lock(struct hlist_bl_head *b)
{
 bit_spin_lock(0, (unsigned long *)b);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_unlock(struct hlist_bl_head *b)
{
 __bit_spin_unlock(0, (unsigned long *)b);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool hlist_bl_is_locked(struct hlist_bl_head *b)
{
 return bit_spin_is_locked(0, (unsigned long *)b);
}
# 8 "include/linux/rculist_bl.h" 2


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_set_first_rcu(struct hlist_bl_head *h,
     struct hlist_bl_node *n)
{
 ;

                        ;
 do { do { bool __cond = !((sizeof(*&h->first) == sizeof(int) || sizeof(*&h->first) == sizeof(long))); extern void __compiletime_assert_17(void) __attribute__((error("Need native word sized stores/loads for atomicity."))); if (__cond) __compiletime_assert_17(); do { } while (0); } while (0); __asm__ __volatile__("": : :"memory"); (*(volatile typeof(*&h->first) *)&(*&h->first)) = ((typeof(*((struct hlist_bl_node *)((unsigned long)n | 0UL))) *)((struct hlist_bl_node *)((unsigned long)n | 0UL))); } while (0)
                                                                ;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct hlist_bl_node *hlist_bl_first_rcu(struct hlist_bl_head *h)
{
 return (struct hlist_bl_node *)
  ((unsigned long)({ typeof(*(h->first)) *_________p1 = (typeof(*(h->first)) *)(*(volatile typeof((h->first)) *)&((h->first))); do { } while (0); ; do { } while(0); ((typeof(*(h->first)) *)(_________p1)); }) & ~0UL);
}
# 46 "include/linux/rculist_bl.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_del_init_rcu(struct hlist_bl_node *n)
{
 if (!hlist_bl_unhashed(n)) {
  __hlist_bl_del(n);
  n->pprev = ((void *)0);
 }
}
# 73 "include/linux/rculist_bl.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_del_rcu(struct hlist_bl_node *n)
{
 __hlist_bl_del(n);
 n->pprev = ((void *) 0x00200200 + 0);
}
# 98 "include/linux/rculist_bl.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void hlist_bl_add_head_rcu(struct hlist_bl_node *n,
     struct hlist_bl_head *h)
{
 struct hlist_bl_node *first;


 first = hlist_bl_first(h);

 n->next = first;
 if (first)
  first->pprev = &n->next;
 n->pprev = &h->first;


 hlist_bl_set_first_rcu(h, n);
}
# 8 "include/linux/dcache.h" 2




# 1 "include/linux/lockref.h" 1
# 24 "include/linux/lockref.h"
struct lockref {
 union {



  struct {
   spinlock_t lock;
   unsigned int count;
  };
 };
};

extern void lockref_get(struct lockref *);
extern int lockref_get_not_zero(struct lockref *);
extern int lockref_get_or_lock(struct lockref *);
extern int lockref_put_or_lock(struct lockref *);

extern void lockref_mark_dead(struct lockref *);
extern int lockref_get_not_dead(struct lockref *);


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __lockref_is_dead(const struct lockref *l)
{
 return ((int)l->count < 0);
}
# 13 "include/linux/dcache.h" 2

struct path;
struct vfsmount;
# 44 "include/linux/dcache.h"
struct qstr {
 union {
  struct {
   u32 len; u32 hash;;
  };
  u64 hash_len;
 };
 const unsigned char *name;
};






struct dentry_stat_t {
 long nr_dentry;
 long nr_unused;
 long age_limit;
 long want_pages;
 long dummy[2];
};
extern struct dentry_stat_t dentry_stat;






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long
partial_name_hash(unsigned long c, unsigned long prevhash)
{
 return (prevhash + (c << 4) + (c >> 4)) * 11;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long end_name_hash(unsigned long hash)
{
 return (unsigned int) hash;
}


extern unsigned int full_name_hash(const unsigned char *, unsigned int);
# 108 "include/linux/dcache.h"
struct dentry {

 unsigned int d_flags;
 seqcount_t d_seq;
 struct hlist_bl_node d_hash;
 struct dentry *d_parent;
 struct qstr d_name;
 struct inode *d_inode;

 unsigned char d_iname[40];


 struct lockref d_lockref;
 const struct dentry_operations *d_op;
 struct super_block *d_sb;
 unsigned long d_time;
 void *d_fsdata;

 struct list_head d_lru;
 struct list_head d_child;
 struct list_head d_subdirs;



 union {
  struct hlist_node d_alias;
   struct callback_head d_rcu;
 } d_u;
};







enum dentry_d_lock_class
{
 DENTRY_D_LOCK_NORMAL,
 DENTRY_D_LOCK_NESTED
};

struct dentry_operations {
 int (*d_revalidate)(struct dentry *, unsigned int);
 int (*d_weak_revalidate)(struct dentry *, unsigned int);
 int (*d_hash)(const struct dentry *, struct qstr *);
 int (*d_compare)(const struct dentry *, const struct dentry *,
   unsigned int, const char *, const struct qstr *);
 int (*d_delete)(const struct dentry *);
 void (*d_release)(struct dentry *);
 void (*d_prune)(struct dentry *);
 void (*d_iput)(struct dentry *, struct inode *);
 char *(*d_dname)(struct dentry *, char *, int);
 struct vfsmount *(*d_automount)(struct path *);
 int (*d_manage)(struct dentry *, bool);
} __attribute__((__aligned__((1 << 5))));
# 226 "include/linux/dcache.h"
extern seqlock_t rename_lock;




extern void d_instantiate(struct dentry *, struct inode *);
extern struct dentry * d_instantiate_unique(struct dentry *, struct inode *);
extern struct dentry * d_materialise_unique(struct dentry *, struct inode *);
extern int d_instantiate_no_diralias(struct dentry *, struct inode *);
extern void __d_drop(struct dentry *dentry);
extern void d_drop(struct dentry *dentry);
extern void d_delete(struct dentry *);
extern void d_set_d_op(struct dentry *dentry, const struct dentry_operations *op);


extern struct dentry * d_alloc(struct dentry *, const struct qstr *);
extern struct dentry * d_alloc_pseudo(struct super_block *, const struct qstr *);
extern struct dentry * d_splice_alias(struct inode *, struct dentry *);
extern struct dentry * d_add_ci(struct dentry *, struct inode *, struct qstr *);
extern struct dentry *d_find_any_alias(struct inode *inode);
extern struct dentry * d_obtain_alias(struct inode *);
extern struct dentry * d_obtain_root(struct inode *);
extern void shrink_dcache_sb(struct super_block *);
extern void shrink_dcache_parent(struct dentry *);
extern void shrink_dcache_for_umount(struct super_block *);
extern void d_invalidate(struct dentry *);


extern struct dentry * d_make_root(struct inode *);


extern void d_genocide(struct dentry *);

extern void d_tmpfile(struct dentry *, struct inode *);

extern struct dentry *d_find_alias(struct inode *);
extern void d_prune_aliases(struct inode *);


extern int have_submounts(struct dentry *);




extern void d_rehash(struct dentry *);
# 281 "include/linux/dcache.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void d_add(struct dentry *entry, struct inode *inode)
{
 d_instantiate(entry, inode);
 d_rehash(entry);
}
# 295 "include/linux/dcache.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct dentry *d_add_unique(struct dentry *entry, struct inode *inode)
{
 struct dentry *res;

 res = d_instantiate_unique(entry, inode);
 d_rehash(res != ((void *)0) ? res : entry);
 return res;
}

extern void dentry_update_name_case(struct dentry *, struct qstr *);


extern void d_move(struct dentry *, struct dentry *);
extern void d_exchange(struct dentry *, struct dentry *);
extern struct dentry *d_ancestor(struct dentry *, struct dentry *);


extern struct dentry *d_lookup(const struct dentry *, const struct qstr *);
extern struct dentry *d_hash_and_lookup(struct dentry *, struct qstr *);
extern struct dentry *__d_lookup(const struct dentry *, const struct qstr *);
extern struct dentry *__d_lookup_rcu(const struct dentry *parent,
    const struct qstr *name, unsigned *seq);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned d_count(const struct dentry *dentry)
{
 return dentry->d_lockref.count;
}


extern int d_validate(struct dentry *, struct dentry *);




extern char *dynamic_dname(struct dentry *, char *, int, const char *, ...);
extern char *simple_dname(struct dentry *, char *, int);

extern char *__d_path(const struct path *, const struct path *, char *, int);
extern char *d_absolute_path(const struct path *, char *, int);
extern char *d_path(const struct path *, char *, int);
extern char *dentry_path_raw(struct dentry *, char *, int);
extern char *dentry_path(struct dentry *, char *, int);
# 348 "include/linux/dcache.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct dentry *dget_dlock(struct dentry *dentry)
{
 if (dentry)
  dentry->d_lockref.count++;
 return dentry;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct dentry *dget(struct dentry *dentry)
{
 if (dentry)
  lockref_get(&dentry->d_lockref);
 return dentry;
}

extern struct dentry *dget_parent(struct dentry *dentry);
# 371 "include/linux/dcache.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int d_unhashed(const struct dentry *dentry)
{
 return hlist_bl_unhashed(&dentry->d_hash);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int d_unlinked(const struct dentry *dentry)
{
 return d_unhashed(dentry) && !((dentry) == (dentry)->d_parent);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cant_mount(const struct dentry *dentry)
{
 return (dentry->d_flags & 0x00000100);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dont_mount(struct dentry *dentry)
{
 spin_lock(&dentry->d_lockref.lock);
 dentry->d_flags |= 0x00000100;
 spin_unlock(&dentry->d_lockref.lock);
}

extern void dput(struct dentry *);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_managed(const struct dentry *dentry)
{
 return dentry->d_flags & (0x00010000|0x00020000|0x00040000);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_mountpoint(const struct dentry *dentry)
{
 return dentry->d_flags & 0x00010000;
}




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __d_set_type(struct dentry *dentry, unsigned type)
{
 dentry->d_flags = (dentry->d_flags & ~0x00700000) | type;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __d_clear_type(struct dentry *dentry)
{
 __d_set_type(dentry, 0x00000000);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void d_set_type(struct dentry *dentry, unsigned type)
{
 spin_lock(&dentry->d_lockref.lock);
 __d_set_type(dentry, type);
 spin_unlock(&dentry->d_lockref.lock);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned __d_entry_type(const struct dentry *dentry)
{
 return dentry->d_flags & 0x00700000;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_can_lookup(const struct dentry *dentry)
{
 return __d_entry_type(dentry) == 0x00100000;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_is_autodir(const struct dentry *dentry)
{
 return __d_entry_type(dentry) == 0x00200000;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_is_dir(const struct dentry *dentry)
{
 return d_can_lookup(dentry) || d_is_autodir(dentry);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_is_symlink(const struct dentry *dentry)
{
 return __d_entry_type(dentry) == 0x00300000;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_is_file(const struct dentry *dentry)
{
 return __d_entry_type(dentry) == 0x00400000;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_is_negative(const struct dentry *dentry)
{
 return __d_entry_type(dentry) == 0x00000000;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool d_is_positive(const struct dentry *dentry)
{
 return !d_is_negative(dentry);
}

extern int sysctl_vfs_cache_pressure;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long vfs_pressure_ratio(unsigned long val)
{
 return ( { typeof(val) quot = (val) / (100); typeof(val) rem = (val) % (100); (quot * (sysctl_vfs_cache_pressure)) + ((rem * (sysctl_vfs_cache_pressure)) / (100)); } );
}
# 9 "include/linux/fs.h" 2
# 1 "include/linux/path.h" 1



struct dentry;
struct vfsmount;

struct path {
 struct vfsmount *mnt;
 struct dentry *dentry;
};

extern void path_get(const struct path *);
extern void path_put(const struct path *);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int path_equal(const struct path *path1, const struct path *path2)
{
 return path1->mnt == path2->mnt && path1->dentry == path2->dentry;
}
# 10 "include/linux/fs.h" 2



# 1 "include/linux/list_lru.h" 1
# 14 "include/linux/list_lru.h"
enum lru_status {
 LRU_REMOVED,
 LRU_REMOVED_RETRY,

 LRU_ROTATE,
 LRU_SKIP,
 LRU_RETRY,

};

struct list_lru_node {
 spinlock_t lock;
 struct list_head list;

 long nr_items;
} ;

struct list_lru {
 struct list_lru_node *node;
 nodemask_t active_nodes;
};

void list_lru_destroy(struct list_lru *lru);
int list_lru_init_key(struct list_lru *lru, struct lock_class_key *key);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int list_lru_init(struct list_lru *lru)
{
 return list_lru_init_key(lru, ((void *)0));
}
# 59 "include/linux/list_lru.h"
bool list_lru_add(struct list_lru *lru, struct list_head *item);
# 72 "include/linux/list_lru.h"
bool list_lru_del(struct list_lru *lru, struct list_head *item);
# 83 "include/linux/list_lru.h"
unsigned long list_lru_count_node(struct list_lru *lru, int nid);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long list_lru_count(struct list_lru *lru)
{
 long count = 0;
 int nid;

 if (!__nodes_empty(&(lru->active_nodes), (1 << 0))) for ((nid) = 0; (nid) < 1; (nid)++)
  count += list_lru_count_node(lru, nid);

 return count;
}

typedef enum lru_status
(*list_lru_walk_cb)(struct list_head *item, spinlock_t *lock, void *cb_arg);
# 118 "include/linux/list_lru.h"
unsigned long list_lru_walk_node(struct list_lru *lru, int nid,
     list_lru_walk_cb isolate, void *cb_arg,
     unsigned long *nr_to_walk);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long
list_lru_walk(struct list_lru *lru, list_lru_walk_cb isolate,
       void *cb_arg, unsigned long nr_to_walk)
{
 long isolated = 0;
 int nid;

 if (!__nodes_empty(&(lru->active_nodes), (1 << 0))) for ((nid) = 0; (nid) < 1; (nid)++) {
  isolated += list_lru_walk_node(lru, nid, isolate,
            cb_arg, &nr_to_walk);
  if (nr_to_walk <= 0)
   break;
 }
 return isolated;
}
# 14 "include/linux/fs.h" 2




# 1 "include/linux/pid.h" 1





enum pid_type
{
 PIDTYPE_PID,
 PIDTYPE_PGID,
 PIDTYPE_SID,
 PIDTYPE_MAX
};
# 50 "include/linux/pid.h"
struct upid {

 int nr;
 struct pid_namespace *ns;
 struct hlist_node pid_chain;
};

struct pid
{
 atomic_t count;
 unsigned int level;

 struct hlist_head tasks[PIDTYPE_MAX];
 struct callback_head rcu;
 struct upid numbers[1];
};

extern struct pid init_struct_pid;

struct pid_link
{
 struct hlist_node node;
 struct pid *pid;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct pid *get_pid(struct pid *pid)
{
 if (pid)
  atomic_add(1, (&pid->count));
 return pid;
}

extern void put_pid(struct pid *pid);
extern struct task_struct *pid_task(struct pid *pid, enum pid_type);
extern struct task_struct *get_pid_task(struct pid *pid, enum pid_type);

extern struct pid *get_task_pid(struct task_struct *task, enum pid_type type);




extern void attach_pid(struct task_struct *task, enum pid_type);
extern void detach_pid(struct task_struct *task, enum pid_type);
extern void change_pid(struct task_struct *task, enum pid_type,
   struct pid *pid);
extern void transfer_pid(struct task_struct *old, struct task_struct *new,
    enum pid_type);

struct pid_namespace;
extern struct pid_namespace init_pid_ns;
# 110 "include/linux/pid.h"
extern struct pid *find_pid_ns(int nr, struct pid_namespace *ns);
extern struct pid *find_vpid(int nr);




extern struct pid *find_get_pid(int nr);
extern struct pid *find_ge_pid(int nr, struct pid_namespace *);
int next_pidmap(struct pid_namespace *pid_ns, unsigned int last);

extern struct pid *alloc_pid(struct pid_namespace *ns);
extern void free_pid(struct pid *pid);
extern void disable_pid_allocation(struct pid_namespace *ns);
# 134 "include/linux/pid.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct pid_namespace *ns_of_pid(struct pid *pid)
{
 struct pid_namespace *ns = ((void *)0);
 if (pid)
  ns = pid->numbers[pid->level].ns;
 return ns;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool is_child_reaper(struct pid *pid)
{
 return pid->numbers[pid->level].nr == 1;
}
# 164 "include/linux/pid.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) pid_t pid_nr(struct pid *pid)
{
 pid_t nr = 0;
 if (pid)
  nr = pid->numbers[0].nr;
 return nr;
}

pid_t pid_nr_ns(struct pid *pid, struct pid_namespace *ns);
pid_t pid_vnr(struct pid *pid);
# 19 "include/linux/fs.h" 2


# 1 "include/linux/capability.h" 1
# 15 "include/linux/capability.h"
# 1 "include/uapi/linux/capability.h" 1
# 18 "include/uapi/linux/capability.h"
struct task_struct;
# 40 "include/uapi/linux/capability.h"
typedef struct __user_cap_header_struct {
 __u32 version;
 int pid;
} *cap_user_header_t;

typedef struct __user_cap_data_struct {
        __u32 effective;
        __u32 permitted;
        __u32 inheritable;
} *cap_user_data_t;
# 69 "include/uapi/linux/capability.h"
struct vfs_cap_data {
 __le32 magic_etc;
 struct {
  __le32 permitted;
  __le32 inheritable;
 } data[2];
};
# 16 "include/linux/capability.h" 2





extern int file_caps_enabled;

typedef struct kernel_cap_struct {
 __u32 cap[2];
} kernel_cap_t;


struct cpu_vfs_cap_data {
 __u32 magic_etc;
 kernel_cap_t permitted;
 kernel_cap_t inheritable;
};





struct file;
struct inode;
struct dentry;
struct user_namespace;

struct user_namespace *current_user_ns(void);

extern const kernel_cap_t __cap_empty_set;
extern const kernel_cap_t __cap_init_eff_set;
# 117 "include/linux/capability.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_combine(const kernel_cap_t a,
           const kernel_cap_t b)
{
 kernel_cap_t dest;
 do { unsigned __capi; for (__capi = 0; __capi < 2; ++__capi) { dest.cap[__capi] = a.cap[__capi] | b.cap[__capi]; } } while (0);
 return dest;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_intersect(const kernel_cap_t a,
      const kernel_cap_t b)
{
 kernel_cap_t dest;
 do { unsigned __capi; for (__capi = 0; __capi < 2; ++__capi) { dest.cap[__capi] = a.cap[__capi] & b.cap[__capi]; } } while (0);
 return dest;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_drop(const kernel_cap_t a,
        const kernel_cap_t drop)
{
 kernel_cap_t dest;
 do { unsigned __capi; for (__capi = 0; __capi < 2; ++__capi) { dest.cap[__capi] = a.cap[__capi] &~ drop.cap[__capi]; } } while (0);
 return dest;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_invert(const kernel_cap_t c)
{
 kernel_cap_t dest;
 do { unsigned __capi; for (__capi = 0; __capi < 2; ++__capi) { dest.cap[__capi] = ~ c.cap[__capi]; } } while (0);
 return dest;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cap_isclear(const kernel_cap_t a)
{
 unsigned __capi;
 for (__capi = 0; __capi < 2; ++__capi) {
  if (a.cap[__capi] != 0)
   return 0;
 }
 return 1;
}
# 165 "include/linux/capability.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cap_issubset(const kernel_cap_t a, const kernel_cap_t set)
{
 kernel_cap_t dest;
 dest = cap_drop(a, set);
 return cap_isclear(dest);
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int cap_is_fs_cap(int cap)
{
 const kernel_cap_t __cap_fs_set = ((kernel_cap_t){{ ((1 << ((0) & 31)) | (1 << ((27) & 31)) | (1 << ((1) & 31)) | (1 << ((2) & 31)) | (1 << ((3) & 31)) | (1 << ((4) & 31))) | (1 << ((9) & 31)), ((1 << ((32) & 31))) } });
 return !!((1 << ((cap) & 31)) & __cap_fs_set.cap[((cap) >> 5)]);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_drop_fs_set(const kernel_cap_t a)
{
 const kernel_cap_t __cap_fs_set = ((kernel_cap_t){{ ((1 << ((0) & 31)) | (1 << ((27) & 31)) | (1 << ((1) & 31)) | (1 << ((2) & 31)) | (1 << ((3) & 31)) | (1 << ((4) & 31))) | (1 << ((9) & 31)), ((1 << ((32) & 31))) } });
 return cap_drop(a, __cap_fs_set);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_raise_fs_set(const kernel_cap_t a,
         const kernel_cap_t permitted)
{
 const kernel_cap_t __cap_fs_set = ((kernel_cap_t){{ ((1 << ((0) & 31)) | (1 << ((27) & 31)) | (1 << ((1) & 31)) | (1 << ((2) & 31)) | (1 << ((3) & 31)) | (1 << ((4) & 31))) | (1 << ((9) & 31)), ((1 << ((32) & 31))) } });
 return cap_combine(a,
      cap_intersect(permitted, __cap_fs_set));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_drop_nfsd_set(const kernel_cap_t a)
{
 const kernel_cap_t __cap_fs_set = ((kernel_cap_t){{ ((1 << ((0) & 31)) | (1 << ((27) & 31)) | (1 << ((1) & 31)) | (1 << ((2) & 31)) | (1 << ((3) & 31)) | (1 << ((4) & 31))) | (1 << ((24) & 31)), ((1 << ((32) & 31))) } });
 return cap_drop(a, __cap_fs_set);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kernel_cap_t cap_raise_nfsd_set(const kernel_cap_t a,
           const kernel_cap_t permitted)
{
 const kernel_cap_t __cap_nfsd_set = ((kernel_cap_t){{ ((1 << ((0) & 31)) | (1 << ((27) & 31)) | (1 << ((1) & 31)) | (1 << ((2) & 31)) | (1 << ((3) & 31)) | (1 << ((4) & 31))) | (1 << ((24) & 31)), ((1 << ((32) & 31))) } });
 return cap_combine(a,
      cap_intersect(permitted, __cap_nfsd_set));
}

extern bool has_capability(struct task_struct *t, int cap);
extern bool has_ns_capability(struct task_struct *t,
         struct user_namespace *ns, int cap);
extern bool has_capability_noaudit(struct task_struct *t, int cap);
extern bool has_ns_capability_noaudit(struct task_struct *t,
          struct user_namespace *ns, int cap);
extern bool capable(int cap);
extern bool ns_capable(struct user_namespace *ns, int cap);
extern bool capable_wrt_inode_uidgid(const struct inode *inode, int cap);
extern bool file_ns_capable(const struct file *file, struct user_namespace *ns, int cap);


extern int get_vfs_caps_from_disk(const struct dentry *dentry, struct cpu_vfs_cap_data *cpu_caps);
# 22 "include/linux/fs.h" 2
# 1 "include/linux/semaphore.h" 1
# 16 "include/linux/semaphore.h"
struct semaphore {
 raw_spinlock_t lock;
 unsigned int count;
 struct list_head wait_list;
};
# 32 "include/linux/semaphore.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sema_init(struct semaphore *sem, int val)
{
 static struct lock_class_key __key;
 *sem = (struct semaphore) { .lock = (raw_spinlock_t) { .raw_lock = { }, }, .count = val, .wait_list = { &((*sem).wait_list), &((*sem).wait_list) }, };
 do { (void)("semaphore->lock"); (void)(&__key); } while (0);
}

extern void down(struct semaphore *sem);
extern int down_interruptible(struct semaphore *sem);
extern int down_killable(struct semaphore *sem);
extern int down_trylock(struct semaphore *sem);
extern int down_timeout(struct semaphore *sem, long jiffies);
extern void up(struct semaphore *sem);
# 23 "include/linux/fs.h" 2
# 1 "./include/uapi/linux/fiemap.h" 1
# 16 "./include/uapi/linux/fiemap.h"
struct fiemap_extent {
 __u64 fe_logical;

 __u64 fe_physical;

 __u64 fe_length;
 __u64 fe_reserved64[2];
 __u32 fe_flags;
 __u32 fe_reserved[3];
};

struct fiemap {
 __u64 fm_start;

 __u64 fm_length;

 __u32 fm_flags;
 __u32 fm_mapped_extents;
 __u32 fm_extent_count;
 __u32 fm_reserved;
 struct fiemap_extent fm_extents[0];
};
# 24 "include/linux/fs.h" 2


# 1 "include/linux/shrinker.h" 1
# 11 "include/linux/shrinker.h"
struct shrink_control {
 gfp_t gfp_mask;






 unsigned long nr_to_scan;


 nodemask_t nodes_to_scan;

 int nid;
};
# 48 "include/linux/shrinker.h"
struct shrinker {
 unsigned long (*count_objects)(struct shrinker *,
           struct shrink_control *sc);
 unsigned long (*scan_objects)(struct shrinker *,
          struct shrink_control *sc);

 int seeks;
 long batch;
 unsigned long flags;


 struct list_head list;

 atomic_long_t *nr_deferred;
};





extern int register_shrinker(struct shrinker *);
extern void unregister_shrinker(struct shrinker *);
# 27 "include/linux/fs.h" 2
# 1 "include/linux/migrate_mode.h" 1
# 10 "include/linux/migrate_mode.h"
enum migrate_mode {
 MIGRATE_ASYNC,
 MIGRATE_SYNC_LIGHT,
 MIGRATE_SYNC,
};
# 28 "include/linux/fs.h" 2


# 1 "include/linux/percpu-rwsem.h" 1
# 10 "include/linux/percpu-rwsem.h"
struct percpu_rw_semaphore {
 unsigned int *fast_read_ctr;
 atomic_t write_ctr;
 struct rw_semaphore rw_sem;
 atomic_t slow_read_ctr;
 wait_queue_head_t write_waitq;
};

extern void percpu_down_read(struct percpu_rw_semaphore *);
extern void percpu_up_read(struct percpu_rw_semaphore *);

extern void percpu_down_write(struct percpu_rw_semaphore *);
extern void percpu_up_write(struct percpu_rw_semaphore *);

extern int __percpu_init_rwsem(struct percpu_rw_semaphore *,
    const char *, struct lock_class_key *);
extern void percpu_free_rwsem(struct percpu_rw_semaphore *);
# 31 "include/linux/fs.h" 2
# 1 "include/linux/blk_types.h" 1
# 10 "include/linux/blk_types.h"
struct bio_set;
struct bio;
struct bio_integrity_payload;
struct page;
struct block_device;
struct io_context;
struct cgroup_subsys_state;
typedef void (bio_end_io_t) (struct bio *, int);
typedef void (bio_destructor_t) (struct bio *);




struct bio_vec {
 struct page *bv_page;
 unsigned int bv_len;
 unsigned int bv_offset;
};



struct bvec_iter {
 sector_t bi_sector;

 unsigned int bi_size;

 unsigned int bi_idx;

 unsigned int bi_bvec_done;

};





struct bio {
 struct bio *bi_next;
 struct block_device *bi_bdev;
 unsigned long bi_flags;
 unsigned long bi_rw;



 struct bvec_iter bi_iter;




 unsigned int bi_phys_segments;





 unsigned int bi_seg_front_size;
 unsigned int bi_seg_back_size;

 atomic_t bi_remaining;

 bio_end_io_t *bi_end_io;

 void *bi_private;
# 81 "include/linux/blk_types.h"
 union {



 };

 unsigned short bi_vcnt;





 unsigned short bi_max_vecs;

 atomic_t bi_cnt;

 struct bio_vec *bi_io_vec;

 struct bio_set *bi_pool;






 struct bio_vec bi_inline_vecs[0];
};
# 150 "include/linux/blk_types.h"
enum rq_flag_bits {

 __REQ_WRITE,
 __REQ_FAILFAST_DEV,
 __REQ_FAILFAST_TRANSPORT,
 __REQ_FAILFAST_DRIVER,

 __REQ_SYNC,
 __REQ_META,
 __REQ_PRIO,
 __REQ_DISCARD,
 __REQ_SECURE,
 __REQ_WRITE_SAME,

 __REQ_NOIDLE,
 __REQ_INTEGRITY,
 __REQ_FUA,
 __REQ_FLUSH,


 __REQ_RAHEAD,
 __REQ_THROTTLED,



 __REQ_SORTED,
 __REQ_SOFTBARRIER,
 __REQ_NOMERGE,
 __REQ_STARTED,
 __REQ_DONTPREP,
 __REQ_QUEUED,
 __REQ_ELVPRIV,
 __REQ_FAILED,
 __REQ_QUIET,
 __REQ_PREEMPT,


 __REQ_ALLOCED,
 __REQ_COPY_USER,
 __REQ_FLUSH_SEQ,
 __REQ_IO_STAT,
 __REQ_MIXED_MERGE,
 __REQ_PM,
 __REQ_HASHED,
 __REQ_MQ_INFLIGHT,
 __REQ_NR_BITS,
};
# 32 "include/linux/fs.h" 2


# 1 "include/uapi/linux/fs.h" 1
# 9 "include/uapi/linux/fs.h"
# 1 "./include/uapi/linux/limits.h" 1
# 10 "include/uapi/linux/fs.h" 2
# 1 "./include/uapi/linux/ioctl.h" 1



# 1 "./arch/mips/include/uapi/asm/ioctl.h" 1
# 25 "./arch/mips/include/uapi/asm/ioctl.h"
# 1 "include/asm-generic/ioctl.h" 1



# 1 "include/uapi/asm-generic/ioctl.h" 1
# 5 "include/asm-generic/ioctl.h" 2





extern unsigned int __invalid_size_argument_for_IOC;
# 26 "./arch/mips/include/uapi/asm/ioctl.h" 2
# 5 "./include/uapi/linux/ioctl.h" 2
# 11 "include/uapi/linux/fs.h" 2
# 42 "include/uapi/linux/fs.h"
struct fstrim_range {
 __u64 start;
 __u64 len;
 __u64 minlen;
};


struct files_stat_struct {
 unsigned long nr_files;
 unsigned long nr_free_files;
 unsigned long max_files;
};

struct inodes_stat_t {
 long nr_inodes;
 long nr_unused;
 long dummy[5];
};
# 35 "include/linux/fs.h" 2

struct export_operations;
struct hd_geometry;
struct iovec;
struct nameidata;
struct kiocb;
struct kobject;
struct pipe_inode_info;
struct poll_table_struct;
struct kstatfs;
struct vm_area_struct;
struct vfsmount;
struct cred;
struct swap_info_struct;
struct seq_file;
struct workqueue_struct;
struct iov_iter;

extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) inode_init(void);
extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) inode_init_early(void);
extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) files_init(unsigned long);

extern struct files_stat_struct files_stat;
extern unsigned long get_max_files(void);
extern int sysctl_nr_open;
extern struct inodes_stat_t inodes_stat;
extern int leases_enable, lease_break_time;
extern int sysctl_protected_symlinks;
extern int sysctl_protected_hardlinks;

struct buffer_head;
typedef int (get_block_t)(struct inode *inode, sector_t iblock,
   struct buffer_head *bh_result, int create);
typedef void (dio_iodone_t)(struct kiocb *iocb, loff_t offset,
   ssize_t bytes, void *private);
# 241 "include/linux/fs.h"
struct iattr {
 unsigned int ia_valid;
 umode_t ia_mode;
 kuid_t ia_uid;
 kgid_t ia_gid;
 loff_t ia_size;
 struct timespec ia_atime;
 struct timespec ia_mtime;
 struct timespec ia_ctime;






 struct file *ia_file;
};




# 1 "include/linux/quota.h" 1
# 40 "include/linux/quota.h"
# 1 "include/linux/percpu_counter.h" 1
# 89 "include/linux/percpu_counter.h"
struct percpu_counter {
 s64 count;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int percpu_counter_init(struct percpu_counter *fbc, s64 amount,
          gfp_t gfp)
{
 fbc->count = amount;
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void percpu_counter_destroy(struct percpu_counter *fbc)
{
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void percpu_counter_set(struct percpu_counter *fbc, s64 amount)
{
 fbc->count = amount;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int percpu_counter_compare(struct percpu_counter *fbc, s64 rhs)
{
 if (fbc->count > rhs)
  return 1;
 else if (fbc->count < rhs)
  return -1;
 else
  return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
percpu_counter_add(struct percpu_counter *fbc, s64 amount)
{
 __asm__ __volatile__("": : :"memory");
 fbc->count += amount;
 __asm__ __volatile__("": : :"memory");
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
__percpu_counter_add(struct percpu_counter *fbc, s64 amount, s32 batch)
{
 percpu_counter_add(fbc, amount);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 percpu_counter_read(struct percpu_counter *fbc)
{
 return fbc->count;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 percpu_counter_read_positive(struct percpu_counter *fbc)
{
 return fbc->count;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 percpu_counter_sum_positive(struct percpu_counter *fbc)
{
 return percpu_counter_read_positive(fbc);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 percpu_counter_sum(struct percpu_counter *fbc)
{
 return percpu_counter_read(fbc);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int percpu_counter_initialized(struct percpu_counter *fbc)
{
 return 1;
}



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void percpu_counter_inc(struct percpu_counter *fbc)
{
 percpu_counter_add(fbc, 1);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void percpu_counter_dec(struct percpu_counter *fbc)
{
 percpu_counter_add(fbc, -1);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void percpu_counter_sub(struct percpu_counter *fbc, s64 amount)
{
 percpu_counter_add(fbc, -amount);
}
# 41 "include/linux/quota.h" 2

# 1 "./include/uapi/linux/dqblk_xfs.h" 1
# 51 "./include/uapi/linux/dqblk_xfs.h"
typedef struct fs_disk_quota {
 __s8 d_version;
 __s8 d_flags;
 __u16 d_fieldmask;
 __u32 d_id;
 __u64 d_blk_hardlimit;
 __u64 d_blk_softlimit;
 __u64 d_ino_hardlimit;
 __u64 d_ino_softlimit;
 __u64 d_bcount;
 __u64 d_icount;
 __s32 d_itimer;

 __s32 d_btimer;
 __u16 d_iwarns;
 __u16 d_bwarns;
 __s32 d_padding2;
 __u64 d_rtb_hardlimit;
 __u64 d_rtb_softlimit;
 __u64 d_rtbcount;
 __s32 d_rtbtimer;
 __u16 d_rtbwarns;
 __s16 d_padding3;
 char d_padding4[8];
} fs_disk_quota_t;
# 147 "./include/uapi/linux/dqblk_xfs.h"
typedef struct fs_qfilestat {
 __u64 qfs_ino;
 __u64 qfs_nblks;
 __u32 qfs_nextents;
} fs_qfilestat_t;

typedef struct fs_quota_stat {
 __s8 qs_version;
 __u16 qs_flags;
 __s8 qs_pad;
 fs_qfilestat_t qs_uquota;
 fs_qfilestat_t qs_gquota;
 __u32 qs_incoredqs;
 __s32 qs_btimelimit;
 __s32 qs_itimelimit;
 __s32 qs_rtbtimelimit;
 __u16 qs_bwarnlimit;
 __u16 qs_iwarnlimit;
} fs_quota_stat_t;
# 190 "./include/uapi/linux/dqblk_xfs.h"
struct fs_qfilestatv {
 __u64 qfs_ino;
 __u64 qfs_nblks;
 __u32 qfs_nextents;
 __u32 qfs_pad;
};

struct fs_quota_statv {
 __s8 qs_version;
 __u8 qs_pad1;
 __u16 qs_flags;
 __u32 qs_incoredqs;
 struct fs_qfilestatv qs_uquota;
 struct fs_qfilestatv qs_gquota;
 struct fs_qfilestatv qs_pquota;
 __s32 qs_btimelimit;
 __s32 qs_itimelimit;
 __s32 qs_rtbtimelimit;
 __u16 qs_bwarnlimit;
 __u16 qs_iwarnlimit;
 __u64 qs_pad2[8];
};
# 43 "include/linux/quota.h" 2
# 1 "include/linux/dqblk_v1.h" 1
# 44 "include/linux/quota.h" 2
# 1 "include/linux/dqblk_v2.h" 1







# 1 "include/linux/dqblk_qtree.h" 1
# 17 "include/linux/dqblk_qtree.h"
struct dquot;


struct qtree_fmt_operations {
 void (*mem2disk_dqblk)(void *disk, struct dquot *dquot);
 void (*disk2mem_dqblk)(struct dquot *dquot, void *disk);
 int (*is_id)(void *disk, struct dquot *dquot);
};


struct qtree_mem_dqinfo {
 struct super_block *dqi_sb;
 int dqi_type;
 unsigned int dqi_blocks;
 unsigned int dqi_free_blk;
 unsigned int dqi_free_entry;
 unsigned int dqi_blocksize_bits;
 unsigned int dqi_entry_size;
 unsigned int dqi_usable_bs;
 unsigned int dqi_qtree_depth;
 struct qtree_fmt_operations *dqi_ops;
};

int qtree_write_dquot(struct qtree_mem_dqinfo *info, struct dquot *dquot);
int qtree_read_dquot(struct qtree_mem_dqinfo *info, struct dquot *dquot);
int qtree_delete_dquot(struct qtree_mem_dqinfo *info, struct dquot *dquot);
int qtree_release_dquot(struct qtree_mem_dqinfo *info, struct dquot *dquot);
int qtree_entry_unused(struct qtree_mem_dqinfo *info, char *disk);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int qtree_depth(struct qtree_mem_dqinfo *info)
{
 unsigned int epb = info->dqi_usable_bs >> 2;
 unsigned long long entries = epb;
 int i;

 for (i = 1; entries < (1ULL << 32); i++)
  entries *= epb;
 return i;
}
# 9 "include/linux/dqblk_v2.h" 2
# 45 "include/linux/quota.h" 2



# 1 "include/linux/projid.h" 1
# 16 "include/linux/projid.h"
struct user_namespace;
extern struct user_namespace init_user_ns;

typedef __kernel_uid32_t projid_t;

typedef struct {
 projid_t val;
} kprojid_t;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) projid_t __kprojid_val(kprojid_t projid)
{
 return projid.val;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool projid_eq(kprojid_t left, kprojid_t right)
{
 return __kprojid_val(left) == __kprojid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool projid_lt(kprojid_t left, kprojid_t right)
{
 return __kprojid_val(left) < __kprojid_val(right);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool projid_valid(kprojid_t projid)
{
 return !projid_eq(projid, (kprojid_t){ -1 });
}
# 64 "include/linux/projid.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) kprojid_t make_kprojid(struct user_namespace *from, projid_t projid)
{
 return (kprojid_t){ projid };
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) projid_t from_kprojid(struct user_namespace *to, kprojid_t kprojid)
{
 return __kprojid_val(kprojid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) projid_t from_kprojid_munged(struct user_namespace *to, kprojid_t kprojid)
{
 projid_t projid = from_kprojid(to, kprojid);
 if (projid == (projid_t)-1)
  projid = 65534;
 return projid;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool kprojid_has_mapping(struct user_namespace *ns, kprojid_t projid)
{
 return true;
}
# 49 "include/linux/quota.h" 2
# 1 "include/uapi/linux/quota.h" 1
# 88 "include/uapi/linux/quota.h"
enum {
 QIF_BLIMITS_B = 0,
 QIF_SPACE_B,
 QIF_ILIMITS_B,
 QIF_INODES_B,
 QIF_BTIME_B,
 QIF_ITIME_B,
};
# 108 "include/uapi/linux/quota.h"
struct if_dqblk {
 __u64 dqb_bhardlimit;
 __u64 dqb_bsoftlimit;
 __u64 dqb_curspace;
 __u64 dqb_ihardlimit;
 __u64 dqb_isoftlimit;
 __u64 dqb_curinodes;
 __u64 dqb_btime;
 __u64 dqb_itime;
 __u32 dqb_valid;
};
# 129 "include/uapi/linux/quota.h"
struct if_dqinfo {
 __u64 dqi_bgrace;
 __u64 dqi_igrace;
 __u32 dqi_flags;
 __u32 dqi_valid;
};
# 151 "include/uapi/linux/quota.h"
enum {
 QUOTA_NL_C_UNSPEC,
 QUOTA_NL_C_WARNING,
 __QUOTA_NL_C_MAX,
};


enum {
 QUOTA_NL_A_UNSPEC,
 QUOTA_NL_A_QTYPE,
 QUOTA_NL_A_EXCESS_ID,
 QUOTA_NL_A_WARNING,
 QUOTA_NL_A_DEV_MAJOR,
 QUOTA_NL_A_DEV_MINOR,
 QUOTA_NL_A_CAUSED_ID,
 __QUOTA_NL_A_MAX,
};
# 50 "include/linux/quota.h" 2



enum quota_type {
 USRQUOTA = 0,
 GRPQUOTA = 1,
 PRJQUOTA = 2,
};

typedef __kernel_uid32_t qid_t;
typedef long long qsize_t;

struct kqid {
 union {
  kuid_t uid;
  kgid_t gid;
  kprojid_t projid;
 };
 enum quota_type type;
};

extern bool qid_eq(struct kqid left, struct kqid right);
extern bool qid_lt(struct kqid left, struct kqid right);
extern qid_t from_kqid(struct user_namespace *to, struct kqid qid);
extern qid_t from_kqid_munged(struct user_namespace *to, struct kqid qid);
extern bool qid_valid(struct kqid qid);
# 91 "include/linux/quota.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kqid make_kqid(struct user_namespace *from,
        enum quota_type type, qid_t qid)
{
 struct kqid kqid;

 kqid.type = type;
 switch (type) {
 case USRQUOTA:
  kqid.uid = make_kuid(from, qid);
  break;
 case GRPQUOTA:
  kqid.gid = make_kgid(from, qid);
  break;
 case PRJQUOTA:
  kqid.projid = make_kprojid(from, qid);
  break;
 default:
  BUG();
 }
 return kqid;
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kqid make_kqid_invalid(enum quota_type type)
{
 struct kqid kqid;

 kqid.type = type;
 switch (type) {
 case USRQUOTA:
  kqid.uid = (kuid_t){ -1 };
  break;
 case GRPQUOTA:
  kqid.gid = (kgid_t){ -1 };
  break;
 case PRJQUOTA:
  kqid.projid = (kprojid_t){ -1 };
  break;
 default:
  BUG();
 }
 return kqid;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kqid make_kqid_uid(kuid_t uid)
{
 struct kqid kqid;
 kqid.type = USRQUOTA;
 kqid.uid = uid;
 return kqid;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kqid make_kqid_gid(kgid_t gid)
{
 struct kqid kqid;
 kqid.type = GRPQUOTA;
 kqid.gid = gid;
 return kqid;
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct kqid make_kqid_projid(kprojid_t projid)
{
 struct kqid kqid;
 kqid.type = PRJQUOTA;
 kqid.projid = projid;
 return kqid;
}


extern spinlock_t dq_data_lock;
# 189 "include/linux/quota.h"
struct mem_dqblk {
 qsize_t dqb_bhardlimit;
 qsize_t dqb_bsoftlimit;
 qsize_t dqb_curspace;
 qsize_t dqb_rsvspace;
 qsize_t dqb_ihardlimit;
 qsize_t dqb_isoftlimit;
 qsize_t dqb_curinodes;
 time_t dqb_btime;
 time_t dqb_itime;
};




struct quota_format_type;

struct mem_dqinfo {
 struct quota_format_type *dqi_format;
 int dqi_fmt_id;

 struct list_head dqi_dirty_list;
 unsigned long dqi_flags;
 unsigned int dqi_bgrace;
 unsigned int dqi_igrace;
 qsize_t dqi_max_spc_limit;
 qsize_t dqi_max_ino_limit;
 void *dqi_priv;
};

struct super_block;
# 229 "include/linux/quota.h"
extern void mark_info_dirty(struct super_block *sb, int type);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int info_dirty(struct mem_dqinfo *info)
{
 return test_bit(31, &info->dqi_flags);
}

enum {
 DQST_LOOKUPS,
 DQST_DROPS,
 DQST_READS,
 DQST_WRITES,
 DQST_CACHE_HITS,
 DQST_ALLOC_DQUOTS,
 DQST_FREE_DQUOTS,
 DQST_SYNCS,
 _DQST_DQSTAT_LAST
};

struct dqstats {
 int stat[_DQST_DQSTAT_LAST];
 struct percpu_counter counter[_DQST_DQSTAT_LAST];
};

extern struct dqstats *dqstats_pcpu;
extern struct dqstats dqstats;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dqstats_inc(unsigned int type)
{
 percpu_counter_inc(&dqstats.counter[type]);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void dqstats_dec(unsigned int type)
{
 percpu_counter_dec(&dqstats.counter[type]);
}
# 277 "include/linux/quota.h"
struct dquot {
 struct hlist_node dq_hash;
 struct list_head dq_inuse;
 struct list_head dq_free;
 struct list_head dq_dirty;
 struct mutex dq_lock;
 atomic_t dq_count;
 wait_queue_head_t dq_wait_unused;
 struct super_block *dq_sb;
 struct kqid dq_id;
 loff_t dq_off;
 unsigned long dq_flags;
 struct mem_dqblk dq_dqb;
};


struct quota_format_ops {
 int (*check_quota_file)(struct super_block *sb, int type);
 int (*read_file_info)(struct super_block *sb, int type);
 int (*write_file_info)(struct super_block *sb, int type);
 int (*free_file_info)(struct super_block *sb, int type);
 int (*read_dqblk)(struct dquot *dquot);
 int (*commit_dqblk)(struct dquot *dquot);
 int (*release_dqblk)(struct dquot *dquot);
};


struct dquot_operations {
 int (*write_dquot) (struct dquot *);
 struct dquot *(*alloc_dquot)(struct super_block *, int);
 void (*destroy_dquot)(struct dquot *);
 int (*acquire_dquot) (struct dquot *);
 int (*release_dquot) (struct dquot *);
 int (*mark_dirty) (struct dquot *);
 int (*write_info) (struct super_block *, int);


 qsize_t *(*get_reserved_space) (struct inode *);
};

struct path;


struct qc_dqblk {
 int d_fieldmask;
 u64 d_spc_hardlimit;
 u64 d_spc_softlimit;
 u64 d_ino_hardlimit;
 u64 d_ino_softlimit;
 u64 d_space;
 u64 d_ino_count;
 s64 d_ino_timer;

 s64 d_spc_timer;
 int d_ino_warns;
 int d_spc_warns;
 u64 d_rt_spc_hardlimit;
 u64 d_rt_spc_softlimit;
 u64 d_rt_space;
 s64 d_rt_spc_timer;
 int d_rt_spc_warns;
};
# 363 "include/linux/quota.h"
struct quotactl_ops {
 int (*quota_on)(struct super_block *, int, int, struct path *);
 int (*quota_on_meta)(struct super_block *, int, int);
 int (*quota_off)(struct super_block *, int);
 int (*quota_sync)(struct super_block *, int);
 int (*get_info)(struct super_block *, int, struct if_dqinfo *);
 int (*set_info)(struct super_block *, int, struct if_dqinfo *);
 int (*get_dqblk)(struct super_block *, struct kqid, struct qc_dqblk *);
 int (*set_dqblk)(struct super_block *, struct kqid, struct qc_dqblk *);
 int (*get_xstate)(struct super_block *, struct fs_quota_stat *);
 int (*set_xstate)(struct super_block *, unsigned int, int);
 int (*get_xstatev)(struct super_block *, struct fs_quota_statv *);
 int (*rm_xquota)(struct super_block *, unsigned int);
};

struct quota_format_type {
 int qf_fmt_id;
 const struct quota_format_ops *qf_ops;
 struct module *qf_owner;
 struct quota_format_type *qf_next;
};


enum {
 _DQUOT_USAGE_ENABLED = 0,
 _DQUOT_LIMITS_ENABLED,
 _DQUOT_SUSPENDED,


 _DQUOT_STATE_FLAGS
};
# 411 "include/linux/quota.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int dquot_state_flag(unsigned int flags, int type)
{
 return flags << _DQUOT_STATE_FLAGS * type;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned int dquot_generic_flag(unsigned int flags, int type)
{
 return (flags >> _DQUOT_STATE_FLAGS * type) & ((1 << _DQUOT_USAGE_ENABLED) | (1 << _DQUOT_LIMITS_ENABLED) | (1 << _DQUOT_SUSPENDED));
}





static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void quota_send_warning(struct kqid qid, dev_t dev,
          const char warntype)
{
 return;
}


struct quota_info {
 unsigned int flags;
 struct mutex dqio_mutex;
 struct mutex dqonoff_mutex;
 struct inode *files[2];
 struct mem_dqinfo info[2];
 const struct quota_format_ops *ops[2];
};

int register_quota_format(struct quota_format_type *fmt);
void unregister_quota_format(struct quota_format_type *fmt);

struct quota_module_name {
 int qm_fmt_id;
 char *qm_mod_name;
};
# 263 "include/linux/fs.h" 2
# 296 "include/linux/fs.h"
enum positive_aop_returns {
 AOP_WRITEPAGE_ACTIVATE = 0x80000,
 AOP_TRUNCATED_PAGE = 0x80001,
};
# 310 "include/linux/fs.h"
struct page;
struct address_space;
struct writeback_control;
# 323 "include/linux/fs.h"
typedef struct {
 size_t written;
 size_t count;
 union {
  char *buf;
  void *data;
 } arg;
 int error;
} read_descriptor_t;

typedef int (*read_actor_t)(read_descriptor_t *, struct page *,
  unsigned long, unsigned long);

struct address_space_operations {
 int (*writepage)(struct page *page, struct writeback_control *wbc);
 int (*readpage)(struct file *, struct page *);


 int (*writepages)(struct address_space *, struct writeback_control *);


 int (*set_page_dirty)(struct page *page);

 int (*readpages)(struct file *filp, struct address_space *mapping,
   struct list_head *pages, unsigned nr_pages);

 int (*write_begin)(struct file *, struct address_space *mapping,
    loff_t pos, unsigned len, unsigned flags,
    struct page **pagep, void **fsdata);
 int (*write_end)(struct file *, struct address_space *mapping,
    loff_t pos, unsigned len, unsigned copied,
    struct page *page, void *fsdata);


 sector_t (*bmap)(struct address_space *, sector_t);
 void (*invalidatepage) (struct page *, unsigned int, unsigned int);
 int (*releasepage) (struct page *, gfp_t);
 void (*freepage)(struct page *);
 ssize_t (*direct_IO)(int, struct kiocb *, struct iov_iter *iter, loff_t offset);
 int (*get_xip_mem)(struct address_space *, unsigned long, int,
      void **, unsigned long *);




 int (*migratepage) (struct address_space *,
   struct page *, struct page *, enum migrate_mode);
 int (*launder_page) (struct page *);
 int (*is_partially_uptodate) (struct page *, unsigned long,
     unsigned long);
 void (*is_dirty_writeback) (struct page *, bool *, bool *);
 int (*error_remove_page)(struct address_space *, struct page *);


 int (*swap_activate)(struct swap_info_struct *sis, struct file *file,
    sector_t *span);
 void (*swap_deactivate)(struct file *file);
};

extern const struct address_space_operations empty_aops;





int pagecache_write_begin(struct file *, struct address_space *mapping,
    loff_t pos, unsigned len, unsigned flags,
    struct page **pagep, void **fsdata);

int pagecache_write_end(struct file *, struct address_space *mapping,
    loff_t pos, unsigned len, unsigned copied,
    struct page *page, void *fsdata);

struct backing_dev_info;
struct address_space {
 struct inode *host;
 struct radix_tree_root page_tree;
 spinlock_t tree_lock;
 atomic_t i_mmap_writable;
 struct rb_root i_mmap;
 struct list_head i_mmap_nonlinear;
 struct mutex i_mmap_mutex;

 unsigned long nrpages;
 unsigned long nrshadows;
 unsigned long writeback_index;
 const struct address_space_operations *a_ops;
 unsigned long flags;
 struct backing_dev_info *backing_dev_info;
 spinlock_t private_lock;
 struct list_head private_list;
 void *private_data;
} __attribute__((aligned(sizeof(long))));





struct request_queue;

struct block_device {
 dev_t bd_dev;
 int bd_openers;
 struct inode * bd_inode;
 struct super_block * bd_super;
 struct mutex bd_mutex;
 struct list_head bd_inodes;
 void * bd_claiming;
 void * bd_holder;
 int bd_holders;
 bool bd_write_holder;

 struct list_head bd_holder_disks;

 struct block_device * bd_contains;
 unsigned bd_block_size;
 struct hd_struct * bd_part;

 unsigned bd_part_count;
 int bd_invalidated;
 struct gendisk * bd_disk;
 struct request_queue * bd_queue;
 struct list_head bd_list;






 unsigned long bd_private;


 int bd_fsfreeze_count;

 struct mutex bd_fsfreeze_mutex;
};
# 468 "include/linux/fs.h"
int mapping_tagged(struct address_space *mapping, int tag);




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mapping_mapped(struct address_space *mapping)
{
 return !((&mapping->i_mmap)->rb_node == ((void *)0)) ||
  !list_empty(&mapping->i_mmap_nonlinear);
}
# 488 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mapping_writably_mapped(struct address_space *mapping)
{
 return (*(volatile typeof((&mapping->i_mmap_writable)->counter) *)&((&mapping->i_mmap_writable)->counter)) > 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mapping_map_writable(struct address_space *mapping)
{
 return atomic_inc_unless_negative(&mapping->i_mmap_writable) ?
  0 : -1;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void mapping_unmap_writable(struct address_space *mapping)
{
 atomic_sub(1, (&mapping->i_mmap_writable));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mapping_deny_writable(struct address_space *mapping)
{
 return atomic_dec_unless_positive(&mapping->i_mmap_writable) ?
  0 : -16;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void mapping_allow_writable(struct address_space *mapping)
{
 atomic_add(1, (&mapping->i_mmap_writable));
}
# 526 "include/linux/fs.h"
struct posix_acl;
# 538 "include/linux/fs.h"
struct inode {
 umode_t i_mode;
 unsigned short i_opflags;
 kuid_t i_uid;
 kgid_t i_gid;
 unsigned int i_flags;






 const struct inode_operations *i_op;
 struct super_block *i_sb;
 struct address_space *i_mapping;






 unsigned long i_ino;







 union {
  const unsigned int i_nlink;
  unsigned int __i_nlink;
 };
 dev_t i_rdev;
 loff_t i_size;
 struct timespec i_atime;
 struct timespec i_mtime;
 struct timespec i_ctime;
 spinlock_t i_lock;
 unsigned short i_bytes;
 unsigned int i_blkbits;
 blkcnt_t i_blocks;






 unsigned long i_state;
 struct mutex i_mutex;

 unsigned long dirtied_when;

 struct hlist_node i_hash;
 struct list_head i_wb_list;
 struct list_head i_lru;
 struct list_head i_sb_list;
 union {
  struct hlist_head i_dentry;
  struct callback_head i_rcu;
 };
 u64 i_version;
 atomic_t i_count;
 atomic_t i_dio_count;
 atomic_t i_writecount;



 const struct file_operations *i_fop;
 struct file_lock *i_flock;
 struct address_space i_data;



 struct list_head i_devices;
 union {
  struct pipe_inode_info *i_pipe;
  struct block_device *i_bdev;
  struct cdev *i_cdev;
 };

 __u32 i_generation;


 __u32 i_fsnotify_mask;
 struct hlist_head i_fsnotify_marks;


 void *i_private;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int inode_unhashed(struct inode *inode)
{
 return hlist_unhashed(&inode->i_hash);
}
# 650 "include/linux/fs.h"
enum inode_i_mutex_lock_class
{
 I_MUTEX_NORMAL,
 I_MUTEX_PARENT,
 I_MUTEX_CHILD,
 I_MUTEX_XATTR,
 I_MUTEX_NONDIR2,
 I_MUTEX_PARENT2,
};

void lock_two_nondirectories(struct inode *, struct inode*);
void unlock_two_nondirectories(struct inode *, struct inode*);
# 673 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) loff_t i_size_read(const struct inode *inode)
{
# 692 "include/linux/fs.h"
 return inode->i_size;

}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void i_size_write(struct inode *inode, loff_t i_size)
{
# 714 "include/linux/fs.h"
 inode->i_size = i_size;

}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) uid_t i_uid_read(const struct inode *inode)
{
 return from_kuid(&init_user_ns, inode->i_uid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) gid_t i_gid_read(const struct inode *inode)
{
 return from_kgid(&init_user_ns, inode->i_gid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void i_uid_write(struct inode *inode, uid_t uid)
{
 inode->i_uid = make_kuid(&init_user_ns, uid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void i_gid_write(struct inode *inode, gid_t gid)
{
 inode->i_gid = make_kgid(&init_user_ns, gid);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned iminor(const struct inode *inode)
{
 return ((unsigned int) ((inode->i_rdev) & ((1U << 20) - 1)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned imajor(const struct inode *inode)
{
 return ((unsigned int) ((inode->i_rdev) >> 20));
}

extern struct block_device *I_BDEV(struct inode *inode);

struct fown_struct {
 rwlock_t lock;
 struct pid *pid;
 enum pid_type pid_type;
 kuid_t uid, euid;
 int signum;
};




struct file_ra_state {
 unsigned long start;
 unsigned int size;
 unsigned int async_size;


 unsigned int ra_pages;
 unsigned int mmap_miss;
 loff_t prev_pos;
};




static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int ra_has_index(struct file_ra_state *ra, unsigned long index)
{
 return (index >= ra->start &&
  index < ra->start + ra->size);
}

struct file {
 union {
  struct llist_node fu_llist;
  struct callback_head fu_rcuhead;
 } f_u;
 struct path f_path;

 struct inode *f_inode;
 const struct file_operations *f_op;





 spinlock_t f_lock;
 atomic_long_t f_count;
 unsigned int f_flags;
 fmode_t f_mode;
 struct mutex f_pos_lock;
 loff_t f_pos;
 struct fown_struct f_owner;
 const struct cred *f_cred;
 struct file_ra_state f_ra;

 u64 f_version;




 void *private_data;



 struct list_head f_ep_links;
 struct list_head f_tfile_llink;

 struct address_space *f_mapping;
} __attribute__((aligned(4)));

struct file_handle {
 __u32 handle_bytes;
 int handle_type;

 unsigned char f_handle[0];
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct file *get_file(struct file *f)
{
 atomic_long_inc(&f->f_count);
 return f;
}
# 869 "include/linux/fs.h"
typedef void *fl_owner_t;

struct file_lock_operations {
 void (*fl_copy_lock)(struct file_lock *, struct file_lock *);
 void (*fl_release_private)(struct file_lock *);
};

struct lock_manager_operations {
 int (*lm_compare_owner)(struct file_lock *, struct file_lock *);
 unsigned long (*lm_owner_key)(struct file_lock *);
 void (*lm_get_owner)(struct file_lock *, struct file_lock *);
 void (*lm_put_owner)(struct file_lock *);
 void (*lm_notify)(struct file_lock *);
 int (*lm_grant)(struct file_lock *, int);
 bool (*lm_break)(struct file_lock *);
 int (*lm_change)(struct file_lock **, int, struct list_head *);
 void (*lm_setup)(struct file_lock *, void **);
};

struct lock_manager {
 struct list_head list;
};

struct net;
void locks_start_grace(struct net *, struct lock_manager *);
void locks_end_grace(struct lock_manager *);
int locks_in_grace(struct net *);


# 1 "include/linux/nfs_fs_i.h" 1



struct nlm_lockowner;




struct nfs_lock_info {
 u32 state;
 struct nlm_lockowner *owner;
 struct list_head list;
};

struct nfs4_lock_state;
struct nfs4_lock_info {
 struct nfs4_lock_state *owner;
};
# 899 "include/linux/fs.h" 2
# 918 "include/linux/fs.h"
struct file_lock {
 struct file_lock *fl_next;
 struct hlist_node fl_link;
 struct list_head fl_block;
 fl_owner_t fl_owner;
 unsigned int fl_flags;
 unsigned char fl_type;
 unsigned int fl_pid;
 int fl_link_cpu;
 struct pid *fl_nspid;
 wait_queue_head_t fl_wait;
 struct file *fl_file;
 loff_t fl_start;
 loff_t fl_end;

 struct fasync_struct * fl_fasync;

 unsigned long fl_break_time;
 unsigned long fl_downgrade_time;

 const struct file_lock_operations *fl_ops;
 const struct lock_manager_operations *fl_lmops;
 union {
  struct nfs_lock_info nfs_fl;
  struct nfs4_lock_info nfs4_fl;
  struct {
   struct list_head link;
   int state;
  } afs;
 } fl_u;
};
# 957 "include/linux/fs.h"
# 1 "include/linux/fcntl.h" 1



# 1 "include/uapi/linux/fcntl.h" 1



# 1 "./arch/mips/include/uapi/asm/fcntl.h" 1
# 63 "./arch/mips/include/uapi/asm/fcntl.h"
struct flock {
 short l_type;
 short l_whence;
 __kernel_off_t l_start;
 __kernel_off_t l_len;
 long l_sysid;
 __kernel_pid_t l_pid;
 long pad[4];
};





# 1 "./include/uapi/asm-generic/fcntl.h" 1
# 155 "./include/uapi/asm-generic/fcntl.h"
struct f_owner_ex {
 int type;
 __kernel_pid_t pid;
};
# 210 "./include/uapi/asm-generic/fcntl.h"
struct flock64 {
 short l_type;
 short l_whence;
 __kernel_loff_t l_start;
 __kernel_loff_t l_len;
 __kernel_pid_t l_pid;

};
# 78 "./arch/mips/include/uapi/asm/fcntl.h" 2
# 5 "include/uapi/linux/fcntl.h" 2
# 5 "include/linux/fcntl.h" 2
# 958 "include/linux/fs.h" 2

extern void send_sigio(struct fown_struct *fown, int fd, int band);


extern int fcntl_getlk(struct file *, unsigned int, struct flock *);
extern int fcntl_setlk(unsigned int, struct file *, unsigned int,
   struct flock *);


extern int fcntl_getlk64(struct file *, unsigned int, struct flock64 *);
extern int fcntl_setlk64(unsigned int, struct file *, unsigned int,
   struct flock64 *);


extern int fcntl_setlease(unsigned int fd, struct file *filp, long arg);
extern int fcntl_getlease(struct file *filp);


void locks_free_lock(struct file_lock *fl);
extern void locks_init_lock(struct file_lock *);
extern struct file_lock * locks_alloc_lock(void);
extern void locks_copy_lock(struct file_lock *, struct file_lock *);
extern void locks_copy_conflock(struct file_lock *, struct file_lock *);
extern void locks_remove_posix(struct file *, fl_owner_t);
extern void locks_remove_file(struct file *);
extern void locks_release_private(struct file_lock *);
extern void posix_test_lock(struct file *, struct file_lock *);
extern int posix_lock_file(struct file *, struct file_lock *, struct file_lock *);
extern int posix_lock_file_wait(struct file *, struct file_lock *);
extern int posix_unblock_lock(struct file_lock *);
extern int vfs_test_lock(struct file *, struct file_lock *);
extern int vfs_lock_file(struct file *, unsigned int, struct file_lock *, struct file_lock *);
extern int vfs_cancel_lock(struct file *filp, struct file_lock *fl);
extern int flock_lock_file_wait(struct file *filp, struct file_lock *fl);
extern int __break_lease(struct inode *inode, unsigned int flags, unsigned int type);
extern void lease_get_mtime(struct inode *, struct timespec *time);
extern int generic_setlease(struct file *, long, struct file_lock **, void **priv);
extern int vfs_setlease(struct file *, long, struct file_lock **, void **);
extern int lease_modify(struct file_lock **, int, struct list_head *);
# 1131 "include/linux/fs.h"
struct fasync_struct {
 spinlock_t fa_lock;
 int magic;
 int fa_fd;
 struct fasync_struct *fa_next;
 struct file *fa_file;
 struct callback_head fa_rcu;
};




extern int fasync_helper(int, struct file *, int, struct fasync_struct **);
extern struct fasync_struct *fasync_insert_entry(int, struct file *, struct fasync_struct **, struct fasync_struct *);
extern int fasync_remove_entry(struct file *, struct fasync_struct **);
extern struct fasync_struct *fasync_alloc(void);
extern void fasync_free(struct fasync_struct *);


extern void kill_fasync(struct fasync_struct **, int, int);

extern void __f_setown(struct file *filp, struct pid *, enum pid_type, int force);
extern void f_setown(struct file *filp, unsigned long arg, int force);
extern void f_delown(struct file *filp);
extern pid_t f_getown(struct file *filp);
extern int send_sigurg(struct fown_struct *fown);

struct mm_struct;
# 1170 "include/linux/fs.h"
extern struct list_head super_blocks;
extern spinlock_t sb_lock;


enum {
 SB_UNFROZEN = 0,
 SB_FREEZE_WRITE = 1,
 SB_FREEZE_PAGEFAULT = 2,
 SB_FREEZE_FS = 3,

 SB_FREEZE_COMPLETE = 4,
};



struct sb_writers {

 struct percpu_counter counter[(SB_FREEZE_COMPLETE - 1)];
 wait_queue_head_t wait;

 int frozen;
 wait_queue_head_t wait_unfrozen;




};

struct super_block {
 struct list_head s_list;
 dev_t s_dev;
 unsigned char s_blocksize_bits;
 unsigned long s_blocksize;
 loff_t s_maxbytes;
 struct file_system_type *s_type;
 const struct super_operations *s_op;
 const struct dquot_operations *dq_op;
 const struct quotactl_ops *s_qcop;
 const struct export_operations *s_export_op;
 unsigned long s_flags;
 unsigned long s_magic;
 struct dentry *s_root;
 struct rw_semaphore s_umount;
 int s_count;
 atomic_t s_active;



 const struct xattr_handler **s_xattr;

 struct list_head s_inodes;
 struct hlist_bl_head s_anon;
 struct list_head s_mounts;
 struct block_device *s_bdev;
 struct backing_dev_info *s_bdi;
 struct mtd_info *s_mtd;
 struct hlist_node s_instances;
 struct quota_info s_dquot;

 struct sb_writers s_writers;

 char s_id[32];
 u8 s_uuid[16];

 void *s_fs_info;
 unsigned int s_max_links;
 fmode_t s_mode;



 u32 s_time_gran;





 struct mutex s_vfs_rename_mutex;





 char *s_subtype;





 char *s_options;
 const struct dentry_operations *s_d_op;




 int cleancache_poolid;

 struct shrinker s_shrink;


 atomic_long_t s_remove_count;


 int s_readonly_remount;


 struct workqueue_struct *s_dio_done_wq;
 struct hlist_head s_pins;





 struct list_lru s_dentry_lru ;
 struct list_lru s_inode_lru ;
 struct callback_head rcu;




 int s_stack_depth;
};

extern struct timespec current_fs_time(struct super_block *sb);





void __sb_end_write(struct super_block *sb, int level);
int __sb_start_write(struct super_block *sb, int level, bool wait);
# 1308 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sb_end_write(struct super_block *sb)
{
 __sb_end_write(sb, SB_FREEZE_WRITE);
}
# 1320 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sb_end_pagefault(struct super_block *sb)
{
 __sb_end_write(sb, SB_FREEZE_PAGEFAULT);
}
# 1332 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sb_end_intwrite(struct super_block *sb)
{
 __sb_end_write(sb, SB_FREEZE_FS);
}
# 1356 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sb_start_write(struct super_block *sb)
{
 __sb_start_write(sb, SB_FREEZE_WRITE, true);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int sb_start_write_trylock(struct super_block *sb)
{
 return __sb_start_write(sb, SB_FREEZE_WRITE, false);
}
# 1385 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sb_start_pagefault(struct super_block *sb)
{
 __sb_start_write(sb, SB_FREEZE_PAGEFAULT, true);
}
# 1403 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void sb_start_intwrite(struct super_block *sb)
{
 __sb_start_write(sb, SB_FREEZE_FS, true);
}


extern bool inode_owner_or_capable(const struct inode *inode);




extern int vfs_create(struct inode *, struct dentry *, umode_t, bool);
extern int vfs_mkdir(struct inode *, struct dentry *, umode_t);
extern int vfs_mknod(struct inode *, struct dentry *, umode_t, dev_t);
extern int vfs_symlink(struct inode *, struct dentry *, const char *);
extern int vfs_link(struct dentry *, struct inode *, struct dentry *, struct inode **);
extern int vfs_rmdir(struct inode *, struct dentry *);
extern int vfs_unlink(struct inode *, struct dentry *, struct inode **);
extern int vfs_rename(struct inode *, struct dentry *, struct inode *, struct dentry *, struct inode **, unsigned int);
extern int vfs_whiteout(struct inode *, struct dentry *);




extern void dentry_unhash(struct dentry *dentry);




extern void inode_init_owner(struct inode *inode, const struct inode *dir,
   umode_t mode);



struct fiemap_extent_info {
 unsigned int fi_flags;
 unsigned int fi_extents_mapped;
 unsigned int fi_extents_max;
 struct fiemap_extent *fi_extents_start;

};
int fiemap_fill_next_extent(struct fiemap_extent_info *info, u64 logical,
       u64 phys, u64 len, u32 flags);
int fiemap_check_flags(struct fiemap_extent_info *fieinfo, u32 fs_flags);
# 1470 "include/linux/fs.h"
typedef int (*filldir_t)(void *, const char *, int, loff_t, u64, unsigned);
struct dir_context {
 const filldir_t actor;
 loff_t pos;
};

struct block_device_operations;







struct iov_iter;

struct file_operations {
 struct module *owner;
 loff_t (*llseek) (struct file *, loff_t, int);
 ssize_t (*read) (struct file *, char *, size_t, loff_t *);
 ssize_t (*write) (struct file *, const char *, size_t, loff_t *);
 ssize_t (*aio_read) (struct kiocb *, const struct iovec *, unsigned long, loff_t);
 ssize_t (*aio_write) (struct kiocb *, const struct iovec *, unsigned long, loff_t);
 ssize_t (*read_iter) (struct kiocb *, struct iov_iter *);
 ssize_t (*write_iter) (struct kiocb *, struct iov_iter *);
 int (*iterate) (struct file *, struct dir_context *);
 unsigned int (*poll) (struct file *, struct poll_table_struct *);
 long (*unlocked_ioctl) (struct file *, unsigned int, unsigned long);
 long (*compat_ioctl) (struct file *, unsigned int, unsigned long);
 int (*mmap) (struct file *, struct vm_area_struct *);
 int (*open) (struct inode *, struct file *);
 int (*flush) (struct file *, fl_owner_t id);
 int (*release) (struct inode *, struct file *);
 int (*fsync) (struct file *, loff_t, loff_t, int datasync);
 int (*aio_fsync) (struct kiocb *, int datasync);
 int (*fasync) (int, struct file *, int);
 int (*lock) (struct file *, int, struct file_lock *);
 ssize_t (*sendpage) (struct file *, struct page *, int, size_t, loff_t *, int);
 unsigned long (*get_unmapped_area)(struct file *, unsigned long, unsigned long, unsigned long, unsigned long);
 int (*check_flags)(int);
 int (*flock) (struct file *, int, struct file_lock *);
 ssize_t (*splice_write)(struct pipe_inode_info *, struct file *, loff_t *, size_t, unsigned int);
 ssize_t (*splice_read)(struct file *, loff_t *, struct pipe_inode_info *, size_t, unsigned int);
 int (*setlease)(struct file *, long, struct file_lock **, void **);
 long (*fallocate)(struct file *file, int mode, loff_t offset,
     loff_t len);
 int (*show_fdinfo)(struct seq_file *m, struct file *f);
};

struct inode_operations {
 struct dentry * (*lookup) (struct inode *,struct dentry *, unsigned int);
 void * (*follow_link) (struct dentry *, struct nameidata *);
 int (*permission) (struct inode *, int);
 struct posix_acl * (*get_acl)(struct inode *, int);

 int (*readlink) (struct dentry *, char *,int);
 void (*put_link) (struct dentry *, struct nameidata *, void *);

 int (*create) (struct inode *,struct dentry *, umode_t, bool);
 int (*link) (struct dentry *,struct inode *,struct dentry *);
 int (*unlink) (struct inode *,struct dentry *);
 int (*symlink) (struct inode *,struct dentry *,const char *);
 int (*mkdir) (struct inode *,struct dentry *,umode_t);
 int (*rmdir) (struct inode *,struct dentry *);
 int (*mknod) (struct inode *,struct dentry *,umode_t,dev_t);
 int (*rename) (struct inode *, struct dentry *,
   struct inode *, struct dentry *);
 int (*rename2) (struct inode *, struct dentry *,
   struct inode *, struct dentry *, unsigned int);
 int (*setattr) (struct dentry *, struct iattr *);
 int (*getattr) (struct vfsmount *mnt, struct dentry *, struct kstat *);
 int (*setxattr) (struct dentry *, const char *,const void *,size_t,int);
 ssize_t (*getxattr) (struct dentry *, const char *, void *, size_t);
 ssize_t (*listxattr) (struct dentry *, char *, size_t);
 int (*removexattr) (struct dentry *, const char *);
 int (*fiemap)(struct inode *, struct fiemap_extent_info *, u64 start,
        u64 len);
 int (*update_time)(struct inode *, struct timespec *, int);
 int (*atomic_open)(struct inode *, struct dentry *,
      struct file *, unsigned open_flag,
      umode_t create_mode, int *opened);
 int (*tmpfile) (struct inode *, struct dentry *, umode_t);
 int (*set_acl)(struct inode *, struct posix_acl *, int);


 int (*dentry_open)(struct dentry *, struct file *, const struct cred *);
} __attribute__((__aligned__((1 << 5))));

ssize_t rw_copy_check_uvector(int type, const struct iovec * uvector,
         unsigned long nr_segs, unsigned long fast_segs,
         struct iovec *fast_pointer,
         struct iovec **ret_pointer);

extern ssize_t vfs_read(struct file *, char *, size_t, loff_t *);
extern ssize_t vfs_write(struct file *, const char *, size_t, loff_t *);
extern ssize_t vfs_readv(struct file *, const struct iovec *,
  unsigned long, loff_t *);
extern ssize_t vfs_writev(struct file *, const struct iovec *,
  unsigned long, loff_t *);

struct super_operations {
    struct inode *(*alloc_inode)(struct super_block *sb);
 void (*destroy_inode)(struct inode *);

    void (*dirty_inode) (struct inode *, int flags);
 int (*write_inode) (struct inode *, struct writeback_control *wbc);
 int (*drop_inode) (struct inode *);
 void (*evict_inode) (struct inode *);
 void (*put_super) (struct super_block *);
 int (*sync_fs)(struct super_block *sb, int wait);
 int (*freeze_fs) (struct super_block *);
 int (*unfreeze_fs) (struct super_block *);
 int (*statfs) (struct dentry *, struct kstatfs *);
 int (*remount_fs) (struct super_block *, int *, char *);
 void (*umount_begin) (struct super_block *);

 int (*show_options)(struct seq_file *, struct dentry *);
 int (*show_devname)(struct seq_file *, struct dentry *);
 int (*show_path)(struct seq_file *, struct dentry *);
 int (*show_stats)(struct seq_file *, struct dentry *);




 int (*bdev_try_to_free_page)(struct super_block*, struct page*, gfp_t);
 long (*nr_cached_objects)(struct super_block *, int);
 long (*free_cached_objects)(struct super_block *, long, int);
};
# 1726 "include/linux/fs.h"
extern void __mark_inode_dirty(struct inode *, int);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void mark_inode_dirty(struct inode *inode)
{
 __mark_inode_dirty(inode, ((1 << 0) | (1 << 1) | (1 << 2)));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void mark_inode_dirty_sync(struct inode *inode)
{
 __mark_inode_dirty(inode, (1 << 0));
}

extern void inc_nlink(struct inode *inode);
extern void drop_nlink(struct inode *inode);
extern void clear_nlink(struct inode *inode);
extern void set_nlink(struct inode *inode, unsigned int nlink);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void inode_inc_link_count(struct inode *inode)
{
 inc_nlink(inode);
 mark_inode_dirty(inode);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void inode_dec_link_count(struct inode *inode)
{
 drop_nlink(inode);
 mark_inode_dirty(inode);
}
# 1762 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void inode_inc_iversion(struct inode *inode)
{
       spin_lock(&inode->i_lock);
       inode->i_version++;
       spin_unlock(&inode->i_lock);
}

enum file_time_flags {
 S_ATIME = 1,
 S_MTIME = 2,
 S_CTIME = 4,
 S_VERSION = 8,
};

extern void touch_atime(const struct path *);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void file_accessed(struct file *file)
{
 if (!(file->f_flags & 01000000))
  touch_atime(&file->f_path);
}

int sync_inode(struct inode *inode, struct writeback_control *wbc);
int sync_inode_metadata(struct inode *inode, int wait);

struct file_system_type {
 const char *name;
 int fs_flags;







 struct dentry *(*mount) (struct file_system_type *, int,
         const char *, void *);
 void (*kill_sb) (struct super_block *);
 struct module *owner;
 struct file_system_type * next;
 struct hlist_head fs_supers;

 struct lock_class_key s_lock_key;
 struct lock_class_key s_umount_key;
 struct lock_class_key s_vfs_rename_key;
 struct lock_class_key s_writers_key[(SB_FREEZE_COMPLETE - 1)];

 struct lock_class_key i_lock_key;
 struct lock_class_key i_mutex_key;
 struct lock_class_key i_mutex_dir_key;
};



extern struct dentry *mount_ns(struct file_system_type *fs_type, int flags,
 void *data, int (*fill_super)(struct super_block *, void *, int));
extern struct dentry *mount_bdev(struct file_system_type *fs_type,
 int flags, const char *dev_name, void *data,
 int (*fill_super)(struct super_block *, void *, int));
extern struct dentry *mount_single(struct file_system_type *fs_type,
 int flags, void *data,
 int (*fill_super)(struct super_block *, void *, int));
extern struct dentry *mount_nodev(struct file_system_type *fs_type,
 int flags, void *data,
 int (*fill_super)(struct super_block *, void *, int));
extern struct dentry *mount_subtree(struct vfsmount *mnt, const char *path);
void generic_shutdown_super(struct super_block *sb);
void kill_block_super(struct super_block *sb);
void kill_anon_super(struct super_block *sb);
void kill_litter_super(struct super_block *sb);
void deactivate_super(struct super_block *sb);
void deactivate_locked_super(struct super_block *sb);
int set_anon_super(struct super_block *s, void *data);
int get_anon_bdev(dev_t *);
void free_anon_bdev(dev_t);
struct super_block *sget(struct file_system_type *type,
   int (*test)(struct super_block *,void *),
   int (*set)(struct super_block *,void *),
   int flags, void *data);
extern struct dentry *mount_pseudo(struct file_system_type *, char *,
 const struct super_operations *ops,
 const struct dentry_operations *dops,
 unsigned long);
# 1862 "include/linux/fs.h"
extern int register_filesystem(struct file_system_type *);
extern int unregister_filesystem(struct file_system_type *);
extern struct vfsmount *kern_mount_data(struct file_system_type *, void *data);

extern void kern_unmount(struct vfsmount *mnt);
extern int may_umount_tree(struct vfsmount *);
extern int may_umount(struct vfsmount *);
extern long do_mount(const char *, const char *,
       const char *, unsigned long, void *);
extern struct vfsmount *collect_mounts(struct path *);
extern void drop_collected_mounts(struct vfsmount *);
extern int iterate_mounts(int (*)(struct vfsmount *, void *), void *,
     struct vfsmount *);
extern int vfs_statfs(struct path *, struct kstatfs *);
extern int user_statfs(const char *, struct kstatfs *);
extern int fd_statfs(int, struct kstatfs *);
extern int vfs_ustat(dev_t, struct kstatfs *);
extern int freeze_super(struct super_block *super);
extern int thaw_super(struct super_block *super);
extern bool our_mnt(struct vfsmount *mnt);

extern int current_umask(void);

extern void ihold(struct inode * inode);
extern void iput(struct inode *);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) struct inode *file_inode(const struct file *f)
{
 return f->f_inode;
}


extern struct kobject *fs_kobj;







extern int locks_mandatory_locked(struct file *);
extern int locks_mandatory_area(int, struct inode *, struct file *, loff_t, size_t);






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int __mandatory_lock(struct inode *ino)
{
 return (ino->i_mode & (0002000 | 00010)) == 0002000;
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mandatory_lock(struct inode *ino)
{
 return ((ino)->i_sb->s_flags & (64)) && __mandatory_lock(ino);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int locks_verify_locked(struct file *file)
{
 if (mandatory_lock(file_inode(file)))
  return locks_mandatory_locked(file);
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int locks_verify_truncate(struct inode *inode,
        struct file *filp,
        loff_t size)
{
 if (inode->i_flock && mandatory_lock(inode))
  return locks_mandatory_area(
   2, inode, filp,
   size < inode->i_size ? size : inode->i_size,
   (size < inode->i_size ? inode->i_size - size
    : size - inode->i_size)
  );
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int break_lease(struct inode *inode, unsigned int mode)
{





 __asm__ __volatile__("": : :"memory");
 if (inode->i_flock)
  return __break_lease(inode, mode, 32);
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int break_deleg(struct inode *inode, unsigned int mode)
{





 __asm__ __volatile__("": : :"memory");
 if (inode->i_flock)
  return __break_lease(inode, mode, 4);
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int try_break_deleg(struct inode *inode, struct inode **delegated_inode)
{
 int ret;

 ret = break_deleg(inode, 00000001|0x0080);
 if (ret == -11 && delegated_inode) {
  *delegated_inode = inode;
  ihold(inode);
 }
 return ret;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int break_deleg_wait(struct inode **delegated_inode)
{
 int ret;

 ret = break_deleg(*delegated_inode, 00000001);
 iput(*delegated_inode);
 *delegated_inode = ((void *)0);
 return ret;
}
# 2052 "include/linux/fs.h"
struct audit_names;
struct filename {
 const char *name;
 const char *uptr;
 struct audit_names *aname;
 bool separate;
};

extern long vfs_truncate(struct path *, loff_t);
extern int do_truncate(struct dentry *, loff_t start, unsigned int time_attrs,
         struct file *filp);
extern int do_fallocate(struct file *file, int mode, loff_t offset,
   loff_t len);
extern long do_sys_open(int dfd, const char *filename, int flags,
   umode_t mode);
extern struct file *file_open_name(struct filename *, int, umode_t);
extern struct file *filp_open(const char *, int, umode_t);
extern struct file *file_open_root(struct dentry *, struct vfsmount *,
       const char *, int);
extern int vfs_open(const struct path *, struct file *, const struct cred *);
extern struct file * dentry_open(const struct path *, int, const struct cred *);
extern int filp_close(struct file *, fl_owner_t id);

extern struct filename *getname(const char *);
extern struct filename *getname_kernel(const char *);

enum {
 FILE_CREATED = 1,
 FILE_OPENED = 2
};
extern int finish_open(struct file *file, struct dentry *dentry,
   int (*open)(struct inode *, struct file *),
   int *opened);
extern int finish_no_open(struct file *file, struct dentry *dentry);



extern int ioctl_preallocate(struct file *filp, void *argp);


extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) vfs_caches_init_early(void);
extern void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) vfs_caches_init(unsigned long);

extern struct kmem_cache *names_cachep;

extern void final_putname(struct filename *name);
# 2108 "include/linux/fs.h"
extern int register_blkdev(unsigned int, const char *);
extern void unregister_blkdev(unsigned int, const char *);
extern struct block_device *bdget(dev_t);
extern struct block_device *bdgrab(struct block_device *bdev);
extern void bd_set_size(struct block_device *, loff_t size);
extern void bd_forget(struct inode *inode);
extern void bdput(struct block_device *);
extern void invalidate_bdev(struct block_device *);
extern void iterate_bdevs(void (*)(struct block_device *, void *), void *);
extern int sync_blockdev(struct block_device *bdev);
extern void kill_bdev(struct block_device *);
extern struct super_block *freeze_bdev(struct block_device *);
extern void emergency_thaw_all(void);
extern int thaw_bdev(struct block_device *bdev, struct super_block *sb);
extern int fsync_bdev(struct block_device *);
extern int sb_is_blkdev_sb(struct super_block *sb);
# 2149 "include/linux/fs.h"
extern int sync_filesystem(struct super_block *);
extern const struct file_operations def_blk_fops;
extern const struct file_operations def_chr_fops;
extern const struct file_operations bad_sock_fops;

extern int ioctl_by_bdev(struct block_device *, unsigned, unsigned long);
extern int blkdev_ioctl(struct block_device *, fmode_t, unsigned, unsigned long);
extern long compat_blkdev_ioctl(struct file *, unsigned, unsigned long);
extern int blkdev_get(struct block_device *bdev, fmode_t mode, void *holder);
extern struct block_device *blkdev_get_by_path(const char *path, fmode_t mode,
            void *holder);
extern struct block_device *blkdev_get_by_dev(dev_t dev, fmode_t mode,
           void *holder);
extern void blkdev_put(struct block_device *bdev, fmode_t mode);

extern int bd_link_disk_holder(struct block_device *bdev, struct gendisk *disk);
extern void bd_unlink_disk_holder(struct block_device *bdev,
      struct gendisk *disk);
# 2182 "include/linux/fs.h"
extern int alloc_chrdev_region(dev_t *, unsigned, unsigned, const char *);
extern int register_chrdev_region(dev_t, unsigned, const char *);
extern int __register_chrdev(unsigned int major, unsigned int baseminor,
        unsigned int count, const char *name,
        const struct file_operations *fops);
extern void __unregister_chrdev(unsigned int major, unsigned int baseminor,
    unsigned int count, const char *name);
extern void unregister_chrdev_region(dev_t, unsigned);
extern void chrdev_show(struct seq_file *,off_t);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int register_chrdev(unsigned int major, const char *name,
      const struct file_operations *fops)
{
 return __register_chrdev(major, 0, 256, name, fops);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void unregister_chrdev(unsigned int major, const char *name)
{
 __unregister_chrdev(major, 0, 256, name);
}







extern const char *__bdevname(dev_t, char *buffer);
extern const char *bdevname(struct block_device *bdev, char *buffer);
extern struct block_device *lookup_bdev(const char *);
extern void blkdev_show(struct seq_file *,off_t);





extern void init_special_inode(struct inode *, umode_t, dev_t);


extern void make_bad_inode(struct inode *);
extern int is_bad_inode(struct inode *);
# 2235 "include/linux/fs.h"
extern void check_disk_size_change(struct gendisk *disk,
       struct block_device *bdev);
extern int revalidate_disk(struct gendisk *);
extern int check_disk_change(struct block_device *);
extern int __invalidate_device(struct block_device *, bool);
extern int invalidate_partition(struct gendisk *, int);

unsigned long invalidate_mapping_pages(struct address_space *mapping,
     unsigned long start, unsigned long end);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void invalidate_remote_inode(struct inode *inode)
{
 if ((((inode->i_mode) & 00170000) == 0100000) || (((inode->i_mode) & 00170000) == 0040000) ||
     (((inode->i_mode) & 00170000) == 0120000))
  invalidate_mapping_pages(inode->i_mapping, 0, -1);
}
extern int invalidate_inode_pages2(struct address_space *mapping);
extern int invalidate_inode_pages2_range(struct address_space *mapping,
      unsigned long start, unsigned long end);
extern int write_inode_now(struct inode *, int);
extern int filemap_fdatawrite(struct address_space *);
extern int filemap_flush(struct address_space *);
extern int filemap_fdatawait(struct address_space *);
extern int filemap_fdatawait_range(struct address_space *, loff_t lstart,
       loff_t lend);
extern int filemap_write_and_wait(struct address_space *mapping);
extern int filemap_write_and_wait_range(struct address_space *mapping,
            loff_t lstart, loff_t lend);
extern int __filemap_fdatawrite_range(struct address_space *mapping,
    loff_t start, loff_t end, int sync_mode);
extern int filemap_fdatawrite_range(struct address_space *mapping,
    loff_t start, loff_t end);

extern int vfs_fsync_range(struct file *file, loff_t start, loff_t end,
      int datasync);
extern int vfs_fsync(struct file *file, int datasync);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int generic_write_sync(struct file *file, loff_t pos, loff_t count)
{
 if (!(file->f_flags & 0x0010) && !(((file->f_mapping->host)->i_sb->s_flags & (16)) || ((file->f_mapping->host)->i_flags & 1)))
  return 0;
 return vfs_fsync_range(file, pos, pos + count - 1,
          (file->f_flags & 0x4000) ? 0 : 1);
}
extern void emergency_sync(void);
extern void emergency_remount(void);

extern sector_t bmap(struct inode *, sector_t);

extern int notify_change(struct dentry *, struct iattr *, struct inode **);
extern int inode_permission(struct inode *, int);
extern int __inode_permission(struct inode *, int);
extern int generic_permission(struct inode *, int);
extern int __check_sticky(struct inode *dir, struct inode *inode);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool execute_ok(struct inode *inode)
{
 return (inode->i_mode & (00100|00010|00001)) || (((inode->i_mode) & 00170000) == 0040000);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void file_start_write(struct file *file)
{
 if (!(((file_inode(file)->i_mode) & 00170000) == 0100000))
  return;
 __sb_start_write(file_inode(file)->i_sb, SB_FREEZE_WRITE, true);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool file_start_write_trylock(struct file *file)
{
 if (!(((file_inode(file)->i_mode) & 00170000) == 0100000))
  return true;
 return __sb_start_write(file_inode(file)->i_sb, SB_FREEZE_WRITE, false);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void file_end_write(struct file *file)
{
 if (!(((file_inode(file)->i_mode) & 00170000) == 0100000))
  return;
 __sb_end_write(file_inode(file)->i_sb, SB_FREEZE_WRITE);
}
# 2331 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int get_write_access(struct inode *inode)
{
 return atomic_inc_unless_negative(&inode->i_writecount) ? 0 : -26;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int deny_write_access(struct file *file)
{
 struct inode *inode = file_inode(file);
 return atomic_dec_unless_positive(&inode->i_writecount) ? 0 : -26;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void put_write_access(struct inode * inode)
{
 atomic_sub(1, (&inode->i_writecount));
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void allow_write_access(struct file *file)
{
 if (file)
  atomic_add(1, (&file_inode(file)->i_writecount));
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool inode_is_open_for_write(const struct inode *inode)
{
 return (*(volatile typeof((&inode->i_writecount)->counter) *)&((&inode->i_writecount)->counter)) > 0;
}
# 2365 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void i_readcount_dec(struct inode *inode)
{
 return;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void i_readcount_inc(struct inode *inode)
{
 return;
}

extern int do_pipe_flags(int *, int);

extern int kernel_read(struct file *, loff_t, char *, unsigned long);
extern ssize_t kernel_write(struct file *, const char *, size_t, loff_t);
extern ssize_t __kernel_write(struct file *, const char *, size_t, loff_t *);
extern struct file * open_exec(const char *);


extern int is_subdir(struct dentry *, struct dentry *);
extern int path_is_under(struct path *, struct path *);




extern loff_t default_llseek(struct file *file, loff_t offset, int whence);

extern loff_t vfs_llseek(struct file *file, loff_t offset, int whence);

extern int inode_init_always(struct super_block *, struct inode *);
extern void inode_init_once(struct inode *);
extern void address_space_init_once(struct address_space *mapping);
extern struct inode * igrab(struct inode *);
extern ino_t iunique(struct super_block *, ino_t);
extern int inode_needs_sync(struct inode *inode);
extern int generic_delete_inode(struct inode *inode);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int generic_drop_inode(struct inode *inode)
{
 return !inode->i_nlink || inode_unhashed(inode);
}

extern struct inode *ilookup5_nowait(struct super_block *sb,
  unsigned long hashval, int (*test)(struct inode *, void *),
  void *data);
extern struct inode *ilookup5(struct super_block *sb, unsigned long hashval,
  int (*test)(struct inode *, void *), void *data);
extern struct inode *ilookup(struct super_block *sb, unsigned long ino);

extern struct inode * iget5_locked(struct super_block *, unsigned long, int (*test)(struct inode *, void *), int (*set)(struct inode *, void *), void *);
extern struct inode * iget_locked(struct super_block *, unsigned long);
extern int insert_inode_locked4(struct inode *, unsigned long, int (*test)(struct inode *, void *), void *);
extern int insert_inode_locked(struct inode *);



static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void lockdep_annotate_inode_mutex_key(struct inode *inode) { };

extern void unlock_new_inode(struct inode *);
extern unsigned int get_next_ino(void);

extern void __iget(struct inode * inode);
extern void iget_failed(struct inode *);
extern void clear_inode(struct inode *);
extern void __destroy_inode(struct inode *);
extern struct inode *new_inode_pseudo(struct super_block *sb);
extern struct inode *new_inode(struct super_block *sb);
extern void free_inode_nonrcu(struct inode *inode);
extern int should_remove_suid(struct dentry *);
extern int file_remove_suid(struct file *);

extern void __insert_inode_hash(struct inode *, unsigned long hashval);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void insert_inode_hash(struct inode *inode)
{
 __insert_inode_hash(inode, inode->i_ino);
}

extern void __remove_inode_hash(struct inode *);
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void remove_inode_hash(struct inode *inode)
{
 if (!inode_unhashed(inode))
  __remove_inode_hash(inode);
}

extern void inode_sb_list_add(struct inode *inode);


extern void submit_bio(int, struct bio *);
extern int bdev_read_only(struct block_device *);

extern int set_blocksize(struct block_device *, int);
extern int sb_set_blocksize(struct super_block *, int);
extern int sb_min_blocksize(struct super_block *, int);

extern int generic_file_mmap(struct file *, struct vm_area_struct *);
extern int generic_file_readonly_mmap(struct file *, struct vm_area_struct *);
extern int generic_file_remap_pages(struct vm_area_struct *, unsigned long addr,
  unsigned long size, unsigned long pgoff);
int generic_write_checks(struct file *file, loff_t *pos, size_t *count, int isblk);
extern ssize_t generic_file_read_iter(struct kiocb *, struct iov_iter *);
extern ssize_t __generic_file_write_iter(struct kiocb *, struct iov_iter *);
extern ssize_t generic_file_write_iter(struct kiocb *, struct iov_iter *);
extern ssize_t generic_file_direct_write(struct kiocb *, struct iov_iter *, loff_t);
extern ssize_t generic_perform_write(struct file *, struct iov_iter *, loff_t);
extern ssize_t do_sync_read(struct file *filp, char *buf, size_t len, loff_t *ppos);
extern ssize_t do_sync_write(struct file *filp, const char *buf, size_t len, loff_t *ppos);
extern ssize_t new_sync_read(struct file *filp, char *buf, size_t len, loff_t *ppos);
extern ssize_t new_sync_write(struct file *filp, const char *buf, size_t len, loff_t *ppos);


extern ssize_t blkdev_read_iter(struct kiocb *iocb, struct iov_iter *to);
extern ssize_t blkdev_write_iter(struct kiocb *iocb, struct iov_iter *from);
extern int blkdev_fsync(struct file *filp, loff_t start, loff_t end,
   int datasync);
extern void block_sync_page(struct page *page);


extern ssize_t generic_file_splice_read(struct file *, loff_t *,
  struct pipe_inode_info *, size_t, unsigned int);
extern ssize_t default_file_splice_read(struct file *, loff_t *,
  struct pipe_inode_info *, size_t, unsigned int);
extern ssize_t iter_file_splice_write(struct pipe_inode_info *,
  struct file *, loff_t *, size_t, unsigned int);
extern ssize_t generic_splice_sendpage(struct pipe_inode_info *pipe,
  struct file *out, loff_t *, size_t len, unsigned int flags);
extern long do_splice_direct(struct file *in, loff_t *ppos, struct file *out,
  loff_t *opos, size_t len, unsigned int flags);


extern void
file_ra_state_init(struct file_ra_state *ra, struct address_space *mapping);
extern loff_t noop_llseek(struct file *file, loff_t offset, int whence);
extern loff_t no_llseek(struct file *file, loff_t offset, int whence);
extern loff_t vfs_setpos(struct file *file, loff_t offset, loff_t maxsize);
extern loff_t generic_file_llseek(struct file *file, loff_t offset, int whence);
extern loff_t generic_file_llseek_size(struct file *file, loff_t offset,
  int whence, loff_t maxsize, loff_t eof);
extern loff_t fixed_size_llseek(struct file *file, loff_t offset,
  int whence, loff_t size);
extern int generic_file_open(struct inode * inode, struct file * filp);
extern int nonseekable_open(struct inode * inode, struct file * filp);
# 2512 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int xip_truncate_page(struct address_space *mapping, loff_t from)
{
 return 0;
}



typedef void (dio_submit_t)(int rw, struct bio *bio, struct inode *inode,
       loff_t file_offset);

enum {

 DIO_LOCKING = 0x01,


 DIO_SKIP_HOLES = 0x02,


 DIO_ASYNC_EXTEND = 0x04,
};


void dio_end_io(struct bio *bio, int error);

ssize_t __blockdev_direct_IO(int rw, struct kiocb *iocb, struct inode *inode,
 struct block_device *bdev, struct iov_iter *iter, loff_t offset,
 get_block_t get_block, dio_iodone_t end_io,
 dio_submit_t submit_io, int flags);
# 2553 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ssize_t blockdev_direct_IO(int rw, struct kiocb *iocb,
  struct inode *inode, struct iov_iter *iter, loff_t offset,
  get_block_t get_block)
{
 return __blockdev_direct_IO(rw, iocb, inode, inode->i_sb->s_bdev, iter,
        offset, get_block, ((void *)0), ((void *)0),
        DIO_LOCKING | DIO_SKIP_HOLES);
}


void inode_dio_wait(struct inode *inode);
void inode_dio_done(struct inode *inode);

extern void inode_set_flags(struct inode *inode, unsigned int flags,
       unsigned int mask);

extern const struct file_operations generic_ro_fops;



extern int readlink_copy(char *, int, const char *);
extern int page_readlink(struct dentry *, char *, int);
extern void *page_follow_link_light(struct dentry *, struct nameidata *);
extern void page_put_link(struct dentry *, struct nameidata *, void *);
extern int __page_symlink(struct inode *inode, const char *symname, int len,
  int nofs);
extern int page_symlink(struct inode *inode, const char *symname, int len);
extern const struct inode_operations page_symlink_inode_operations;
extern void kfree_put_link(struct dentry *, struct nameidata *, void *);
extern int generic_readlink(struct dentry *, char *, int);
extern void generic_fillattr(struct inode *, struct kstat *);
int vfs_getattr_nosec(struct path *path, struct kstat *stat);
extern int vfs_getattr(struct path *, struct kstat *);
void __inode_add_bytes(struct inode *inode, loff_t bytes);
void inode_add_bytes(struct inode *inode, loff_t bytes);
void __inode_sub_bytes(struct inode *inode, loff_t bytes);
void inode_sub_bytes(struct inode *inode, loff_t bytes);
loff_t inode_get_bytes(struct inode *inode);
void inode_set_bytes(struct inode *inode, loff_t bytes);

extern int vfs_readdir(struct file *, filldir_t, void *);
extern int iterate_dir(struct file *, struct dir_context *);

extern int vfs_stat(const char *, struct kstat *);
extern int vfs_lstat(const char *, struct kstat *);
extern int vfs_fstat(unsigned int, struct kstat *);
extern int vfs_fstatat(int , const char *, struct kstat *, int);

extern int do_vfs_ioctl(struct file *filp, unsigned int fd, unsigned int cmd,
      unsigned long arg);
extern int __generic_block_fiemap(struct inode *inode,
      struct fiemap_extent_info *fieinfo,
      loff_t start, loff_t len,
      get_block_t *get_block);
extern int generic_block_fiemap(struct inode *inode,
    struct fiemap_extent_info *fieinfo, u64 start,
    u64 len, get_block_t *get_block);

extern void get_filesystem(struct file_system_type *fs);
extern void put_filesystem(struct file_system_type *fs);
extern struct file_system_type *get_fs_type(const char *name);
extern struct super_block *get_super(struct block_device *);
extern struct super_block *get_super_thawed(struct block_device *);
extern struct super_block *get_active_super(struct block_device *bdev);
extern void drop_super(struct super_block *sb);
extern void iterate_supers(void (*)(struct super_block *, void *), void *);
extern void iterate_supers_type(struct file_system_type *,
           void (*)(struct super_block *, void *), void *);

extern int dcache_dir_open(struct inode *, struct file *);
extern int dcache_dir_close(struct inode *, struct file *);
extern loff_t dcache_dir_lseek(struct file *, loff_t, int);
extern int dcache_readdir(struct file *, struct dir_context *);
extern int simple_setattr(struct dentry *, struct iattr *);
extern int simple_getattr(struct vfsmount *, struct dentry *, struct kstat *);
extern int simple_statfs(struct dentry *, struct kstatfs *);
extern int simple_open(struct inode *inode, struct file *file);
extern int simple_link(struct dentry *, struct inode *, struct dentry *);
extern int simple_unlink(struct inode *, struct dentry *);
extern int simple_rmdir(struct inode *, struct dentry *);
extern int simple_rename(struct inode *, struct dentry *, struct inode *, struct dentry *);
extern int noop_fsync(struct file *, loff_t, loff_t, int);
extern int simple_empty(struct dentry *);
extern int simple_readpage(struct file *file, struct page *page);
extern int simple_write_begin(struct file *file, struct address_space *mapping,
   loff_t pos, unsigned len, unsigned flags,
   struct page **pagep, void **fsdata);
extern int simple_write_end(struct file *file, struct address_space *mapping,
   loff_t pos, unsigned len, unsigned copied,
   struct page *page, void *fsdata);
extern int always_delete_dentry(const struct dentry *);
extern struct inode *alloc_anon_inode(struct super_block *);
extern int simple_nosetlease(struct file *, long, struct file_lock **, void **);
extern const struct dentry_operations simple_dentry_operations;

extern struct dentry *simple_lookup(struct inode *, struct dentry *, unsigned int flags);
extern ssize_t generic_read_dir(struct file *, char *, size_t, loff_t *);
extern const struct file_operations simple_dir_operations;
extern const struct inode_operations simple_dir_inode_operations;
struct tree_descr { char *name; const struct file_operations *ops; int mode; };
struct dentry *d_alloc_name(struct dentry *, const char *);
extern int simple_fill_super(struct super_block *, unsigned long, struct tree_descr *);
extern int simple_pin_fs(struct file_system_type *, struct vfsmount **mount, int *count);
extern void simple_release_fs(struct vfsmount **mount, int *count);

extern ssize_t simple_read_from_buffer(void *to, size_t count,
   loff_t *ppos, const void *from, size_t available);
extern ssize_t simple_write_to_buffer(void *to, size_t available, loff_t *ppos,
  const void *from, size_t count);

extern int __generic_file_fsync(struct file *, loff_t, loff_t, int);
extern int generic_file_fsync(struct file *, loff_t, loff_t, int);

extern int generic_check_addressable(unsigned, u64);
# 2676 "include/linux/fs.h"
extern int inode_change_ok(const struct inode *, struct iattr *);
extern int inode_newsize_ok(const struct inode *, loff_t offset);
extern void setattr_copy(struct inode *inode, const struct iattr *attr);

extern int file_update_time(struct file *file);

extern int generic_show_options(struct seq_file *m, struct dentry *root);
extern void save_mount_options(struct super_block *sb, char *options);
extern void replace_mount_options(struct super_block *sb, char *options);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) ino_t parent_ino(struct dentry *dentry)
{
 ino_t res;





 spin_lock(&dentry->d_lockref.lock);
 res = dentry->d_parent->d_inode->i_ino;
 spin_unlock(&dentry->d_lockref.lock);
 return res;
}







struct simple_transaction_argresp {
 ssize_t size;
 char data[0];
};



char *simple_transaction_get(struct file *file, const char *buf,
    size_t size);
ssize_t simple_transaction_read(struct file *file, char *buf,
    size_t size, loff_t *pos);
int simple_transaction_release(struct inode *inode, struct file *file);

void simple_transaction_set(struct file *file, size_t n);
# 2752 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __attribute__((format(printf, 1, 2)))
void __simple_attr_check_format(const char *fmt, ...)
{

}

int simple_attr_open(struct inode *inode, struct file *file,
       int (*get)(void *, u64 *), int (*set)(void *, u64),
       const char *fmt);
int simple_attr_release(struct inode *inode, struct file *file);
ssize_t simple_attr_read(struct file *file, char *buf,
    size_t len, loff_t *ppos);
ssize_t simple_attr_write(struct file *file, const char *buf,
     size_t len, loff_t *ppos);

struct ctl_table;
int proc_nr_files(struct ctl_table *table, int write,
    void *buffer, size_t *lenp, loff_t *ppos);
int proc_nr_dentry(struct ctl_table *table, int write,
    void *buffer, size_t *lenp, loff_t *ppos);
int proc_nr_inodes(struct ctl_table *table, int write,
     void *buffer, size_t *lenp, loff_t *ppos);
int __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) get_filesystem_list(char *buf);
# 2783 "include/linux/fs.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int is_sxid(umode_t mode)
{
 return (mode & 0004000) || ((mode & 0002000) && (mode & 00010));
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int check_sticky(struct inode *dir, struct inode *inode)
{
 if (!(dir->i_mode & 0001000))
  return 0;

 return __check_sticky(dir, inode);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void inode_has_no_xattr(struct inode *inode)
{
 if (!is_sxid(inode->i_mode) && (inode->i_sb->s_flags & (1<<28)))
  inode->i_flags |= 4096;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool dir_emit(struct dir_context *ctx,
       const char *name, int namelen,
       u64 ino, unsigned type)
{
 return ctx->actor(ctx, name, namelen, ctx->pos, ino, type) == 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool dir_emit_dot(struct file *file, struct dir_context *ctx)
{
 return ctx->actor(ctx, ".", 1, ctx->pos,
     file->f_path.dentry->d_inode->i_ino, 4) == 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool dir_emit_dotdot(struct file *file, struct dir_context *ctx)
{
 return ctx->actor(ctx, "..", 2, ctx->pos,
     parent_ino(file->f_path.dentry), 4) == 0;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool dir_emit_dots(struct file *file, struct dir_context *ctx)
{
 if (ctx->pos == 0) {
  if (!dir_emit_dot(file, ctx))
   return false;
  ctx->pos = 1;
 }
 if (ctx->pos == 1) {
  if (!dir_emit_dotdot(file, ctx))
   return false;
  ctx->pos = 2;
 }
 return true;
}
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool dir_relax(struct inode *inode)
{
 mutex_unlock(&inode->i_mutex);
 mutex_lock(&inode->i_mutex);
 return !((inode)->i_flags & 16);
}
# 10 "include/linux/poll.h" 2
# 1 "include/linux/sysctl.h" 1
# 28 "include/linux/sysctl.h"
# 1 "include/uapi/linux/sysctl.h" 1
# 29 "include/uapi/linux/sysctl.h"
struct completion;






struct __sysctl_args {
 int *name;
 int nlen;
 void *oldval;
 size_t *oldlenp;
 void *newval;
 size_t newlen;
 unsigned long __unused[4];
};





enum
{
 CTL_KERN=1,
 CTL_VM=2,
 CTL_NET=3,
 CTL_PROC=4,
 CTL_FS=5,
 CTL_DEBUG=6,
 CTL_DEV=7,
 CTL_BUS=8,
 CTL_ABI=9,
 CTL_CPU=10,
 CTL_ARLAN=254,
 CTL_S390DBF=5677,
 CTL_SUNRPC=7249,
 CTL_PM=9899,
 CTL_FRV=9898,
};


enum
{
 CTL_BUS_ISA=1
};


enum
{
 INOTIFY_MAX_USER_INSTANCES=1,
 INOTIFY_MAX_USER_WATCHES=2,
 INOTIFY_MAX_QUEUED_EVENTS=3
};


enum
{
 KERN_OSTYPE=1,
 KERN_OSRELEASE=2,
 KERN_OSREV=3,
 KERN_VERSION=4,
 KERN_SECUREMASK=5,
 KERN_PROF=6,
 KERN_NODENAME=7,
 KERN_DOMAINNAME=8,

 KERN_PANIC=15,
 KERN_REALROOTDEV=16,

 KERN_SPARC_REBOOT=21,
 KERN_CTLALTDEL=22,
 KERN_PRINTK=23,
 KERN_NAMETRANS=24,
 KERN_PPC_HTABRECLAIM=25,
 KERN_PPC_ZEROPAGED=26,
 KERN_PPC_POWERSAVE_NAP=27,
 KERN_MODPROBE=28,
 KERN_SG_BIG_BUFF=29,
 KERN_ACCT=30,
 KERN_PPC_L2CR=31,

 KERN_RTSIGNR=32,
 KERN_RTSIGMAX=33,

 KERN_SHMMAX=34,
 KERN_MSGMAX=35,
 KERN_MSGMNB=36,
 KERN_MSGPOOL=37,
 KERN_SYSRQ=38,
 KERN_MAX_THREADS=39,
  KERN_RANDOM=40,
  KERN_SHMALL=41,
  KERN_MSGMNI=42,
  KERN_SEM=43,
  KERN_SPARC_STOP_A=44,
  KERN_SHMMNI=45,
 KERN_OVERFLOWUID=46,
 KERN_OVERFLOWGID=47,
 KERN_SHMPATH=48,
 KERN_HOTPLUG=49,
 KERN_IEEE_EMULATION_WARNINGS=50,
 KERN_S390_USER_DEBUG_LOGGING=51,
 KERN_CORE_USES_PID=52,
 KERN_TAINTED=53,
 KERN_CADPID=54,
 KERN_PIDMAX=55,
   KERN_CORE_PATTERN=56,
 KERN_PANIC_ON_OOPS=57,
 KERN_HPPA_PWRSW=58,
 KERN_HPPA_UNALIGNED=59,
 KERN_PRINTK_RATELIMIT=60,
 KERN_PRINTK_RATELIMIT_BURST=61,
 KERN_PTY=62,
 KERN_NGROUPS_MAX=63,
 KERN_SPARC_SCONS_PWROFF=64,
 KERN_HZ_TIMER=65,
 KERN_UNKNOWN_NMI_PANIC=66,
 KERN_BOOTLOADER_TYPE=67,
 KERN_RANDOMIZE=68,
 KERN_SETUID_DUMPABLE=69,
 KERN_SPIN_RETRY=70,
 KERN_ACPI_VIDEO_FLAGS=71,
 KERN_IA64_UNALIGNED=72,
 KERN_COMPAT_LOG=73,
 KERN_MAX_LOCK_DEPTH=74,
 KERN_NMI_WATCHDOG=75,
 KERN_PANIC_ON_NMI=76,
};




enum
{
 VM_UNUSED1=1,
 VM_UNUSED2=2,
 VM_UNUSED3=3,
 VM_UNUSED4=4,
 VM_OVERCOMMIT_MEMORY=5,
 VM_UNUSED5=6,
 VM_UNUSED7=7,
 VM_UNUSED8=8,
 VM_UNUSED9=9,
 VM_PAGE_CLUSTER=10,
 VM_DIRTY_BACKGROUND=11,
 VM_DIRTY_RATIO=12,
 VM_DIRTY_WB_CS=13,
 VM_DIRTY_EXPIRE_CS=14,
 VM_NR_PDFLUSH_THREADS=15,
 VM_OVERCOMMIT_RATIO=16,
 VM_PAGEBUF=17,
 VM_HUGETLB_PAGES=18,
 VM_SWAPPINESS=19,
 VM_LOWMEM_RESERVE_RATIO=20,
 VM_MIN_FREE_KBYTES=21,
 VM_MAX_MAP_COUNT=22,
 VM_LAPTOP_MODE=23,
 VM_BLOCK_DUMP=24,
 VM_HUGETLB_GROUP=25,
 VM_VFS_CACHE_PRESSURE=26,
 VM_LEGACY_VA_LAYOUT=27,
 VM_SWAP_TOKEN_TIMEOUT=28,
 VM_DROP_PAGECACHE=29,
 VM_PERCPU_PAGELIST_FRACTION=30,
 VM_ZONE_RECLAIM_MODE=31,
 VM_MIN_UNMAPPED=32,
 VM_PANIC_ON_OOM=33,
 VM_VDSO_ENABLED=34,
 VM_MIN_SLAB=35,
};



enum
{
 NET_CORE=1,
 NET_ETHER=2,
 NET_802=3,
 NET_UNIX=4,
 NET_IPV4=5,
 NET_IPX=6,
 NET_ATALK=7,
 NET_NETROM=8,
 NET_AX25=9,
 NET_BRIDGE=10,
 NET_ROSE=11,
 NET_IPV6=12,
 NET_X25=13,
 NET_TR=14,
 NET_DECNET=15,
 NET_ECONET=16,
 NET_SCTP=17,
 NET_LLC=18,
 NET_NETFILTER=19,
 NET_DCCP=20,
 NET_IRDA=412,
};


enum
{
 RANDOM_POOLSIZE=1,
 RANDOM_ENTROPY_COUNT=2,
 RANDOM_READ_THRESH=3,
 RANDOM_WRITE_THRESH=4,
 RANDOM_BOOT_ID=5,
 RANDOM_UUID=6
};


enum
{
 PTY_MAX=1,
 PTY_NR=2
};


enum
{
 BUS_ISA_MEM_BASE=1,
 BUS_ISA_PORT_BASE=2,
 BUS_ISA_PORT_SHIFT=3
};


enum
{
 NET_CORE_WMEM_MAX=1,
 NET_CORE_RMEM_MAX=2,
 NET_CORE_WMEM_DEFAULT=3,
 NET_CORE_RMEM_DEFAULT=4,

 NET_CORE_MAX_BACKLOG=6,
 NET_CORE_FASTROUTE=7,
 NET_CORE_MSG_COST=8,
 NET_CORE_MSG_BURST=9,
 NET_CORE_OPTMEM_MAX=10,
 NET_CORE_HOT_LIST_LENGTH=11,
 NET_CORE_DIVERT_VERSION=12,
 NET_CORE_NO_CONG_THRESH=13,
 NET_CORE_NO_CONG=14,
 NET_CORE_LO_CONG=15,
 NET_CORE_MOD_CONG=16,
 NET_CORE_DEV_WEIGHT=17,
 NET_CORE_SOMAXCONN=18,
 NET_CORE_BUDGET=19,
 NET_CORE_AEVENT_ETIME=20,
 NET_CORE_AEVENT_RSEQTH=21,
 NET_CORE_WARNINGS=22,
};







enum
{
 NET_UNIX_DESTROY_DELAY=1,
 NET_UNIX_DELETE_DELAY=2,
 NET_UNIX_MAX_DGRAM_QLEN=3,
};


enum
{
 NET_NF_CONNTRACK_MAX=1,
 NET_NF_CONNTRACK_TCP_TIMEOUT_SYN_SENT=2,
 NET_NF_CONNTRACK_TCP_TIMEOUT_SYN_RECV=3,
 NET_NF_CONNTRACK_TCP_TIMEOUT_ESTABLISHED=4,
 NET_NF_CONNTRACK_TCP_TIMEOUT_FIN_WAIT=5,
 NET_NF_CONNTRACK_TCP_TIMEOUT_CLOSE_WAIT=6,
 NET_NF_CONNTRACK_TCP_TIMEOUT_LAST_ACK=7,
 NET_NF_CONNTRACK_TCP_TIMEOUT_TIME_WAIT=8,
 NET_NF_CONNTRACK_TCP_TIMEOUT_CLOSE=9,
 NET_NF_CONNTRACK_UDP_TIMEOUT=10,
 NET_NF_CONNTRACK_UDP_TIMEOUT_STREAM=11,
 NET_NF_CONNTRACK_ICMP_TIMEOUT=12,
 NET_NF_CONNTRACK_GENERIC_TIMEOUT=13,
 NET_NF_CONNTRACK_BUCKETS=14,
 NET_NF_CONNTRACK_LOG_INVALID=15,
 NET_NF_CONNTRACK_TCP_TIMEOUT_MAX_RETRANS=16,
 NET_NF_CONNTRACK_TCP_LOOSE=17,
 NET_NF_CONNTRACK_TCP_BE_LIBERAL=18,
 NET_NF_CONNTRACK_TCP_MAX_RETRANS=19,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_CLOSED=20,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_WAIT=21,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_ECHOED=22,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_ESTABLISHED=23,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_SENT=24,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_RECD=25,
 NET_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_ACK_SENT=26,
 NET_NF_CONNTRACK_COUNT=27,
 NET_NF_CONNTRACK_ICMPV6_TIMEOUT=28,
 NET_NF_CONNTRACK_FRAG6_TIMEOUT=29,
 NET_NF_CONNTRACK_FRAG6_LOW_THRESH=30,
 NET_NF_CONNTRACK_FRAG6_HIGH_THRESH=31,
 NET_NF_CONNTRACK_CHECKSUM=32,
};


enum
{

 NET_IPV4_FORWARD=8,
 NET_IPV4_DYNADDR=9,

 NET_IPV4_CONF=16,
 NET_IPV4_NEIGH=17,
 NET_IPV4_ROUTE=18,
 NET_IPV4_FIB_HASH=19,
 NET_IPV4_NETFILTER=20,

 NET_IPV4_TCP_TIMESTAMPS=33,
 NET_IPV4_TCP_WINDOW_SCALING=34,
 NET_IPV4_TCP_SACK=35,
 NET_IPV4_TCP_RETRANS_COLLAPSE=36,
 NET_IPV4_DEFAULT_TTL=37,
 NET_IPV4_AUTOCONFIG=38,
 NET_IPV4_NO_PMTU_DISC=39,
 NET_IPV4_TCP_SYN_RETRIES=40,
 NET_IPV4_IPFRAG_HIGH_THRESH=41,
 NET_IPV4_IPFRAG_LOW_THRESH=42,
 NET_IPV4_IPFRAG_TIME=43,
 NET_IPV4_TCP_MAX_KA_PROBES=44,
 NET_IPV4_TCP_KEEPALIVE_TIME=45,
 NET_IPV4_TCP_KEEPALIVE_PROBES=46,
 NET_IPV4_TCP_RETRIES1=47,
 NET_IPV4_TCP_RETRIES2=48,
 NET_IPV4_TCP_FIN_TIMEOUT=49,
 NET_IPV4_IP_MASQ_DEBUG=50,
 NET_TCP_SYNCOOKIES=51,
 NET_TCP_STDURG=52,
 NET_TCP_RFC1337=53,
 NET_TCP_SYN_TAILDROP=54,
 NET_TCP_MAX_SYN_BACKLOG=55,
 NET_IPV4_LOCAL_PORT_RANGE=56,
 NET_IPV4_ICMP_ECHO_IGNORE_ALL=57,
 NET_IPV4_ICMP_ECHO_IGNORE_BROADCASTS=58,
 NET_IPV4_ICMP_SOURCEQUENCH_RATE=59,
 NET_IPV4_ICMP_DESTUNREACH_RATE=60,
 NET_IPV4_ICMP_TIMEEXCEED_RATE=61,
 NET_IPV4_ICMP_PARAMPROB_RATE=62,
 NET_IPV4_ICMP_ECHOREPLY_RATE=63,
 NET_IPV4_ICMP_IGNORE_BOGUS_ERROR_RESPONSES=64,
 NET_IPV4_IGMP_MAX_MEMBERSHIPS=65,
 NET_TCP_TW_RECYCLE=66,
 NET_IPV4_ALWAYS_DEFRAG=67,
 NET_IPV4_TCP_KEEPALIVE_INTVL=68,
 NET_IPV4_INET_PEER_THRESHOLD=69,
 NET_IPV4_INET_PEER_MINTTL=70,
 NET_IPV4_INET_PEER_MAXTTL=71,
 NET_IPV4_INET_PEER_GC_MINTIME=72,
 NET_IPV4_INET_PEER_GC_MAXTIME=73,
 NET_TCP_ORPHAN_RETRIES=74,
 NET_TCP_ABORT_ON_OVERFLOW=75,
 NET_TCP_SYNACK_RETRIES=76,
 NET_TCP_MAX_ORPHANS=77,
 NET_TCP_MAX_TW_BUCKETS=78,
 NET_TCP_FACK=79,
 NET_TCP_REORDERING=80,
 NET_TCP_ECN=81,
 NET_TCP_DSACK=82,
 NET_TCP_MEM=83,
 NET_TCP_WMEM=84,
 NET_TCP_RMEM=85,
 NET_TCP_APP_WIN=86,
 NET_TCP_ADV_WIN_SCALE=87,
 NET_IPV4_NONLOCAL_BIND=88,
 NET_IPV4_ICMP_RATELIMIT=89,
 NET_IPV4_ICMP_RATEMASK=90,
 NET_TCP_TW_REUSE=91,
 NET_TCP_FRTO=92,
 NET_TCP_LOW_LATENCY=93,
 NET_IPV4_IPFRAG_SECRET_INTERVAL=94,
 NET_IPV4_IGMP_MAX_MSF=96,
 NET_TCP_NO_METRICS_SAVE=97,
 NET_TCP_DEFAULT_WIN_SCALE=105,
 NET_TCP_MODERATE_RCVBUF=106,
 NET_TCP_TSO_WIN_DIVISOR=107,
 NET_TCP_BIC_BETA=108,
 NET_IPV4_ICMP_ERRORS_USE_INBOUND_IFADDR=109,
 NET_TCP_CONG_CONTROL=110,
 NET_TCP_ABC=111,
 NET_IPV4_IPFRAG_MAX_DIST=112,
  NET_TCP_MTU_PROBING=113,
 NET_TCP_BASE_MSS=114,
 NET_IPV4_TCP_WORKAROUND_SIGNED_WINDOWS=115,
 NET_TCP_DMA_COPYBREAK=116,
 NET_TCP_SLOW_START_AFTER_IDLE=117,
 NET_CIPSOV4_CACHE_ENABLE=118,
 NET_CIPSOV4_CACHE_BUCKET_SIZE=119,
 NET_CIPSOV4_RBM_OPTFMT=120,
 NET_CIPSOV4_RBM_STRICTVALID=121,
 NET_TCP_AVAIL_CONG_CONTROL=122,
 NET_TCP_ALLOWED_CONG_CONTROL=123,
 NET_TCP_MAX_SSTHRESH=124,
 NET_TCP_FRTO_RESPONSE=125,
};

enum {
 NET_IPV4_ROUTE_FLUSH=1,
 NET_IPV4_ROUTE_MIN_DELAY=2,
 NET_IPV4_ROUTE_MAX_DELAY=3,
 NET_IPV4_ROUTE_GC_THRESH=4,
 NET_IPV4_ROUTE_MAX_SIZE=5,
 NET_IPV4_ROUTE_GC_MIN_INTERVAL=6,
 NET_IPV4_ROUTE_GC_TIMEOUT=7,
 NET_IPV4_ROUTE_GC_INTERVAL=8,
 NET_IPV4_ROUTE_REDIRECT_LOAD=9,
 NET_IPV4_ROUTE_REDIRECT_NUMBER=10,
 NET_IPV4_ROUTE_REDIRECT_SILENCE=11,
 NET_IPV4_ROUTE_ERROR_COST=12,
 NET_IPV4_ROUTE_ERROR_BURST=13,
 NET_IPV4_ROUTE_GC_ELASTICITY=14,
 NET_IPV4_ROUTE_MTU_EXPIRES=15,
 NET_IPV4_ROUTE_MIN_PMTU=16,
 NET_IPV4_ROUTE_MIN_ADVMSS=17,
 NET_IPV4_ROUTE_SECRET_INTERVAL=18,
 NET_IPV4_ROUTE_GC_MIN_INTERVAL_MS=19,
};

enum
{
 NET_PROTO_CONF_ALL=-2,
 NET_PROTO_CONF_DEFAULT=-3


};

enum
{
 NET_IPV4_CONF_FORWARDING=1,
 NET_IPV4_CONF_MC_FORWARDING=2,
 NET_IPV4_CONF_PROXY_ARP=3,
 NET_IPV4_CONF_ACCEPT_REDIRECTS=4,
 NET_IPV4_CONF_SECURE_REDIRECTS=5,
 NET_IPV4_CONF_SEND_REDIRECTS=6,
 NET_IPV4_CONF_SHARED_MEDIA=7,
 NET_IPV4_CONF_RP_FILTER=8,
 NET_IPV4_CONF_ACCEPT_SOURCE_ROUTE=9,
 NET_IPV4_CONF_BOOTP_RELAY=10,
 NET_IPV4_CONF_LOG_MARTIANS=11,
 NET_IPV4_CONF_TAG=12,
 NET_IPV4_CONF_ARPFILTER=13,
 NET_IPV4_CONF_MEDIUM_ID=14,
 NET_IPV4_CONF_NOXFRM=15,
 NET_IPV4_CONF_NOPOLICY=16,
 NET_IPV4_CONF_FORCE_IGMP_VERSION=17,
 NET_IPV4_CONF_ARP_ANNOUNCE=18,
 NET_IPV4_CONF_ARP_IGNORE=19,
 NET_IPV4_CONF_PROMOTE_SECONDARIES=20,
 NET_IPV4_CONF_ARP_ACCEPT=21,
 NET_IPV4_CONF_ARP_NOTIFY=22,
};


enum
{
 NET_IPV4_NF_CONNTRACK_MAX=1,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_SYN_SENT=2,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_SYN_RECV=3,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_ESTABLISHED=4,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_FIN_WAIT=5,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_CLOSE_WAIT=6,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_LAST_ACK=7,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_TIME_WAIT=8,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_CLOSE=9,
 NET_IPV4_NF_CONNTRACK_UDP_TIMEOUT=10,
 NET_IPV4_NF_CONNTRACK_UDP_TIMEOUT_STREAM=11,
 NET_IPV4_NF_CONNTRACK_ICMP_TIMEOUT=12,
 NET_IPV4_NF_CONNTRACK_GENERIC_TIMEOUT=13,
 NET_IPV4_NF_CONNTRACK_BUCKETS=14,
 NET_IPV4_NF_CONNTRACK_LOG_INVALID=15,
 NET_IPV4_NF_CONNTRACK_TCP_TIMEOUT_MAX_RETRANS=16,
 NET_IPV4_NF_CONNTRACK_TCP_LOOSE=17,
 NET_IPV4_NF_CONNTRACK_TCP_BE_LIBERAL=18,
 NET_IPV4_NF_CONNTRACK_TCP_MAX_RETRANS=19,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_CLOSED=20,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_WAIT=21,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_COOKIE_ECHOED=22,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_ESTABLISHED=23,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_SENT=24,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_RECD=25,
  NET_IPV4_NF_CONNTRACK_SCTP_TIMEOUT_SHUTDOWN_ACK_SENT=26,
 NET_IPV4_NF_CONNTRACK_COUNT=27,
 NET_IPV4_NF_CONNTRACK_CHECKSUM=28,
};


enum {
 NET_IPV6_CONF=16,
 NET_IPV6_NEIGH=17,
 NET_IPV6_ROUTE=18,
 NET_IPV6_ICMP=19,
 NET_IPV6_BINDV6ONLY=20,
 NET_IPV6_IP6FRAG_HIGH_THRESH=21,
 NET_IPV6_IP6FRAG_LOW_THRESH=22,
 NET_IPV6_IP6FRAG_TIME=23,
 NET_IPV6_IP6FRAG_SECRET_INTERVAL=24,
 NET_IPV6_MLD_MAX_MSF=25,
};

enum {
 NET_IPV6_ROUTE_FLUSH=1,
 NET_IPV6_ROUTE_GC_THRESH=2,
 NET_IPV6_ROUTE_MAX_SIZE=3,
 NET_IPV6_ROUTE_GC_MIN_INTERVAL=4,
 NET_IPV6_ROUTE_GC_TIMEOUT=5,
 NET_IPV6_ROUTE_GC_INTERVAL=6,
 NET_IPV6_ROUTE_GC_ELASTICITY=7,
 NET_IPV6_ROUTE_MTU_EXPIRES=8,
 NET_IPV6_ROUTE_MIN_ADVMSS=9,
 NET_IPV6_ROUTE_GC_MIN_INTERVAL_MS=10
};

enum {
 NET_IPV6_FORWARDING=1,
 NET_IPV6_HOP_LIMIT=2,
 NET_IPV6_MTU=3,
 NET_IPV6_ACCEPT_RA=4,
 NET_IPV6_ACCEPT_REDIRECTS=5,
 NET_IPV6_AUTOCONF=6,
 NET_IPV6_DAD_TRANSMITS=7,
 NET_IPV6_RTR_SOLICITS=8,
 NET_IPV6_RTR_SOLICIT_INTERVAL=9,
 NET_IPV6_RTR_SOLICIT_DELAY=10,
 NET_IPV6_USE_TEMPADDR=11,
 NET_IPV6_TEMP_VALID_LFT=12,
 NET_IPV6_TEMP_PREFERED_LFT=13,
 NET_IPV6_REGEN_MAX_RETRY=14,
 NET_IPV6_MAX_DESYNC_FACTOR=15,
 NET_IPV6_MAX_ADDRESSES=16,
 NET_IPV6_FORCE_MLD_VERSION=17,
 NET_IPV6_ACCEPT_RA_DEFRTR=18,
 NET_IPV6_ACCEPT_RA_PINFO=19,
 NET_IPV6_ACCEPT_RA_RTR_PREF=20,
 NET_IPV6_RTR_PROBE_INTERVAL=21,
 NET_IPV6_ACCEPT_RA_RT_INFO_MAX_PLEN=22,
 NET_IPV6_PROXY_NDP=23,
 NET_IPV6_ACCEPT_SOURCE_ROUTE=25,
 NET_IPV6_ACCEPT_RA_FROM_LOCAL=26,
 __NET_IPV6_MAX
};


enum {
 NET_IPV6_ICMP_RATELIMIT=1
};


enum {
 NET_NEIGH_MCAST_SOLICIT=1,
 NET_NEIGH_UCAST_SOLICIT=2,
 NET_NEIGH_APP_SOLICIT=3,
 NET_NEIGH_RETRANS_TIME=4,
 NET_NEIGH_REACHABLE_TIME=5,
 NET_NEIGH_DELAY_PROBE_TIME=6,
 NET_NEIGH_GC_STALE_TIME=7,
 NET_NEIGH_UNRES_QLEN=8,
 NET_NEIGH_PROXY_QLEN=9,
 NET_NEIGH_ANYCAST_DELAY=10,
 NET_NEIGH_PROXY_DELAY=11,
 NET_NEIGH_LOCKTIME=12,
 NET_NEIGH_GC_INTERVAL=13,
 NET_NEIGH_GC_THRESH1=14,
 NET_NEIGH_GC_THRESH2=15,
 NET_NEIGH_GC_THRESH3=16,
 NET_NEIGH_RETRANS_TIME_MS=17,
 NET_NEIGH_REACHABLE_TIME_MS=18,
};


enum {
 NET_DCCP_DEFAULT=1,
};


enum {
 NET_IPX_PPROP_BROADCASTING=1,
 NET_IPX_FORWARDING=2
};


enum {
 NET_LLC2=1,
 NET_LLC_STATION=2,
};


enum {
 NET_LLC2_TIMEOUT=1,
};


enum {
 NET_LLC_STATION_ACK_TIMEOUT=1,
};


enum {
 NET_LLC2_ACK_TIMEOUT=1,
 NET_LLC2_P_TIMEOUT=2,
 NET_LLC2_REJ_TIMEOUT=3,
 NET_LLC2_BUSY_TIMEOUT=4,
};


enum {
 NET_ATALK_AARP_EXPIRY_TIME=1,
 NET_ATALK_AARP_TICK_TIME=2,
 NET_ATALK_AARP_RETRANSMIT_LIMIT=3,
 NET_ATALK_AARP_RESOLVE_TIME=4
};



enum {
 NET_NETROM_DEFAULT_PATH_QUALITY=1,
 NET_NETROM_OBSOLESCENCE_COUNT_INITIALISER=2,
 NET_NETROM_NETWORK_TTL_INITIALISER=3,
 NET_NETROM_TRANSPORT_TIMEOUT=4,
 NET_NETROM_TRANSPORT_MAXIMUM_TRIES=5,
 NET_NETROM_TRANSPORT_ACKNOWLEDGE_DELAY=6,
 NET_NETROM_TRANSPORT_BUSY_DELAY=7,
 NET_NETROM_TRANSPORT_REQUESTED_WINDOW_SIZE=8,
 NET_NETROM_TRANSPORT_NO_ACTIVITY_TIMEOUT=9,
 NET_NETROM_ROUTING_CONTROL=10,
 NET_NETROM_LINK_FAILS_COUNT=11,
 NET_NETROM_RESET=12
};


enum {
 NET_AX25_IP_DEFAULT_MODE=1,
 NET_AX25_DEFAULT_MODE=2,
 NET_AX25_BACKOFF_TYPE=3,
 NET_AX25_CONNECT_MODE=4,
 NET_AX25_STANDARD_WINDOW=5,
 NET_AX25_EXTENDED_WINDOW=6,
 NET_AX25_T1_TIMEOUT=7,
 NET_AX25_T2_TIMEOUT=8,
 NET_AX25_T3_TIMEOUT=9,
 NET_AX25_IDLE_TIMEOUT=10,
 NET_AX25_N2=11,
 NET_AX25_PACLEN=12,
 NET_AX25_PROTOCOL=13,
 NET_AX25_DAMA_SLAVE_TIMEOUT=14
};


enum {
 NET_ROSE_RESTART_REQUEST_TIMEOUT=1,
 NET_ROSE_CALL_REQUEST_TIMEOUT=2,
 NET_ROSE_RESET_REQUEST_TIMEOUT=3,
 NET_ROSE_CLEAR_REQUEST_TIMEOUT=4,
 NET_ROSE_ACK_HOLD_BACK_TIMEOUT=5,
 NET_ROSE_ROUTING_CONTROL=6,
 NET_ROSE_LINK_FAIL_TIMEOUT=7,
 NET_ROSE_MAX_VCS=8,
 NET_ROSE_WINDOW_SIZE=9,
 NET_ROSE_NO_ACTIVITY_TIMEOUT=10
};


enum {
 NET_X25_RESTART_REQUEST_TIMEOUT=1,
 NET_X25_CALL_REQUEST_TIMEOUT=2,
 NET_X25_RESET_REQUEST_TIMEOUT=3,
 NET_X25_CLEAR_REQUEST_TIMEOUT=4,
 NET_X25_ACK_HOLD_BACK_TIMEOUT=5,
 NET_X25_FORWARD=6
};


enum
{
 NET_TR_RIF_TIMEOUT=1
};


enum {
 NET_DECNET_NODE_TYPE = 1,
 NET_DECNET_NODE_ADDRESS = 2,
 NET_DECNET_NODE_NAME = 3,
 NET_DECNET_DEFAULT_DEVICE = 4,
 NET_DECNET_TIME_WAIT = 5,
 NET_DECNET_DN_COUNT = 6,
 NET_DECNET_DI_COUNT = 7,
 NET_DECNET_DR_COUNT = 8,
 NET_DECNET_DST_GC_INTERVAL = 9,
 NET_DECNET_CONF = 10,
 NET_DECNET_NO_FC_MAX_CWND = 11,
 NET_DECNET_MEM = 12,
 NET_DECNET_RMEM = 13,
 NET_DECNET_WMEM = 14,
 NET_DECNET_DEBUG_LEVEL = 255
};


enum {
 NET_DECNET_CONF_LOOPBACK = -2,
 NET_DECNET_CONF_DDCMP = -3,
 NET_DECNET_CONF_PPP = -4,
 NET_DECNET_CONF_X25 = -5,
 NET_DECNET_CONF_GRE = -6,
 NET_DECNET_CONF_ETHER = -7


};


enum {
 NET_DECNET_CONF_DEV_PRIORITY = 1,
 NET_DECNET_CONF_DEV_T1 = 2,
 NET_DECNET_CONF_DEV_T2 = 3,
 NET_DECNET_CONF_DEV_T3 = 4,
 NET_DECNET_CONF_DEV_FORWARDING = 5,
 NET_DECNET_CONF_DEV_BLKSIZE = 6,
 NET_DECNET_CONF_DEV_STATE = 7
};


enum {
 NET_SCTP_RTO_INITIAL = 1,
 NET_SCTP_RTO_MIN = 2,
 NET_SCTP_RTO_MAX = 3,
 NET_SCTP_RTO_ALPHA = 4,
 NET_SCTP_RTO_BETA = 5,
 NET_SCTP_VALID_COOKIE_LIFE = 6,
 NET_SCTP_ASSOCIATION_MAX_RETRANS = 7,
 NET_SCTP_PATH_MAX_RETRANS = 8,
 NET_SCTP_MAX_INIT_RETRANSMITS = 9,
 NET_SCTP_HB_INTERVAL = 10,
 NET_SCTP_PRESERVE_ENABLE = 11,
 NET_SCTP_MAX_BURST = 12,
 NET_SCTP_ADDIP_ENABLE = 13,
 NET_SCTP_PRSCTP_ENABLE = 14,
 NET_SCTP_SNDBUF_POLICY = 15,
 NET_SCTP_SACK_TIMEOUT = 16,
 NET_SCTP_RCVBUF_POLICY = 17,
};


enum {
 NET_BRIDGE_NF_CALL_ARPTABLES = 1,
 NET_BRIDGE_NF_CALL_IPTABLES = 2,
 NET_BRIDGE_NF_CALL_IP6TABLES = 3,
 NET_BRIDGE_NF_FILTER_VLAN_TAGGED = 4,
 NET_BRIDGE_NF_FILTER_PPPOE_TAGGED = 5,
};


enum {
 NET_IRDA_DISCOVERY=1,
 NET_IRDA_DEVNAME=2,
 NET_IRDA_DEBUG=3,
 NET_IRDA_FAST_POLL=4,
 NET_IRDA_DISCOVERY_SLOTS=5,
 NET_IRDA_DISCOVERY_TIMEOUT=6,
 NET_IRDA_SLOT_TIMEOUT=7,
 NET_IRDA_MAX_BAUD_RATE=8,
 NET_IRDA_MIN_TX_TURN_TIME=9,
 NET_IRDA_MAX_TX_DATA_SIZE=10,
 NET_IRDA_MAX_TX_WINDOW=11,
 NET_IRDA_MAX_NOREPLY_TIME=12,
 NET_IRDA_WARN_NOREPLY_TIME=13,
 NET_IRDA_LAP_KEEPALIVE_TIME=14,
};



enum
{
 FS_NRINODE=1,
 FS_STATINODE=2,
 FS_MAXINODE=3,
 FS_NRDQUOT=4,
 FS_MAXDQUOT=5,
 FS_NRFILE=6,
 FS_MAXFILE=7,
 FS_DENTRY=8,
 FS_NRSUPER=9,
 FS_MAXSUPER=10,
 FS_OVERFLOWUID=11,
 FS_OVERFLOWGID=12,
 FS_LEASES=13,
 FS_DIR_NOTIFY=14,
 FS_LEASE_TIME=15,
 FS_DQSTATS=16,
 FS_XFS=17,
 FS_AIO_NR=18,
 FS_AIO_MAX_NR=19,
 FS_INOTIFY=20,
 FS_OCFS2=988,
};


enum {
 FS_DQ_LOOKUPS = 1,
 FS_DQ_DROPS = 2,
 FS_DQ_READS = 3,
 FS_DQ_WRITES = 4,
 FS_DQ_CACHE_HITS = 5,
 FS_DQ_ALLOCATED = 6,
 FS_DQ_FREE = 7,
 FS_DQ_SYNCS = 8,
 FS_DQ_WARNINGS = 9,
};




enum {
 DEV_CDROM=1,
 DEV_HWMON=2,
 DEV_PARPORT=3,
 DEV_RAID=4,
 DEV_MAC_HID=5,
 DEV_SCSI=6,
 DEV_IPMI=7,
};


enum {
 DEV_CDROM_INFO=1,
 DEV_CDROM_AUTOCLOSE=2,
 DEV_CDROM_AUTOEJECT=3,
 DEV_CDROM_DEBUG=4,
 DEV_CDROM_LOCK=5,
 DEV_CDROM_CHECK_MEDIA=6
};


enum {
 DEV_PARPORT_DEFAULT=-3
};


enum {
 DEV_RAID_SPEED_LIMIT_MIN=1,
 DEV_RAID_SPEED_LIMIT_MAX=2
};


enum {
 DEV_PARPORT_DEFAULT_TIMESLICE=1,
 DEV_PARPORT_DEFAULT_SPINTIME=2
};


enum {
 DEV_PARPORT_SPINTIME=1,
 DEV_PARPORT_BASE_ADDR=2,
 DEV_PARPORT_IRQ=3,
 DEV_PARPORT_DMA=4,
 DEV_PARPORT_MODES=5,
 DEV_PARPORT_DEVICES=6,
 DEV_PARPORT_AUTOPROBE=16
};


enum {
 DEV_PARPORT_DEVICES_ACTIVE=-3,
};


enum {
 DEV_PARPORT_DEVICE_TIMESLICE=1,
};


enum {
 DEV_MAC_HID_KEYBOARD_SENDS_LINUX_KEYCODES=1,
 DEV_MAC_HID_KEYBOARD_LOCK_KEYCODES=2,
 DEV_MAC_HID_MOUSE_BUTTON_EMULATION=3,
 DEV_MAC_HID_MOUSE_BUTTON2_KEYCODE=4,
 DEV_MAC_HID_MOUSE_BUTTON3_KEYCODE=5,
 DEV_MAC_HID_ADB_MOUSE_SENDS_KEYCODES=6
};


enum {
 DEV_SCSI_LOGGING_LEVEL=1,
};


enum {
 DEV_IPMI_POWEROFF_POWERCYCLE=1,
};


enum
{
 ABI_DEFHANDLER_COFF=1,
 ABI_DEFHANDLER_ELF=2,
 ABI_DEFHANDLER_LCALL7=3,
 ABI_DEFHANDLER_LIBCSO=4,
 ABI_TRACE=5,
 ABI_FAKE_UTSNAME=6,
};
# 29 "include/linux/sysctl.h" 2


struct ctl_table;
struct nsproxy;
struct ctl_table_root;
struct ctl_table_header;
struct ctl_dir;

typedef int proc_handler (struct ctl_table *ctl, int write,
     void *buffer, size_t *lenp, loff_t *ppos);

extern int proc_dostring(struct ctl_table *, int,
    void *, size_t *, loff_t *);
extern int proc_dointvec(struct ctl_table *, int,
    void *, size_t *, loff_t *);
extern int proc_dointvec_minmax(struct ctl_table *, int,
    void *, size_t *, loff_t *);
extern int proc_dointvec_jiffies(struct ctl_table *, int,
     void *, size_t *, loff_t *);
extern int proc_dointvec_userhz_jiffies(struct ctl_table *, int,
     void *, size_t *, loff_t *);
extern int proc_dointvec_ms_jiffies(struct ctl_table *, int,
        void *, size_t *, loff_t *);
extern int proc_doulongvec_minmax(struct ctl_table *, int,
      void *, size_t *, loff_t *);
extern int proc_doulongvec_ms_jiffies_minmax(struct ctl_table *table, int,
          void *, size_t *, loff_t *);
extern int proc_do_large_bitmap(struct ctl_table *, int,
    void *, size_t *, loff_t *);
# 87 "include/linux/sysctl.h"
struct ctl_table_poll {
 atomic_t event;
 wait_queue_head_t wait;
};

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void *proc_sys_poll_event(struct ctl_table_poll *poll)
{
 return (void *)(unsigned long)(*(volatile typeof((&poll->event)->counter) *)&((&poll->event)->counter));
}
# 105 "include/linux/sysctl.h"
struct ctl_table
{
 const char *procname;
 void *data;
 int maxlen;
 umode_t mode;
 struct ctl_table *child;
 proc_handler *proc_handler;
 struct ctl_table_poll *poll;
 void *extra1;
 void *extra2;
};

struct ctl_node {
 struct rb_node node;
 struct ctl_table_header *header;
};



struct ctl_table_header
{
 union {
  struct {
   struct ctl_table *ctl_table;
   int used;
   int count;
   int nreg;
  };
  struct callback_head rcu;
 };
 struct completion *unregistering;
 struct ctl_table *ctl_table_arg;
 struct ctl_table_root *root;
 struct ctl_table_set *set;
 struct ctl_dir *parent;
 struct ctl_node *node;
};

struct ctl_dir {

 struct ctl_table_header header;
 struct rb_root root;
};

struct ctl_table_set {
 int (*is_seen)(struct ctl_table_set *);
 struct ctl_dir dir;
};

struct ctl_table_root {
 struct ctl_table_set default_set;
 struct ctl_table_set *(*lookup)(struct ctl_table_root *root,
        struct nsproxy *namespaces);
 int (*permissions)(struct ctl_table_header *head, struct ctl_table *table);
};


struct ctl_path {
 const char *procname;
};



void proc_sys_poll_notify(struct ctl_table_poll *poll);

extern void setup_sysctl_set(struct ctl_table_set *p,
 struct ctl_table_root *root,
 int (*is_seen)(struct ctl_table_set *));
extern void retire_sysctl_set(struct ctl_table_set *set);

void register_sysctl_root(struct ctl_table_root *root);
struct ctl_table_header *__register_sysctl_table(
 struct ctl_table_set *set,
 const char *path, struct ctl_table *table);
struct ctl_table_header *__register_sysctl_paths(
 struct ctl_table_set *set,
 const struct ctl_path *path, struct ctl_table *table);
struct ctl_table_header *register_sysctl(const char *path, struct ctl_table *table);
struct ctl_table_header *register_sysctl_table(struct ctl_table * table);
struct ctl_table_header *register_sysctl_paths(const struct ctl_path *path,
      struct ctl_table *table);

void unregister_sysctl_table(struct ctl_table_header * table);

extern int sysctl_init(void);
# 11 "include/linux/poll.h" 2
# 1 "./arch/mips/include/asm/uaccess.h" 1
# 17 "./arch/mips/include/asm/uaccess.h"
# 1 "./arch/mips/include/asm/asm-eva.h" 1
# 18 "./arch/mips/include/asm/uaccess.h" 2
# 220 "./arch/mips/include/asm/uaccess.h"
struct __large_struct { unsigned long buf[100]; };
# 267 "./arch/mips/include/asm/uaccess.h"
extern void __get_user_unknown(void);
# 489 "./arch/mips/include/asm/uaccess.h"
extern void __put_user_unknown(void);
# 593 "./arch/mips/include/asm/uaccess.h"
extern void __get_user_unaligned_unknown(void);
# 761 "./arch/mips/include/asm/uaccess.h"
extern void __put_user_unaligned_unknown(void);
# 786 "./arch/mips/include/asm/uaccess.h"
extern size_t __copy_user(void *__to, const void *__from, size_t __n);
# 845 "./arch/mips/include/asm/uaccess.h"
extern size_t __copy_user_inatomic(void *__to, const void *__from, size_t __n);
# 1199 "./arch/mips/include/asm/uaccess.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) __kernel_size_t
__clear_user(void *addr, __kernel_size_t size)
{
 __kernel_size_t res;

 might_fault();
 __asm__ __volatile__(
  "move\t$4, %1\n\t"
  "move\t$5, $0\n\t"
  "move\t$6, %2\n\t"
  "jal\t" "__bzero" "\n\t"
  "move\t%0, $6"
  : "=r" (res)
  : "r" (addr), "r" (size)
  : "$4", "$5", "$6", "$8", "$9", "$31");

 return res;
}
# 1248 "./arch/mips/include/asm/uaccess.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long
__strncpy_from_user(char *__to, const char *__from, long __len)
{
 long res;

 if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "move\t$6, %3\n\t"
   "jal\t" "__strncpy_from_kernel_nocheck_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (__to), "r" (__from), "r" (__len)
   : "$2", "$3", "$4", "$5", "$6", "$8", "$31", "memory");
 } else {
  might_fault();
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "move\t$6, %3\n\t"
   "jal\t" "__strncpy_from_user_nocheck_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (__to), "r" (__from), "r" (__len)
   : "$2", "$3", "$4", "$5", "$6", "$8", "$31", "memory");
 }

 return res;
}
# 1297 "./arch/mips/include/asm/uaccess.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long
strncpy_from_user(char *__to, const char *__from, long __len)
{
 long res;

 if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "move\t$6, %3\n\t"
   "jal\t" "__strncpy_from_kernel_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (__to), "r" (__from), "r" (__len)
   : "$2", "$3", "$4", "$5", "$6", "$8", "$31", "memory");
 } else {
  might_fault();
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "move\t$6, %3\n\t"
   "jal\t" "__strncpy_from_user_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (__to), "r" (__from), "r" (__len)
   : "$2", "$3", "$4", "$5", "$6", "$8", "$31", "memory");
 }

 return res;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long __strlen_user(const char *s)
{
 long res;

 if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "jal\t" "__strlen_kernel_nocheck_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s)
   : "$2", "$4", "$8", "$31");
 } else {
  might_fault();
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "jal\t" "__strlen_user_nocheck_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s)
   : "$2", "$4", "$8", "$31");
 }

 return res;
}
# 1369 "./arch/mips/include/asm/uaccess.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long strlen_user(const char *s)
{
 long res;

 if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "jal\t" "__strlen_kernel_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s)
   : "$2", "$4", "$8", "$31");
 } else {
  might_fault();
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "jal\t" "__strlen_kernel_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s)
   : "$2", "$4", "$8", "$31");
 }

 return res;
}


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long __strnlen_user(const char *s, long n)
{
 long res;

 if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "jal\t" "__strnlen_kernel_nocheck_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s), "r" (n)
   : "$2", "$4", "$5", "$8", "$31");
 } else {
  might_fault();
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "jal\t" "__strnlen_user_nocheck_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s), "r" (n)
   : "$2", "$4", "$5", "$8", "$31");
 }

 return res;
}
# 1436 "./arch/mips/include/asm/uaccess.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) long strnlen_user(const char *s, long n)
{
 long res;

 might_fault();
 if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "jal\t" "__strnlen_kernel_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s), "r" (n)
   : "$2", "$4", "$5", "$8", "$31");
 } else {
  __asm__ __volatile__(
   "move\t$4, %1\n\t"
   "move\t$5, %2\n\t"
   "jal\t" "__strnlen_user_asm" "\n\t"
   "move\t%0, $2"
   : "=r" (res)
   : "r" (s), "r" (n)
   : "$2", "$4", "$5", "$8", "$31");
 }

 return res;
}

struct exception_table_entry
{
 unsigned long insn;
 unsigned long nextinsn;
};

extern int fixup_exception(struct pt_regs *regs);
# 12 "include/linux/poll.h" 2
# 1 "include/uapi/linux/poll.h" 1
# 1 "./arch/mips/include/uapi/asm/poll.h" 1






# 1 "./include/uapi/asm-generic/poll.h" 1
# 35 "./include/uapi/asm-generic/poll.h"
struct pollfd {
 int fd;
 short events;
 short revents;
};
# 8 "./arch/mips/include/uapi/asm/poll.h" 2
# 1 "include/uapi/linux/poll.h" 2
# 13 "include/linux/poll.h" 2

extern struct ctl_table epoll_table[];
# 26 "include/linux/poll.h"
struct poll_table_struct;




typedef void (*poll_queue_proc)(struct file *, wait_queue_head_t *, struct poll_table_struct *);





typedef struct poll_table_struct {
 poll_queue_proc _qproc;
 unsigned long _key;
} poll_table;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void poll_wait(struct file * filp, wait_queue_head_t * wait_address, poll_table *p)
{
 if (p && p->_qproc && wait_address)
  p->_qproc(filp, wait_address, p);
}






static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool poll_does_not_wait(const poll_table *p)
{
 return p == ((void *)0) || p->_qproc == ((void *)0);
}







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long poll_requested_events(const poll_table *p)
{
 return p ? p->_key : ~0UL;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void init_poll_funcptr(poll_table *pt, poll_queue_proc qproc)
{
 pt->_qproc = qproc;
 pt->_key = ~0UL;
}

struct poll_table_entry {
 struct file *filp;
 unsigned long key;
 wait_queue_t wait;
 wait_queue_head_t *wait_address;
};




struct poll_wqueues {
 poll_table pt;
 struct poll_table_page *table;
 struct task_struct *polling_task;
 int triggered;
 int error;
 int inline_index;
 struct poll_table_entry inline_entries[((832 - 256) / sizeof(struct poll_table_entry))];
};

extern void poll_initwait(struct poll_wqueues *pwq);
extern void poll_freewait(struct poll_wqueues *pwq);
extern int poll_schedule_timeout(struct poll_wqueues *pwq, int state,
     ktime_t *expires, unsigned long slack);
extern long select_estimate_accuracy(struct timespec *tv);


static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int poll_schedule(struct poll_wqueues *pwq, int state)
{
 return poll_schedule_timeout(pwq, state, ((void *)0), 0);
}





typedef struct {
 unsigned long *in, *out, *ex;
 unsigned long *res_in, *res_out, *res_ex;
} fd_set_bits;
# 129 "include/linux/poll.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function))
int get_fd_set(unsigned long nr, void *ufdset, unsigned long *fdset)
{
 nr = ((((nr)+(8*sizeof(long))-1)/(8*sizeof(long)))*sizeof(long));
 if (ufdset)
  return ({ void *__cu_to; const void *__cu_from; long __cu_len; __cu_to = (fdset); __cu_from = (ufdset); __cu_len = (nr); if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) { __cu_len = ({ register void *__cu_to_r __asm__("$4"); register const void *__cu_from_r __asm__("$5"); register long __cu_len_r __asm__("$6"); __cu_to_r = (__cu_to); __cu_from_r = (__cu_from); __cu_len_r = (__cu_len); __asm__ __volatile__( ".set\tnoreorder\n\t" "jal\t" "__copy_user" "\n\t" ".set\tnoat\n\t" "addu" "\t$1, %1, %2\n\t" ".set\tat\n\t" ".set\treorder" : "+r" (__cu_to_r), "+r" (__cu_from_r), "+r" (__cu_len_r) : : "$8", "$9", "$10", "$11", "$12", "$14", "$15", "$24", "$31", "$0", "memory"); __cu_len_r; }); } else { if (__builtin_expect(!!(({ unsigned long __addr = (unsigned long) ((__cu_from)); unsigned long __size = (__cu_len); unsigned long __mask = (current_thread_info()->addr_limit).seg; unsigned long __ok; (void)0; __ok = (signed long)(__mask & (__addr | (__addr + __size) | ((__builtin_constant_p(__size) && (signed long) (__size) > 0) ? 0 : (__size)))); __ok == 0; })), 1)) { might_fault(); __cu_len = ({ register void *__cu_to_r __asm__("$4"); register const void *__cu_from_r __asm__("$5"); register long __cu_len_r __asm__("$6"); __cu_to_r = (__cu_to); __cu_from_r = (__cu_from); __cu_len_r = (__cu_len); __asm__ __volatile__( ".set\tnoreorder\n\t" "jal\t" "__copy_user" "\n\t" ".set\tnoat\n\t" "addu" "\t$1, %1, %2\n\t" ".set\tat\n\t" ".set\treorder" : "+r" (__cu_to_r), "+r" (__cu_from_r), "+r" (__cu_len_r) : : "$8", "$9", "$10", "$11", "$12", "$14", "$15", "$24", "$31", "$0", "memory"); __cu_len_r; }); } } __cu_len; }) ? -14 : 0;

 ({ size_t __len = (nr); void *__ret; if (__builtin_constant_p(nr) && __len >= 64) __ret = memset((fdset), (0), __len); else __ret = __builtin_memset((fdset), (0), __len); __ret; });
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long
set_fd_set(unsigned long nr, void *ufdset, unsigned long *fdset)
{
 if (ufdset)
  return ({ void *__cu_to; const void *__cu_from; long __cu_len; __cu_to = (ufdset); __cu_from = (fdset); __cu_len = (((((nr)+(8*sizeof(long))-1)/(8*sizeof(long)))*sizeof(long))); might_fault(); if ((((current_thread_info()->addr_limit)).seg == ((((mm_segment_t) { 0UL }))).seg)) __cu_len = ({ register void *__cu_to_r __asm__("$4"); register const void *__cu_from_r __asm__("$5"); register long __cu_len_r __asm__("$6"); __cu_to_r = (__cu_to); __cu_from_r = (__cu_from); __cu_len_r = (__cu_len); __asm__ __volatile__( "jal\t" "__copy_user" "\n\t" : "+r" (__cu_to_r), "+r" (__cu_from_r), "+r" (__cu_len_r) : : "$8", "$9", "$10", "$11", "$12", "$14", "$15", "$24", "$31", "$0", "memory"); __cu_len_r; }); else __cu_len = ({ register void *__cu_to_r __asm__("$4"); register const void *__cu_from_r __asm__("$5"); register long __cu_len_r __asm__("$6"); __cu_to_r = (__cu_to); __cu_from_r = (__cu_from); __cu_len_r = (__cu_len); __asm__ __volatile__( "jal\t" "__copy_user" "\n\t" : "+r" (__cu_to_r), "+r" (__cu_from_r), "+r" (__cu_len_r) : : "$8", "$9", "$10", "$11", "$12", "$14", "$15", "$24", "$31", "$0", "memory"); __cu_len_r; }); __cu_len; });
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function))
void zero_fd_set(unsigned long nr, unsigned long *fdset)
{
 ({ size_t __len = (((((nr)+(8*sizeof(long))-1)/(8*sizeof(long)))*sizeof(long))); void *__ret; if (__builtin_constant_p(((((nr)+(8*sizeof(long))-1)/(8*sizeof(long)))*sizeof(long))) && __len >= 64) __ret = memset((fdset), (0), __len); else __ret = __builtin_memset((fdset), (0), __len); __ret; });
}



extern int do_select(int n, fd_set_bits *fds, struct timespec *end_time);
extern int do_sys_poll(struct pollfd * ufds, unsigned int nfds,
         struct timespec *end_time);
extern int core_sys_select(int n, fd_set *inp, fd_set *outp,
      fd_set *exp, struct timespec *end_time);

extern int poll_select_set_timeout(struct timespec *to, long sec, long nsec);
# 32 "include/linux/rtc.h" 2




extern struct class *rtc_class;
# 54 "include/linux/rtc.h"
struct rtc_class_ops {
 int (*open)(struct device *);
 void (*release)(struct device *);
 int (*ioctl)(struct device *, unsigned int, unsigned long);
 int (*read_time)(struct device *, struct rtc_time *);
 int (*set_time)(struct device *, struct rtc_time *);
 int (*read_alarm)(struct device *, struct rtc_wkalrm *);
 int (*set_alarm)(struct device *, struct rtc_wkalrm *);
 int (*proc)(struct device *, struct seq_file *);
 int (*set_mmss)(struct device *, unsigned long secs);
 int (*read_callback)(struct device *, int data);
 int (*alarm_irq_enable)(struct device *, unsigned int enabled);
};


typedef struct rtc_task {
 void (*func)(void *private_data);
 void *private_data;
} rtc_task_t;


struct rtc_timer {
 struct rtc_task task;
 struct timerqueue_node node;
 ktime_t period;
 int enabled;
};





struct rtc_device
{
 struct device dev;
 struct module *owner;

 int id;
 char name[20];

 const struct rtc_class_ops *ops;
 struct mutex ops_lock;

 struct cdev char_dev;
 unsigned long flags;

 unsigned long irq_data;
 spinlock_t irq_lock;
 wait_queue_head_t irq_queue;
 struct fasync_struct *async_queue;

 struct rtc_task *irq_task;
 spinlock_t irq_task_lock;
 int irq_freq;
 int max_user_freq;

 struct timerqueue_head timerqueue;
 struct rtc_timer aie_timer;
 struct rtc_timer uie_rtctimer;
 struct hrtimer pie_timer;
 int pie_enabled;
 struct work_struct irqwork;

 int uie_unsupported;
# 129 "include/linux/rtc.h"
};


extern struct rtc_device *rtc_device_register(const char *name,
     struct device *dev,
     const struct rtc_class_ops *ops,
     struct module *owner);
extern struct rtc_device *devm_rtc_device_register(struct device *dev,
     const char *name,
     const struct rtc_class_ops *ops,
     struct module *owner);
extern void rtc_device_unregister(struct rtc_device *rtc);
extern void devm_rtc_device_unregister(struct device *dev,
     struct rtc_device *rtc);

extern int rtc_read_time(struct rtc_device *rtc, struct rtc_time *tm);
extern int rtc_set_time(struct rtc_device *rtc, struct rtc_time *tm);
extern int rtc_set_mmss(struct rtc_device *rtc, unsigned long secs);
extern int rtc_set_ntp_time(struct timespec now);
int __rtc_read_alarm(struct rtc_device *rtc, struct rtc_wkalrm *alarm);
extern int rtc_read_alarm(struct rtc_device *rtc,
   struct rtc_wkalrm *alrm);
extern int rtc_set_alarm(struct rtc_device *rtc,
    struct rtc_wkalrm *alrm);
extern int rtc_initialize_alarm(struct rtc_device *rtc,
    struct rtc_wkalrm *alrm);
extern void rtc_update_irq(struct rtc_device *rtc,
   unsigned long num, unsigned long events);

extern struct rtc_device *rtc_class_open(const char *name);
extern void rtc_class_close(struct rtc_device *rtc);

extern int rtc_irq_register(struct rtc_device *rtc,
    struct rtc_task *task);
extern void rtc_irq_unregister(struct rtc_device *rtc,
    struct rtc_task *task);
extern int rtc_irq_set_state(struct rtc_device *rtc,
    struct rtc_task *task, int enabled);
extern int rtc_irq_set_freq(struct rtc_device *rtc,
    struct rtc_task *task, int freq);
extern int rtc_update_irq_enable(struct rtc_device *rtc, unsigned int enabled);
extern int rtc_alarm_irq_enable(struct rtc_device *rtc, unsigned int enabled);
extern int rtc_dev_update_irq_enable_emul(struct rtc_device *rtc,
      unsigned int enabled);

void rtc_handle_legacy_irq(struct rtc_device *rtc, int num, int mode);
void rtc_aie_update_irq(void *private);
void rtc_uie_update_irq(void *private);
enum hrtimer_restart rtc_pie_update_irq(struct hrtimer *timer);

int rtc_register(rtc_task_t *task);
int rtc_unregister(rtc_task_t *task);
int rtc_control(rtc_task_t *t, unsigned int cmd, unsigned long arg);

void rtc_timer_init(struct rtc_timer *timer, void (*f)(void* p), void* data);
int rtc_timer_start(struct rtc_device *rtc, struct rtc_timer* timer,
   ktime_t expires, ktime_t period);
int rtc_timer_cancel(struct rtc_device *rtc, struct rtc_timer* timer);
void rtc_timer_do_work(struct work_struct *work);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) bool is_leap_year(unsigned int year)
{
 return (!(year % 4) && (year % 100)) || !(year % 400);
}
# 18 "./arch/mips/include/asm/time.h" 2

# 1 "include/linux/clockchips.h" 1
# 12 "include/linux/clockchips.h"
enum clock_event_nofitiers {
 CLOCK_EVT_NOTIFY_ADD,
 CLOCK_EVT_NOTIFY_BROADCAST_ON,
 CLOCK_EVT_NOTIFY_BROADCAST_OFF,
 CLOCK_EVT_NOTIFY_BROADCAST_FORCE,
 CLOCK_EVT_NOTIFY_BROADCAST_ENTER,
 CLOCK_EVT_NOTIFY_BROADCAST_EXIT,
 CLOCK_EVT_NOTIFY_SUSPEND,
 CLOCK_EVT_NOTIFY_RESUME,
 CLOCK_EVT_NOTIFY_CPU_DYING,
 CLOCK_EVT_NOTIFY_CPU_DEAD,
};



# 1 "include/linux/clocksource.h" 1
# 22 "include/linux/clocksource.h"
typedef u64 cycle_t;
struct clocksource;
struct module;
# 44 "include/linux/clocksource.h"
struct cyclecounter {
 cycle_t (*read)(const struct cyclecounter *cc);
 cycle_t mask;
 u32 mult;
 u32 shift;
};
# 67 "include/linux/clocksource.h"
struct timecounter {
 const struct cyclecounter *cc;
 cycle_t cycle_last;
 u64 nsec;
};
# 81 "include/linux/clocksource.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u64 cyclecounter_cyc2ns(const struct cyclecounter *cc,
          cycle_t cycles)
{
 u64 ret = (u64)cycles;
 ret = (ret * cc->mult) >> cc->shift;
 return ret;
}
# 99 "include/linux/clocksource.h"
extern void timecounter_init(struct timecounter *tc,
        const struct cyclecounter *cc,
        u64 start_tstamp);
# 111 "include/linux/clocksource.h"
extern u64 timecounter_read(struct timecounter *tc);
# 127 "include/linux/clocksource.h"
extern u64 timecounter_cyc2time(struct timecounter *tc,
    cycle_t cycle_tstamp);
# 167 "include/linux/clocksource.h"
struct clocksource {




 cycle_t (*read)(struct clocksource *cs);
 cycle_t mask;
 u32 mult;
 u32 shift;
 u64 max_idle_ns;
 u32 maxadj;




 const char *name;
 struct list_head list;
 int rating;
 int (*enable)(struct clocksource *cs);
 void (*disable)(struct clocksource *cs);
 unsigned long flags;
 void (*suspend)(struct clocksource *cs);
 void (*resume)(struct clocksource *cs);
# 198 "include/linux/clocksource.h"
 struct module *owner;
} __attribute__((__aligned__((1 << 5))));
# 224 "include/linux/clocksource.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 clocksource_khz2mult(u32 khz, u32 shift_constant)
{







 u64 tmp = ((u64)1000000) << shift_constant;

 tmp += khz/2;
 ({ uint32_t __base = (khz); uint32_t __rem; (void)(((typeof((tmp)) *)0) == ((uint64_t *)0)); if (__builtin_expect(!!(((tmp) >> 32) == 0), 1)) { __rem = (uint32_t)(tmp) % __base; (tmp) = (uint32_t)(tmp) / __base; } else __rem = __div64_32(&(tmp), __base); __rem; });

 return (u32)tmp;
}
# 250 "include/linux/clocksource.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 clocksource_hz2mult(u32 hz, u32 shift_constant)
{







 u64 tmp = ((u64)1000000000) << shift_constant;

 tmp += hz/2;
 ({ uint32_t __base = (hz); uint32_t __rem; (void)(((typeof((tmp)) *)0) == ((uint64_t *)0)); if (__builtin_expect(!!(((tmp) >> 32) == 0), 1)) { __rem = (uint32_t)(tmp) % __base; (tmp) = (uint32_t)(tmp) / __base; } else __rem = __div64_32(&(tmp), __base); __rem; });

 return (u32)tmp;
}
# 277 "include/linux/clocksource.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) s64 clocksource_cyc2ns(cycle_t cycles, u32 mult, u32 shift)
{
 return ((u64) cycles * mult) >> shift;
}


extern int clocksource_register(struct clocksource*);
extern int clocksource_unregister(struct clocksource*);
extern void clocksource_touch_watchdog(void);
extern struct clocksource* clocksource_get_next(void);
extern void clocksource_change_rating(struct clocksource *cs, int rating);
extern void clocksource_suspend(void);
extern void clocksource_resume(void);
extern struct clocksource * __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) clocksource_default_clock(void);
extern void clocksource_mark_unstable(struct clocksource *cs);

extern u64
clocks_calc_max_nsecs(u32 mult, u32 shift, u32 maxadj, u64 mask);
extern void
clocks_calc_mult_shift(u32 *mult, u32 *shift, u32 from, u32 to, u32 minsec);





extern int
__clocksource_register_scale(struct clocksource *cs, u32 scale, u32 freq);
extern void
__clocksource_updatefreq_scale(struct clocksource *cs, u32 scale, u32 freq);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int clocksource_register_hz(struct clocksource *cs, u32 hz)
{
 return __clocksource_register_scale(cs, 1, hz);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int clocksource_register_khz(struct clocksource *cs, u32 khz)
{
 return __clocksource_register_scale(cs, 1000, khz);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __clocksource_updatefreq_hz(struct clocksource *cs, u32 hz)
{
 __clocksource_updatefreq_scale(cs, 1, hz);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void __clocksource_updatefreq_khz(struct clocksource *cs, u32 khz)
{
 __clocksource_updatefreq_scale(cs, 1000, khz);
}


extern int timekeeping_notify(struct clocksource *clock);

extern cycle_t clocksource_mmio_readl_up(struct clocksource *);
extern cycle_t clocksource_mmio_readl_down(struct clocksource *);
extern cycle_t clocksource_mmio_readw_up(struct clocksource *);
extern cycle_t clocksource_mmio_readw_down(struct clocksource *);

extern int clocksource_mmio_init(void *, const char *,
 unsigned long, int, unsigned, cycle_t (*)(struct clocksource *));

extern int clocksource_i8253_init(void);







static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clocksource_of_init(void) {}
# 28 "include/linux/clockchips.h" 2




struct clock_event_device;
struct module;


enum clock_event_mode {
 CLOCK_EVT_MODE_UNUSED = 0,
 CLOCK_EVT_MODE_SHUTDOWN,
 CLOCK_EVT_MODE_PERIODIC,
 CLOCK_EVT_MODE_ONESHOT,
 CLOCK_EVT_MODE_RESUME,
};
# 96 "include/linux/clockchips.h"
struct clock_event_device {
 void (*event_handler)(struct clock_event_device *);
 int (*set_next_event)(unsigned long evt,
        struct clock_event_device *);
 int (*set_next_ktime)(ktime_t expires,
        struct clock_event_device *);
 ktime_t next_event;
 u64 max_delta_ns;
 u64 min_delta_ns;
 u32 mult;
 u32 shift;
 enum clock_event_mode mode;
 unsigned int features;
 unsigned long retries;

 void (*broadcast)(const struct cpumask *mask);
 void (*set_mode)(enum clock_event_mode mode,
         struct clock_event_device *);
 void (*suspend)(struct clock_event_device *);
 void (*resume)(struct clock_event_device *);
 unsigned long min_delta_ticks;
 unsigned long max_delta_ticks;

 const char *name;
 int rating;
 int irq;
 int bound_on;
 const struct cpumask *cpumask;
 struct list_head list;
 struct module *owner;
} __attribute__((__aligned__((1 << 5))));
# 139 "include/linux/clockchips.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) unsigned long div_sc(unsigned long ticks, unsigned long nsec,
       int shift)
{
 uint64_t tmp = ((uint64_t)ticks) << shift;

 ({ uint32_t __base = (nsec); uint32_t __rem; (void)(((typeof((tmp)) *)0) == ((uint64_t *)0)); if (__builtin_expect(!!(((tmp) >> 32) == 0), 1)) { __rem = (uint32_t)(tmp) % __base; (tmp) = (uint32_t)(tmp) / __base; } else __rem = __div64_32(&(tmp), __base); __rem; });
 return (unsigned long) tmp;
}


extern u64 clockevent_delta2ns(unsigned long latch,
          struct clock_event_device *evt);
extern void clockevents_register_device(struct clock_event_device *dev);
extern int clockevents_unbind_device(struct clock_event_device *ced, int cpu);

extern void clockevents_config(struct clock_event_device *dev, u32 freq);
extern void clockevents_config_and_register(struct clock_event_device *dev,
         u32 freq, unsigned long min_delta,
         unsigned long max_delta);

extern int clockevents_update_freq(struct clock_event_device *ce, u32 freq);

extern void clockevents_exchange_device(struct clock_event_device *old,
     struct clock_event_device *new);
extern void clockevents_set_mode(struct clock_event_device *dev,
     enum clock_event_mode mode);
extern int clockevents_program_event(struct clock_event_device *dev,
         ktime_t expires, bool force);

extern void clockevents_handle_noop(struct clock_event_device *dev);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void
clockevents_calc_mult_shift(struct clock_event_device *ce, u32 freq, u32 minsec)
{
 return clocks_calc_mult_shift(&ce->mult, &ce->shift, 1000000000L,
          freq, minsec);
}

extern void clockevents_suspend(void);
extern void clockevents_resume(void);
# 193 "include/linux/clockchips.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int tick_check_broadcast_expired(void) { return 0; }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void tick_setup_hrtimer_broadcast(void) {};



extern int clockevents_notify(unsigned long reason, void *arg);
# 20 "./arch/mips/include/asm/time.h" 2


extern spinlock_t rtc_lock;







extern int rtc_mips_set_time(unsigned long);
extern int rtc_mips_set_mmss(unsigned long);




extern void plat_time_init(void);





extern unsigned int mips_hpt_frequency;





extern int (*perf_irq)(void);




extern unsigned int __attribute__((weak)) get_c0_compare_int(void);
extern int r4k_clockevent_init(void);
extern int gic_clockevent_init(void);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int mips_clockevent_init(void)
{



 return r4k_clockevent_init();



}




extern int init_r4k_clocksource(void);

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int init_mips_clocksource(void)
{

 return init_r4k_clocksource();



}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void clockevent_set_clock(struct clock_event_device *cd,
     unsigned int clock)
{
 clockevents_calc_mult_shift(cd, clock, 4);
}
# 24 "arch/mips/ath79/setup.c" 2
# 1 "./arch/mips/include/asm/reboot.h" 1
# 12 "./arch/mips/include/asm/reboot.h"
extern void (*_machine_restart)(char *command);
extern void (*_machine_halt)(void);
# 25 "arch/mips/ath79/setup.c" 2
# 1 "./arch/mips/include/asm/mips_machine.h" 1
# 18 "./arch/mips/include/asm/mips_machine.h"
struct mips_machine {
 unsigned long mach_type;
 const char *mach_id;
 const char *mach_name;
 void (*mach_setup)(void);
};
# 51 "./arch/mips/include/asm/mips_machine.h"
extern long __mips_machines_start;
extern long __mips_machines_end;


int mips_machtype_setup(char *id) __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function));
void mips_machine_setup(void) __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function));
# 26 "arch/mips/ath79/setup.c" 2

# 1 "./arch/mips/include/asm/mach-ath79/ath79.h" 1
# 18 "./arch/mips/include/asm/mach-ath79/ath79.h"
# 1 "include/linux/io.h" 1
# 25 "include/linux/io.h"
struct device;

__attribute__((externally_visible)) void __iowrite32_copy(void *to, const void *from, size_t count);
void __iowrite64_copy(void *to, const void *from, size_t count);


int ioremap_page_range(unsigned long addr, unsigned long end,
         phys_addr_t phys_addr, pgprot_t prot);
# 45 "include/linux/io.h"
void * devm_ioport_map(struct device *dev, unsigned long port,
          unsigned int nr);
void devm_ioport_unmap(struct device *dev, void *addr);
# 63 "include/linux/io.h"
void *devm_ioremap(struct device *dev, resource_size_t offset,
       unsigned long size);
void *devm_ioremap_nocache(struct device *dev, resource_size_t offset,
        unsigned long size);
void devm_iounmap(struct device *dev, void *addr);
int check_signature(const volatile void *io_addr,
   const unsigned char *signature, int length);
void devm_ioremap_release(struct device *dev, void *res);
# 93 "include/linux/io.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int arch_phys_wc_add(unsigned long base,
      unsigned long size)
{
 return 0;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void arch_phys_wc_del(int handle)
{
}
# 19 "./arch/mips/include/asm/mach-ath79/ath79.h" 2

enum ath79_soc_type {
 ATH79_SOC_UNKNOWN,
 ATH79_SOC_AR7130,
 ATH79_SOC_AR7141,
 ATH79_SOC_AR7161,
 ATH79_SOC_AR7240,
 ATH79_SOC_AR7241,
 ATH79_SOC_AR7242,
 ATH79_SOC_AR9130,
 ATH79_SOC_AR9132,
 ATH79_SOC_AR9330,
 ATH79_SOC_AR9331,
 ATH79_SOC_AR9341,
 ATH79_SOC_AR9342,
 ATH79_SOC_AR9344,
 ATH79_SOC_QCA9533,
 ATH79_SOC_QCA9556,
 ATH79_SOC_QCA9558,
 ATH79_SOC_TP9343,
 ATH79_SOC_QCA9561,
};

extern enum ath79_soc_type ath79_soc;
extern unsigned int ath79_soc_rev;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar71xx(void)
{
 return (ath79_soc == ATH79_SOC_AR7130 ||
  ath79_soc == ATH79_SOC_AR7141 ||
  ath79_soc == ATH79_SOC_AR7161);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar724x(void)
{
 return (ath79_soc == ATH79_SOC_AR7240 ||
  ath79_soc == ATH79_SOC_AR7241 ||
  ath79_soc == ATH79_SOC_AR7242);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar7240(void)
{
 return (ath79_soc == ATH79_SOC_AR7240);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar7241(void)
{
 return (ath79_soc == ATH79_SOC_AR7241);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar7242(void)
{
 return (ath79_soc == ATH79_SOC_AR7242);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar913x(void)
{
 return (ath79_soc == ATH79_SOC_AR9130 ||
  ath79_soc == ATH79_SOC_AR9132);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar933x(void)
{
 return (ath79_soc == ATH79_SOC_AR9330 ||
  ath79_soc == ATH79_SOC_AR9331);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar9341(void)
{
 return (ath79_soc == ATH79_SOC_AR9341);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar9342(void)
{
 return (ath79_soc == ATH79_SOC_AR9342);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar9344(void)
{
 return (ath79_soc == ATH79_SOC_AR9344);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_ar934x(void)
{
 return soc_is_ar9341() || soc_is_ar9342() || soc_is_ar9344();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca9533(void)
{
 return ath79_soc == ATH79_SOC_QCA9533;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca953x(void)
{
 return soc_is_qca9533();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca9556(void)
{
 return ath79_soc == ATH79_SOC_QCA9556;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca9558(void)
{
 return ath79_soc == ATH79_SOC_QCA9558;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca955x(void)
{
 return soc_is_qca9556() || soc_is_qca9558();
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_tp9343(void)
{
 return ath79_soc == ATH79_SOC_TP9343;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca9561(void)
{
 return ath79_soc == ATH79_SOC_QCA9561;
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) int soc_is_qca956x(void)
{
 return soc_is_tp9343() || soc_is_qca9561();
}

extern void *ath79_ddr_base;
extern void *ath79_gpio_base;
extern void *ath79_pll_base;
extern void *ath79_reset_base;

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ath79_pll_wr(unsigned reg, u32 val)
{
 __raw_writel(val, ath79_pll_base + reg);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 ath79_pll_rr(unsigned reg)
{
 return __raw_readl(ath79_pll_base + reg);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ath79_reset_wr(unsigned reg, u32 val)
{
 __raw_writel(val, ath79_reset_base + reg);
 (void) __raw_readl(ath79_reset_base + reg);
}

static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) u32 ath79_reset_rr(unsigned reg)
{
 return __raw_readl(ath79_reset_base + reg);
}

void ath79_device_reset_set(u32 mask);
void ath79_device_reset_clear(u32 mask);
u32 ath79_device_reset_get(u32 mask);

void ath79_flash_acquire(void);
void ath79_flash_release(void);
# 28 "arch/mips/ath79/setup.c" 2
# 1 "./arch/mips/include/asm/mach-ath79/ar71xx_regs.h" 1
# 29 "arch/mips/ath79/setup.c" 2
# 1 "arch/mips/ath79/common.h" 1
# 22 "arch/mips/ath79/common.h"
void ath79_clocks_init(void);
unsigned long ath79_get_sys_clk_rate(const char *id);

void ath79_ddr_wb_flush(unsigned int reg);

void ath79_gpio_function_enable(u32 mask);
void ath79_gpio_function_disable(u32 mask);
void ath79_gpio_function_setup(u32 set, u32 clear);
void ath79_gpio_output_select(unsigned gpio, u8 val);
void ath79_gpio_init(void);
# 30 "arch/mips/ath79/setup.c" 2
# 1 "arch/mips/ath79/dev-common.h" 1
# 15 "arch/mips/ath79/dev-common.h"
void ath79_register_uart(void);
void ath79_register_wdt(void);
# 31 "arch/mips/ath79/setup.c" 2
# 1 "arch/mips/ath79/machtypes.h" 1
# 17 "arch/mips/ath79/machtypes.h"
enum ath79_mach_type {
 ATH79_MACH_GENERIC = 0,
 ATH79_MACH_ALFA_AP96,
 ATH79_MACH_ALFA_NX,
 ATH79_MACH_ALL0258N,
 ATH79_MACH_ALL0305,
 ATH79_MACH_ALL0315N,
 ATH79_MACH_ANTMINER_S1,
        ATH79_MACH_ANTMINER_S3,
 ATH79_MACH_AP113,
 ATH79_MACH_AP121,
 ATH79_MACH_AP121_MINI,
 ATH79_MACH_AP132,
 ATH79_MACH_AP135_020,
 ATH79_MACH_AP136_010,
 ATH79_MACH_AP136_020,
 ATH79_MACH_AP81,
 ATH79_MACH_AP83,
 ATH79_MACH_AP96,
 ATH79_MACH_ARCHER_C5,
 ATH79_MACH_ARCHER_C7,
 ATH79_MACH_AW_NR580,
 ATH79_MACH_BHU_BXU2000N2_A1,
 ATH79_MACH_BSB,
 ATH79_MACH_CAP4200AG,
 ATH79_MACH_CARAMBOLA2,
 ATH79_MACH_CPE510,
 ATH79_MACH_DB120,
 ATH79_MACH_PB44,
 ATH79_MACH_DGL_5500_A1,
 ATH79_MACH_DHP_1565_A1,
 ATH79_MACH_DIR_505_A1,
 ATH79_MACH_DIR_600_A1,
 ATH79_MACH_DIR_615_C1,
 ATH79_MACH_DIR_615_E1,
 ATH79_MACH_DIR_615_E4,
 ATH79_MACH_DIR_825_B1,
 ATH79_MACH_DIR_825_C1,
 ATH79_MACH_DIR_835_A1,
 ATH79_MACH_DLAN_PRO_500_WP,
 ATH79_MACH_DLAN_PRO_1200_AC,
 ATH79_MACH_DRAGINO2,
 ATH79_MACH_ESR900,
 ATH79_MACH_EW_DORIN,
 ATH79_MACH_EW_DORIN_ROUTER,
 ATH79_MACH_EAP300V2,
 ATH79_MACH_EAP7660D,
 ATH79_MACH_EL_M150,
 ATH79_MACH_EL_MINI,
 ATH79_MACH_ESR1750,
 ATH79_MACH_EPG5000,
 ATH79_MACH_F9K1115V2,
 ATH79_MACH_GL_INET,
 ATH79_MACH_GS_OOLITE,
 ATH79_MACH_HIWIFI_HC6361,
 ATH79_MACH_JA76PF,
 ATH79_MACH_JA76PF2,
 ATH79_MACH_JWAP003,
 ATH79_MACH_HORNET_UB,
 ATH79_MACH_MR12,
 ATH79_MACH_MR16,
 ATH79_MACH_MR600V2,
 ATH79_MACH_MR600,
 ATH79_MACH_MR900,
 ATH79_MACH_MR900v2,
 ATH79_MACH_MYNET_N600,
 ATH79_MACH_MYNET_N750,
 ATH79_MACH_MYNET_REXT,
 ATH79_MACH_MZK_W04NU,
 ATH79_MACH_MZK_W300NH,
 ATH79_MACH_NBG460N,
 ATH79_MACH_NBG6716,
 ATH79_MACH_OM2P_HSv2,
 ATH79_MACH_OM2P_HS,
 ATH79_MACH_OM2P_LC,
 ATH79_MACH_OM2Pv2,
 ATH79_MACH_OM2P,
 ATH79_MACH_OM5P_AN,
 ATH79_MACH_OM5P,
 ATH79_MACH_ONION_OMEGA,
 ATH79_MACH_PB42,
 ATH79_MACH_PB92,
 ATH79_MACH_QIHOO_C301,
 ATH79_MACH_R6100,
 ATH79_MACH_RB_411,
 ATH79_MACH_RB_411U,
 ATH79_MACH_RB_433,
 ATH79_MACH_RB_433U,
 ATH79_MACH_RB_435G,
 ATH79_MACH_RB_450G,
 ATH79_MACH_RB_450,
 ATH79_MACH_RB_493,
 ATH79_MACH_RB_493G,
 ATH79_MACH_RB_711GR100,
 ATH79_MACH_RB_750,
 ATH79_MACH_RB_750G_R3,
 ATH79_MACH_RB_751,
 ATH79_MACH_RB_751G,
 ATH79_MACH_RB_922GS,
 ATH79_MACH_RB_951G,
 ATH79_MACH_RB_951U,
 ATH79_MACH_RB_2011G,
 ATH79_MACH_RB_2011L,
 ATH79_MACH_RB_2011US,
 ATH79_MACH_RB_2011R5,
 ATH79_MACH_RB_SXTLITE2ND,
 ATH79_MACH_RB_SXTLITE5ND,
 ATH79_MACH_RW2458N,
 ATH79_MACH_SMART_300,
 ATH79_MACH_TEW_632BRP,
 ATH79_MACH_TEW_673GRU,
 ATH79_MACH_TEW_712BR,
 ATH79_MACH_TEW_732BR,
 ATH79_MACH_MC_MAC1200R,
 ATH79_MACH_TL_MR10U,
 ATH79_MACH_TL_MR11U,
 ATH79_MACH_TL_MR13U,
 ATH79_MACH_TL_MR3020,
 ATH79_MACH_TL_MR3040,
 ATH79_MACH_TL_MR3040_V2,
 ATH79_MACH_TL_MR3220,
 ATH79_MACH_TL_MR3220_V2,
 ATH79_MACH_TL_MR3420,
 ATH79_MACH_TL_MR3420_V2,
 ATH79_MACH_TL_WA701ND_V2,
 ATH79_MACH_TL_WA750RE,
       ATH79_MACH_TL_WA7210N_V2,
 ATH79_MACH_TL_WA7510N_V1,
 ATH79_MACH_TL_WA850RE,
 ATH79_MACH_TL_WA860RE,
 ATH79_MACH_TL_WA801ND_V2,
 ATH79_MACH_TL_WA830RE_V2,
 ATH79_MACH_TL_WA901ND,
 ATH79_MACH_TL_WA901ND_V2,
 ATH79_MACH_TL_WA901ND_V3,
 ATH79_MACH_TL_WDR3500,
 ATH79_MACH_TL_WDR4300,
 ATH79_MACH_TL_WDR4900_V2,
 ATH79_MACH_TL_WR1041N_V2,
 ATH79_MACH_TL_WR1043ND,
 ATH79_MACH_TL_WR1043ND_V2,
 ATH79_MACH_TL_WR2543N,
 ATH79_MACH_TL_WR703N,
 ATH79_MACH_TL_WR710N,
 ATH79_MACH_TL_WR720N_V3,
 ATH79_MACH_TL_WR741ND,
 ATH79_MACH_TL_WR741ND_V4,
 ATH79_MACH_TL_WR841N_V1,
 ATH79_MACH_TL_WR841N_V7,
 ATH79_MACH_TL_WR841N_V8,
 ATH79_MACH_TL_WR841N_V9,
 ATH79_MACH_TL_WR842N_V2,
 ATH79_MACH_TL_WR941ND,
 ATH79_MACH_TL_WR941ND_V5,
 ATH79_MACH_TUBE2H,
 ATH79_MACH_UBNT_AIRGW,
 ATH79_MACH_UBNT_AIRROUTER,
 ATH79_MACH_UBNT_BULLET_M,
 ATH79_MACH_UBNT_LOCO_M_XW,
 ATH79_MACH_UBNT_LSSR71,
 ATH79_MACH_UBNT_LSX,
 ATH79_MACH_UBNT_NANO_M,
 ATH79_MACH_UBNT_NANO_M_XW,
 ATH79_MACH_UBNT_ROCKET_M,
 ATH79_MACH_UBNT_ROCKET_M_XW,
 ATH79_MACH_UBNT_RSPRO,
 ATH79_MACH_UBNT_RS,
 ATH79_MACH_UBNT_UAP_PRO,
 ATH79_MACH_UBNT_UNIFI,
 ATH79_MACH_UBNT_UNIFI_OUTDOOR,
 ATH79_MACH_UBNT_UNIFI_OUTDOOR_PLUS,
 ATH79_MACH_UBNT_XM,
 ATH79_MACH_WHR_G301N,
 ATH79_MACH_WHR_HP_G300N,
 ATH79_MACH_WHR_HP_GN,
 ATH79_MACH_WLAE_AG300N,
 ATH79_MACH_WLR8100,
 ATH79_MACH_WNDAP360,
 ATH79_MACH_WNDR3700,
 ATH79_MACH_WNDR3700_V4,
 ATH79_MACH_WNDR4300,
 ATH79_MACH_WNR2000,
 ATH79_MACH_WNR2000_V3,
 ATH79_MACH_WNR2000_V4,
 ATH79_MACH_WNR2200,
 ATH79_MACH_WNR612_V2,
 ATH79_MACH_WNR1000_V2,
 ATH79_MACH_WP543,
 ATH79_MACH_WPE72,
 ATH79_MACH_WPJ344,
 ATH79_MACH_WPJ531,
 ATH79_MACH_WPJ558,
 ATH79_MACH_WRT160NL,
 ATH79_MACH_WRT400N,
 ATH79_MACH_WZR_HP_AG300H,
 ATH79_MACH_WZR_HP_G300NH,
 ATH79_MACH_WZR_HP_G300NH2,
 ATH79_MACH_WZR_HP_G450H,
 ATH79_MACH_WZR_450HP2,
 ATH79_MACH_ZCN_1523H_2,
 ATH79_MACH_ZCN_1523H_5,
};
# 32 "arch/mips/ath79/setup.c" 2







static char ath79_sys_type[64];

static void ath79_restart(char *command)
{
 do { arch_local_irq_disable(); do { } while (0); } while (0);
 ath79_device_reset_set((1UL << (24)));
 for (;;)
  if (cpu_wait)
   cpu_wait();
}

static void ath79_halt(void)
{
 while (1)
  cpu_wait();
}

static void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) ath79_detect_sys_type(void)
{
 char *chip = "????";
 u32 id;
 u32 major;
 u32 minor;
 u32 rev = 0;
 u32 ver = 1;

 id = ath79_reset_rr(0x90);
 major = id & 0xfff0;

 switch (major) {
 case 0x00a0:
  minor = id & 0x3;
  rev = id >> 2;
  rev &= 0x3;
  switch (minor) {
  case 0x0:
   ath79_soc = ATH79_SOC_AR7130;
   chip = "7130";
   break;

  case 0x1:
   ath79_soc = ATH79_SOC_AR7141;
   chip = "7141";
   break;

  case 0x2:
   ath79_soc = ATH79_SOC_AR7161;
   chip = "7161";
   break;
  }
  break;

 case 0x00c0:
  ath79_soc = ATH79_SOC_AR7240;
  chip = "7240";
  rev = id & 0x3;
  break;

 case 0x0100:
  ath79_soc = ATH79_SOC_AR7241;
  chip = "7241";
  rev = id & 0x3;
  break;

 case 0x1100:
  ath79_soc = ATH79_SOC_AR7242;
  chip = "7242";
  rev = id & 0x3;
  break;

 case 0x00b0:
  minor = id & 0x3;
  rev = id >> 2;
  rev &= 0x3;
  switch (minor) {
  case 0x0:
   ath79_soc = ATH79_SOC_AR9130;
   chip = "9130";
   break;

  case 0x1:
   ath79_soc = ATH79_SOC_AR9132;
   chip = "9132";
   break;
  }
  break;

 case 0x0110:
  ath79_soc = ATH79_SOC_AR9330;
  chip = "9330";
  rev = id & 0x3;
  break;

 case 0x1110:
  ath79_soc = ATH79_SOC_AR9331;
  chip = "9331";
  rev = id & 0x3;
  break;

 case 0x0120:
  ath79_soc = ATH79_SOC_AR9341;
  chip = "9341";
  rev = id & 0xf;
  break;

 case 0x1120:
  ath79_soc = ATH79_SOC_AR9342;
  chip = "9342";
  rev = id & 0xf;
  break;

 case 0x2120:
  ath79_soc = ATH79_SOC_AR9344;
  chip = "9344";
  rev = id & 0xf;
  break;

 case 0x0160:
  ver = 2;


 case 0x0140:
  ath79_soc = ATH79_SOC_QCA9533;
  chip = "9533";
  rev = id & 0xf;
  break;

 case 0x0130:
  ath79_soc = ATH79_SOC_QCA9556;
  chip = "9556";
  rev = id & 0xf;
  break;

 case 0x1130:
  ath79_soc = ATH79_SOC_QCA9558;
  chip = "9558";
  rev = id & 0xf;
  break;

 case 0x0150:
  ath79_soc = ATH79_SOC_TP9343;
  chip = "9343";
  rev = id & 0xf;
  break;

 case 0x1150:
  ath79_soc = ATH79_SOC_QCA9561;
  chip = "9561";
  rev = id & 0xf;
  break;

 default:
  panic("ath79: unknown SoC, id:0x%08x", id);
 }

 ath79_soc_rev = rev;

 if (soc_is_qca953x() || soc_is_qca955x() || soc_is_qca9561())
  sprintf(ath79_sys_type, "Qualcomm Atheros QCA%s ver %u rev %u",
   chip, ver, rev);
 else if (soc_is_tp9343())
  sprintf(ath79_sys_type, "Qualcomm Atheros TP%s rev %u",
   chip, rev);
 else
  sprintf(ath79_sys_type, "Atheros AR%s rev %u", chip, rev);
 printk("\001" "6" "SoC: %s\n", ath79_sys_type);
}

const char *get_system_type(void)
{
 return ath79_sys_type;
}

unsigned int get_c0_compare_int(void)
{
 return 7;
}

void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) plat_mem_setup(void)
{
 set_io_port_base(0xa0000000);

 ath79_reset_base = __ioremap_mode(((0x18000000 + 0x00060000)), (0x100), (2<<(((((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1) + 1) + 1) + 1)))
                          ;
 ath79_pll_base = __ioremap_mode(((0x18000000 + 0x00050000)), (0x100), (2<<(((((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1) + 1) + 1) + 1)))
                      ;
 ath79_ddr_base = __ioremap_mode(((0x18000000 + 0x00000000)), (0x100), (2<<(((((0 ? (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1)))) + 1 : (0 ? ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))) + 1 : ((((((0 ? (0) : (0) + 1) + 1) + 1) + 1))))) + 1) + 1) + 1) + 1)))
                           ;

 ath79_detect_sys_type();
 detect_memory_region(0, (2 * 1024 * 1024), (128 * 1024 * 1024));

 _machine_restart = ath79_restart;
 _machine_halt = ath79_halt;
 pm_power_off = ath79_halt;
}

void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) plat_time_init(void)
{
 unsigned long cpu_clk_rate;
 unsigned long ahb_clk_rate;
 unsigned long ddr_clk_rate;
 unsigned long ref_clk_rate;

 ath79_clocks_init();

 cpu_clk_rate = ath79_get_sys_clk_rate("cpu");
 ahb_clk_rate = ath79_get_sys_clk_rate("ahb");
 ddr_clk_rate = ath79_get_sys_clk_rate("ddr");
 ref_clk_rate = ath79_get_sys_clk_rate("ref");

 printk("\001" "6" "Clocks: CPU:%lu.%03luMHz, DDR:%lu.%03luMHz, AHB:%lu.%03luMHz, Ref:%lu.%03luMHz", cpu_clk_rate / 1000000, (cpu_clk_rate / 1000) % 1000, ddr_clk_rate / 1000000, (ddr_clk_rate / 1000) % 1000, ahb_clk_rate / 1000000, (ahb_clk_rate / 1000) % 1000, ref_clk_rate / 1000000, (ref_clk_rate / 1000) % 1000)



                                                       ;

 mips_hpt_frequency = cpu_clk_rate / 2;
}

static const char __setup_str_mips_machtype_setup[] __attribute__ ((__section__(".init.rodata"))) __attribute__((aligned(1))) = "board="; static struct obs_kernel_param __setup_mips_machtype_setup __attribute__((__used__)) __attribute__ ((__section__(".init.setup"))) __attribute__((aligned((sizeof(long))))) = { __setup_str_mips_machtype_setup, mips_machtype_setup, 0 };

static int __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) ath79_setup(void)
{
 ath79_gpio_init();
 ath79_register_uart();
 ath79_register_wdt();

 mips_machine_setup();

 return 0;
}

static initcall_t __initcall_ath79_setup3 __attribute__((__used__)) __attribute__((__section__(".initcall" "3" ".init"))) = ath79_setup; ;

static void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) ath79_generic_init(void)
{

}

static const char machine_name_ATH79_MACH_GENERIC[] __attribute__ ((__section__(".init.rodata"))) __attribute__((aligned(1))) = "Generic AR71XX/AR724X/AR913X based board"; static const char machine_id_ATH79_MACH_GENERIC[] __attribute__ ((__section__(".init.rodata"))) __attribute__((aligned(1))) = "Generic"; static struct mips_machine machine_ATH79_MACH_GENERIC __attribute__((__used__)) __attribute__ ((__section__(".mips.machines.init"))) = { .mach_type = ATH79_MACH_GENERIC, .mach_id = machine_id_ATH79_MACH_GENERIC, .mach_name = machine_name_ATH79_MACH_GENERIC, .mach_setup = ath79_generic_init, };


                         ;
