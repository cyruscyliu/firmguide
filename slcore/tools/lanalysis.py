#!/usr/bin/python
import sys
import argparse

sys.path.extend(['.', '..', '../..'])

from slcore.aregister import register_analysis, register_analysis_group


def list_analysis_and_group():
    """Self-testing."""
    analyses = register_analysis()
    print('List all analyses.')
    print('  {:20}{:20}{:20}{:40}{}'.format(
        'FILENAME', 'NAME', 'CALLBACK',
        'REQUIRMENT', 'DESCRIPTION'))
    for callback, attributes in analyses.items():
        analysis_object = attributes['object']
        print('  {:20}{:20}{:20}{:40}{}'.format(
            attributes['filename'],
            analysis_object.name,
            callback,
            ','.join(analysis_object.required),
            analysis_object.description))

    analysis_groups = register_analysis_group(analyses)
    if analysis_groups is None:
        return False
    print('List all analysis groups.')
    print('  {:20}{:20}{:20}{:40}{}'.format(
        'FILENAME', 'NAME', 'CALLBACK',
        'MEMBERS', 'DESCRIPTION'))
    for callback, attributes in analysis_groups.items():
        analysis_group_object = attributes['object']
        print('  {:20}{:20}{:20}{:40}{}'.format(
            attributes['filename'],
            analysis_group_object.name,
            callback,
            ','.join([analysis['class'].__name__
                      for analysis in analysis_group_object.members]),
            analysis_group_object.description
        ))
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        '-a', '--all', action='store_true', default=False,
        help='list all analysis and analysis group')
    args = parser.parse_args()

    if args.all:
        list_analysis_and_group()
    else:
        list_analysis_and_group()
