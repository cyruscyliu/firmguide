# 1 "arch/mips/ath79/irq.c"
# 1 "/root/openwrt-build-docker/share/15.05-cc3a47a374475253f93a08eea6eaadce/chaos_calmer-15.05/build_dir/target-mips_34kc_uClibc-0.9.33.2/linux-ar71xx_generic/linux-3.18.20//"
# 1 "<command-line>"
# 1 "././include/linux/kconfig.h" 1



# 1 "include/generated/autoconf.h" 1
# 5 "././include/linux/kconfig.h" 2
# 1 "<command-line>" 2
# 1 "arch/mips/ath79/irq.c"
# 15 "arch/mips/ath79/irq.c"
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
# 16 "arch/mips/ath79/irq.c" 2

# 1 "include/linux/interrupt.h" 1







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
# 9 "include/linux/interrupt.h" 2

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



# 1 "include/linux/preempt_mask.h" 1
# 5 "include/linux/hardirq.h" 2
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
# 6 "include/linux/hardirq.h" 2
# 1 "include/linux/ftrace_irq.h" 1
# 9 "include/linux/ftrace_irq.h"
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ftrace_nmi_enter(void) { }
static inline __attribute__((always_inline)) __attribute__((no_instrument_function)) void ftrace_nmi_exit(void) { }
# 7 "include/linux/hardirq.h" 2
# 1 "include/linux/vtime.h" 1



# 1 "include/linux/context_tracking_state.h" 1



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

# 1 "include/linux/smp.h" 1
# 14 "include/linux/smp.h"
# 1 "include/linux/llist.h" 1
# 59 "include/linux/llist.h"
# 1 "./arch/mips/include/asm/cmpxchg.h" 1
# 12 "./arch/mips/include/asm/cmpxchg.h"
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
# 13 "./arch/mips/include/asm/cmpxchg.h" 2


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
# 60 "include/linux/llist.h" 2

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
# 7 "include/linux/percpu.h" 2

# 1 "include/linux/pfn.h" 1
# 9 "include/linux/percpu.h" 2


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
# 5 "include/linux/context_tracking_state.h" 2
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

# 1 "include/linux/atomic.h" 1



# 1 "./arch/mips/include/asm/atomic.h" 1
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
# 85 "include/linux/jump_label.h" 2

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
# 15 "include/linux/irq.h"
# 1 "include/linux/spinlock.h" 1
# 57 "include/linux/spinlock.h"
# 1 "include/linux/bottom_half.h" 1
# 10 "include/linux/bottom_half.h"
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
# 417 "include/linux/spinlock.h"
extern int _atomic_dec_and_lock(atomic_t *atomic, spinlock_t *lock);
# 16 "include/linux/irq.h" 2

# 1 "include/linux/gfp.h" 1




# 1 "include/linux/mmzone.h" 1
# 9 "include/linux/mmzone.h"
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
# 75 "./arch/mips/include/asm/page.h"
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
# 15 "./arch/mips/include/asm/cpu-type.h"
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
# 6 "include/linux/gfp.h" 2


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

# 1 "include/linux/hrtimer.h" 1
# 18 "include/linux/hrtimer.h"
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
# 19 "include/linux/hrtimer.h" 2






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
# 15 "include/linux/interrupt.h" 2
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
# 18 "arch/mips/ath79/irq.c" 2


# 1 "./arch/mips/include/asm/irq_cpu.h" 1
# 16 "./arch/mips/include/asm/irq_cpu.h"
extern void mips_cpu_irq_init(void);
extern void rm7k_cpu_irq_init(void);
extern void rm9k_cpu_irq_init(void);


struct device_node;
extern int mips_cpu_intc_init(struct device_node *of_node,
         struct device_node *parent);
# 21 "arch/mips/ath79/irq.c" 2


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
# 24 "arch/mips/ath79/irq.c" 2
# 1 "./arch/mips/include/asm/mach-ath79/ar71xx_regs.h" 1
# 25 "arch/mips/ath79/irq.c" 2
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
# 26 "arch/mips/ath79/irq.c" 2

static void (*ath79_ip2_handler)(void);
static void (*ath79_ip3_handler)(void);
static struct irq_chip ip2_chip;
static struct irq_chip ip3_chip;

static void ath79_misc_irq_handler(unsigned int irq, struct irq_desc *desc)
{
 void *base = ath79_reset_base;
 u32 pending;

 pending = __raw_readl(base + 0x10) &
    __raw_readl(base + 0x14);

 if (!pending) {
  spurious_interrupt();
  return;
 }

 while (pending) {
  int bit = __ffs(pending);

  generic_handle_irq((8 + (bit)));
  pending &= ~(1UL << (bit));
 }
}

static void ar71xx_misc_irq_unmask(struct irq_data *d)
{
 unsigned int irq = d->irq - 8;
 void *base = ath79_reset_base;
 u32 t;

 t = __raw_readl(base + 0x14);
 __raw_writel(t | (1 << irq), base + 0x14);


 __raw_readl(base + 0x14);
}

static void ar71xx_misc_irq_mask(struct irq_data *d)
{
 unsigned int irq = d->irq - 8;
 void *base = ath79_reset_base;
 u32 t;

 t = __raw_readl(base + 0x14);
 __raw_writel(t & ~(1 << irq), base + 0x14);


 __raw_readl(base + 0x14);
}

static void ar724x_misc_irq_ack(struct irq_data *d)
{
 unsigned int irq = d->irq - 8;
 void *base = ath79_reset_base;
 u32 t;

 t = __raw_readl(base + 0x10);
 __raw_writel(t & ~(1 << irq), base + 0x10);


 __raw_readl(base + 0x10);
}

static struct irq_chip ath79_misc_irq_chip = {
 .name = "MISC",
 .irq_unmask = ar71xx_misc_irq_unmask,
 .irq_mask = ar71xx_misc_irq_mask,
};

static void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) ath79_misc_irq_init(void)
{
 void *base = ath79_reset_base;
 int i;

 __raw_writel(0, base + 0x14);
 __raw_writel(0, base + 0x10);

 if (soc_is_ar71xx() || soc_is_ar913x())
  ath79_misc_irq_chip.irq_mask_ack = ar71xx_misc_irq_mask;
 else if (soc_is_ar724x() ||
   soc_is_ar933x() ||
   soc_is_ar934x() ||
   soc_is_qca953x() ||
   soc_is_qca955x() ||
   soc_is_qca956x())
  ath79_misc_irq_chip.irq_ack = ar724x_misc_irq_ack;
 else
  BUG();

 for (i = 8;
      i < 8 + 32; i++) {
  irq_set_chip_and_handler(i, &ath79_misc_irq_chip,
      handle_level_irq);
 }

 irq_set_chained_handler((0 + (6)), ath79_misc_irq_handler);
}

static void ar934x_ip2_irq_dispatch(unsigned int irq, struct irq_desc *desc)
{
 u32 status;

 disable_irq_nosync(irq);

 status = ath79_reset_rr(0xac);

 if (status & ((1UL << (4)) | (1UL << (5)) | (1UL << (6)) | (1UL << (7)) | (1UL << (8)))) {
  ath79_ddr_wb_flush(0xa8);
  generic_handle_irq((((8 + 32) + 6) + (0)));
 } else if (status & ((1UL << (0)) | (1UL << (1)) | (1UL << (2)) | (1UL << (3)))) {
  ath79_ddr_wb_flush(0xac);
  generic_handle_irq((((8 + 32) + 6) + (1)));
 } else {
  spurious_interrupt();
 }

 enable_irq(irq);
}

static void ar934x_ip2_irq_init(void)
{
 int i;

 for (i = ((8 + 32) + 6);
      i < ((8 + 32) + 6) + 2; i++)
  irq_set_chip_and_handler(i, &ip2_chip, handle_level_irq);

 irq_set_chained_handler((0 + (2)), ar934x_ip2_irq_dispatch);
}

static void qca955x_ip2_irq_dispatch(unsigned int irq, struct irq_desc *desc)
{
 u32 status;

 disable_irq_nosync(irq);

 status = ath79_reset_rr(0xac);
 status &= ((1UL << (4)) | (1UL << (5)) | (1UL << (6)) | (1UL << (7)) | (1UL << (8))) | ((1UL << (0)) | (1UL << (1)) | (1UL << (2)) | (1UL << (3)));

 if (status == 0) {
  spurious_interrupt();
  goto enable;
 }

 if (status & ((1UL << (4)) | (1UL << (5)) | (1UL << (6)) | (1UL << (7)) | (1UL << (8)))) {

  generic_handle_irq((((8 + 32) + 6) + (0)));
 }

 if (status & ((1UL << (0)) | (1UL << (1)) | (1UL << (2)) | (1UL << (3)))) {

  generic_handle_irq((((8 + 32) + 6) + (1)));
 }

enable:
 enable_irq(irq);
}

static void qca955x_ip3_irq_dispatch(unsigned int irq, struct irq_desc *desc)
{
 u32 status;

 disable_irq_nosync(irq);

 status = ath79_reset_rr(0xac);
 status &= ((1UL << (12)) | (1UL << (13)) | (1UL << (14)) | (1UL << (15)) | (1UL << (16))) |
    (1UL << (24)) |
    (1UL << (28));

 if (status == 0) {
  spurious_interrupt();
  goto enable;
 }

 if (status & (1UL << (24))) {

  generic_handle_irq(((((8 + 32) + 6) + 2) + (0)));
 }

 if (status & (1UL << (28))) {

  generic_handle_irq(((((8 + 32) + 6) + 2) + (1)));
 }

 if (status & ((1UL << (12)) | (1UL << (13)) | (1UL << (14)) | (1UL << (15)) | (1UL << (16)))) {

  generic_handle_irq(((((8 + 32) + 6) + 2) + (2)));
 }

enable:
 enable_irq(irq);
}

static void qca955x_irq_init(void)
{
 int i;

 for (i = ((8 + 32) + 6);
      i < ((8 + 32) + 6) + 2; i++)
  irq_set_chip_and_handler(i, &ip2_chip, handle_level_irq);

 irq_set_chained_handler((0 + (2)), qca955x_ip2_irq_dispatch);

 for (i = (((8 + 32) + 6) + 2);
      i < (((8 + 32) + 6) + 2) + 3; i++)
  irq_set_chip_and_handler(i, &ip3_chip, handle_level_irq);

 irq_set_chained_handler((0 + (3)), qca955x_ip3_irq_dispatch);
}

static void qca956x_ip2_irq_dispatch(unsigned int irq, struct irq_desc *desc)
{
 u32 status;

 disable_irq_nosync(irq);

 status = ath79_reset_rr(0xac);
 status &= ((1UL << (4)) | (1UL << (5)) | (1UL << (6)) | (1UL << (7)) | (1UL << (8))) | ((1UL << (0)) | (1UL << (1)) | (1UL << (2)) | (1UL << (3)));

 if (status == 0) {
  spurious_interrupt();
  goto enable;
 }

 if (status & ((1UL << (4)) | (1UL << (5)) | (1UL << (6)) | (1UL << (7)) | (1UL << (8)))) {

  generic_handle_irq((((8 + 32) + 6) + (0)));
 }

 if (status & ((1UL << (0)) | (1UL << (1)) | (1UL << (2)) | (1UL << (3)))) {

  generic_handle_irq((((8 + 32) + 6) + (1)));
 }

enable:
 enable_irq(irq);
}

static void qca956x_ip3_irq_dispatch(unsigned int irq, struct irq_desc *desc)
{
 u32 status;

 disable_irq_nosync(irq);

 status = ath79_reset_rr(0xac);
 status &= ((1UL << (12)) | (1UL << (13)) | (1UL << (14)) | (1UL << (15)) | (1UL << (16))) |
    (1UL << (24)) | (1UL << (28));

 if (status == 0) {
  spurious_interrupt();
  goto enable;
 }

 if (status & (1UL << (24))) {

  generic_handle_irq(((((8 + 32) + 6) + 2) + (0)));
 }

 if (status & (1UL << (28))) {

  generic_handle_irq(((((8 + 32) + 6) + 2) + (1)));
 }

 if (status & ((1UL << (12)) | (1UL << (13)) | (1UL << (14)) | (1UL << (15)) | (1UL << (16)))) {

  generic_handle_irq(((((8 + 32) + 6) + 2) + (2)));
 }

enable:
 enable_irq(irq);
}

static void qca956x_enable_timer_cb(void) {
 u32 misc;

 misc = ath79_reset_rr(0x14);
 misc |= (1UL << (28));
 ath79_reset_wr(0x14, misc);
}

static void qca956x_irq_init(void)
{
 int i;

 for (i = ((8 + 32) + 6);
      i < ((8 + 32) + 6) + 2; i++)
  irq_set_chip_and_handler(i, &ip2_chip, handle_level_irq);

 irq_set_chained_handler((0 + (2)), qca956x_ip2_irq_dispatch);

 for (i = (((8 + 32) + 6) + 2);
      i < (((8 + 32) + 6) + 2) + 3; i++)
  irq_set_chip_and_handler(i, &ip3_chip, handle_level_irq);

 irq_set_chained_handler((0 + (3)), qca956x_ip3_irq_dispatch);



 late_time_init = &qca956x_enable_timer_cb;
}

 void plat_irq_dispatch(void)
{
 unsigned long pending;

 pending = ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$12" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$12" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }) & ({ int __res; if (0 == 0) __asm__ __volatile__( "mfc0\t%0, " "$13" "\n\t" : "=r" (__res)); else __asm__ __volatile__( ".set\tmips32\n\t" "mfc0\t%0, " "$13" ", " "0" "\n\t" ".set\tmips0\n\t" : "=r" (__res)); __res; }) & 0x0000ff00;

 if (pending & ((unsigned long)(1) << 15))
  do_IRQ((0 + (7)));

 else if (pending & ((unsigned long)(1) << 10))
  ath79_ip2_handler();

 else if (pending & ((unsigned long)(1) << 12))
  do_IRQ((0 + (4)));

 else if (pending & ((unsigned long)(1) << 13))
  do_IRQ((0 + (5)));

 else if (pending & ((unsigned long)(1) << 11))
  ath79_ip3_handler();

 else if (pending & ((unsigned long)(1) << 14))
  do_IRQ((0 + (6)));

 else
  spurious_interrupt();
}
# 366 "arch/mips/ath79/irq.c"
static void ath79_default_ip2_handler(void)
{
 do_IRQ((0 + (2)));
}

static void ath79_default_ip3_handler(void)
{
 do_IRQ((0 + (3)));
}

static void ar71xx_ip2_handler(void)
{
 ath79_ddr_wb_flush(0xa8);
 do_IRQ((0 + (2)));
}

static void ar724x_ip2_handler(void)
{
 ath79_ddr_wb_flush(0x88);
 do_IRQ((0 + (2)));
}

static void ar913x_ip2_handler(void)
{
 ath79_ddr_wb_flush(0x88);
 do_IRQ((0 + (2)));
}

static void ar933x_ip2_handler(void)
{
 ath79_ddr_wb_flush(0x88);
 do_IRQ((0 + (2)));
}

static void ar71xx_ip3_handler(void)
{
 ath79_ddr_wb_flush(0xa4);
 do_IRQ((0 + (3)));
}

static void ar724x_ip3_handler(void)
{
 ath79_ddr_wb_flush(0x84);
 do_IRQ((0 + (3)));
}

static void ar913x_ip3_handler(void)
{
 ath79_ddr_wb_flush(0x84);
 do_IRQ((0 + (3)));
}

static void ar933x_ip3_handler(void)
{
 ath79_ddr_wb_flush(0x84);
 do_IRQ((0 + (3)));
}

static void ar934x_ip3_handler(void)
{
 ath79_ddr_wb_flush(0xa4);
 do_IRQ((0 + (3)));
}

static void ath79_ip2_disable(struct irq_data *data)
{
 disable_irq((0 + (2)));
}

static void ath79_ip2_enable(struct irq_data *data)
{
 enable_irq((0 + (2)));
}

static void ath79_ip3_disable(struct irq_data *data)
{
 disable_irq((0 + (3)));
}

static void ath79_ip3_enable(struct irq_data *data)
{
 enable_irq((0 + (3)));
}

void __attribute__ ((__section__(".init.text"))) __attribute__((__cold__)) __attribute__((no_instrument_function)) arch_init_irq(void)
{
 ip2_chip = dummy_irq_chip;
 ip3_chip = dummy_irq_chip;
 ip2_chip.irq_disable = ath79_ip2_disable;
 ip2_chip.irq_enable = ath79_ip2_enable;
 ip3_chip.irq_disable = ath79_ip3_disable;
 ip3_chip.irq_enable = ath79_ip3_enable;

 if (soc_is_ar71xx()) {
  ath79_ip2_handler = ar71xx_ip2_handler;
  ath79_ip3_handler = ar71xx_ip3_handler;
 } else if (soc_is_ar724x()) {
  ath79_ip2_handler = ar724x_ip2_handler;
  ath79_ip3_handler = ar724x_ip3_handler;
 } else if (soc_is_ar913x()) {
  ath79_ip2_handler = ar913x_ip2_handler;
  ath79_ip3_handler = ar913x_ip3_handler;
 } else if (soc_is_ar933x()) {
  ath79_ip2_handler = ar933x_ip2_handler;
  ath79_ip3_handler = ar933x_ip3_handler;
 } else if (soc_is_ar934x()) {
  ath79_ip2_handler = ath79_default_ip2_handler;
  ath79_ip3_handler = ar934x_ip3_handler;
 } else if (soc_is_qca953x()) {
  ath79_ip2_handler = ath79_default_ip2_handler;
  ath79_ip3_handler = ath79_default_ip3_handler;
 } else if (soc_is_qca955x()) {
  ath79_ip2_handler = ath79_default_ip2_handler;
  ath79_ip3_handler = ath79_default_ip3_handler;
 } else if (soc_is_qca956x()) {
  ath79_ip2_handler = ath79_default_ip2_handler;
  ath79_ip3_handler = ath79_default_ip3_handler;
 } else {
  BUG();
 }

 cp0_perfcount_irq = (8 + (5));
 mips_cpu_irq_init();
 ath79_misc_irq_init();

 if (soc_is_ar934x())
  ar934x_ip2_irq_init();
 else if (soc_is_qca955x())
  qca955x_irq_init();
 else if (soc_is_qca956x())
  qca956x_irq_init();
}
