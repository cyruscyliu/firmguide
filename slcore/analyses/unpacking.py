from slcore.compositor import unpack
from slcore.amanager import Analysis


class Unpacking(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'unpacking'
        self.description = 'Unpack given image.'

    def run(self, **kwargs):
        status = self.check_components()
        if not status:
            return status

        # Note: ffirmware not firmware, otherwise the firmware
        # will be unpacked for two times, and if the format
        # is not supported, we cannot even come here
        path_to_firmware = kwargs.pop('ffirmware')
        if path_to_firmware is None:
            # Note: if ffirmware is None, we just use what we've done
            status = self.check_components()
            if not status:
                return status
            path_to_firmware = \
                components = self.firmware.get_components()
        else:
            components = unpack(
                path_to_firmware,
                target_dir=self.analysis_manager.project.attrs['path'])

        for k, v in components.get_attributes().items():
            if isinstance(v, str):
                for line in v.strip().split('\n'):
                    self.info('{}: {}'.format(k, line), 1)
            else:
                self.info('{}: {}'.format(k, v), 1)
        return True
