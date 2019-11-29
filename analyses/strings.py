import re
import os
import yaml

from prettytable import PrettyTable
from analyses.common.analysis import Analysis
from database.dbf import get_database
from supervisor.logging_setup import logger_info


def get_strings(firmware):
    """
    We get strings from uncompressed binary.

    :param firmware:
    :return: [strings] or None
    """
    strings = []
    # get candidate files which contain useful strings
    candidates = get_candidates(firmware)
    if candidates is None:
        return None
    for candidate in candidates:
        info = os.popen('strings {} -n 2 | grep -E "^[a-zA-Z]+[a-zA-Z0-9_-]{{1,20}}"'.format(candidate))
        strings += info.readlines()
    return strings


def get_candidates(firmware):
    """
    We can find useful strings in uncompressed binary.

    :param firmware: the firmware.
    :return: [paths/to/candidates] or None
    """
    kernel = firmware.get_path_to_kernel()
    if kernel is None:
        return None
    working_dir = os.path.dirname(kernel)
    candidates = [kernel]
    for file_ in os.listdir(working_dir):
        if file_.endswith('7z') or file_.endswith('xz'):
            zimage = os.path.join(working_dir, file_[:-3])
            if os.path.exists(zimage):
                candidates.append(zimage)
    return candidates


class Strings(Analysis):
    def get_all_strings(self, firmware):
        self.strings = get_strings(firmware)

    def get_toh_by_strings(self, firmware):
        search_most_possible_toh_record(firmware, self.strings)

    def run(self, firmware):
        self.get_all_strings(firmware)

        if self.strings is None:
            self.context['input'] = 'no strings at all'
            return False
        # kernel version is very critical
        for string in self.strings:
            string = string.strip()
            if len(string) < 20:
                continue
            r = re.search(r'[lL]inux version ([1-5]+\.\d+\.\d+).*', string)
            if r is not None:
                kernel_version = r.groups()[0]
                firmware.set_kernel_version(kernel_version)
                self.info(firmware, 'get the kernel version: {}'.format(kernel_version), 1)
                break
        # TODO: refactor the following 2 methods
        # search_most_possible_target(firmware, strings)
        # search_most_possible_subtarget(firmware, strings)
        # uart
        for string in self.strings:
            if string.find('8250') != -1 or string.find('16550') != -1:
                firmware.set_uart_model('ns16550A')
                self.info(firmware, 'uart model {} found'.format('ns16550A'), 1)
                break
            else:
                pass
        for string in self.strings:
            if string.find('root=') != -1:
                # root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200\n
                a, _, b = string.partition('console=')
                if _ is '':
                    continue
                else:
                    uart_baud = b.split(',')[1].strip()
                    firmware.set_uart_baud(uart_baud)
                    self.info(firmware, 'uart baud {} found'.format(uart_baud), 1)
                    break
        # ic
        for string in self.strings:
            if string.find('ic') != -1:
                break
        # cpu
        architecture = firmware.get_architecture()
        if architecture != 'arm':
            self.context['input'] = 'search strings to find CPU only valid for ARM'
            return False
        candidates = yaml.safe_load(open(os.path.join(os.getcwd(), 'database', 'arm32.cpu.yaml')))
        # construct
        target_strings = {}
        votes = {}
        for k, cpus in candidates.items():
            target_strings[k] = []
            votes[k] = 0
            for cpu in cpus:
                target_strings[k].append(cpu['cpu_arch_name'])
                target_strings[k].append(cpu['cpu_name'])
            target_strings[k] = list(set(target_strings[k]))
        for string in self.strings:
            string = string.strip()
            for k, v in target_strings.items():
                if string in v:
                    votes[k] += 1
        vote = 0
        model = ''
        for k, v in votes.items():
            if v > vote:
                vote = v
                model = k
        self.info(firmware, 'get cpu model: {}'.format(candidates[model]), 1)
        for cpu in candidates[model]:
            path_to_cpu = firmware.find_cpu_nodes(new=True)
            for k, v in cpu.items():
                firmware.set_node_property(path_to_cpu, k, v)
        return True

    def __init__(self):
        super().__init__()
        self.name = 'strings'
        self.description = 'handle strings'
        self.required = ['extraction', 'revision']
        self.context['hint'] = 'lack of strings'
        self.critical = False
        #
        self.strings = []


def search_most_possible_toh_record(firmware, strings, extent=None):
    LOG_SUFFIX = '[STRINGS for ToH]'
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
    if firmware.get_revision() is None:
        return
    filterd_results_2 = []
    for v in filterd_results:
        if firmware.get_revision() == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
            filterd_results_2.append(v)
    if len(filterd_results_2) == 1:
        # logger.info('only one left, choose it automatically {}'.format(LOG_SUFFIX))
        firmware.set_toh(filterd_results[0])
        return
    if len(filterd_results_2) == 0:
        # logger.info('nothing left {}'.format(LOG_SUFFIX))
        return


def search_most_possible_subtarget(firmware, strings, extent=None):
    if firmware.get_target() is None:
        return
    LOG_SUFFIX = '[STRINGS for SUBTARGET]'
    if extent is None:
        extent = ['subtarget']
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent, transpose=True, deduplicated=True, target=firmware.get_target())
    subtargets = []
    for ext in extent:
        subtargets += results[openwrt.header.index(ext)]
    subtarget_searched = {}
    for string in strings:
        for subtarget in subtargets:
            if subtarget.startswith('?'):
                subtarget = subtarget[1:]
            if len(subtarget) > len(string) or len(subtarget) < 2 or subtarget == 'generic':
                continue
            if string.find(subtarget) != -1:
                if subtarget not in subtarget_searched:
                    subtarget_searched[subtarget] = {'count': 0, 'strings': []}
                subtarget_searched[subtarget]['count'] += 1
                subtarget_searched[subtarget]['strings'].append(string.strip())
                break
    sum_of_occurrence = 0
    for k, v in subtarget_searched.items():
        sum_of_occurrence += v['count']
    if not sum_of_occurrence:
        # logger.info('get nothing, however here are some options {}'.format(LOG_SUFFIX))
        results = openwrt.select('*', target=firmware.get_target())
        table = PrettyTable(openwrt.header_last_selected)
        filterd_results = []
        for v in results:
            table.add_row(v)
            if v[openwrt.header_last_selected.index('supportedcurrentrel')] == '':
                continue
            filterd_results.append(v)
        # for line in table.__unicode__().split('\n'):
        #     logger.info(line)
        # logger.debug('filter out candidates by empty supportedcurrentrel')
        # if len(filterd_results) == 1:
        #     logger.info('only one left, choose it automatically')
        #     firmware.most_possible_subtarget = filterd_results[0][openwrt.header_last_selected.index('subtarget')]
        #     firmware.openwrt = filterd_results[0]
        #     logger.info('\033[32mget the most possible subtarget {}\033[0m'.format(firmware.most_possible_subtarget))
        #     return

        # use kernel version to infer supportedcurrentrel
        # logger.debug('filter out candidates by matching kernel version')
        if firmware.get_revision() is None:
            return

        filterd_results_2 = []
        for v in filterd_results:
            if firmware.get_revision() == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
                filterd_results_2.append(v)
        if len(filterd_results_2) == 1:
            # logger.debug('only one left, choose it for you automatically')
            # firmware.set('subtarget', value=filterd_results_2[0][openwrt.header_last_selected.index('subtarget')])
            firmware.set_toh(filterd_results_2[0], header=openwrt.header_last_selected)
            # logger.info('\033[32mget the most possible subtarget {}\033[0m {}'.format(
            #     firmware.get_subtarget(), LOG_SUFFIX))
            return
        if firmware.get_subtarget() is None:
            tries = 2
            # logger.info('please input the pid of what you choose: ')
            while tries:
                pid = input()
                result = openwrt.select('*', pid=pid)
                if not len(result):
                    # logger.info('one more time')
                    tries -= 1
                    continue
                firmware.set_toh(result[0])
                # logger.info('\033[32mcorrect the most possible target {}\033[0m'.format(
                #     firmware.get_target(), LOG_SUFFIX))
                # logger.info('\033[32mcorrect the most possible subtarget {}\033[0m'.format(
                #     firmware.get_subtarget(), LOG_SUFFIX))
                table = PrettyTable(openwrt.header_last_selected)
                table.add_row(result[0])
                # for line in table.__unicode__().split('\n'):
                #     logger.info(line)
                return
    most_possible = None
    max_count = 0
    for k, v in subtarget_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        # logger.debug('>> {}, confidence: {:.2f}, {}'.format(k, confidence, v['strings']))
        if count > max_count:
            most_possible = k
            max_count = count
    logger_info(firmware.uuid, 'analysis', 'strings', 'get the most possible subtarget {}'.format(most_possible), 1)
    firmware.set_subtarget(most_possible)


def search_most_possible_target(firmware, strings, extent=None):
    LOG_SUFFIX = '[STRINGS for TARGET]'
    if extent is None:
        extent = ['target']
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent, deduplicated=True)
    targets = []
    for ext in extent:
        targets += results[openwrt.header.index(ext)]
    target_searched = {}
    for string in strings:
        for target in targets:
            if target.startswith('?'):
                target = target[1:]
            if len(target) > len(string) or len(target) < 2:
                continue
            if string.find(target) != -1:
                if target not in target_searched:
                    target_searched[target] = {'count': 0, 'strings': []}
                target_searched[target]['count'] += 1
                target_searched[target]['strings'].append(string.strip())
                break
    sum_of_occurrence = 0
    for k, v in target_searched.items():
        sum_of_occurrence += v['count']
    most_possible = None
    max_count = 0
    for k, v in target_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        # logger.debug('>> {}, confidence: {:.2f}, {}'.format(k, confidence, v['strings']))
        if count > max_count:
            most_possible = k
            max_count = count
    logger_info(firmware.uuid, 'analysis', 'strings', 'get the most possible target {}'.format(most_possible), 1)
    firmware.set_target(most_possible)
