"""
These interfaces unpack, pack given firmware blob to uImages.
"""
import os
import binwalk
import tempfile

from logger import logger_info, logger_debug, logger_warning

UNKNOWN, TRX_KERNEL, LEGACY_UIMAGE, FIT_UIMAGE = -1, 0, 1, 2


class Components(object):
    def __init__(self, uuid=None, arch=None, endian=None):
        self.output = '' # for debug

        self.path = None
        self.image_type = UNKNOWN
        self.image_path = None

        # components
        self.kernel_path = None
        self.dtb_path = None
        self.uimage_path = None
        self.rootfs_path = None

        # properties
        self.uuid = uuid
        self.arch = arch
        self.endian = endian

    def get_path(self):
        return self.path

    def get_image(self):
        return self.image_path

    def get_image_name(self):
        return os.path.basename(self.image_path)

    def get_kernel(self):
        return self.kernel_path

    def has_device_tree(self):
        return self.dtb_path is not None

    def get_dtb(self):
        return self.dtb_path

    def get_uimage(self):
        return self.uimage_path

    def get_rootfs(self):
        return self.rootfs_path

    def get_all(self):
        all_ = [self.kernel_path, self.dtb, self.uimage_path, self.rootfs_path]
        if self.dtb_path is not None:
            all_.append(self.dtb_path)
        return all_

def replace_extension(path, src, dst):
    filename, file_extension = os.path.splitext(path)
    file_extension = file_extension.replace(src, dst)
    return filename + file_extension


def __handle_trx_kernel(image_path):
    kernel = replace_extension(image_path, 'trx', 'kernel')
    os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
    uimage = replace_extension(image_path, 'trx', 'uimage')
    # if firmware.get_architecture() == 'arm':
    #     os.system('mkimage -A arm -C none -O linux -T kernel -d {} '
    #               '-a 0x8000 -e 0x8000 {} >/dev/null 2>&1'.format(kernel, uimage))
    return kernel, None, uimage


def __handle_fit_uimage(image_path):
    kernel = replace_extension(image_path, 'fit', 'kernel')
    dtb = image_path.replace('uimage.fit', 'dtb')
    os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
    uimage = replace_extension(image_path, 'fit', 'uimage')
    # mkimage -A arm -C none -O linux -T kernel -d path/to/zImage -a 0x8000 -e 0x8000
    #     path/to/uImage >/dev/null 2>&1
    # if firmware.get_architecture() == 'arm':
    #     os.system('mkimage -A arm -C none -O linux -T kernel -d {} '
    #               '-a 0x8000 -e 0x8000 {} >/dev/null 2>&1'.format(kernel, uimage))
    os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(image_path, dtb))
    return kernel, dtb, uimage


def __handle_legacy_uimage(image_path, uimage3=False, uimage3_offset=None):
    kernel = replace_extension(image_path, 'uimage', 'kernel')
    os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(image_path, kernel))
    uimage = image_path

    if not uimage3:
        return kernel, None, uimage

    # reconstruct the uimage if uimage3
    uncompressed_kernel = os.path.join(
        os.path.dirname(image_path), '{:x}'.format(uimage3_offset + 0x40).upper())
    os.system('mv {0} {0}.bak'.format(image_path))
    os.system('dd if={0}.bak of={0} bs=1 count=64 >/dev/null 2>&1'.format(image_path))
    os.system('dd if=/dev/zero of={} bs=1 seek=31 count=1 >/dev/null 2>&1'.format(image_path))
    os.system('dd if={} of={} bs=1 seek=64 >/dev/null 2>&1'.format(uncompressed_kernel, image_path))

    # find dtb in mips legacy uimage
    module = __binwalk_scan_all(image_path, tempfile.gettempdir(), extract=False)
    for result in module.results:
        if str(result.description.lower()).find('mips built-in fdt') != -1:
            dtb = module.extractor.output[result.file.path].carved[result.offset]
            return kernel, dtb, uimage

    return kernel, None, uimage


def __binwalk_scan_all(path, target_dir, extract=True):
    size = os.path.getsize(path)

    # we set block=sizeof(path), so there is one and only one module in this scan
    for module in binwalk.scan(
            path, signature=True, extract=extract, quiet=True, block=size, directory=target_dir):
        return module

def pack(components, load_address="0x00008000"):
    """
    :param components: return from unpack
    :param load_adress: have to start with "0x"
    :return: componetns
    """
    kernel = components.get_kernel()
    uimage = components.get_uimage()

    if components.arch == 'arm':
         os.system('mkimage -A arm -C none -O linux -T kernel -d {0} -a {1} -e {1} {2} >/dev/null 2>&1'.format(kernel, load_address, uimage))
    elif components.arch == 'mips':
         os.system('mkimage -A mips -C none -O linux -T kernel -d {0} -a {1} -e {1} {2} >/dev/null 2>&1'.format(kernel, load_address, uimage))

    return components


def unpack(path, uuid=None, arch=None, endian=None, target_dir=None, extract=True):
    """
    :param path: absolute path-like string
    :param uuid: uuid for this components
    :param arch: arm or mips
    :param endian: l or b
    :param target_dir: working directory, parent directory of the path by default
    :param extract: whether to save binwalk extractions or not
    :return: components
    """
    if not os.path.exists(path):
        return None

    if target_dir is None:
        target_dir = os.path.dirname(path)
    # remove duplicated extraction sub-dirs
    os.system('rm -rf {}/_{}*extracted'.format(target_dir, os.path.basename(path)))

    # binwalk output is useful when returns None
    components = Components(uuid, arch, endian)
    components.path = path

    module = __binwalk_scan_all(path, target_dir, extract=extract)

    # to avoid ref-ed before def-ed
    for result in module.results:
        if str(result.description).find('flattened image tree') != -1:
            components.image_type = FIT_UIMAGE
            logger_info(uuid, 'composition', 'unpack', 'image_type: {}'.format('fit uimage'), 1)
            components.image_path = module.extractor.output[result.file.path].carved[result.offset]
            components.kernel_path, components.dtb_path, components.uimage_path = __handle_fit_uimage(components.image_path)
            break
        elif str(result.description).find('uImage') != -1:
            components.image_type = LEGACY_UIMAGE
            logger_info(uuid, 'composition', 'unpack', 'image_type: {}'.format('legacy uimage'), 1)
            components.image_path = module.extractor.output[result.file.path].carved[result.offset]
            # some uimages are compress type 3 which QEMU does not support
            uimage3, uimage3_offset = False, None
            if result.description.lower().startswith('uimage') and result.stub0 == 3:
                uimage3 = True
                uimage3_offset = result.offset
            components.kernel_path, components.dtb_path, components.uimage_path = __handle_legacy_uimage(
                components.image_path, uimage3=uimage3, uimage3_offset=uimage3_offset)
            break
        elif str(result.description).find('TRX') != -1:
            components.image_type = TRX_KERNEL
            logger_info(uuid, 'composition', 'unpack', 'image_type: {}'.format('trx image'), 1)
            # because *.trx will be overwrote by *.7z, we replace 7z with trx here
            components.image_path = \
                module.extractor.output[result.file.path].carved[result.offset].replace('7z', 'trx')
            components.kernel_path, components.dtb_path, components.uimage_path = __handle_trx_kernel(components.image_path)
            break
        else:
            components.image_type = UNKNOWN
        components.output += '0x%.8X    %s\n' % (result.offset, result.description)

    if not extract:
        os.system('rm -rf {}/_{}*extracted'.format(target_dir, os.path.basename(path)))

    supported = components.image_type != UNKNOWN
    if supported:
        for k, v in components.__dict__.items():
            if k == 'image_type' or k == 'output':
                continue
            else:
                logger_debug(uuid, 'composition', 'unpack', '{}: {}'.format(k, v), 1)
    else:
        logger_warning(uuid, 'composition', 'unpack', 'cannot unpack this firmware of nonstandard format', 0)
        for line in components.output.split('\n'):
            if not len(line):
                continue
            logger_debug(uuid, 'composition', 'unpack', '{}'.format(line), 0)
        return None

    return components

