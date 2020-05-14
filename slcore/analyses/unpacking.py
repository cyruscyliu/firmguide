from slcore.compositor import unpack
from slcore.analysis import Analysis


class PluginUnpacking(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'unpacking'
        self.description = 'Plugin - Unpack given image.'

    def run(self, firmware, **kwargs):
        path_to_firmware = kwargs.pop(
            'firmware', firmware.get_components().get_path_to_raw())

        components = unpack(
            path_to_firmware, target_dir=firmware.get_target_dir())
        for k, v in components.get_attributes().items():
            if isinstance(v, str):
                for line in v.strip().split('\n'):
                    self.info(firmware, '{}: {}'.format(k, line), 1)
            else:
                self.info(firmware, '{}: {}'.format(k, v), 1)
