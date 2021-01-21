import os
import logging

from slcore.common import setup_logging
from slcore.cgenerator import generate_cmd_parser
from slcore.aregister import register_analysis_and_group
from slcore.pmanager import Project
from slcore.profile.firmware import Firmware
from slcore.srcodecontroller import get_srcodecontroller
from slcore.qemucontroller import get_qemucontroller


def setup_analysis_manager(self, **kwargs):
    # Each instance includes
    # Because non-data should be obtained by analysis itself,
    # we handle things in the following as early as possible.
    firmware = Firmware()

    path_to_dtb = kwargs.pop('dtb', None)
    firmware.set_realdtb(path_to_dtb)
    load_address = kwargs.pop('load', None)
    firmware.set_kernel_load_address(load_address)
    machine_name = kwargs.pop('machine_name', None)
    firmware.set_machine_name(machine_name)
    arch = kwargs.pop('arch', None)
    firmware.set_arch(arch)
    endian = kwargs.pop('endian', None)
    firmware.set_endian(endian)

    firmware.path_to_profile = os.path.join(
        self.project.attrs['path'], '.profile')
    self.firmware = firmware

    self.path_to_trace = kwargs.pop('trace', None) or  'firmguide.trace'
    self.trace_format = 'qemudebug'

    # Each instance may not include
    qemu_dir = self.project.attrs['qemu_dir']
    if qemu_dir is not None:
        qemu_ver = os.path.basename(qemu_dir.split('-')[1])
    else:
        qemu_ver = None
    self.qemuc = get_qemucontroller(qemu_dir, version=qemu_ver)
    source = kwargs.pop('source', None)
    cross_compile = kwargs.pop('cross_compile', None)
    self.srcodec = get_srcodecontroller(source, cross_compile=cross_compile)


def check_and_load(external_tool):
    external_tool_path = '.' + external_tool
    if os.path.exists(external_tool_path):
        return open(external_tool_path).readline().strip()
    else:
        return None


if __name__ == '__main__':
    # #########################################
    # 1 register commands and parse the cmdline
    # #########################################
    parser = generate_cmd_parser()
    args = vars(parser.parse_args()) # to dict
    project_args = {}

    # #########################################
    # 2 check wrong command or no command
    # #########################################
    if 'callback' not in args:
        parser.print_help()
        exit(-1)

    # #########################################
    # 3 register project
    # #########################################
    project_args['base_dir'] = os.path.dirname(os.path.realpath(__file__))
    project_args['rootfs_dir'] = os.path.join(project_args['base_dir'], 'rootfs')
    output = args['path'] or project_args['base_dir']
    project_args['path'] = output
    logname = args.pop('logname') or 'firmguide'
    project_args['logname'] = logname
    project_args['qemu_dir'] = check_and_load('qemu')
    project_args['sparse_dir'] = check_and_load('sparse')
    project_args['llvm_dir'] = check_and_load('llvmbin')
    project = Project(**project_args)

    # #########################################
    # 4 setup logger as early as possible
    # #########################################
    debug = args.pop('debug')
    if debug:
        setup_logging(output, logname, default_level=logging.DEBUG)
    else:
        setup_logging(output, logname)

    # #########################################
    # 5 run analysis commands
    # #########################################
    analyses_and_groups = register_analysis_and_group()
    callback = args.pop('callback')
    if callback not in analyses_and_groups:
        print('error: callback {} is not implemented'.format(callback))
        exit(-1)
    analysis_manager = \
        analyses_and_groups[callback]['object'].register(**args)

    analysis_manager.project = project
    setup_analysis_manager(analysis_manager, **args)
    analysis_manager.print_analyses_chain()
    analysis_manager.run()
    analysis_manager.wrapup()
