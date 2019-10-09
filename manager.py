import os
import yaml
import shutil
import logging

logger = logging.getLogger()


def check_and_restore_analysis(firmware):
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
    analysis = os.path.join(firmware.working_dir, 'analysis')
    if first_time:
        os.mkdir(firmware.working_dir)
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
    if not os.path.exists(firmware.working_path):
        shutil.copy(
            os.path.join(os.getcwd(), firmware.path),
            os.path.join(firmware.working_path)
        )


def save_analysis(firmware):
    analysis = os.path.join(firmware.working_dir, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)


def finished(firmware, task, func):
    try:
        status = firmware.analysis_progress[task][func]
        logger.info('{}_{} done before'.format(task, func))
        return True
    except KeyError:
        return False


def finish(firmware, task, func):
    if task not in firmware.analysis_progress:
        firmware.analysis_progress[task] = {}
    firmware.analysis_progress[task][func] = 1
