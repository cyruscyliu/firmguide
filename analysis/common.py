import os

import yaml
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
    logger.info('search possible openwrt toh record(s) by strings')
    if extent is None:
        extent = ['*']
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent, row=True)
    table = PrettyTable(openwrt.header_last_selected)
    filterd_results = []
    for k, vs in results.items():
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
        logger.info('nothing left')
        return
    
    for line in table.__unicode__().split('\n'):
        logger.info(line)

    # use kernel version to infer supportedcurrentrel
    logger.info('filter out candidates by matching kernel version')
    if firmware.openwrt_revision is None:
        return
    filterd_results_2 = []
    for v in filterd_results:
        if firmware.openwrt_revision == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
            filterd_results_2.append(v)
    if len(filterd_results_2) == 1:
        logger.info('only one left, choose it automatically')
        firmware.openwrt = filterd_results[0]
        firmware.most_possible_target = filterd_results[0][openwrt.header_last_selected.index('target')]
        firmware.most_possible_subtarget = filterd_results[0][openwrt.header_last_selected.index('subtarget')]
        logger.info('\033[32mget the most possible target {}\033[0m'.format(firmware.most_possible_target))
        logger.info('\033[32mget the most possible subtarget {}\033[0m'.format(firmware.most_possible_subtarget))
        return
    if len(filterd_results_2) == 0:
        logger.info('nothing left')
        return


def search_most_possible_subtarget(firmware, strings, extent=None):
    if firmware.most_possible_target is None:
        return

    if extent is None:
        extent = ['subtarget']
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent, deduplicated=True, target=firmware.most_possible_target)
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
    logger.info('search possible subtarget(s) by strings')
    sum_of_occurrence = 0
    for k, v in subtarget_searched.items():
        sum_of_occurrence += v['count']
    if not sum_of_occurrence:
        logger.info('get nothing, however here are some options')
        results = openwrt.select('*', target=firmware.most_possible_target, row=True)
        table = PrettyTable(openwrt.header_last_selected)
        filterd_results = []
        for k, v in results.items():
            table.add_row(v)
            if v[openwrt.header_last_selected.index('supportedcurrentrel')] == '':
                continue
            filterd_results.append(v)
        for line in table.__unicode__().split('\n'):
            logger.info(line)
        logger.info('filter out candidates by empty supportedcurrentrel')
        if len(filterd_results) == 1:
            logger.info('only one left, choose it automatically')
            firmware.most_possible_subtarget = filterd_results[0][openwrt.header_last_selected.index('subtarget')]
            firmware.openwrt = filterd_results[0]
            logger.info('\033[32mget the most possible subtarget {}\033[0m'.format(firmware.most_possible_subtarget))
            return

        # use kernel version to infer supportedcurrentrel
        logger.info('filter out candidates by matching kernel version')
        if firmware.openwrt_revision is None:
            return

        filterd_results_2 = []
        for v in filterd_results:
            if firmware.openwrt_revision == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
                filterd_results_2.append(v)
        if len(filterd_results_2) == 1:
            logger.info('only one left, choose it for you automatically')
            firmware.most_possible_subtarget = filterd_results_2[0][openwrt.header_last_selected.index('subtarget')]
            firmware.openwrt = filterd_results_2[0]
            logger.info('\033[32mget the most possible subtarget {}\033[0m'.format(firmware.most_possible_subtarget))
            return
        # if firmware.most_possible_subtarget is None:
        #     tries = 2
        #     logger.info('please input the pid of what you choose: ')
        #     while tries:
        #         pid = input('please input the pid of what you choose: ')
        #         result = openwrt.select('*', pid=pid, row=True)
        #         if not len(result):
        #             logger.info('one more time')
        #             tries -= 1
        #             continue
        #         firmware.most_possible_subtarget = result[pid][openwrt.header_last_selected.index('subtarget')]
        #         firmware.openwrt = result[pid]
        #         break
    most_possible = None
    max_count = 0
    for k, v in subtarget_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        logger.info('>> {}, confidence: {:.2f}, {}'.format(k, confidence, v['strings']))
        if count > max_count:
            most_possible = k
            max_count = count
        firmware.metadata['possible_subtargets'].append({'value': k, 'confidence': confidence})
    logger.info('\033[32mget the most possible subtarget {}\033[0m'.format(most_possible))
    firmware.most_possible_subtarget = most_possible
    openwrt.table.close()


def search_most_possible_target(firmware, strings, extent=None):
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
    logger.info('search possible target(s) by strings')
    sum_of_occurrence = 0
    for k, v in target_searched.items():
        sum_of_occurrence += v['count']
    most_possible = None
    max_count = 0
    for k, v in target_searched.items():
        count = v['count']
        confidence = round(count / sum_of_occurrence, 2)
        logger.info('>> {}, confidence: {:.2f}, {}'.format(k, confidence, v['strings']))
        if count > max_count:
            most_possible = k
            max_count = count
        firmware.metadata['possible_targets'].append({'value': k, 'confidence': confidence})
    logger.info('\033[32mget the most possible target {}\033[0m'.format(most_possible))
    firmware.most_possible_target = most_possible
    openwrt.table.close()
