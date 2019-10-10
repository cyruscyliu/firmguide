import argparse
import os

import yaml
import logging.config

from analysis.cpu import get_cpu_model_info
from analysis.flash import get_flash_info
from analysis.ic import get_ic_info
from analysis.metadata import get_metadata
from analysis.extraction import extract_kernel_and_dtb
from analysis.ram import get_ram_info
from analysis.timer import get_timer_info
from analysis.uart import get_uart_info
from database.dbf import get_database
from manager import check_and_restore, save_analysis, setup


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


def run(args):
    if args.dbt is None:
        raise ValueError('no database available')
    dbi = get_database(args.dbt, profile=args.profile)
    for firmware in dbi.get_firmware():
        setup(args, firmware)
        check_and_restore(firmware)

        # let's start
        extract_kernel_and_dtb(firmware)
        get_metadata(firmware)
        # get_source_code(firmware)
        get_cpu_model_info(firmware)
        get_ram_info(firmware)
        get_flash_info(firmware)
        get_uart_info(firmware)
        get_ic_info(firmware)
        get_timer_info(firmware)
        save_analysis(firmware)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-dbt', required=True, choices=['text', 'firmadyne'], type=str,
                        help='assign the firmware db type')
    parser.add_argument('-d', '--debug', action='store_true', help='show verbose logs')
    parser.add_argument('-p', '--profile', choices=['simple', 'dt', 'ipxact'], default='dt',
                        help='assign the device profile standard')
    parser.add_argument('-wd', '--working_directory',
                        help='assign the working directory for getting metadata, '
                             'save and store mechanism is on except by default /tmp or %%TEMP%%')
    args = parser.parse_args()
    if args.debug:
        setup_logging(default_level=logging.DEBUG)
    else:
        setup_logging(default_level=logging.INFO)
    logger = logging.getLogger()
    run(args)
