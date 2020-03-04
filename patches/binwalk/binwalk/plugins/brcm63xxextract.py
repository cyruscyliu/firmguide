import binwalk.core.plugin


class BCM63XXExtractPlugin(binwalk.core.plugin.Plugin):
    """
    Broadcom 96345 extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^broadcom 96345 firmware header',
                                           extension='imagetag',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass

    def scan(self, result):
        if result.description.lower().startswith('broadcom 96345 firmware header'):
            # result.offset is the start of the header
            #     the size of the header is 256 bytes
            # we have
            #     1. cfe_loader_size
            #     2. rootfs_size
            #     3  kernel_size = len(kernel_header) + lzma
            try:
                kernel_start = 256 + int(result.cfe_loader_size, 10) + result.offset
                kernel_size = int(result.kernel_size)
                result.offset = kernel_start
                result.size = kernel_size
            except ValueError:
                pass

