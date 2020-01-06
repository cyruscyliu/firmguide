import os
import tempfile
import yaml
import shutil

from supervisor.logging_setup import logger_info


def check_and_restore(firmware):
    # handle analysis
    analysis = os.path.join(firmware.working_directory, 'analysis')
    if not os.path.exists(analysis) or firmware.rerun:
        with open(analysis, 'w') as f:
            f.close()
    with open(analysis, 'r') as f:
        analysis_progress = yaml.safe_load(f)
        if analysis_progress is None:
            firmware.analysis_progress = {}
        else:
            firmware.analysis_progress = analysis_progress

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

        architecture = firmware.get_architecture()
        endian = firmware.get_endian()
        if architecture == 'arm':
            target_list = 'arm-softmmu'  # support both b&l
        elif architecture == 'mips':
            if endian == 'l':
                target_list = 'mipsel-softmmu'  # l
            else:
                target_list = 'mips-softmmu'  # b by default
        else:
            target_list = 'arm-softmmu,mipsel-softmmu,mips-softmmu'
        os.system('cd {0}/qemu-4.0.0 && ./configure --target-list={1} >/dev/null 2>&1'.format(
            firmware.working_directory, target_list))
        os.system('cd {0}/qemu-4.0.0 && make -j4'.format(firmware.working_directory))

    # logging
    logger_info(firmware.get_uuid(), 'save_and_restore', 'begin', firmware.brief(), 0)


def save_analysis(firmware):
    analysis = os.path.join(firmware.working_directory, 'analysis')
    with open(analysis, 'w') as f:
        yaml.safe_dump(firmware.analysis_progress, f)
    firmware.save_profile(working_dir=firmware.working_directory)
    firmware.stats()
    logger_info(firmware.get_uuid(), 'save_and_restore', 'save', firmware.summary(), 0)


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


def setup_diagnosis(args, firmware):
    # 1 we need the trace
    firmware.path_to_trace = args.trace
    firmware.trace_format = args.trace_format
    firmware.architecture = args.architecture
    firmware.endian = args.endian
    firmware.max_iteration = args.max
    # 2 and the uuid
    firmware.uuid = 'diagnosis'


def setup_working_directory(args, firmware):
    # prepare working directory
    if args.working_directory is None:
        working_dir = tempfile.gettempdir()
    else:
        working_dir = os.path.realpath(args.working_directory)
    target_dir = os.path.join(working_dir, firmware.uuid)
    firmware.set_working_dir(target_dir)
    os.makedirs(firmware.working_directory, exist_ok=True)


def setup_working_path(firmware):
    target_path = os.path.join(firmware.get_working_dir(), firmware.get_name())
    firmware.set_working_path(target_path)


def setup_code_generation(args, firmware):
    # load the profile
    firmware.set_profile(path_to_profile=args.generation)
    firmware.uuid = firmware.get_uuid()
    setup_working_directory(args, firmware)

    setup_working_path(firmware)
    firmware.no_inference = True
    # avoid modify our well-defined profile
    extension = 'yaml' if args.profile == 'simple' else 'dt'
    firmware.path_to_profile = os.path.join(firmware.working_directory, 'profile.' + extension)
    # we still need the trace
    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}.trace'.format(firmware.get_uuid())
    firmware.max_iteration = args.max


def setup_statistics(args, firmware):
    firmware.uuid = 'stats'
    setup_working_directory(args, firmware)


def setup_print_profile(args, firmware):
    firmware.uuid = args.uuid
    setup_working_directory(args, firmware)

    extension = 'yaml' if args.profile == 'simple' else 'dt'
    path_to_profile = os.path.join(firmware.working_directory, 'profile.' + extension)

    if os.path.exists(path_to_profile):
        # load the profile
        firmware.set_profile(path_to_profile=path_to_profile)
        try:
            firmware.size = os.path.getsize(firmware.get_path())
        except TypeError as e:
            print('May be you forget -wd? Otherwise, please run rm {} and full command'.format(path_to_profile))
            raise e
        setup_working_path(firmware)
    else:
        print('the profile {} does not exist'.format(path_to_profile))


def setup_single_analysis(args, firmware):
    # must assign the uuid
    firmware.uuid = args.uuid
    setup_working_directory(args, firmware)

    extension = 'yaml' if args.profile == 'simple' else 'dt'
    path_to_profile = os.path.join(firmware.working_directory, 'profile.' + extension)

    if os.path.exists(path_to_profile):
        # load the profile
        firmware.set_profile(path_to_profile=path_to_profile)
        try:
            firmware.size = os.path.getsize(firmware.get_path())
        except TypeError as e:
            print('May be you forget -wd? Otherwise, please run rm {} and full command'.format(path_to_profile))
            raise e
        setup_working_path(firmware)
    else:
        # load from the command line
        firmware.set_profile(path_to_profile=path_to_profile, first=True)
        firmware.set_uuid(args.uuid)
        firmware.set_path(args.firmware)
        firmware.set_name(os.path.basename(args.firmware))
        firmware.size = os.path.getsize(args.firmware)
        firmware.set_architecture(args.architecture)
        firmware.set_endian(args.endian)
        firmware.set_brand(args.brand)
        firmware.set_path_to_source_code(args.source_code)
        firmware.set_path_to_makeout(args.makeout)
        firmware.set_path_to_gcc(args.gcc)
        setup_working_path(firmware)

    firmware.trace_format = args.trace_format
    firmware.path_to_trace = 'log/{}.trace'.format(firmware.get_uuid())
    firmware.rerun = args.rerun
    firmware.do_not_diagnosis = args.quick
    firmware.max_iteration = args.max
