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
        2.3 create an empty device profile
        2.4 copy firmware to the wd
    3. To restore a previous task,
        3.1 load the analysis file
        3.2 load the device profile

    :param firmware: the firmware.
    :return: None
    """
    rerun = firmware.rerun

    # check first time or not
    first_time = True
    if os.path.exists(firmware.working_directory):
        first_time = False
    if rerun:
        first_time = True

    # handle wd
    os.makedirs(firmware.working_directory, exist_ok=True)

    # handle analysis
    analysis = os.path.join(firmware.working_directory, 'analysis')
    if not os.path.exists(analysis):
        first_time = True

    if first_time:
        with open(analysis, 'w') as f:
            f.close()
    with open(analysis, 'r') as f:
        analysis_progress = yaml.safe_load(f)
        if analysis_progress is None:
            firmware.analysis_progress = {}
        else:
            firmware.analysis_progress = analysis_progress

    # handle profile, otherwise we load the profile before
    if first_time:
        firmware.set_profile(working_dir=firmware.working_directory, first=True)

    # copy the firmware to working path
    if not os.path.exists(firmware.working_path):
        shutil.copy(
            os.path.join(os.getcwd(), firmware.get_path()),
            os.path.join(firmware.working_path)
        )

    # build the QEMU in working directory, skip tiny firmware
    if not os.path.exists(os.path.join(firmware.working_directory, 'qemu-4.0.0')):
        print('to avoid QEMU pollution, build the QEMU in the working directory {}'.format(firmware.working_directory))
        shutil.copy(
            os.path.join('build', 'qemu-4.0.0-patched.tar.xz'),
            os.path.join(firmware.working_directory, 'qemu-4.0.0-patched.tar.xz')
        )
        os.system('tar --skip-old-files -Jxf {0}/qemu-4.0.0-patched.tar.xz -C {0}'.format(firmware.working_directory))
        os.system('cd {0}/qemu-4.0.0 && ./configure --target-list=arm-softmmu,mipsel-softmmu >/dev/null'.format(
            firmware.working_directory))
        os.system('cd {0}/qemu-4.0.0 && make -j4'.format(firmware.working_directory))

    # logging
    if first_time:
        logger_info(firmware.get_uuid(), 'save_and_restore', 'first', firmware.brief(), 0)
    else:
        logger_info(firmware.get_uuid(), 'save_and_restore', 'restore', firmware.brief(), 0)


def save_analysis(firmware):
    analysis = os.path.join(firmware.working_directory, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)
    firmware.save_profile(working_dir=firmware.working_directory)
    logger_info(firmware.get_uuid(), 'save_and_restore', 'save', firmware.summary(), 0)


def finished(firmware, analysis):
    try:
        status = firmware.analysis_progress[analysis.name]
        return True
    except KeyError:
        return False


def finish(firmware, analysis):
    if analysis.name not in firmware.analysis_progress:
        firmware.analysis_progress[analysis.name] = 1


def setup_working_dir(args, firmware):
    # set the working directory
    # but not actually create the dir or copy the file
    if args.working_directory is None:
        working_dir = tempfile.gettempdir()
    else:
        working_dir = os.path.realpath(args.working_directory)
    target_dir = os.path.join(working_dir, firmware.get_uuid())
    target_path = os.path.join(working_dir, firmware.get_uuid(), firmware.get_name())
    firmware.set_working_dir(target_dir)
    firmware.set_working_path(target_path)


def setup_diagnosis(args, firmware):
    setup_working_dir(args, firmware)
    firmware.path_to_trace = args.trace
    firmware.trace_format = args.trace_format


def setup_code_generation(args, firmware):
    # load from profile
    firmware.set_profile(path_to_profile=args.generation)
    # 0 setup working directory
    setup_working_dir(args, firmware)
    # 1 ignore inference analysis
    firmware.no_inference = True
    # 2 avoid modify our well-defined profile
    extension = 'yaml' if args.profile == 'simple' else 'dt'
    firmware.path_to_profile = os.path.join(firmware.working_directory, 'profile.' + extension)
    # 3 we still need the trace
    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}.trace'.format(firmware.get_uuid())


def setup_single_analysis(args, firmware):
    # 1 must assign the uuid
    firmware.set_uuid(args.uuid)

    if args.rerun:
        # 1.1 assign the profile
        extension = 'yaml' if args.profile == 'simple' else 'dt'
        path_to_profile = os.path.join(firmware.working_directory, 'profile.' + extension)
        setup_working_dir(args, firmware)
    else:
        # 1.2 load from the command line
        firmware.path = args.firmware
        firmware.name = os.path.basename(args.firmware)
        firmware.size = os.path.getsize(args.firmware)
        # set architecture and endian
        firmware.architecture = args.architecture
        firmware.endian = args.endian
        # set brand
        firmware.brand = args.brand
        # set source code
        firmware.path_to_source_code = args.source_code
        # set diagnosis
        firmware.trace_format = args.trace_format
        firmware.path_to_trace = 'log/{}.trace'.format(firmware.get_uuid())

    firmware.do_not_diagnosis = args.quick
