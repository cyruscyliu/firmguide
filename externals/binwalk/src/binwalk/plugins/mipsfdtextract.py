import os
import binwalk.core.plugin


class MIPSFDTExtractPlugin(binwalk.core.plugin.Plugin):
    """
    mips fdt extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^mips built-in fdt',
                                           extension='dtb',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass
