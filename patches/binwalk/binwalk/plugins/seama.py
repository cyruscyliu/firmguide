import binwalk.core.plugin


class SEAMAPlugin(binwalk.core.plugin.Plugin):
    """
    SEAMA image extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^seama firmware header',
                                           extension='seama',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass

    def scan(self, result):
        if result.description.lower().startswith('seama firmware header'):
            # 0x0 + 12 + 16 + meta_size = kernel_start
            try:
                if result.image_size > 0:
                    kernel_start = result.offset + 12 + 16 + result.meta_size
                    kernel_size = result.image_size
                    result.offset = kernel_start
                    result.size = kernel_size
            except ValueError:
                pass
            except TypeError:
                pass

