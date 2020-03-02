import os
import yaml
import shutil
import tempfile

from settings import *
from logger import logger_info, logger_debug
from slcore.profile.firmwaref import get_firmware


def restore_analysis(firmware):
    # handle analysis
    analysis = os.path.join(firmware.target_dir, 'analysis')
    if not os.path.exists(analysis) or firmware.rerun:
        with open(analysis, 'w') as f:
            f.close()

    with open(analysis, 'r') as f:
        analysis_progress = yaml.safe_load(f)
        if analysis_progress is None:
            firmware.analysis_progress = {}
        else:
            firmware.analysis_progress = analysis_progress


def save_analysis(firmware):
    analysis = os.path.join(firmware.target_dir, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)


def finished(firmware, analysis):
    if firmware.analysis_progress is None:
        return False

    try:
        status = firmware.analysis_progress[analysis.name]
        return True
    except KeyError:
        return False


def finish(firmware, analysis):
    if firmware.analysis_progress is None:
        return

    if analysis.type == 'diag':
        return

    if analysis.name not in firmware.analysis_progress:
        firmware.analysis_progress[analysis.name] = 1

def setup_target_dir(uuid):
    target_dir = os.path.join(WORKING_DIR, uuid)
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

def get_target_dir(uuid):
    target_dir = os.path.join(WORKING_DIR, uuid)
    return target_dir


def migrate(uuid, path_to_profile=None, components=None):
    firmware = get_firmware('simple')

    # two basics
    firmware.uuid = uuid
    firmware.target_dir = setup_target_dir(firmware.uuid)

    # load profile from path_to_profile
    if path_to_profile:
        firmware.set_profile(path_to_profile=path_to_profile)
        # change save-to-path to avoid modifing our well-defined profile
        firmware.path_to_profile = os.path.join(firmware.get_target_dir(), 'profile.yaml')
        logger_info(firmware.uuid, 'environment', 'migrate', 'migrate from {} to {}'.format(path_to_profile, firmware.get_target_dir()), 1)
    else:
        firmware.set_profile(target_dir=firmware.get_target_dir(), first=True)
        logger_info(firmware.uuid, 'environment', 'migrate', 'create new profile {}'.format(firmware.path_to_profile), 1)

    firmware.set_uuid(uuid)

    # handle components
    if components is not None:
        # copy the firmware to working path
        firmware.set_working_path(
            os.path.join(firmware.get_target_dir(), components.get_raw_name()))
        if not os.path.exists(firmware.working_path):
            shutil.copy(
                os.path.join(os.getcwd(), components.get_path_to_raw()),
                os.path.join(firmware.working_path)
        )
        firmware.set_components(components)

    return firmware


def snapshot(firmware):
    firmware.save_profile(working_dir=firmware.get_target_dir())
    logger_info(firmware.get_uuid(), 'environment', 'snapshot', 'profile at {}'.format(firmware.path_to_profile), 1)
    firmware.stats()
    logger_info(firmware.get_uuid(), 'environment', 'snapshot', 'statistics at {}'.format(firmware.path_to_summary), 1)
    return True


def archive(firmware):
    pass

