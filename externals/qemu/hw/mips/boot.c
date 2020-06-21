#include "qemu/osdep.h"
#include "qapi/error.h"
#include "qemu/error-report.h"
#include "qemu/units.h"
#include "qemu-common.h"
#include "hw/mips/mips.h"
#include <libfdt.h>
#include "hw/mips/cpudevs.h"
#include "target/mips/cpu-qom.h"
#include "sysemu/device_tree.h"
#include "sysemu/sysemu.h"
#include "target/mips/cpu.h"
#include "qemu/option.h"
#include "hw/loader.h"
#include "elf.h"

#define ENVP_ADDR           0xBFC00000 // 2(256)
#define ENVP_NB_ENTRIES     16
#define ENVP_ENTRY_SIZE     252
#define BOOT_LOADER_ADDR    0xBFD00000 // 48 bytes

static void do_cpu_reset(void *opaque)
{
    CommonResetData *reset_data = (CommonResetData *)opaque;
    MIPSCPU *cpu = reset_data->cpu;

    cpu_reset(CPU(cpu));
    cpu->env.active_tc.PC = reset_data->vector;
}

static inline bool have_dtb(const struct mips_boot_info *info)
{
    return info->dtb_filename;
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
    hwaddr ep, loadaddr;
    uint64_t kernel_entry, kernel_low, kernel_high, image_high;
    long kernel_size, prom_size;
    uint32_t *prom_buf, *boot_loader_buf;
    int big_endian, prom_index = 0;
    int argc = 0;

#ifdef TARGET_WORDS_BIGENDIAN
    big_endian = 1;
#else
    big_endian = 0;
#endif

    /* kernel is loaded from 0 max to 0x0FFFFFFF(256M)
     * initrd is loaded after the kernel max to 0x0FFFFFFF(256M)
     *
     * ram and flash are allocated in machine_init not here
     */

    /* load kernel */
    kernel_size = load_elf(info->kernel_filename, NULL, cpu_mips_kseg0_to_phys, NULL,
                           &kernel_entry, &kernel_low, &kernel_high, big_endian, EM_MIPS, 1, 0);
    if (kernel_size < 0) {
        int is_linux;
        kernel_size = load_uimage(info->kernel_filename, &ep, &loadaddr, &is_linux,
                                  cpu_mips_kseg0_to_phys, NULL);
        kernel_entry = (uint64_t)ep;
        kernel_low = cpu_mips_kseg0_to_phys(NULL, loadaddr);
        kernel_high = cpu_mips_kseg0_to_phys(NULL, loadaddr) + (uint64_t)kernel_size;
        if (kernel_size < 0) {
            error_report("could not load kernel '%s'", info->kernel_filename);
            exit(1);
        }
    }
    /* we just leverage INITRD_PAGE_MASK, just for convenience */
    image_high = (kernel_high + ~INITRD_PAGE_MASK) & INITRD_PAGE_MASK;

    /* load initrd */
    if (info->initrd_filename) {
        info->initrd_size = get_image_size(info->initrd_filename);
        if (info->initrd_size > 0) {
            // suppose the kernel size (including bss )is less than 0x01000000(16M)
            info->initrd_start = (kernel_high + ~INITRD_PAGE_MASK) & INITRD_PAGE_MASK;
            if (info->initrd_start + info->initrd_size > info->ram_size) {
                error_report("memory too small for initial ram disk '%s'",
                             info->initrd_filename);
                exit(1);
            }
            info->initrd_size = load_image_targphys(info->initrd_filename, info->initrd_start,
                                              info->ram_size - info->initrd_start);
            image_high = (info->initrd_start + info->initrd_size + ~INITRD_PAGE_MASK) & INITRD_PAGE_MASK;
        } else {
            error_report("could not load initial ram disk '%s'",
                         info->initrd_filename);
            exit(1);
        }
    }

    /* update fdt */
    if (info->dtb_filename) {
        /* generally, the device tree blob is after the kernel image or the initrd */
        info->dtb_start = image_high;
        info->dtb_limit = info->ram_size;
        if (info->dtb_offset) {
            info->dtb_start = kernel_low + info->dtb_offset;
        }
    }

    /* store cmdline  */
    prom_size = ENVP_NB_ENTRIES * (sizeof(int32_t) + ENVP_ENTRY_SIZE);
    prom_buf = g_malloc(prom_size);

    if (info->initrd_size > 0) {
        prom_set(prom_buf, prom_index++, "rd_start=0x%" PRIx64 " rd_size=%" PRId64 " %s",
                 cpu_mips_phys_to_kseg0(NULL, info->initrd_start), info->initrd_size,
                 info->kernel_cmdline);
        prom_set(prom_buf, prom_index++, "initrd_start=0x%" PRIx32, (unsigned int)cpu_mips_phys_to_kseg0(NULL, info->initrd_start));
        prom_set(prom_buf, prom_index++, "initrd_size=%" PRId32, (int)info->initrd_size);
        argc += 3;
    } else {
        prom_set(prom_buf, prom_index++, "%s", info->kernel_cmdline);
        argc += 1;
    }
    prom_set(prom_buf, prom_index, NULL);

    rom_add_blob_fixed("prom", prom_buf, prom_size, cpu_mips_kseg0_to_phys(NULL, ENVP_ADDR));
    g_free(prom_buf);

    /* small bootloader */
    boot_loader_buf = g_malloc(0x30);
    boot_loader_buf[0x0] = tswap32(0x3c040000);                                      /* lui a0, 0 */
    boot_loader_buf[0x1] = tswap32(0x34840000 | argc);                               /* ori a0, a0, ARGC */
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

QemuOptsList enhance_dtb_opts = {
    .name = "dtb",
    .implied_opt_name = "path",
    .merge_lists = true,
    .head = QTAILQ_HEAD_INITIALIZER(enhance_dtb_opts.head),
    .desc = {
        {
            .name = "path",
            .type = QEMU_OPT_STRING,
            .help = "file path of device tree blob",
        }, {
            .name = "offset",
            .type = QEMU_OPT_NUMBER,
            .help = "offset to which we put the device tree blob relative to the start of the kernel image",
        },
        { /* End of list */ }
    },
};

struct rom_hotfix_blob kernel_builtin_fdt;

int mips_load_dtb(hwaddr addr, struct mips_boot_info *binfo,
                  hwaddr addr_limit, AddressSpace *as)
{
    void *fdt = NULL;
    int size, dt_size, rc = 0;
    uint32_t acells, scells;

    if (binfo->dtb_filename) {
        char *filename;
        filename = qemu_find_file(QEMU_FILE_TYPE_BIOS, binfo->dtb_filename);
        if (!filename) {
            fprintf(stderr, "Couldn't open dtb file %s\n", binfo->dtb_filename);
            goto fail;
        }
        // the size returned by load_device_tree is too large to override instructions
        dt_size = (get_image_size(filename) + ~DTB_PAGE_MASK) & DTB_PAGE_MASK;
        fdt = load_device_tree(filename, &size);
        if (!fdt) {
            fprintf(stderr, "Couldn't open dtb file %s\n", filename);
            g_free(filename);
            goto fail;
        }
        g_free(filename);
    } else {
        return 0;
    }

    if (addr_limit > addr && size > (addr_limit - addr)) {
        /* Installing the device tree blob at addr would exceed addr_limit.
         * Whether this constitutes failure is up to the caller to decide,
         * so just return 0 as size, i.e., no error.
         */
        g_free(fdt);
        return 0;
    }

    acells = qemu_fdt_getprop_cell(fdt, "/", "#address-cells",
                                   NULL, &error_fatal);
    scells = qemu_fdt_getprop_cell(fdt, "/", "#size-cells",
                                   NULL, &error_fatal);
    if (acells == 0 || scells == 0) {
        fprintf(stderr, "dtb file invalid (#address-cells or #size-cells 0)\n");
        goto fail;
    }

    if (scells < 2 && binfo->ram_size >= (1ULL << 32)) {
        /* This is user error so deserves a friendlier error message
         * than the failure of setprop_sized_cells would provide
         */
        fprintf(stderr, "qemu: dtb file not compatible with "
                "RAM size > 4GB\n");
         goto fail;
    }

    rc = fdt_path_offset(fdt, "/chosen");
    if (rc < 0) {
        qemu_fdt_add_subnode(fdt, "/chosen");
    }

    if (binfo->kernel_cmdline && *binfo->kernel_cmdline) {
        rc = qemu_fdt_setprop_string(fdt, "/chosen", "bootargs",
                                     binfo->kernel_cmdline);
        if (rc < 0) {
            fprintf(stderr, "couldn't set /chosen/bootargs\n");
            goto fail;
        }
    }
    if (binfo->initrd_size) {
        rc = qemu_fdt_setprop_cell(fdt, "/chosen", "linux,initrd-start",
                                   binfo->initrd_start);
        if (rc < 0) {
            fprintf(stderr, "couldn't set /chosen/linux,initrd-start\n");
            goto fail;
        }

        rc = qemu_fdt_setprop_cell(fdt, "/chosen", "linux,initrd-end",
                                   binfo->initrd_start + binfo->initrd_size);
        if (rc < 0) {
            fprintf(stderr, "couldn't set /chosen/linux,initrd-end\n");
            goto fail;
        }
    }

    qemu_fdt_dumpdtb(fdt, size);

    /* Put the DTB into the memory map as a ROM image: this will ensure
     * the DTB is copied again upon reset, even if addr points into RAM.
     */
    if (binfo->dtb_offset) {
        kernel_builtin_fdt.data = g_malloc(size);
        memcpy(kernel_builtin_fdt.data, fdt, size);
        kernel_builtin_fdt.size = dt_size;
        kernel_builtin_fdt.offset = binfo->dtb_offset;
        kernel_builtin_fdt.addr = binfo->dtb_start;
        qemu_register_reset(rom_hotfix_reset, &kernel_builtin_fdt);
    } else {
        rom_add_blob_fixed_as("dtb", fdt, size, addr, as);
    }

    g_free(fdt);
    return size;

fail:
    g_free(fdt);
    return -1;
}

void mips_load_kernel(MIPSCPU *cpu, struct mips_boot_info *info)
{
    CommonResetData *reset_data;
    int64_t entry;
    QemuOpts *dtb_opts;

    dtb_opts = qemu_opts_parse(&enhance_dtb_opts,
                          qemu_opt_get(qemu_get_machine_opts(), "dtb"),
                          true, NULL);

    info->dtb_filename = qemu_opt_get(dtb_opts, "path");
    info->dtb_offset = qemu_opt_get_number(dtb_opts, "offset", 0);

    if (!info->kernel_filename) {
        error_report("could not boot without kernel");
        exit(1);
    }
    entry = mips_setup_direct_kernel_boot(cpu, info);
    if (have_dtb(info)) {
        if (mips_load_dtb(info->dtb_start, info, info->dtb_limit, NULL) < 0) {
            exit(1);
        }
    }

    reset_data = g_malloc0(sizeof(CommonResetData));
    reset_data->cpu = cpu;
    reset_data->vector = entry;

    qemu_register_reset(do_cpu_reset, reset_data);
}
