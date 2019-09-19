import argparse
import os
import yaml
import shutil
import tempfile
import logging.config

from analysis.metadata import get_metadata
from analysis.extraction import extract_kernel_and_dtb, get_kernel_and_dtb
from analysis.srcode import get_source_code
from database.dbf import get_database

progress = 0


def setup_logging(default_path="logging.yaml", default_level=logging.INFO, env_key="LOG_CFG"):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            logging.config.dictConfig(yaml.safe_load(f))
    else:
        logging.basicConfig(level=default_level)


def copy_to_tmp(firmware):
    global progress
    if firmware.relative:
        full_path = os.path.join(firmware.storage, firmware.path)
    else:
        full_path = firmware.path
    working_dir = tempfile.gettempdir()
    target_dir = os.path.join(working_dir, firmware.uuid)
    if not os.path.exists(target_dir):
        os.mkdir(os.path.join(working_dir, firmware.uuid))
    target_full_path = shutil.copy(full_path, target_dir)
    firmware.working_dir = target_dir
    firmware.working_path = target_full_path
    firmware.size = os.path.getsize(firmware.working_path)
    logger.info('[{}] firmware {} at {}'.format(progress, firmware.uuid, target_full_path))
    progress += 1


def run(args):
    if args.dbt is None:
        raise ValueError('no database available')
    dbi = get_database(args.dbt)
    count = dbi.get_count()
    if not count:
        return ValueError('no firmware available')
    if count > 100:
        raise NotImplementedError('multi threads not implemented yet')

    logger.info('there are {} firmware in the repo'.format(count))
    for firmware in dbi.get_firmware():
        if not args.s1:
            continue
        copy_to_tmp(firmware)
        extract_kernel_and_dtb(firmware)
        get_metadata(firmware)
        try:
            get_source_code(firmware)
        except ValueError as e:
            logging.warning(e)
            continue
        if not args.s2:
            continue
        get_kernel_and_dtb(firmware)
        if not args.s5:
            continue
        # infer_cpu(firmware)
        if not args.s6:
            continue
        # generate_cpu(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dbt', required=True, choices=['text'], type=str,
                        help='assign the firmware db type')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    parser.add_argument('-s1', action='store_true', help='s1: get metadata and source code')
    parser.add_argument('-s2', action='store_true', help='s2: extract kernel, dtb if any')
    parser.add_argument('-s5', action='store_true', help='s5: get all info for cpu')
    parser.add_argument('-s6', action='store_true', help='s6: implement cpu')
    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    logger = logging.getLogger()
    run(args)
