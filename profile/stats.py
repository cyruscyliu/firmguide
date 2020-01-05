import os
import yaml


def status_wrapper(status):
    if not isinstance(status, bool):
        return str(status)
   
    if status:
        return 'T'
    else:
        return 'F'


def statistics(firmware):
    summary = []

    working_dir = os.path.dirname(firmware.get_working_dir())

    for uuid in os.listdir(working_dir):
        summary_path = os.path.join(working_dir, uuid, 'stats.yaml')
        if os.path.exists(summary_path):
            summary.append(yaml.safe_load(open(summary_path)))

    # construct header
    headers = []
    for key, properties in firmware.stat_reference.items():
        levels = properties['level'].split('/')
        if properties['mode'] == 'count':
            headers.append(key)
        elif properties['mode'] == 'stats':
            for expect in properties['expect']:
                headers.append('/'.join([key, expect]))

    # get value wst header
    values = []
    for s in summary:
        value = []
        for header in headers:
            levels = header.split('/')
            if len(levels) == 1:
                value.append(status_wrapper(s[levels[0]]))
            elif len(levels) == 2:
                try:
                    value.append(status_wrapper(s[levels[0]][levels[1]]))
                except TypeError:
                    value.append(status_wrapper(False))
        values.append(value)

    path_to_stats = os.path.join(os.getcwd(), 'log', 'stats.csv')
    with open(path_to_stats, 'w') as f:
        f.write('{}\n'.format(','.join(headers)))
        for value in values:
            f.write('{}\n'.format(','.join(value)))
    print('stats at {}'.format(path_to_stats))
