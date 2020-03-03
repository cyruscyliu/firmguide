from slcore.analyses.analysis import Analysis
from slcore.database.dbf import get_database


class InitValue(Analysis):
    def run(self, firmware):
        iv = get_database('iv', arch=firmware.arch(), board=firmware.board)
        for mmio in iv:
            firmware.insert_bamboo_devices(mmio['base'], mmio['size'], value=mmio['value'])
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

