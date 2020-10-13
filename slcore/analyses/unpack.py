from slcore.compositor import unpack
from slcore.amanager import Analysis


class Unpack(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'unpack'
        self.description = 'Unpack firmware.'
        self.critical = True

    def run(self, **kwargs):
        path_to_firmware = kwargs.pop('firmware')
        show = kwargs.pop('show', False)

        components = unpack(
            path_to_firmware,
            target_dir=self.analysis_manager.project.attrs['path'])
        if not components.supported:
            self.error_info = '{} is not supported'.format(path_to_firmware)
            return False
        self.analysis_manager.firmware.set_components(components)

        path_to_dtb = components.get_path_to_dtb()
        if path_to_dtb is not None:
            self.info('find {}'.format(path_to_dtb), 1)
        self.analysis_manager.firmware.set_realdtb(path_to_dtb)

        # self.analysis_manager.firmware.set_kernel_load_address(load_address)

        if not show:
            return True
        # Show details
        for k, v in components.get_attributes().items():
            if isinstance(v, str):
                for line in v.strip().split('\n'):
                    self.info('{}: {}'.format(k, line), 1)
            else:
                self.info('{}: {}'.format(k, v), 1)
        return True
