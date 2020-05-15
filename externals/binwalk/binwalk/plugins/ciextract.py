import binwalk.core.plugin


class CIExtractPlugin(binwalk.core.plugin.Plugin):
    """
    CombinedImage extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^combined image header',
                                           extension='ci',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass

    def scan(self, result):
        if result.description.lower().startswith('combined image header'):
            # result.offset is the start of the header
            #     the size of the header is 64KB, 0x10000
            # we have
            #     1. kernel_size
            #     2. rootfs_size
            try:
                kernel_start = result.offset + 0x10000
                kernel_size = int(result.kernel_size[:8], 16)
                result.offset = kernel_start
                result.size = kernel_size
            except ValueError:
                pass
            except TypeError:
                pass

