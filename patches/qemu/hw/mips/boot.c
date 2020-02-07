#include "qemu/osdep.h"
#include "qapi/error.h"
#include "qemu/error-report.h"
#include "qemu/units.h"
#include "qemu-common.h"
#include "hw/mips/mips.h"
#include "hw/mips/cpudevs.h"
#include "target/mips/cpu-qom.h"
#include "target/mips/cpu.h"
#include "hw/loader.h"
#include "elf.h"

#define ENVP_ADDR           0x80000100 // 2(256)
#define ENVP_NB_ENTRIES     2
#define ENVP_ENTRY_SIZE     252
#define BOOT_LOADER_ADDR    0x80000000 // 48 bytes

static void do_cpu_reset(void *opaque)
{
    CommonResetData *reset_data = (CommonResetData *)opaque;
    MIPSCPU *cpu = reset_data->cpu;

    cpu_reset(CPU(cpu));
    cpu->env.active_tc.PC = reset_data->vector;
}

static void GCC_FMT_ATTR(3, 4) prom_set(uint32_t* prom_buf, int index,
                                        const char *string, ...)
{
    va_list ap;
    int32_t table_addr;
    
    if (index >= ENVP_NB_ENTRIES)
        return;

    if (string == NULL) {
        prom_buf[index] = 0;
        return;
    }

    table_addr = sizeof(int32_t) * ENVP_NB_ENTRIES + index * ENVP_ENTRY_SIZE;
    prom_buf[index] = tswap32(ENVP_ADDR + table_addr);

    va_start(ap, string);
    vsnprintf((char *)prom_buf + table_addr, ENVP_ENTRY_SIZE, string, ap);
    va_end(ap);
}

/* ROM and pseudo bootloader
 *
 * The following code implements a very very simple bootloader. It first
 * loads the registers a0 to a3 to the values expected by the OS, and
 * then jump at the kernel address.
 *
 * The bootloader should pass the locations of the kernel arguments and
 * environment variables tables. Those tables contain the 32-bit address
 * of NULL terminated strings. The environment variables table should be
 * terminated by a NULL address.
 *
 * For a simpler implementation, the number of kernel arguments is fixed
 * to two (the name of the kernel and the command line), and the two
 * tables are actually the same one.
 *
 * The registers a0 to a3 should contain the following values:
 *     a0 - number of kernel arguments
 *     a1 - 32-bit address of the kernel arguments table
 *     a2 - 32-bit address of the environment variables table
 *     a3 - RAM size in bytes
 *
 */

static int64_t mips_setup_direct_kernel_boot(MIPSCPU *cpu, struct mips_boot_info *info)
{
    int64_t kernel_entry, kernel_high, initrd_size;
    long kernel_size, prom_size;
    ram_addr_t initrd_offset;
    uint32_t *prom_buf, *boot_loader_buf;
    int big_endian, prom_index = 0;

#ifdef TARGET_WORDS_BIGENDIAN
    big_endian = 1;
#else
    big_endian = 0;
#endif

    /* kernel is loaded from 0 max to 0x0FFFFFFF(256M)
     * device tree is in the kernel image
     * initrd is loaded after the kernel max to 0x0FFFFFFF(256M)
     *
     * ram and flash are allocated in machine_init not here
     */
    
    /* load kernel */
    kernel_size = load_elf(info->kernel_filename, NULL, 
                           cpu_mips_kseg0_to_phys, NULL,
                           (uint64_t *)&kernel_entry, NULL,
                           (uint64_t *)&kernel_high, big_endian, EM_MIPS, 1, 0);

    if (kernel_size >= 0) {
        if ((kernel_entry & ~0x7fffffffULL) == 0x80000000)
            kernel_entry = (int32_t)kernel_entry;
    } else {
        hwaddr ep, loadaddr;
        int is_linux;

        kernel_size = load_uimage(info->kernel_filename, &ep,
                                  &loadaddr, &is_linux,
                                  cpu_mips_kseg0_to_phys, NULL);
        kernel_high = loadaddr + kernel_size;

        if (kernel_size >=0) {
            kernel_entry = (uint32_t)ep;
        } else {
            error_report("could not load kernel '%s'", info->kernel_filename);
            exit(1);
        }
    }

    /* load initrd */
    initrd_size = 0;
    initrd_offset = 0;
    if (info->initrd_filename) {
        initrd_size = get_image_size(info->initrd_filename);
        if (initrd_size > 0) {
            initrd_offset = (kernel_high + ~INITRD_PAGE_MASK) & INITRD_PAGE_MASK;
            if (initrd_offset + initrd_size > ram_size) {
                error_report("memory too small for initial ram disk '%s'",
                             info->initrd_filename);
                exit(1);
            }
            initrd_size = load_image_targphys(info->initrd_filename,
                                              initrd_offset,
                                              ram_size - initrd_offset);
        }
        if (initrd_size == (target_ulong) -1) {
            error_report("could not load initial ram disk '%s'",
                         info->initrd_filename);
            exit(1);
        }
    }

    /* store cmdline  */
    prom_size = ENVP_NB_ENTRIES * (sizeof(int32_t) + ENVP_ENTRY_SIZE);
    prom_buf = g_malloc(prom_size);

    prom_set(prom_buf, prom_index++, "%s", info->kernel_filename);
    if (initrd_size > 0) {
        prom_set(prom_buf, prom_index++, "rd_start=0x%" PRIx64 " rd_size=%" PRId64 " %s",
                 cpu_mips_phys_to_kseg0(NULL, initrd_offset), initrd_size,
                 info->kernel_cmdline);
    } else {
        prom_set(prom_buf, prom_index++, "%s", info->kernel_cmdline);
    }

    rom_add_blob_fixed("prom", prom_buf, prom_size, cpu_mips_kseg0_to_phys(NULL, ENVP_ADDR));
    g_free(prom_buf);

    /* small bootloader */
    boot_loader_buf = g_malloc(0x30);
    boot_loader_buf[0x0] = tswap32(0x3c040000);                                      /* lui a0, 0 */
    boot_loader_buf[0x1] = tswap32(0x34840002);                                      /* ori a0, a0, 2 */
    boot_loader_buf[0x2] = tswap32(0x3c050000 | ((ENVP_ADDR >> 16) & 0xffff));       /* lui a1, high(ENVP_ADDR) */
    boot_loader_buf[0x3] = tswap32(0x34a50000 | (ENVP_ADDR & 0xffff));               /* ori a1, a0, low(ENVP_ADDR) */
    boot_loader_buf[0x4] = tswap32(0x3c060000 | ((ENVP_ADDR >> 16) & 0xffff));       /* lui a2, high(ENVP_ADDR) */
    boot_loader_buf[0x5] = tswap32(0x34c60000 | (ENVP_ADDR & 0xffff));               /* ori a2, a2, low(ENVP_ADDR) */
    boot_loader_buf[0x6] = tswap32(0x3c070000 | (info->ram_size >> 16));             /* lui a3, high(env->ram_size) */
    boot_loader_buf[0x7] = tswap32(0x34e70000 | (info->ram_size & 0xffff));          /* ori a3, a3, low(env->ram_size) */
    boot_loader_buf[0x8] = tswap32(0x3c1f0000 | ((kernel_entry >> 16) & 0xffff));    /* lui ra, high(kernel_addr) */;
    boot_loader_buf[0x9] = tswap32(0x37ff0000 | (kernel_entry & 0xffff));            /* ori ra, ra, low(kernel_addr) */
    boot_loader_buf[0xa] = tswap32(0x03e00008);                                      /* jr ra */
    boot_loader_buf[0xb] = tswap32(0x00000000);                                      /* nop */

    rom_add_blob_fixed("bootloader", boot_loader_buf, 0x30, cpu_mips_kseg0_to_phys(NULL, BOOT_LOADER_ADDR));
    g_free(boot_loader_buf);

    return (int64_t)BOOT_LOADER_ADDR;
}

void mips_load_kernel(MIPSCPU *cpu, struct mips_boot_info *info)
{
    CommonResetData *reset_data;
    int64_t entry;

    if (!info->kernel_filename) {
        error_report("could not boot without kernel");
        exit(1);
    }
    entry = mips_setup_direct_kernel_boot(cpu, info);

    reset_data = g_malloc0(sizeof(CommonResetData));
    reset_data->cpu = cpu;
    reset_data->vector = entry;

    qemu_register_reset(do_cpu_reset, reset_data);
}

