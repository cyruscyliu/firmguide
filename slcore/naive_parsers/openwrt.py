from pyquery import PyQuery as pq
from slcore.database.dbf import get_database

import os

def search_most_possible_target(strings, extent=None):
    # by default we search the target
    if extent is None:
        extent = ['target']
    # get the database
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent, deduplicated=True, transpose=True)
    # the result would be [[all_record[0], [all_record[1]]
    targets = []
    for ext in extent:
        targets += results[openwrt.header_last_selected.index(ext)]
    # we would like to search target from strings
    target_searched = {}
    for string in strings:
        for target in targets:
            if target.startswith('?'):
                target = target[1:]
            if len(target) > len(string) or len(target) < 2:
                continue
            if target in string.split('_'):
                if target not in target_searched:
                    target_searched[target] = {'count': 0, 'strings': []}
                target_searched[target]['count'] += 1
                target_searched[target]['strings'].append(string.strip())
                break
    # find the most possible target
    sum_of_occurrence = 0
    for k, v in target_searched.items():
        sum_of_occurrence += v['count']
    most_possible = None
    max_count = 0
    for k, v in target_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        if count > max_count:
            most_possible = k
            max_count = count

def search_most_possible_subtarget(target, strings, extent=None, revision=None):
    # we just search the subtarget
    if extent is None:
        extent = ['subtarget']
    # get the database
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent, transpose=True, deduplicated=True, target=target)
    subtargets = []
    for ext in extent:
        subtargets += results[openwrt.header_last_selected.index(ext)]
    # let's start
    subtarget_searched = {}
    for string in strings:
        for subtarget in subtargets:
            if subtarget.startswith('?'):
                subtarget = subtarget[1:]
            if len(subtarget) > len(string) or len(subtarget) < 2 or subtarget == 'generic':
                continue
            if subtarget in string.split('_'):
                if subtarget not in subtarget_searched:
                    subtarget_searched[subtarget] = {'count': 0, 'strings': []}
                subtarget_searched[subtarget]['count'] += 1
                subtarget_searched[subtarget]['strings'].append(string.strip())
                break
    # find the most possible subtarget
    sum_of_occurrence = 0
    for k, v in subtarget_searched.items():
        sum_of_occurrence += v['count']
    if not sum_of_occurrence:
        # nothing, but we may filter the candidates
        results = openwrt.select('*', target=target)
        filtered_results = []
        for v in results:
            if v[openwrt.header_last_selected.index('supportedcurrentrel')] == '':
                continue
            filtered_results.append(v)
        # use kernel version to infer supportedcurrentrel
        # logger.debug('filter out candidates by matching kernel version')
        if revision is None:
            return
        filtered_results_2 = []
        for v in filtered_results:
            if revision == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
                filtered_results_2.append(v)
        if len(filtered_results_2) == 1:
            # logger.debug('only one left, choose it for you automatically')
            subtarget = filtered_results_2[0][openwrt.header_last_selected.index('subtarget')]
            if subtarget == '':
                subtarget = None
            # firmware.set_toh(filtered_results_2[0], header=openwrt.header_last_selected)
            return
    most_possible = None
    max_count = 0
    for k, v in subtarget_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        if count > max_count:
            most_possible = k
            max_count = count
    # firmware.set_subtarget(most_possible)


def search_most_possible_toh_record(strings, extent=None, revision=None):
    if extent is None:
        extent = ['*']
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent)
    table = PrettyTable(openwrt.header_last_selected)
    filterd_results = []
    for vs in results:
        possible = False
        for v in vs:
            for string in strings:
                if len(v) < len(string) or len(v) < 2 or v == 'generic':
                    continue
                if v.find(string) != -1:
                    filterd_results.append(vs)
                    table.add_row(vs)
                    possible = True
                    break
            if possible:
                break
    if len(filterd_results) == 0:
        # logger.info('nothing left {}'.format(LOG_SUFFIX))
        return

    # for line in table.__unicode__().split('\n'):
    #     logger.debug(line)

    # use kernel version to infer supportedcurrentrel
    # logger.debug('filter out candidates by matching kernel version {}'.format(LOG_SUFFIX))
    if revision is None:
        return
    filterd_results_2 = []
    for v in filterd_results:
        if revision == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
            filterd_results_2.append(v)
    if len(filterd_results_2) == 1:
        # logger.info('only one left, choose it automatically {}'.format(LOG_SUFFIX))
        # firmware.set_toh(filterd_results[0])
        return
    if len(filterd_results_2) == 0:
        # logger.info('nothing left {}'.format(LOG_SUFFIX))
        return


def parse_openwrt_url(url):
    """
    Example:
        http://archive.openwrt.org/chaos_calmer/15.05/ar71xx/generic/openwrt-15.05-ar71xx-generic-bxu2000n-2-a1-kernel.bin
                                                  ^     ^       ^
                                              revision      subtarget
                                                      target
        http://archive.openwrt.org/backfire/10.03/orion/openwrt-wrt350nv2-squashfs-recovery.bin
                                              ^     ^
                                            revision
                                                  target
    """
    homepage = os.path.dirname(url)

    items = homepage.split('/')
    revision = items[4]
    target = items[5]
    subtarget = None
    if len(items) == 7:
        subtarget = items[6]

    return revision, target, subtarget


def find_openwrt_revision(kernel_version):
    openwrt_mapping = get_database('openwrt.yaml')
    openwrt_revision = openwrt_mapping.select('revision', kernel_version=kernel_version)
    return openwrt_revision


def find_openwrt_toh(revision, target, subtarget):
    openwrt = get_database('openwrt')
    results = openwrt.select('*', supportedcurrentrel=revision, target=target, subtarget=subtarget)
    if len(results) == 1:
        toh = results[0]
        header = openwrt.header_last_selected
    else:
        toh = None
        header = None
    return toh


def find_machine_name_by_openwrt_toh(toh):
    machine_name = toh['model']
    machine_name = '_'.join(machine_name.split())
    machine_name = machine_name.lower()
    return machine_name


def find_cpu_by_openwrt_toh(toh):
    cpu = toh['packagearchitecture']
    soc = toh['cpu']
    if cpu is not None and cpu != '':
        # TODO map to cpu.arm32.yaml or cpu.mips.yaml
        return cpu


def find_ram_size_by_openwrt_toh(toh):
    ram = toh['rammb']
    if ram is not None and ram != '':
        return '{} * MiB'.format(ram)

