import argparse
import os
import yaml
import shutil
import tempfile
import logging.config

from analysis.cpu import get_cpu_model_info, check_qemu_support_for_cpu, make_cpu
from analysis.flash import get_flash_info, make_flash, check_qemu_support_for_flash
from analysis.ic import get_ic_info, check_qemu_support_for_ic
from analysis.metadata import get_metadata
from analysis.extraction import extract_kernel_and_dtb, get_kernel_and_dtb
from analysis.ram import get_ram_info, make_ram
from analysis.srcode import get_source_code
from analysis.uart import get_uart_info, check_qemu_support_for_uart
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
        if not args.s3:
            continue
        get_cpu_model_info(firmware)
        check_qemu_support_for_cpu(firmware)
        if not args.s6:
            continue
        get_ram_info(firmware)
        if not args.s7:
            continue
        get_flash_info(firmware)
        check_qemu_support_for_flash(firmware)
        if not args.s9:
            continue
        get_uart_info(firmware)
        check_qemu_support_for_uart(firmware)
        if not args.s11:
            continue
        get_ic_info(firmware)
        check_qemu_support_for_ic(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dbt', required=True, choices=['text'], type=str,
                        help='assign the firmware db type')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    parser.add_argument('-s1', action='store_true', help='s1: get metadata and source code')
    parser.add_argument('-s2', action='store_true', help='s2: extract kernel, dtb if any')
    parser.add_argument('-s3', action='store_true', help='s3: get all info for cpu')
    parser.add_argument('-s6', action='store_true', help='s6: get all info for ram')
    parser.add_argument('-s7', action='store_true', help='s7: get all info for flash')
    parser.add_argument('-s9', action='store_true', help='s9: get all info for uart')
    parser.add_argument('-s11', action='store_true', help='s11: get all info for ic')
    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    logger = logging.getLogger()
    run(args)
