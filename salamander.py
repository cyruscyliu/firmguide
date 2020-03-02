#!/usr/bin/python
from logger import setup_logging
from slcore.project import project_create, project_open, \
    project_rename, project_close, project_delete, project_show
import argparse
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


if __name__ == '__main__':
    # 1
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-r', '--rerun', action='store_true', default=False,
                        help='ingore save and restore and rerun all analysis')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')

    # 1.1 project
    project = parser.add_subparsers(title='project')
    # 1.1.1 ./salamander create --help
    pproject_create = project.add_parser('create', help='create a project', conflict_handler='resolve')
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
    # 1.1.2 project open
    pproject_open = project.add_parser('open', help='  open a project', conflict_handler='resolve')
    pproject_open.add_argument('-u', '--uuid', type=str, required=True)
    pproject_open.set_defaults(func=__project_open)
    # 1.1.3 project rename
    pproject_rename = project.add_parser('rename', help='rename a project', conflict_handler='resolve')
    pproject_rename.add_argument('-u', '--uuid', type=str, required=True)
    pproject_rename.set_defaults(func=__project_rename)
    # 1.1.4 project close
    pproject_close = project.add_parser('close', help=' close a project', conflict_handler='resolve')
    pproject_close.set_defaults(func=__project_close)
    # 1.1.4 project delete
    pproject_delete = project.add_parser('delete', help='delete a project', conflict_handler='resolve')
    pproject_delete.add_argument('-u', '--uuid', type=str, required=True)
    pproject_delete.set_defaults(func=__project_delete)
    # 1.1.5 project show
    pproject_close = project.add_parser('show', help='  show a project', conflict_handler='resolve')
    pproject_close.set_defaults(func=__project_show)

    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    args.func(args)

