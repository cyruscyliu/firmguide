import os

from slcore.amanager import Analysis


class PBtngCMD(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'pbtngcmd'
        self.description = 'Print booting cmdline for given image.'
        self.required = ['preparation']

    def run(self, **kwargs):
        # running command
        self.info(self.analysis_manager.firmware.running_command, 1)

        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.warning('please set the source code for debugging interface', 1)
            return True

        qemuc = self.analysis_manager.qemuc
        if not qemuc.supported:
            self.error_info = 'please setup the QEMU'
            return False
        gdb_cmdline, debug_cmdline, help_info = qemuc.debug_ifs(
            self.analysis_manager.firmware.running_command,
            os.path.join(srcodec.get_path_to_source_code(), 'vmlinux'))
        for help_info_line in help_info:
            self.info(help_info_line, 1)
        return True
