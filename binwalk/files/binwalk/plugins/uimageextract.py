import os
import binwalk.core.plugin


class uImageExtractPlugin(binwalk.core.plugin.Plugin):
    """
    uImage extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^uimage',
                                           extension='uimage',
                                           cmd=self.extractor)
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^flattened image tree',
                                           extension='uimage.fit',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass
