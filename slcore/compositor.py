"""
These interfaces unpack, pack given firmware blob to uImages.
"""
import os
import types
import binwalk
import tempfile

from logger import logger_info, logger_debug, logger_warning
from settings import *

TRX_KERNEL, LEGACY_UIMAGE, FIT_UIMAGE = 1, 2, 3

COMPONENT_ATTRIBUTES = [
    'path_to_raw', 'type', 'path_to_image', 'path_to_kernel',
    'path_to_dtb', 'path_to_rootfs', 'path_to_uimage',
]

class Common(object):
    def set_attributes(self, attrs):
        if isinstance(attrs, list):
            for attr in attrs:
                self.__dict__[attr] = None
                self.__setattr__('set_'+attr, lambda x, a=attr: self.__dict__.__setitem__(a, x))
                self.__setattr__('get_'+attr, lambda a=attr: self.__dict__.__getitem__(a))
        elif isinstance(attrs, dict):
            for k, v in attrs.items():
                self.__dict__[k] = v

    def get_attributes(self):
        attrs = {}

        for k, v in self.__dict__.items():
            if isinstance(v, types.FunctionType):
                continue
            attrs[k] = v

        return attrs


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


def replace_extension(path, src, dst):
    filename, file_extension = os.path.splitext(path)
    file_extension = file_extension.replace(src, dst)
    return filename + file_extension


def __handle_trx_kernel(image_path):
    kernel = replace_extension(image_path, 'trx', 'kernel')
    os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
    uimage = replace_extension(image_path, 'trx', 'uimage')
    return kernel, None, uimage


def __handle_fit_uimage(image_path):
    kernel = replace_extension(image_path, 'fit', 'kernel')
    dtb = image_path.replace('uimage.fit', 'dtb')
    os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
    uimage = replace_extension(image_path, 'fit', 'uimage')
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

def enlarge_image(path, target_size):
    size_of_image = os.path.getsize(path)
    if size_of_image == target_size:
        return
    os.system('dd if=/dev/zero of={} seek={} bs=1 count={} > /dev/null 2>&1'.format(
        path, size_of_image, target_size - size_of_image))


def pack_kernel(components, arch='arm', load_address="0x00008000"):
    kernel = components.get_path_to_kernel()
    uimage = components.get_path_to_uimage()
    os.system('mkimage -A {0} -C none -O linux -T kernel -d {1} -a {2} -e {2} {3} >/dev/null 2>&1'.format(arch, kernel, load_address, uimage))
    return uimage


def pack_image(components, flash_size=None):
    rootfs = components.get_path_to_rootfs()
    if rootfs is None:
        rootfs = DEFAULT_ROOTFS
    enlarge_image(rootfs, flash_size)
    return rootfs

def pack_initramfs(components, mounted_to=None):
    return mounted_to

def unpack(path, target_dir=None, extract=True):
    """
    :param path: absolute path-like string
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
    components = Components()
    components.set_path_to_raw(path)

    module = __binwalk_scan_all(path, target_dir, extract=extract)

    # to avoid ref-ed before def-ed
    for result in module.results:
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
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage= __handle_legacy_uimage(
                components.path_to_image, uimage3=uimage3, uimage3_offset=uimage3_offset)
        elif str(result.description).find('TRX') != -1:
            components.set_type(TRX_KERNEL)
            # because *.trx will be overwrote by *.7z, we replace 7z with trx here
            components.set_path_to_image(
                module.extractor.output[result.file.path].carved[result.offset].replace('7z', 'trx'))
            components.path_to_kernel, components.path_to_dtb, components.path_to_uimage = __handle_trx_kernel(
                components.path_to_image)
        elif str(result.description).find('Squashfs filesystem') != -1:
            components.set_path_to_rootfs(
                module.extractor.output[result.file.path].carved[result.offset])
        components.output += '0x%.8X    %s\n' % (result.offset, result.description)

    if not extract:
        os.system('rm -rf {}/_{}*extracted'.format(target_dir, os.path.basename(path)))

    components.supported = components.get_type() != None

    return components

