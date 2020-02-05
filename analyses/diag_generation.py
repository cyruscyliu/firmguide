"""
this file controls the generation of the qemu code
"""
from slcore.generation.compilerf import get_compiler
from slcore.qemuc import QEMUController
from slcore.compositor import pack, enlarge_image
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
        flash_size = firmware.get_flash_size(0)
        if flash_size:
            flash_size = eval(flash_size.replace('MiB', '0x100000'))
            enlarge_image(firmware.get_path(), flash_size)

        pack(firmware.components, kernel_load_address=kernel_load_address)
        image = firmware.get_path_to_rootfs()
        if image is None:
            image = firmware.get_path()
        running_command = machine_compiler.qemuc.get_command(
            firmware.get_architecture(), firmware.get_endian(), firmware.get_machine_name(),
            firmware.get_path_to_uimage(),
            flash=firmware.get_flash_type(0), image=image,
            dtb=firmware.get_path_to_dtb()
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

