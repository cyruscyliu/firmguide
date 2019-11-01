import os
import yaml
import fdt

from render import Template


def sort_analyses(element):
    return int(element['uuid'])


def p_wrapper(string, indent):
    # return '<p>' + ' ' * indent + string + '</p>\n'
    return ' ' * indent + string


def main():
    context = {
        'paused_analyses': [
        ], 'analyses': [
            # {'uuid': 'uuid', 'stime': 'start time', 'etime': 'end time', 'level': 'level', 'info': 'info'}
        ], 'emulation': [
            {'uuid': 'uuid', 'dt': 'dt', 'cpu': 'cpu', 'ram': 'ram'},
        ]}

    for uuid in os.listdir(os.path.join(os.getcwd(), 'build')):
        if uuid in ['binwalk-2.1.1', 'qemu-4.0.0', 'qemu-4.0.0.tar.xz', 'v2.1.1.tar.gz']:
            continue
        dt = os.path.join(os.getcwd(), 'build', uuid, 'profile.dt')
        with open(dt, 'r') as f:
            profile = f.read()
        profile_dt = fdt.parse_dts(profile)
        cpu = 0
        if profile_dt.exist_node('/cpus/cpu@0'):
            cpu = 1
        ram = 0
        if profile_dt.exist_node('/memory'):
            ram = 1
        dt = 0
        if profile_dt.exist_node('/chosen'):
            dt = 1
        context['emulation'].append({'uuid': uuid, 'dt': dt, 'cpu': cpu, 'ram': ram})

    lines = ''
    with open(os.path.join(os.getcwd(), 'tools', 'web', 'statistics.template')) as f:
        for line in f:
            lines += line

    html = Template(lines).render(context)
    with open(os.path.join(os.getcwd(), 'tools', 'web', 'statistics.html'), 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()
