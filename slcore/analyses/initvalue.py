from slcore.analysis import Analysis
from slcore.database.dbf import get_database


class InitValue(Analysis):
    def run(self, firmware):
        iv = get_database('qemu.iv')

        bamboos = firmware.get_bamboo_devices()
        for name, pros in bamboos.items():
            for compatible in pros['compatible']:
                offset_values = iv.select('model', compatible=compatible)
                if offset_values is None:
                    continue
                for offset_value in offset_values:
                    offset = offset_value['offset']
                    value = offset_value['value']
                    size = offset_value['size']
                    base = int(pros['mmio_base'], 16) + offset
                    status = firmware.insert_bamboo_devices(
                        base, size, value=value, compatible=compatible)
                    self.debug(
                        firmware,
                        'update base 0x{:08x} size 0x{:04x} of {} {}'.format(
                            base, size, compatible, status), 1)
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

