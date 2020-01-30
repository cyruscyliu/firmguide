import os
import yaml
import shutil
import tempfile

from logger import logger_info, logger_debug
from settings import *
from profile.firmwaref import get_firmware


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

    logger_info(firmware.get_uuid(), 'environment', 'restore_analysis', firmware.brief(), 0)


def save_analysis(firmware):
    analysis = os.path.join(firmware.target_dir, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)

    logger_info(firmware.get_uuid(), 'environment', 'save_analysis', firmware.summary(), 0)


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
    logger_info(uuid, 'environment', 'tdir', 'process in {}'.format(target_dir), 1)
    return target_dir

def migrate(components, path_to_profile, quick=False, trace_format='qemudebug', max_=20):
    firmware = get_firmware('simple')

    # two basics
    firmware.uuid = components.uuid
    firmware.target_dir = setup_target_dir(firmware.uuid)

    # load profile from path_to_profile
    if path_to_profile:
        firmware.set_profile(path_to_profile=path_to_profile)
        # change save-to-path to avoid modifing our well-defined profile
        firmware.path_to_profile = os.path.join(firmware.get_target_dir(), 'profile.yaml')
        logger_info(firmware.get_uuid(), 'environment', 'migrate', 'migrate from {} to {}'.format(path_to_profile, firmware.get_target_dir()), 1)
    else:
        firmware.set_profile(target_dir=firmware.get_target_dir(), first=True)
        logger_info(firmware.get_uuid(), 'environment', 'migrate', 'create new profile {}'.format(path_to_profile), 1)

    firmware.set_uuid(components.uuid)
    firmware.set_name(components.get_image_name())
    firmware.set_path(components.get_path())
    firmware.set_working_path(components.get_path())
    firmware.set_components(components)
    firmware.set_architecture(components.arch)
    firmware.set_endian(components.endian)

    firmware.trace_format = trace_format
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_architecture(), firmware.get_endian())
    firmware.do_not_diagnosis = quick
    firmware.max_iteration = max_

    # copy the firmware to working path
    if not os.path.exists(firmware.working_path):
        shutil.copy(
            os.path.join(os.getcwd(), firmware.get_path()),
            os.path.join(firmware.working_path))
    return firmware


def snapshot(firmware):
    firmware.save_profile(working_dir=firmware.get_target_dir())
    logger_info(firmware.get_uuid(), 'environment', 'snapshot', 'profile at {}'.format(firmware.path_to_profile), 1)
    firmware.stats()
    logger_info(firmware.get_uuid(), 'environment', 'snapshot', 'statistics at {}'.format(firmware.path_to_summary), 1)
    return True


def setup_working_directory(args, firmware):
    # prepare working directory
    if args.working_dir is None:
        working_dir = tempfile.gettempdir()
    else:
        working_dir = os.path.realpath(args.working_dir)
    firmware.set_working_dir(working_dir)
    os.makedirs(firmware.get_working_dir(), exist_ok=True)


def setup_tmp_profile(firmware, label):
    # get a empty profile
    firmware.path_to_profile = os.path.join(tempfile.gettempdir(), '{}.yaml'.format(label))
    firmware.create_empty_profile()
    firmware.load_from_profile()


def setup_diagnosis(args, firmware):
    # a profile is need to simplify implementation
    # but we only need a temp one, no need for uuid
    setup_tmp_profile(firmware, 'diagnosis')

    # 1 we need the trace
    firmware.path_to_trace = args.trace
    firmware.trace_format = args.trace_format

    name = args.trace.split('.')[0]
    # 2 and the uuid, we set it if any
    uuid = name.split('-')[0]
    firmware.uuid = uuid
    firmware.set_uuid(uuid)

    # 3 uuid.arch.endian.trace
    architecture = name.split('-')[1]
    assert architecture in ['arm', 'mips'], 'cannot support this architecture {}'.format(architecture)
    firmware.set_architecture(architecture)
    endian = name.split('-')[2]
    assert endian in ['l', 'b'], 'cannot support this endianness {}'.format(endian)
    firmware.set_endian(endian)

    firmware.max_iteration = args.max


def setup_code_generation(args, firmware):
    setup_working_directory(args, firmware)

    # load profile from args.generation
    # we can known its uuid
    firmware.set_profile(path_to_profile=args.generation)
    firmware.uuid = firmware.get_uuid()

    # then setup its target dir
    firmware.setup_target_directory()
    firmware.setup_working_path()

    # we have loaded the profile, to
    # avoid modify our well-defined profile, change save to path
    extension = 'yaml' if args.profile == 'simple' else 'dt'
    firmware.path_to_profile = os.path.join(firmware.get_target_dir(), 'profile.' + extension)

    # we still need the trace
    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_architecture(), firmware.get_endian())
    firmware.max_iteration = args.max


def setup_statistics(args, firmware):
    setup_working_directory(args, firmware)


def setup_single_analysis(args, firmware):
    setup_working_directory(args, firmware)

    if args.uuid is None:
        print('uuid cannot be empty')
        exit(-1)

    firmware.uuid = args.uuid
    firmware.setup_target_directory()

    path_to_profile = os.path.join(firmware.get_target_dir(), 'profile.' + firmware.profile_ext)
    firmware.path_to_profile = path_to_profile

    empty = False
    # enforce no empty profile which will crash thw whole system
    if not os.path.exists(path_to_profile) or firmware.is_empty_profile():
        os.system('rm -f {}'.format(path_to_profile))
        empty = True

    if empty and args.firmware is None:
        print('please use full command because of missing profile')
        exit(-1)

    if not empty:
        # load the profile
        firmware.set_profile(path_to_profile=path_to_profile)
        firmware.setup_working_path()
        if not os.path.exists(firmware.get_path()):
            print('May be you forget -wd?')
            exit(-1)
        else:
            firmware.size = os.path.getsize(firmware.get_path())
    else:
        # load from the command line
        firmware.set_profile(path_to_profile=path_to_profile, first=True)
        firmware.set_uuid(args.uuid)
        firmware.set_path(args.firmware)
        firmware.set_name(os.path.basename(args.firmware))
        firmware.setup_working_path()
        firmware.size = os.path.getsize(args.firmware)
        firmware.set_architecture(args.architecture)
        firmware.set_endian(args.endian)
        firmware.set_brand(args.brand)
        firmware.set_path_to_source_code(args.source_code)
        firmware.set_path_to_makeout(args.makeout)
        firmware.set_path_to_gcc(args.gcc)

    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}-{}-{}.trace'.format(
        firmware.get_uuid(), firmware.get_architecture(), firmware.get_endian())
    firmware.rerun = args.rerun
    firmware.do_not_diagnosis = args.quick
    firmware.max_iteration = args.max
