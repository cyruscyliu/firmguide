"""ImageLIB.

This lib processes images by unpacking, packing and fixing them. This lib
is the basic of the project and designed in a modular and layered way.
    * This lib is a very basis which should be used only by a upper module.
    * This lib defines several interface processing images which a replaceable
    module should implement.

.. Interfaces:
    * unpack
    * pack_kernel
    * pack_image
    * pack_initramfs
    * fix_choosen_bootargs
    * fix_cmdline
    * fix_owrtdtb
"""
import os
import binwalk

from slcore.common import Common
from slcore.parser import fit_parser


TRX_KERNEL = 1
LEGACY_UIMAGE = 2
FIT_UIMAGE = 3
IMAGETAG_KERNEL = 4
COMBINEDIMAGE_KERNEL = 5
UBI_KERNEL = 6
SEAMA_KERNEL = 7
UBIQUITI_KERNEL = 8
TPLINK_KERNEL = 9


COMPONENT_ATTRIBUTES = [
    'path_to_raw', 'type', 'path_to_image', 'path_to_kernel',
    'path_to_dtb', 'path_to_rootfs', 'path_to_uimage',
]


class Components(Common):
    def __init__(self):
        """
        image+rootfs=raw
        header+kernel[+dtb]=image
        uheader+kernel=uimage
        """
        super().__init__()

        # binwalk output for debug
        self.output = ''
        self.supported = False

        self.set_attributes(COMPONENT_ATTRIBUTES)

    def get_raw_name(self):
        return os.path.basename(self.path_to_raw)

    def has_device_tree(self):
        return self.path_to_dtb is not None

    def has_kernel(self):
        return self.path_to_kernel is not None


def __ubidump(path, peb_size, min_io_size, output=None):
    size = os.path.getsize(path)

    n_blocks = size // peb_size
    if n_blocks * peb_size < size:
        n_blocks += 1

    if output is None:
        output = path + '.ubidump'

    offset = 0
    os.system('touch {}'.format(output))
    while n_blocks:
        # print('copy 0x{:x}+0x{:x}'.format(offset + min_io_size, peb_size - min_io_size))
        os.system('dd if={} of={} bs=1 count={} seek={} skip={} >/dev/null 2>&1'.format(
            path, output, peb_size - min_io_size, os.path.getsize(output), offset + min_io_size
        ))
        offset += peb_size
        n_blocks -= 1
    return output

def __replace_extension(path, src, dst):
    filename, file_extension = os.path.splitext(path)
    file_extension = file_extension.replace(src, dst)
    return filename + file_extension


def __handle_trx_kernel(image_path):
    kernel = __replace_extension(image_path, 'trx', 'kernel')
    os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
    uimage = __replace_extension(image_path, 'trx', 'uimage')

    dtb = __scan_dtb(kernel, extract=True)
    return kernel, dtb, uimage


def __handle_fit_uimage(image_path):
    kernel = __replace_extension(image_path, 'fit', 'kernel')
    dtb = image_path.replace('uimage.fit', 'dtb')
    uimage = __replace_extension(image_path, 'fit', 'uimage')

    # handle kernel
    os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
    lzma_kernel = False
    fit = fit_parser(os.popen('dumpimage -l {}'.format(image_path)).readlines())
    # {
    #   'images': {
    #       'kernel@1': {
    #           'properties': {'type': 'Kernel Image', 'compression': 'lzma compressed'}
    #       }
    #   }
    # }
    for _, k in fit['images'].items():
        if 'properties' not in k:
            continue
        v = k['properties']
        if 'type' in v and v['type'] == 'Kernel Image' \
                and v['compression'] == 'lzma compressed':
            lzma_kernel = True
    if lzma_kernel:
        module = __binwalk_scan_all(kernel, os.path.dirname(kernel), extract=True)
        for result in module.results:
            if str(result.description.lower()).find('lzma compressed data') != -1:
                # we will get kernel.7z, so kernel=kernel.7z[:-3]
                kernel = module.extractor.output[result.file.path].carved[result.offset][:-3]
                uimage = kernel + '.uimage'

    # handle dtb
    os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(image_path, dtb))
    return kernel, dtb, uimage


def __scan_dtb(image_path, extract=True):
    dtb = None

    module = __binwalk_scan_all(image_path, os.path.dirname(image_path), extract=extract)
    for result in module.results:
        if str(result.description.lower()).find('mips built-in fdt') != -1:
            dtb = module.extractor.output[result.file.path].carved[result.offset]
        elif str(result.description).find('Flattened device tree') != -1:
            # we sometimes get the dtb directly
            dtb = module.extractor.output[result.file.path].carved[result.offset]
    return dtb


def __handle_legacy_uimage(image_path, uimage3=False, uimage3_offset=None):
    kernel = __replace_extension(image_path, 'uimage', 'kernel')
    os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(image_path, kernel))
    uimage = image_path

    if uimage3:
        # reconstruct the uimage if uimage3
        uncompressed_kernel = os.path.join(
            os.path.dirname(image_path), '{:x}'.format(uimage3_offset + 0x40).upper())
        os.system('mv {0} {0}.bak'.format(image_path))
        os.system('dd if={0}.bak of={0} bs=1 count=64 >/dev/null 2>&1'.format(image_path))
        os.system('dd if=/dev/zero of={} bs=1 seek=31 count=1 conv=notrunc >/dev/null 2>&1'.format(image_path))
        # append 1M zeros as bss
        os.system('dd if=/dev/zero of={} bs=1 seek={} count={} conv=notrunc >/dev/null 2>&1'.format(
            uncompressed_kernel, os.path.getsize(uncompressed_kernel), 1048576))
        os.system('dd if={} of={} bs=1 seek=64 >/dev/null 2>&1'.format(uncompressed_kernel, image_path))
        # don't forget this
        kernel = uncompressed_kernel

    # find dtb in mips legacy uimage
    dtb = __scan_dtb(kernel, extract=True)

    return kernel, dtb, uimage


def __handle_lzma_kernel(image_path):
    if not os.path.exists(image_path):
        print('plugin for {} is missing'.format(image_path))
        return None, None, None
    kernel = __replace_extension(image_path, 'imagetag', 'kernel')
    uimage = __replace_extension(image_path, 'imagetag', 'uimage')
    dtb = None

    # find the real kernel
    module = __binwalk_scan_all(image_path, os.path.dirname(image_path), extract=True)
    for result in module.results:
        if str(result.description.lower()).find('lzma compressed data') != -1:
            if result.offset != 0:
                return None, None, None
            # we will get kernel.7z, so kernel=kernel.7z[:-3]
            kernel = module.extractor.output[result.file.path].carved[result.offset][:-3]
            uimage = kernel + '.uimage'
            # find the dtb in the kernel
            dtb = __scan_dtb(kernel, extract=True)
    return kernel, dtb, uimage


def __binwalk_scan_all(path, target_dir, extract=True):
    size = os.path.getsize(path)

    # we set block=sizeof(path), so there is one and only one module in this scan
    for module in binwalk.scan(
            path, signature=True, extract=extract, quiet=True, block=size, directory=target_dir):
        return module

def __enlarge_image(path, target_size):
    size_of_image = os.path.getsize(path)
    if size_of_image == target_size:
        return
    os.system('dd if=/dev/zero of={} seek={} bs=1 count={} > /dev/null 2>&1'.format(
        path, size_of_image, target_size - size_of_image))


def pack_kernel(components, arch='arm', load_address="0x00008000", entry_point="0x00008000"):
    """Add a uimage header to a kernel."""
    kernel = components.get_path_to_kernel()
    uimage = components.get_path_to_uimage()
    os.system(
        'mkimage -A {0} -C none -O linux -T kernel -d {1} -a {2} -e {3} {4} >/dev/null 2>&1'.format(
            arch, kernel, load_address, entry_point, uimage))
    return uimage


def pack_image(components, flash_size=None):
    """Pack a image."""
    raise NotImplementedError()


def pack_initramfs(components, mounted_to=None):
    """Make a initramfs."""
    return mounted_to


def fix_choosen_bootargs(components):
    """Remove choosen node in the dtb in a kernel image."""
    # this function must be called when the path_to_kernel is correct
    kernel = components.get_path_to_kernel()
    os.system('cp {0} {0}.fix_choosen_bootargs'.format(kernel))

    output = os.popen('strings -t d {} | grep console=ttyS0,'.format(kernel)).readlines()
    # 2323 ,console=ttyS0,115200
    if not len(output):
        return False
    start, label, console = output[0].strip().partition(' ')
    # start=2323, label=' ', console=,console=ttyS0,115200
    pre, console, param = console.partition('console')
    real_start = int(start) + len(pre)
    # 2323 ,
    # 2324 console
    os.system('dd if=/dev/zero of={0} bs=1 seek={1} count=1 conv=notrunc >/dev/null 2>&1'.format(kernel, real_start - 1))
    return True

def fix_owrtdtb(components, new_path_to_dtb):
    """Replace built-in dtb with new dtb."""
    # .fill 4000
    size = os.path.getsize(new_path_to_dtb)
    if size > 16 * 1024:
        return False

    kernel = components.get_path_to_kernel()
    os.system('cp {0} {0}.fix_owrtdtb'.format(kernel))

    output = os.popen('strings -t d {} | grep OWRTDTB:'.format(kernel)).readlines()
    # ['   1032 OWRTDTB:\n']
    if not len(output):
        return False
    start, label, _ = output[0].strip().partition('OWRTDTB')

    a = 'dd if=/dev/zero of={} bs=1 seek={} count={} conv=notrunc > /dev/null 2>&1'.format(
        kernel, int(start) + 8, size + 1)
    os.system(a)
    b = 'dd if={} of={} bs=1 seek={} count={} conv=notrunc > /dev/null 2>&1'.format(
        new_path_to_dtb, kernel, int(start) + 8, size)
    os.system(b)
    return True


def fix_smp(components):
    """Disable SMP/Keep only 1 cpu in dts."""
    path_to_dtb = components.get_path_to_dtb()
    os.system('cp {0} {0}.fix_smp'.format(path_to_dtb))

    from slcore.dt_parsers.common import load_dtb
    from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
    dts = load_dtb(path_to_dtb)
    path_to_cpu = find_flatten_cpu_in_fdt(dts)[0]['path']
    if not path_to_cpu.endswith('@0'):
        # only one cpu, skip
        return True

    next_path_to_cpu = path_to_cpu[:-1] + str(int(path_to_cpu[-1]) + 1)
    while dts.exist_node(next_path_to_cpu):
        dts.remove_node(
            os.path.basename(next_path_to_cpu),
            os.path.dirname(next_path_to_cpu))
        next_path_to_cpu = next_path_to_cpu[:-1] + str(int(next_path_to_cpu[-1]) + 1)

    with open(path_to_dtb, 'wb') as f:
        f.write(dts.to_dtb(version=17))
    return True


def fix_armdtb(components, new_path_to_dtb):
    """Disable built-in dtb in arm image"""
    kernel = components.get_path_to_kernel()
    os.system('cp {0} {0}.fix_armdtb'.format(kernel))

    path_to_dtb = __scan_dtb(kernel, extract=True)
    if path_to_dtb is None:
        return False

    start = int(os.path.basename(path_to_dtb).split('.')[0], 16)
    a = 'dd if=/dev/zero of={} bs=1 seek={} count=8 conv=notrunc > /dev/null 2>&1'.format(
        kernel, start)
    os.system(a)
    return True


def fix_cmdline(components):
    """Remove the default cmdline in a kernel image."""
    # this api should be called before pack_kernel
    kernel = components.get_path_to_kernel()
    os.system('cp {0} {0}.cmdline'.format(kernel))

    output = os.popen('strings -t d {} | grep CMDLINE'.format(kernel)).readlines()
    if not len(output):
        return False

    # 408 CMDLINE:board=BXU2000n-2-A1 console=ttyS0,115200 \
    #     mtdparts=spi0.0:256k(u-boot)ro,64k(u-boot-env)ro,1408k(kernel), \
    #     8448k(rootfs),6016k(user),64k(cfg),64k(oem),64k(art)ro
    # 0x408: CMDL
    # 0x40C: INE:
    # 0x410: \0   0x410 = start + 0x8
    start, label, cmdline = output[0].strip().partition('CMDLINE')
    if len(cmdline) == 1:
        return False
    length = len(cmdline) - 1
    os.system('dd if=/dev/zero of={0} bs=1 seek={1} count={2} conv=notrunc >/dev/null 2>&1'.format(kernel, int(start) + 8, length))
    return True


def unpack(path, target_dir=None, extract=True):
    """Unpack a image.

    Args:
        path(str)      : The path to the image.
        target_dir(str): Working directory, parent directory of the path by default.
        extract(bool)  : Whether or not to inactive binwalk extractions.

    Returns:
        Components: A Component object.
    """
    components = Components()
    if not os.path.exists(path):
        print('[-] {} not exist'.format(path))
        components.supported = False
        return components

    if target_dir is None:
        target_dir = os.path.dirname(path)
    # remove duplicated extraction sub-dirs
    os.system('rm -rf {}/_{}*extracted'.format(target_dir, os.path.basename(path)))

    # binwalk output is useful when returns None
    components.set_path_to_raw(path)

    module = __binwalk_scan_all(path, target_dir, extract=extract)

    # to avoid ref-ed before def-ed
    for result in module.results:
        # some helpers
        v1 = 0
        if str(result.description).find('flattened image tree') != -1:
            components.set_type(FIT_UIMAGE)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_fit_uimage(
                components.path_to_image)
        elif str(result.description).find('uImage') != -1:
            components.set_type(LEGACY_UIMAGE)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            # some uimages are compress type 3 which QEMU does not support
            uimage3, uimage3_offset = False, None
            if result.description.lower().startswith('uimage') and result.stub0 == 3:
                uimage3 = True
                uimage3_offset = result.offset
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_legacy_uimage(
                components.path_to_image, uimage3=uimage3, uimage3_offset=uimage3_offset)
        elif str(result.description).find('TRX') != -1:
            # sometimes, we have trx header + uImage(uImage header + lzma kernel)
            path_to_image = module.extractor.output[result.file.path].carved[result.offset]
            if path_to_image.endswith('uimage'):
                components = unpack(path_to_image, target_dir=os.path.dirname(path_to_image))
            elif path_to_image.endswith('7x'):
                # because *.trx will be overwrote by *.7z, we replace 7z with trx here
                path_to_image = path_to_image.replace('7z', 'trx')
                components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_trx_kernel(
                    components.path_to_image)
            components.set_type(TRX_KERNEL)
            path_to_image = module.extractor.output[result.file.path].carved[result.offset]
            components.set_path_to_image(path_to_image)
        elif str(result.description).find('Broadcom 96345 firmware header') != -1:
            components.set_type(IMAGETAG_KERNEL)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            # this kernel is not recognized yet
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_lzma_kernel(
                components.path_to_image)
        elif str(result.description).find('Combined image header') != -1:
            components.set_type(COMBINEDIMAGE_KERNEL)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            # this kernel is not recognized yet
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_lzma_kernel(
                components.path_to_image)
        elif str(result.description).find('Flattened device tree') != -1:
            # we sometimes get the dtb directly
            dtb = module.extractor.output[result.file.path].carved[result.offset]
            components.path_to_dtb = dtb
        elif str(result.description).find('Squashfs filesystem') != -1:
            components.set_path_to_rootfs(
                module.extractor.output[result.file.path].carved[result.offset])
        elif str(result.description).find('UBI erase count header') != -1:
            if components.get_type() != None:
                continue
            v1 = min(result.offset, v1)
            if result.jump != 0:
                # we have a correct peb size
                path_to_raw = components.get_path_to_raw()
                path_to_image = module.extractor.output[result.file.path].carved[v1]
                output = __ubidump(path_to_image, result.jump, result.data_offset)
                components = unpack(output, target_dir=os.path.dirname(output))
                components.set_type(UBI_KERNEL)
                components.set_path_to_raw(path_to_raw)
                components.set_path_to_image(path_to_image)
                break
        elif str(result.description).find('SEAMA firmware header') != -1:
            components.set_type(SEAMA_KERNEL)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            # this kernel is not recognized yet
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_lzma_kernel(
                components.path_to_image)
        # Ubiquiti partition header, header size: 56 bytes, name: "kernel"
        elif str(result.description).find('Ubiquiti partition header') != -1:
            if str(result.description).find('kernel') == -1:
                continue
            components.set_type(UBIQUITI_KERNEL)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            # this kernel is not recognized yet
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_lzma_kernel(
                components.path_to_image)
        elif str(result.description).find('AVM EVA header') != -1:
            break
        elif str(result.description).find('SENAO firmware header') != -1:
            break
        elif str(result.description).find('TPLink firmware header') != -1:
            components.set_type(TPLINK_KERNEL)
            components.set_path_to_image(module.extractor.output[result.file.path].carved[result.offset])
            # this kernel is not recognized yet
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_lzma_kernel(
                components.path_to_image)
        components.output += '0x%.8X    %s\n' % (result.offset, result.description)

    if not extract:
        os.system('rm -rf {}/_{}*extracted'.format(target_dir, os.path.basename(path)))

    components.supported = components.get_type() != None

    return components

