"""
this file controls the generation of the qemu code
"""
from slcore.generation.compilerf import get_compiler
from slcore.qemuc import QEMUController
from slcore.compositor import pack_kernel, pack_image
from analyses.analysis import Analysis


class CodeGeneration(Analysis):
    def run(self, firmware):
        machine_compiler = get_compiler(firmware)
        machine_compiler.qemuc = QEMUController()

        # multi-level redering
        machine_compiler.compile()
        # link all files locally
        machine_compiler.link()
        machine_compiler.install()

        machine_compiler.make()

        kernel_load_address = firmware.get_kernel_load_address()
        kernel = pack_kernel(firmware.components, load_address=kernel_load_address)

        if firmware.probe_flash():
            flash_size = firmware.get_flash_size(0)
            if flash_size:
                flash_size = eval(flash_size.replace('MiB', '0x100000'))
            image = pack_image(firmware.components, flash_size=flash_size)
        else:
            image = None

        running_command = machine_compiler.qemuc.get_command(
            firmware.get_architecture(), firmware.get_endian(), firmware.get_machine_name(),
            kernel,
            flash=firmware.get_flash_type(0), image=image,
            dtb=firmware.get_components().get_path_to_dtb()
        )

        self.info(firmware, running_command, 1)
        firmware.running_command = running_command
        machine_compiler.uninstall()

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'code_generation'
        self.description = 'generate qemu code from profile'
        self.context['hint'] = 'some properties are not satisfied'
        self.critical = True
        self.required = []
        self.type = 'diag'

