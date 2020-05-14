#!/usr/bin/python
import os
import sys
import yaml
import argparse

sys.path.extend(['..'])
from slcore.analysis import Analysis, AnalysisGroup


def register_analysis():
    """Register all analysis and return their classes."""
    analyses = {}

    for module_file in os.listdir(os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'analyses')):
        module_path = os.path.join('slcore/analyses', module_file)
        if not module_path.endswith('py'):
            continue
        module_path = module_path[:-3].replace('/', '.')

        module = __import__(module_path, fromlist=[''])
        for analysis in dir(module):
            if analysis == 'Analysis':
                continue
            analysis_class = getattr(module, analysis)
            if not isinstance(analysis_class, type):
                continue
            if not issubclass(analysis_class, Analysis):
                continue
            if analysis not in analyses:
                callback = analysis.lower()
                analyses[callback] = {
                    'class': analysis_class,
                    'filename': module_file,
                    'object': analysis_class(None)}
    return analyses


def register_analysis_group(analyses):
    analysis_groups = {}
    for root, dirs, confs in os.walk(os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'aconfigs')):
        for conf in confs:
            conf_path = os.path.join(root, conf)
            groups = yaml.safe_load(open(conf_path))
            for group, attributes in groups.items():
                analysis_group = AnalysisGroup()
                analysis_group.name = conf[:-(len('.a.yaml'))]
                if 'description' in attributes:
                    analysis_group.description = attributes['description']
                for analysis in attributes['analyses']:
                    if analysis.lower() not in analyses:
                        print('error: there is no analysis named {}'.format(analysis))
                        exit()
                    analysis_group.members.append(analyses[analysis.lower()])
                    callback = group
                    analysis_groups[callback] = {
                        'class': AnalysisGroup,
                        'filename': conf,
                        'object': analysis_group}
    return analysis_groups


def list_analysis_and_group():
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
            ','.join([analysis['class'].__name__ for analysis in analysis_group_object.members]),
            analysis_group_object.description
        ))


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
