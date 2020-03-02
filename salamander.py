#!/usr/bin/python
from logger import setup_logging
from slcore.project import project_create, project_open, \
    project_rename, project_close, project_delete, project_show, \
    get_current_project
from slcore.tools.scan_dtcb import project_scan_declare, \
    project_scan_dtcb
from slcore.tools.scan_topology import project_scan_topology
from slcore.model import run_model
from slcore.environment import migrate, snapshot, archive
from slcore.srcodec import SRCodeController
import os
import argparse
import logging
import logging.config

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


def __model_ict(args):
    project = get_current_project()
    if project is None:
        return

    uuid = project.attrs['uuid']
    if args.debug:
        setup_logging(default_level=logging.DEBUG, uuid=uuid)
    else:
        setup_logging(default_level=logging.INFO, uuid=uuid)

    target_dir = project.attrs['target_dir']
    path_to_profile = os.path.join(target_dir, 'profile.yaml')
    if not os.path.exists(path_to_profile):
        path_to_profile = None

    firmware = migrate(uuid, path_to_profile=path_to_profile)
    firmware.set_arch(project.attrs['arch'])
    firmware.set_endian(project.attrs['endian'])

    # 2.1 low level source code controller
    srcodec = SRCodeController()
    path_to_source_code = project.attrs['source']
    srcodec.set_path_to_source_code(path_to_source_code)
    srcodec.set_path_to_vmlinux(os.path.join(path_to_source_code, 'vmlinux'))
    srcodec.set_path_to_dot_config(os.path.join(path_to_source_code, '.config'))
    srcodec.set_path_to_cross_compile(project.attrs['cross_compile'])
    srcodec.set_endian(project.attrs['endian'])
    srcodec.set_arch(project.attrs['arch'])
    srcodec.set_path_to_makeout(project.attrs['makeout'])
    firmware.srcodec = srcodec

    # 3. analyze the source code
    status = run_model(firmware)

    # 4. take snapshots to save results
    status = snapshot(firmware)
    return archive(firmware)


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


    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)

    try:
        args.func(args)
    except AttributeError as e:
        parser.print_help()


