import os
import binwalk.core.plugin


class FDTExtractPlugin(binwalk.core.plugin.Plugin):
    """
    fdt extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^flattened device tree',
                                           extension='dtb',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass
