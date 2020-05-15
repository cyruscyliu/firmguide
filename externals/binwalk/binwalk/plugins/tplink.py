import binwalk.core.plugin


class TPLinkPlugin(binwalk.core.plugin.Plugin):
    """
    TPLink image extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^tplink firmware header',
                                           extension='seama',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass

    def scan(self, result):
        if result.description.lower().startswith('tplink firmware header'):
            try:
                kernel_start = result.offset + result.kernel_offset
                result.offset = kernel_start
                result.size = result.kernel_size
            except ValueError:
                pass
            except TypeError:
                pass

