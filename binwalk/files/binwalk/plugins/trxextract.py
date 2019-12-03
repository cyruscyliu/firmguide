import binwalk.core.plugin


class TRXExtractPlugin(binwalk.core.plugin.Plugin):
    """
    uImage extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^trx',
                                           extension='trx',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass

    def scan(self, result):
        if result.description.lower().startswith('trx'):
            kernel_start = result.stub0 + result.offset
            kernel_end = result.stub1 + result.offset
            result.offset = kernel_start
            result.size = kernel_end - kernel_start
