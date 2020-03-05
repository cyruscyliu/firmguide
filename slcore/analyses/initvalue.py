from slcore.analyses.analysis import Analysis
from slcore.database.dbf import get_database


class InitValue(Analysis):
    def run(self, firmware):
        print(firmware.get_board())
        iv = get_database('iv').select('iv', arch=firmware.get_arch(), board=firmware.get_board())
        if iv is None:
            return True
        for mmio in iv:
            firmware.insert_bamboo_devices(
                mmio['base'], mmio['size'], value=mmio['value'], compatible=mmio['compatible'])
            self.debug(firmware, 'update base 0x{:08x} size 0x{:04x} of {}'.format(
                mmio['base'], mmio['size'], mmio['compatible']), 1)
        firmware.update_bamboo_devices()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'initvalue'
        self.description = 'update init value of registers'
        self.required = ['preprocdt']
        self.context['hint'] = ''
        self.critical = False
        #
        self.globals = []

