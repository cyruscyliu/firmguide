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
    paused_analyses = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'pause.yaml')))
    f = open(os.path.join(os.getcwd(), 'tools', 'pause'), 'w')
    for k, v in paused_analyses.items():
        record = {'uuid': p_wrapper(k, 0)}
        for kk, vv in v.items():
            record[p_wrapper(kk, 0)] = vv.replace('\n', '</br>')
        context['paused_analyses'].append(record)

    pids = {}
    last_id = {}
    with open(os.path.join(os.getcwd(), 'log', 'salamander.log')) as f:
        '2019-10-13 22 22:05 463 - 17328 - INFO - [34mextract_kernel_and_dtb_by_binwalk done before[0m'
        for line in f:
            time, pid, level, info = line.split(' - ')
            id = None
            if info.startswith('['):
                id = info.split(' ')[0][1:-1]
                last_id[pid] = id
            if pid not in pids:
                pids[pid] = {}
            if id is not None and id not in pids[pid]:
                pids[pid][id] = {'stime': time, 'level': level, 'info': info.strip()}
            if id is not None and id in pids[pid]:
                pids[pid][id]['etime'] = time
            if level == 'WARNING':
                pids[pid][last_id[pid]]['level'] = level
            if level == 'ERROR':
                pids[pid][last_id[pid]]['level'] = level
    for pid, v in pids.items():
        for id, vv in v.items():
            context['analyses'].append(
                {'uuid': id, 'stime': vv['stime'], 'etime': vv['etime'], 'level': vv['level'], 'info': vv['info']}
            )
    context['analyses'].sort(key=sort_analyses)

    for uuid in os.listdir(os.path.join(os.getcwd(), 'build')):
        if uuid in ['binwalk-2.1.1', 'qemu-4.0.0', 'qemu-4.0.0.tar.xz', 'v2.1.1.tar.gz']:
            continue
        dt = os.path.join(os.getcwd(), 'build', uuid, 'profile.dt')
        with open(dt, 'r') as f:
            profile = f.read()
        profile_dt = fdt.parse_dts(profile)
        cpu = 0
        if profile_dt.exist_node('/cpus'):
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
