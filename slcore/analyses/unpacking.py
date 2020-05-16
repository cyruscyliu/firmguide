from slcore.compositor import unpack
from slcore.amanager import Analysis


class Unpacking(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'unpacking'
        self.description = 'Unpack given image.'

    def run(self, **kwargs):
        path_to_firmware = kwargs.pop('firmware')
        if path_to_firmware is None:
            path_to_firmware = \
                self.firmware.get_components().get_path_to_raw()

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
