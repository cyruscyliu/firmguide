import os
import json


def get_all_log_files():
    ret = []
    candidates = os.listdir('log')
    for candidate in candidates:
        path_to_candidate = os.path.join('log', candidate)
        if os.path.isfile(path_to_candidate) and path_to_candidate.endswith('log'):
            ret.append(os.path.realpath(path_to_candidate))
    return ret


def parse_record(global_context, record):
    if record['group'] == 'save_and_restore':
        if record['object'] != 'save':
            # new record
            global_context[record['uuid']] = {
                'uuid': record['uuid'], 'analysis': 0, 'saved': False, 'code_generation': False, 'tracing': 0}
        else:
            # done
            global_context[record['uuid']]['saved'] = True
    elif record['group'] == 'analysis':
        global_context[record['uuid']]['analysis'] += 1
    elif record['group'] == 'code_generation' and record['object'] == 'link':
        global_context[record['uuid']]['code_generation'] = True
    elif record['group'] == 'tracing':
        global_context[record['uuid']]['tracing'] += 1


def parse_log_file(path_to_log_file):
    # timestamp pid loglevel uuid group object message
    global_context = {}
    with open(path_to_log_file) as f:
        for line in f:
            items = line.split(' - ')
            if len(items) != 7:
                continue
            record = {
                'timestamp': items[0], 'pid': items[1], 'loglevel': items[2], 'uuid': items[3],
                'group': items[4], 'object': items[5], 'message': items[6],
            }
            parse_record(global_context, record)
    return list(global_context.values())


def update_data():
    log_files = get_all_log_files()
    records = []
    for log_file in log_files:
        records.extend(parse_log_file(log_file))
    with open('dashboard/data.json', 'w') as f:
        json.dump(records, f)
