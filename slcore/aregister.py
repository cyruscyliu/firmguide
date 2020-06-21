import os
import yaml

from slcore.amanager import Analysis, AnalysisGroup


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
                        print('error: there is no analysis named {}'.format(
                            analysis))
                        return None
                    analysis_group.members.append(analyses[analysis.lower()])
                    callback = group
                    analysis_groups[callback] = {
                        'class': AnalysisGroup,
                        'filename': conf,
                        'object': analysis_group}
    return analysis_groups


def register_analysis_and_group():
    analyses = register_analysis()
    analysis_groups = register_analysis_group(analyses)

    analyses_and_groups = analyses
    for k, v in analysis_groups.items():
        analyses_and_groups[k] = v
    return analyses_and_groups
