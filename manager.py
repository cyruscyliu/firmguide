import os
import yaml
import shutil
import logging

logger = logging.getLogger()


def check_and_restore_analysis(firmware):
    first_time = True
    if os.path.exists(firmware.working_dir):
        first_time = False
    analysis = os.path.join(firmware.working_dir, 'analysis')
    if first_time:
        os.mkdir(firmware.working_dir)
        with open(analysis, 'w') as f:
            f.close()
    with open(analysis, 'r') as f:
        analysis_progress = yaml.safe_load(f)
        if analysis_progress is None:
            firmware.analysis_progress = {}
        else:
            firmware.analysis_progress = analysis_progress
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
