#!/usr/bin/python
import yaml
import sys

sys.path.extend(['../..'])

from slcore.cgenerator import construct_cmd_args, \
    get_parser, generate_cmd_parser


def list_cmd_argsf(path, subcommand=None):
    """List commands and their arguments in file."""
    cmd_args = yaml.safe_load(open(path))

    if len(cmd_args) > 1:
        parser = get_parser()
        commands = parser.add_subparsers(
            title='List Command and Arguments',
            prog='subcommand')
    else:
        commands = None

    for cmd, args in cmd_args.items():
        if commands is None:
            parser = construct_cmd_args(cmd, args)
        else:
            construct_cmd_args(cmd, args, parser=commands)

    if subcommand is None:
        parser.print_help()
    else:
        print(parser.parse_args([subcommand, '-h']))


def list_cmd_args(subcommand=None):
    """List all commands and their arguments."""
    parser = generate_cmd_parser()

    if subcommand is None:
        parser.print_help()
    else:
        print(parser.parse_args([subcommand, '-h']))


if __name__ == '__main__':
    parser = get_parser()
    parser.add_argument(
        '-l', '--list', action='store_true', default=False,
        help='list all commands and arguments')
    parser.add_argument(
        '-f', '--file', default=False,
        help='list all commands and arguments in given file')
    parser.add_argument(
        '-s', '--subcommand',
        help='show subcommand help message and exit')
    args = parser.parse_args()

    if args.list:
        list_cmd_args(subcommand=args.subcommand)
    elif args.file:
        list_cmd_argsf(args.file, subcommand=args.subcommand)
    else:
        list_cmd_args(subcommand=args.subcommand)
