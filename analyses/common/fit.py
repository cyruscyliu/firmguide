import re

import logging

logger = logging.getLogger()


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

