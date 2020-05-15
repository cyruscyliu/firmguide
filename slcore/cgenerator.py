#!/usr/bin/python
import os
import yaml
import argparse

g_parameters = ['help', 'description']

l_parameters = [
    'short', 'action', 'nargs', 'const', 'default',
    'type', 'choices', 'required', 'help', 'metavar', 'dest']


def get_parser():
    return argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage='%(prog)s [options]')


def __init_parameters(paras, args):
    if 'type' in args and \
            args['type'] is not None and\
            isinstance(args['type'], str):
        args['type'] = eval(args['type'])

    for para in paras:
        if para not in args:
            args[para] = None


def add_argument(parser, **arguments):
    """Wrapper of parser.add_argument()."""
    if 'action' in arguments and \
            arguments['action'] == 'store_true':
        parser.add_argument(
            '-' + arguments['short'], '--' + arguments['flag'],
            action=arguments['action'],
            default=arguments['default'],
            required=arguments['required'],
            help=arguments['help'],
            dest=arguments['dest'])
    else:
        parser.add_argument(
            '-' + arguments['short'], '--' + arguments['flag'],
            action=arguments['action'],
            nargs=arguments['nargs'],
            const=arguments['const'],
            default=arguments['default'],
            type=arguments['type'],
            choices=arguments['choices'],
            required=arguments['required'],
            help=arguments['help'],
            metavar=arguments['metavar'],
            dest=arguments['dest'])


def construct_global_args(args, parser=None):
    """Construct global arguments."""
    if parser is None:
        parser = get_parser()

    if 'optional' in args:
        for flag, parameters in args['optional'].items():
            __init_parameters(l_parameters, parameters)
            parameters['flag'] = flag
            add_argument(parser, **parameters)

    if 'callback' in args:
        parser.set_defaults(callback=args['callback'])

    return parser


def construct_cmd_args(cmd, args, parser=None):
    """Construct subcommands and their arguments."""
    if parser is None:
        parser = get_parser()
    else:
        __init_parameters(g_parameters, args)
        parser = parser.add_parser(
            cmd, conflict_handler='resolve',
            help=args['help'], description=args['description'])

    if 'optional' in args:
        for flag, parameters in args['optional'].items():
            __init_parameters(l_parameters, parameters)
            parameters['flag'] = flag
            add_argument(parser, **parameters)

    if 'callback' in args:
        parser.set_defaults(callback=args['callback'])

    return parser


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


def generate_cmd_parser():
    """Generate commands parser according to xxx.cmd.yamls."""
    parser = get_parser()
    commands = parser.add_subparsers(
        title='Salamander Command and Arguments',
        metavar='subcommands', help='sub-command help'
    )

    for root, dirs, files in os.walk(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)), 'cmdconfigs')):
        for file in files:
            if not file.endswith('cmd.yaml'):
                continue
            path = os.path.join(root, file)
            cmd_args = yaml.safe_load(open(path))
            if file == 'global.cmd.yaml':
                construct_global_args(cmd_args['global'], parser=parser)
                continue
            for cmd, args in cmd_args.items():
                construct_cmd_args(cmd, args, parser=commands)
    return parser


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
