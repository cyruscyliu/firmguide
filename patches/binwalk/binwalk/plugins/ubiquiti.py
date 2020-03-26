import binwalk.core.plugin


class UbiquitiPlugin(binwalk.core.plugin.Plugin):
    """
    Ubiquiti image extractor plugin.
    """
    MODULES = ['Signature']

    def init(self):
        if self.module.extractor.enabled:
            self.module.extractor.add_rule(txtrule=None,
                                           regex='^ubiquiti partition header',
                                           extension='ubiquiti',
                                           cmd=self.extractor)

    def extractor(self, fname):
        pass

    def scan(self, result):
        if result.description.lower().startswith('ubiquiti partition header'):
            try:
                image_start = result.offset + result.header_size
                result.offset = image_start
                result.size = result.part_size
            except ValueError:
                pass
            except TypeError:
                pass

