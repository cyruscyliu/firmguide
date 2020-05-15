import os

def get_initramfs(arch, endian):
    return os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '{}e{}.cpio.rootfs'.format(arch, endian))


