import os
import re
import shutil
import tempfile

import logging
from prettytable import PrettyTable
from database.dbf import get_database

logger = logging.getLogger()


def vote(to_be_voted, comments):
    """
    to_be_voted = [
        {"value": value1, "confidence": confidence1},
        {"value": value2, "confidence": confidence2},
        {"value": value3, "confidence": confidence3},
    ]
    Same confidence should has same value, or expertise is needed.
    """
    highest = {'value': None, 'confidence': 0, 'count': 0}
    if len(to_be_voted) == 0:
        raise ValueError('has not found any information on {}'.format(comments))
    elif len(to_be_voted) == 1:
        return to_be_voted[0]['value']
    else:
        for vote in to_be_voted:
            if vote['confidence'] > highest['confidence']:
                highest = {'value': vote['value'], 'confidence': vote['confidence'], 'count': 0}
            elif vote['confidence'] == highest['confidence']:
                if highest['count'] == 0:
                    highest['value'] = vote['value']
                    highest['confidence'] = vote['confidence']
                else:
                    if highest['value'] != vote['value']:
                        raise ValueError('bad votes: {}'.format(to_be_voted))
                highest['count'] += 1
            else:
                pass
    return highest['value']


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
        logger.info('nothing left {}'.format(LOG_SUFFIX))
        return

    for line in table.__unicode__().split('\n'):
        logger.debug(line)

    # use kernel version to infer supportedcurrentrel
    logger.debug('filter out candidates by matching kernel version {}'.format(LOG_SUFFIX))
    if firmware.get_revision() is None:
        return
    filterd_results_2 = []
    for v in filterd_results:
        if firmware.get_revision() == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
            filterd_results_2.append(v)
    if len(filterd_results_2) == 1:
        logger.info('only one left, choose it automatically {}'.format(LOG_SUFFIX))
        firmware.set_toh(filterd_results[0])
        return
    if len(filterd_results_2) == 0:
        logger.info('nothing left {}'.format(LOG_SUFFIX))
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
        logger.info('get nothing, however here are some options {}'.format(LOG_SUFFIX))
        results = openwrt.select('*', target=firmware.get_target())
        table = PrettyTable(openwrt.header_last_selected)
        filterd_results = []
        for v in results:
            table.add_row(v)
            if v[openwrt.header_last_selected.index('supportedcurrentrel')] == '':
                continue
            filterd_results.append(v)
        for line in table.__unicode__().split('\n'):
            logger.info(line)
        logger.debug('filter out candidates by empty supportedcurrentrel')
        # if len(filterd_results) == 1:
        #     logger.info('only one left, choose it automatically')
        #     firmware.most_possible_subtarget = filterd_results[0][openwrt.header_last_selected.index('subtarget')]
        #     firmware.openwrt = filterd_results[0]
        #     logger.info('\033[32mget the most possible subtarget {}\033[0m'.format(firmware.most_possible_subtarget))
        #     return

        # use kernel version to infer supportedcurrentrel
        logger.debug('filter out candidates by matching kernel version')
        if firmware.get_revision() is None:
            return

        filterd_results_2 = []
        for v in filterd_results:
            if firmware.get_revision() == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
                filterd_results_2.append(v)
        if len(filterd_results_2) == 1:
            logger.debug('only one left, choose it for you automatically')
            # firmware.set('subtarget', value=filterd_results_2[0][openwrt.header_last_selected.index('subtarget')])
            firmware.set_toh(filterd_results_2[0], header=openwrt.header_last_selected)
            logger.info('\033[32mget the most possible subtarget {}\033[0m {}'.format(
                firmware.get_subtarget(), LOG_SUFFIX))
            return
        if firmware.get_subtarget() is None:
            tries = 2
            logger.info('please input the pid of what you choose: ')
            while tries:
                pid = input()
                result = openwrt.select('*', pid=pid)
                if not len(result):
                    logger.info('one more time')
                    tries -= 1
                    continue
                firmware.set_toh(result[0])
                logger.info('\033[32mcorrect the most possible target {}\033[0m'.format(
                    firmware.get_target(), LOG_SUFFIX))
                logger.info('\033[32mcorrect the most possible subtarget {}\033[0m'.format(
                    firmware.get_subtarget(), LOG_SUFFIX))
                table = PrettyTable(openwrt.header_last_selected)
                table.add_row(result[0])
                for line in table.__unicode__().split('\n'):
                    logger.info(line)
                return
    most_possible = None
    max_count = 0
    for k, v in subtarget_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        logger.debug('>> {}, confidence: {:.2f}, {}'.format(k, confidence, v['strings']))
        if count > max_count:
            most_possible = k
            max_count = count
    logger.info('\033[32mget the most possible subtarget {}\033[0m {}'.format(most_possible, LOG_SUFFIX))
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
        logger.debug('>> {}, confidence: {:.2f}, {}'.format(k, confidence, v['strings']))
        if count > max_count:
            most_possible = k
            max_count = count
    logger.info('\033[32mget the most possible target {}\033[0m {}'.format(most_possible, LOG_SUFFIX))
    firmware.set_target(most_possible)


def search_most_possible_kernel_version(firmware, strings):
    for string in strings:
        string = string.strip()
        if len(string) < 20:
            continue
        if not string.startswith('Linux'):
            continue
        r = re.search(r'[lL]inux version ([1-5]+\.\d+\.\d+).*', string)
        if r is not None:
            kernel_version = r.groups()[0]
            firmware.set_kernel_version(kernel_version)


progress = 0


def copy_to_tmp(firmware):
    global progress
    full_path = os.path.join(os.getcwd(), firmware.path)
    working_dir = tempfile.gettempdir()
    target_dir = os.path.join(working_dir, firmware.uuid)
    if not os.path.exists(target_dir):
        os.mkdir(os.path.join(working_dir, firmware.uuid))
    target_path = shutil.copy(full_path, target_dir)
    firmware.set_working_env(target_dir, target_path)
    logger.info('[{}] firmware {} at {}'.format(progress, firmware.uuid, target_path))
    progress += 1


def fit_parser(dumpimage_lines):
    fit = {
        'properties': {
            'timestamp': None
        }, 'images': {
        }, 'configurations': {
            'default configuration': None,
        }
    }
    level = 0
    image_node = ''
    conf_node = ''
    config = False
    for line in dumpimage_lines:
        if not len(line):
            continue
        if line.startswith('  '):
            level = 2
        elif line.startswith(' '):
            level = 1
        else:
            pass
        items = line.strip().split(': ')
        if level == 0 and line.startswith('FIT description'):
            fit['properties']['description'] = items[1].strip()
        elif level == 0 and line.startswith('Created'):
            # fit['properties']['timestamp'] = time.strptime(items[1].strip(), "%a %b %d %H:%M:%S %Y")
            fit['properties']['timestamp'] = items[1].strip()
        elif level == 1 and line.startswith(' Image'):
            assert len(items) == 1
            image_node = line.strip().split('(')[1].split(')')[0]
            if image_node not in fit['images']:
                fit['images'][image_node] = {'properties': {}, 'hash': {}}
        elif level == 2 and line.startswith('  Description'):
            fit['images'][image_node]['properties']['description'] = items[1].strip()
        elif level == 2 and line.startswith('  Created'):
            fit['images'][image_node]['properties']['timestamp'] = items[1].strip()
            # time.strptime(items[1].strip(), "%a %b %d %H:%M:%S %Y")
        elif level == 2 and line.startswith('  Type'):
            fit['images'][image_node]['properties']['type'] = items[1].strip()
        elif level == 2 and line.startswith('  Compression'):
            fit['images'][image_node]['properties']['compression'] = items[1].strip()
        elif level == 2 and line.startswith('  Architecture'):
            fit['images'][image_node]['properties']['arch'] = items[1].strip()
        elif level == 2 and line.startswith('  OS'):
            fit['images'][image_node]['properties']['os'] = items[1].strip()
        elif level == 2 and line.startswith('  Load Address'):
            fit['images'][image_node]['properties']['load address'] = items[1].strip()
        elif level == 2 and line.startswith('  entry point'):
            fit['images'][image_node]['properties']['entry point'] = items[1].strip()
        elif level == 1 and line.startswith(' Default Configuration'):
            fit['configurations']['default configuration'] = items[1].strip('\'')
        elif level == 1 and line.startswith(' Configuration'):
            assert len(items) == 1
            conf_node = line.strip().split('(')[1].split(')')[0]
            if conf_node not in fit['configurations']:
                fit['configurations'][conf_node] = {}
            config = True
        elif level == 2 and config and line.startswith('  Kernel'):
            fit['configurations'][conf_node]['kernel'] = items[1].strip()
        elif level == 2 and config and line.startswith('  FDT'):
            fit['configurations'][conf_node]['fdt'] = items[1].strip()
        else:
            logging.debug('not support line {}'.format(dumpimage_lines))
    return fit


def description_parser(firmware, description):
    kernel_version = re.search(r'Linux-(\d+\.\d+\.\d+)', description)
    if kernel_version:
        kernel_version = kernel_version.groups()[0]
        firmware.set_kernel_version(kernel_version)
