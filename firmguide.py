#!/usr/bin/python
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
    # 1. Each instance must include
    qemu_dir = self.project.attrs['qemu_dir']
    qemu_ver = os.path.basename(qemu_dir.split('-')[1])
    self.qemuc = get_qemucontroller(qemu_dir, version=qemu_ver)

    # Because non-data should be obtained by analysis itself,
    # we handle things in the following as early as possible.
    firmware = Firmware()
    # 
    path_to_dtb = kwargs.pop('dtb', None)
    firmware.set_realdtb(path_to_dtb)
    # 
    load_address = kwargs.pop('load', None)
    firmware.set_kernel_load_address(load_address)
    # 
    machine_name = kwargs.pop('machine_name', None)
    firmware.set_machine_name(machine_name)
    # 
    arch = kwargs.pop('arch', None)
    firmware.set_arch(arch)
    # 
    endian = kwargs.pop('endian', None)
    firmware.set_endian(endian)
    # 
    firmware.path_to_profile = os.path.join(
        self.project.attrs['path'], '.profile')
    self.firmware = firmware

    self.path_to_trace = kwargs.pop('trace', None) or  'firmguide.trace'
    self.trace_format = 'qemudebug'

    # Each instance may not include
    source = kwargs.pop('source', None)
    if 'source' in kwargs:
        self.srcodec = get_srcodecontroller(source, 
            self.project.attrs['cross_compile'],
            self.project.attrs['arch'], 
            self.project.attrs['endian'],
            self.project.attrs['makeout'])
    else:
        self.srcodec = get_srcodecontroller(source, 
            None, None, None, None)


if __name__ == '__main__':
    # 1 register commands and parse the cmdline
    parser = generate_cmd_parser()

    args = vars(parser.parse_args()) # to dict
    project_args = {}

    # 2 check: wrong command/no command
    if 'callback' not in args:
        parser.print_help()
        exit(-1)

    # 3 register project with must-exist things
    project_args['base_dir'] = os.path.dirname(os.path.realpath(__file__))
    project_args['qemu_dir'] = open('.qemu').readline().strip()
    project_args['rootfs_dir'] = os.path.join(project_args['base_dir'], 'rootfs')
    # output directory
    output = args['path'] or project_args['base_dir']
    project_args['path'] = output
    # log name
    logname = args.pop('logname') or 'firmguide'
    project_args['logname'] = logname
    # for expert-mode
    # project_args['sparse_dir'] = open('.sparse').readline().strip()
    # for automation-mode
    # project_args['llvm_dir'] = open('.llvmbin').readline().strip()

    # 4 setup logger as early as possible
    debug = args.pop('debug')
    if debug:
        setup_logging(output, logname, default_level=logging.DEBUG)
    else:
        setup_logging(output, logname)

    # 5 analysis commands
    project = Project(**project_args)
    # 5.1 register analysis and analysis group
    analyses_and_groups = register_analysis_and_group()
    callback = args.pop('callback')
    if callback not in analyses_and_groups:
        print('error: callback {} is not implemented'.format(callback))
        exit(-1)
    # 5.2 register analysis manager
    analysis_manager = \
        analyses_and_groups[callback]['object'].register(**args)
    # 5.3 warmup
    analysis_manager.project = project
    setup_analysis_manager(analysis_manager, **args)
    # 5.4 let's go 
    analysis_manager.print_analyses_chain()
    analysis_manager.run()
    # 5.5 warpup
    analysis_manager.wrapup()
