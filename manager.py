import logging.config
import os
import tempfile

import yaml
import shutil
import logging

logger = logging.getLogger()


def check_and_restore(firmware, **kwargs):
    """
    1. Check whether the wd exists or not, if not let first_time be true.
    2. For the first time,
        2.1 create the wd
        2.2 create an analysis file for analysis process
        2.3 create an empty device profile (one at once)
        2.4 copy firmware to the wd
    3. To restore a previous task,
        3.1 load the analysis file
        3.2 load the device profile (one at once)

    :param firmware: the firmware.
    :return: None
    """
    first_time = True
    if os.path.exists(firmware.working_dir):
        first_time = False
    rerun = kwargs.pop('rerun', False)
    if rerun:
        first_time = True
    analysis = os.path.join(firmware.working_dir, 'analysis')
    if first_time:
        os.makedirs(firmware.working_dir, exist_ok=True)
        with open(analysis, 'w') as f:
            f.close()
        firmware.set_profile(working_dir=firmware.working_dir, first=True)
    with open(analysis, 'r') as f:
        analysis_progress = yaml.safe_load(f)
        if analysis_progress is None:
            firmware.analysis_progress = {}
        else:
            firmware.analysis_progress = analysis_progress
    firmware.set_profile(working_dir=firmware.working_dir)
    firmware.handle_preset()
    if not os.path.exists(firmware.working_path):
        shutil.copy(
            os.path.join(os.getcwd(), firmware.path),
            os.path.join(firmware.working_path)
        )

    if first_time:
        logger.info('[{}] for the first time, {}'.format(firmware.id, firmware.brief()))
    else:
        logger.info('[{}] restore the analysis, {}'.format(firmware.id, firmware.brief()))


def save_analysis(firmware):
    analysis = os.path.join(firmware.working_dir, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)
    firmware.save_profile(working_dir=firmware.working_dir)
    logger.info('[{}] saved the analysis'.format(firmware.id))


def finished(firmware, task, func):
    try:
        status = firmware.analysis_progress[task][func]
        logger.info('\033[34m{}_{} done before\033[0m'.format(task, func))
        return True
    except KeyError:
        return False


def finish(firmware, task, func):
    if task not in firmware.analysis_progress:
        firmware.analysis_progress[task] = {}
    firmware.analysis_progress[task][func] = 1


def setup(args, firmware):
    # set the working directory but not actually create the dir or copy the file
    if args.working_directory is None:
        working_dir = tempfile.gettempdir()
    else:
        working_dir = os.path.realpath(args.working_directory)
    target_dir = os.path.join(working_dir, firmware.uuid)
    target_path = os.path.join(working_dir, firmware.uuid, firmware.name)
    firmware.set_working_env(target_dir, target_path)


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
