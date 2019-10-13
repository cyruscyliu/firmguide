import os
import yaml

from tools.web.render import Template


def p_wrapper(string, indent):
    # return '<p>' + ' ' * indent + string + '</p>\n'
    return ' ' * indent + string


def main():
    context = {
        'paused_analyses': [],
        'analyses': [
            {'uuid': 'uuid', 'md5': 'md5', 'start': 'start', 'duration': 'duration', 'ERROR': 'ERROR'}
        ]}
    paused_analyses = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'pause.yaml')))
    f = open(os.path.join(os.getcwd(), 'tools', 'pause'), 'w')
    for k, v in paused_analyses.items():
        record = {'uuid': p_wrapper(k, 0)}
        for kk, vv in v.items():
            record[p_wrapper(kk, 0)] = vv.replace('\n', '</br>')
        context['paused_analyses'].append(record)

    lines = ''
    with open(os.path.join(os.getcwd(), 'tools', 'web', 'statistics.template')) as f:
        for line in f:
            lines += line

    html = Template(lines).render(context)
    with open(os.path.join(os.getcwd(), 'tools', 'web', 'statistics.html'), 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()
