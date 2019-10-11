"""
Handle all about source code.
"""
import os
import yaml
import logging

from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'let\'s get its source code'


def get_source_code(firmware):
    if finished(firmware, 'get_source_code', 'by_default'):
        return
    brand = firmware.get_brand()
    if brand == 'openwrt':
        if firmware.homepage is None:
            target = firmware.get_target()
            subtarget = firmware.get_subtarget()

            with open(os.path.join(os.getcwd(), 'database', 'openwrt.yaml')) as f:
                openwrt_release_info = yaml.safe_load(f)
            try:
                url = openwrt_release_info[firmware.get_revision()]['url']
                possible_package = os.path.join(url, target, subtarget)
                logger.info(
                    '\033[32mdownload page found for OpenWrt project {}\033[0m'.format(
                        possible_package))
            except NotImplementedError:
                logger.info('no available url for this version {}'.format(firmware.get('revision')))
                return
    finish(firmware, 'get_source_code', 'by_default')
