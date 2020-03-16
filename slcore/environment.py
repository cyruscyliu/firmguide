import os
import yaml
import shutil

from settings import WORKING_DIR
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


def setup_target_dir(uuid):
    target_dir = os.path.join(WORKING_DIR, uuid)
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

def get_target_dir(uuid):
    target_dir = os.path.join(WORKING_DIR, uuid)
    return target_dir

