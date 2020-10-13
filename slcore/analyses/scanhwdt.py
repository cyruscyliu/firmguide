from slcore.analyses.scanhw import UpdateHardware
from slcore.dt_parsers.common import load_dtb


class UpdateHardwareDT(UpdateHardware):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'scanhwdt'
        self.description = \
            'Add unknown hardware to FirmGuide hardware list.'

    def run(self, **kwargs):
        path_to_dtb = self.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no device tree blob available.'
            return False

        try:
            dts = load_dtb(path_to_dtb.strip())
            self.scan_and_update(dts)
        except Exception as e:
            self.warning('{} of {}'.format(str(e), path_to_dtb.strip()), 0)
        return True
