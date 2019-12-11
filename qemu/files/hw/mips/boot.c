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

static void do_cpu_reset(void *opaque)
{
    CommonResetData *reset_data = (CommonResetData *)opaque;
    MIPSCPU *cpu = reset_data->cpu;

    cpu_reset(CPU(cpu));
    cpu->env.active_tc.PC = reset_data->vector;
}

static int64_t mips_setup_direct_kernel_boot(MIPSCPU *cpu, struct mips_boot_info *info)
{
    const size_t params_size = 264;
    int64_t entry, kernel_high, initrd_size;
    long kernel_size;
    ram_addr_t initrd_offset;
    uint32_t *params_buf;
    int big_endian;

#ifdef TARGET_WORDS_BIGENDIAN
    big_endian = 1;
#else
    big_endian = 0;
#endif
    kernel_size = load_elf(info->kernel_filename, NULL,
                           cpu_mips_kseg0_to_phys, NULL,
                           (uint64_t *)&entry, NULL,
                           (uint64_t *)&kernel_high, big_endian,
                           EM_MIPS, 1, 0);
    if (kernel_size >= 0) {
        if ((entry & ~0x7fffffffULL) == 0x80000000)
            entry = (int32_t)entry;
    } else {
        hwaddr ep, loadaddr;
        int is_linux;

        kernel_size = load_uimage(loaderparams.kernel_filename, &ep,
                                  &loadaddr, &is_linux,
                                  cpu_mips_kseg0_to_phys, NULL);

        if (kernel_size >=0) {
            entry = (uint32_t)ep;
        } else {
            error_report("could not load kernel neither as an elf ('%s': %s) nor as an uimage",
                         loaderparams.kernel_filename,
                         load_elf_strerror(kernel_size));
            exit(1);
        }
    }

    /* load initrd */
    initrd_size = 0;
    initrd_offset = 0;
    if (info->initrd_filename) {
        initrd_size = get_image_size (info->initrd_filename);
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

    /* Store command line.  */
    params_buf = g_malloc(params_size);

    params_buf[0] = tswap32(ram_size);
    params_buf[1] = tswap32(0x12345678);


    if (initrd_size > 0) {
        snprintf((char *)params_buf + 8, 256, "rd_start=0x%" PRIx64 " rd_size=%" PRId64 " %s",
                 cpu_mips_phys_to_kseg0(NULL, initrd_offset),
                 initrd_size, info->kernel_cmdline);
    } else {
        snprintf((char *)params_buf + 8, 256, "%s", info->kernel_cmdline);
    }

    rom_add_blob_fixed("params", params_buf, params_size,
                       16 * MiB - params_size);

    g_free(params_buf);
    return entry;
}

void mips_load_kernel(MIPSCPU *cpu, struct mips_boot_info *info)
{
    CommonResetData *reset_data;
    int64_t entry;

    if (info->kernel_filename) {
        entry = mips_setup_direct_kernel_boot(cpu, info);
    }

    reset_data = g_malloc0(sizeof(CommonResetData));
    reset_data->cpu = cpu;
    reset_data->vector = entry;

    qemu_register_reset(do_cpu_reset, reset_data);
}


