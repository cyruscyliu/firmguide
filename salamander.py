#!/usr/bin/python
import os
import argparse
import logging
import logging.config
from logger import setup_logging
from slcore.project import project_create, project_open, \
    project_rename, project_close, project_delete, project_show, \
    get_current_project, project_get_srcodec, project_get_qemuc
from slcore.tools.scan_dtcb import project_scan_declare, project_scan_dtcb
from slcore.tools.scan_topology import project_scan_topology
from slcore.environment import migrate, snapshot, archive
from slcore.scheduler import run_static_analysis, run_diagnosis, run_model
from slcore.generation.dt_renderer import run_dt_renderer
from slcore.compositor import unpack

logger = logging.getLogger()


def __project_create(args):
    project_create(
        args.uuid, args.arch, args.endian,
        brand=args.brand, target=args.target, subtarget=args.subtarget,
        source=args.source, cross_compile=args.cross_compile, makeout=args.makeout)


def __project_open(args):
    project_open(args.uuid)


def __project_rename(args):
    project_rename(args.uuid)


def __project_close(args):
    project_close()


def __project_delete(args):
    project_delete(args.uuid)


def __project_show(args):
    project_show()


def __scan_declare(args):
    project_scan_declare()


def __scan_dtcb(args):
    project_scan_dtcb(args.dtb)


def __scan_topology(args):
    project_scan_topology(args.dtb)


def __standard_warmup(args, components=None):
    project = get_current_project()
    if project is None:
        exit()

    uuid = project.attrs['uuid']
    if args.debug:
        setup_logging(default_level=logging.DEBUG, uuid=uuid)
    else:
        setup_logging(default_level=logging.INFO, uuid=uuid)

    target_dir = project.attrs['target_dir']
    path_to_profile = os.path.join(target_dir, 'profile.yaml')
    if not os.path.exists(path_to_profile):
        path_to_profile = None

    firmware = migrate(uuid, path_to_profile=path_to_profile, components=components)
    firmware.set_arch(project.attrs['arch'])
    firmware.set_endian(project.attrs['endian'])
    firmware.set_machine_name(uuid)
    firmware.rerun = args.rerun

    firmware.srcodec = project_get_srcodec()
    firmware.qemuc = project_get_qemuc()

    firmware.max_iteration = 1
    firmware.trace_format = 'qemudebug'
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_arch(), firmware.get_endian()
    )
    firmware.debug = args.debug

    return firmware


def __standard_wrapup(firmware):
    status = snapshot(firmware)
    return archive(firmware)

def __model_ict(args):
    # 1 standard_setup
    firmware = __standard_warmup(args)
    # 2. analyze the source code
    status = run_model(firmware)
    # 3. take snapshots to save results
    return __standard_wrapup(firmware)


def __analyze(args):
    # 1 standard_setup
    firmware = __standard_warmup(args)
    # 2. analyze the source code
    status = run_static_analysis(firmware)
    # 3. take snapshots to save results
    return __standard_wrapup(firmware)


def __diagnose(args):
    # 1 standard_setup
    firmware = __standard_warmup(args)

    # 2. test the machine
    if not firmware.get_components():
        firmware.components = unpack(args.firmware, target_dir=firmware.target_dir)

    if args.dtb:
        firmware.set_dtb(args.dtb)
    elif firmware.get_components().get_path_to_dtb():
        firmware.set_dtb(firmware.get_components().get_path_to_dtb())
    else:
        print('neither dtb was found in tested firmware nor -dtb was assigned')
        return __standard_wrapup(firmware)

    status = run_diagnosis(firmware)

    # 3. take snapshots to save results
    return __standard_wrapup(firmware)

def __generate(args):
    # 1 standard_setup
    firmware = __standard_warmup(args)

    # 2 generate code from dtb
    firmware.set_dtb(args.dtb)
    status = run_dt_renderer(firmware)

    # 3. take snapshots to save results
    return __standard_wrapup(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    commands = parser.add_subparsers(title='salamander commands')
    # 1 project
    # 1.1 ./salamander create --help
    pproject_create = commands.add_parser('create', help='create a project', conflict_handler='resolve')
    pproject_create.add_argument('-u', '--uuid', type=str, required=True)
    pproject_create.add_argument('-a', '--arch', choices=['arm', 'arm64', 'mips'], required=True)
    pproject_create.add_argument('-e', '--endian', choices=['b', 'l'], required=True)
    pproject_create.add_argument('-b', '--brand', choices=['openwrt'], required=True)
    pproject_create.add_argument('-t', '--target', required=True)
    pproject_create.add_argument('-st', '--subtarget', required=True)
    pproject_create.add_argument('-s', '--source', metavar='path/to/source', required=True)
    pproject_create.add_argument('-cc', '--cross_compile', metavar='path/to/cc_prefix', required=True)
    pproject_create.add_argument('-m', '--makeout', metavar='path/to/makeout', required=True)
    pproject_create.set_defaults(func=__project_create)
    # 1.2 project open
    pproject_open = commands.add_parser('open', help='open a project', conflict_handler='resolve')
    pproject_open.add_argument('-u', '--uuid', type=str, required=True)
    pproject_open.set_defaults(func=__project_open)
    # 1.3 project rename
    pproject_rename = commands.add_parser('rename', help='rename a project', conflict_handler='resolve')
    pproject_rename.add_argument('-u', '--uuid', type=str, required=True)
    pproject_rename.set_defaults(func=__project_rename)
    # 1.4 project close
    pproject_close = commands.add_parser('close', help='close a project', conflict_handler='resolve')
    pproject_close.set_defaults(func=__project_close)
    # 1.4 project delete
    pproject_delete = commands.add_parser('delete', help='delete a project', conflict_handler='resolve')
    pproject_delete.add_argument('-u', '--uuid', type=str, required=True)
    pproject_delete.set_defaults(func=__project_delete)
    # 1.5 project show
    pproject_close = commands.add_parser('show', help='show a project', conflict_handler='resolve')
    pproject_close.set_defaults(func=__project_show)
    # 2 plugins
    # 2.1 scan_declare
    pscan_declare = commands.add_parser('declare', help='find new peripherals defined by XXX_DECLARE')
    pscan_declare.set_defaults(func=__scan_declare)
    # 2.2 scan_dtcb
    pscan_dtcb = commands.add_parser('dtcb', help='find callbacks w.s.t compatibles in a device tree')
    pscan_dtcb.add_argument('-dtb', '--dtb', required=True)
    pscan_dtcb.set_defaults(func=__scan_dtcb)
    # 2.3 model_ict
    pmodel_ict = commands.add_parser('ictm', help='model intc/clk/timer in current project')
    pmodel_ict.set_defaults(func=__model_ict)
    # 2.4 scan_topology
    pscan_topology = commands.add_parser('topology', help='find interrupts topology in a device tree')
    pscan_topology.add_argument('-dtb', '--dtb', required=True)
    pscan_topology.set_defaults(func=__scan_topology)
    # 3 cores
    # 3.1 analyze
    panalyze = commands.add_parser('analyze', help='model machine in current project')
    panalyze.set_defaults(func=__analyze)
    # 3.2 generate
    pgenerate = commands.add_parser('generate', help='test machine in current project')
    pgenerate.add_argument('-dtb', '--dtb', required=True)
    pgenerate.set_defaults(func=__generate)
    # 3.3 diagnose
    pdiagnose = commands.add_parser('diagnose', help='test machine in current project')
    pdiagnose.add_argument('-dtb', '--dtb', required=False)
    pdiagnose.add_argument('-f', '--firmware', required=True)
    pdiagnose.set_defaults(func=__diagnose)


    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    try:
        args.func(args)
    except AttributeError as e:
        parser.print_help()


