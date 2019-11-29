import os
import tempfile
import yaml
import shutil

from supervisor.logging_setup import logger_info


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
    rerun = firmware.rerun
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
        logger_info(firmware.uuid, 'save_and_restore', 'first', firmware.brief(), 0)
    else:
        logger_info(firmware.uuid, 'save_and_restore', 'restore', firmware.brief(), 0)


def save_analysis(firmware):
    analysis = os.path.join(firmware.working_dir, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)
    firmware.save_profile(working_dir=firmware.working_dir)
    logger_info(firmware.uuid, 'save_and_restore', 'save', firmware.summary(), 0)


def finished(firmware, analysis):
    try:
        status = firmware.analysis_progress[analysis.name]
        return True
    except KeyError:
        return False


def finish(firmware, analysis):
    if analysis.name not in firmware.analysis_progress:
        firmware.analysis_progress[analysis.name] = 1


def setup(args, firmware):
    # set the working directory but not actually create the dir or copy the file
    if args.working_directory is None:
        working_dir = tempfile.gettempdir()
    else:
        working_dir = os.path.realpath(args.working_directory)
    target_dir = os.path.join(working_dir, firmware.uuid)
    target_path = os.path.join(working_dir, firmware.uuid, firmware.name)
    firmware.set_working_env(target_dir, target_path)
    # set the trace format
    firmware.trace_format = args.trace_format
    firmware.do_not_diagnosis = args.quick
    # set the rerun control
    firmware.rerun = args.rerun
