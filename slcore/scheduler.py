import os
import shutil

from slcore.analyses.manager import AnalysesManager
from slcore.environment import restore_analysis, save_analysis
from slcore.project import get_current_project, project_get_srcodec, \
    project_get_qemuc
from slcore.compositor import unpack
from slcore.analyses.static_analysis.mfilter import Filter
from slcore.analyses.static_analysis.ram import RAM
from slcore.analyses.static_analysis.loaddr import LoadAddr
from slcore.analyses.static_analysis.entrypoint import EntryPoint
from slcore.analyses.preparation import Preparation
from slcore.analyses.initvalue import InitValue
from slcore.analyses.preprocdt import DTPreprocessing
from slcore.analyses.trace import DoTracing, LoadTrace
from slcore.analyses.c_user_level import Checking
from slcore.analyses.c_data_abort import DataAbort
from slcore.analyses.c_undef_inst import UndefInst
from slcore.analyses.c_panic import Panic
from slcore.analyses.bamboos import Bamboos
from slcore.profile.firmwaref import get_firmware


def run_static_analysis(firmware, binary=True):
    # restore what we have done
    restore_analysis(firmware)

    analyses_manager = AnalysesManager(firmware)
    at = analyses_manager.new_analyses_tree()
    analyses_manager.register_analysis(Filter(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(RAM(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(LoadAddr(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(EntryPoint(analyses_manager), analyses_tree=at)
    status = analyses_manager.run(target_analyses_tree=at)

    save_analysis(firmware)
    return status


def run_trace_analysis(firmware):
    analyses_manager = AnalysesManager(firmware)

    at = analyses_manager.new_analyses_tree()
    analyses_manager.register_analysis(LoadTrace(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(Checking(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DataAbort(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(UndefInst(analyses_manager), analyses_tree=at)
    status = analyses_manager.run(target_analyses_tree=at)

    return status


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)

    at = analyses_manager.new_analyses_tree()
    analyses_manager.register_analysis(Preparation(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DTPreprocessing(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(InitValue(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DoTracing(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(LoadTrace(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(Checking(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DataAbort(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(UndefInst(analyses_manager), analyses_tree=at)
    # analyses_manager.register_analysis(CallStack(analyses_manager), analyses_tree=at)
    # analyses_manager.register_analysis(Panic(analyses_manager), analyses_tree=at)
    # analyses_manager.register_analysis(Bamboos(analyses_manager), analyses_tree=at)

    max_iteration = firmware.max_iteration

    status = False
    while max_iteration:
        max_iteration -= 1
        try:
            status = analyses_manager.run(target_analyses_tree=at)
        except SystemExit:
            break

    firmware.set_iteration(firmware.max_iteration - max_iteration)
    if not firmware.get_stage('user_mode') and firmware.debug:
        firmware.qemuc.debug(firmware.running_command, firmware.srcodec.get_path_to_vmlinux())

    return status


def run_dt_renderer(firmware):
    analyses_manager = AnalysesManager(firmware)
    at = analyses_manager.new_analyses_tree()
    analyses_manager.register_analysis(Preparation(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DTPreprocessing(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(InitValue(analyses_manager), analyses_tree=at)
    analyses_manager.run(target_analyses_tree=at)


def project_standard_warmup(args, components=None, profile=None):
    project = get_current_project()
    if project is None:
        print('please open/create a new project')
        exit()

    target_dir = project.attrs['target_dir']
    path_to_profile = os.path.join(target_dir, 'profile.yaml')
    if not os.path.exists(path_to_profile):
        path_to_profile = None
    if profile is not None:
        path_to_profile = profile

    firmware = project_migrate(path_to_profile=path_to_profile, components=components)
    firmware.set_arch(project.attrs['arch'])
    firmware.set_endian(project.attrs['endian'])
    firmware.rerun = args.rerun

    firmware.srcodec = project_get_srcodec()
    firmware.qemuc = project_get_qemuc()
    if hasattr(args, 'nocompilation'):
        firmware.cancle_compilation = args.nocompilation

    firmware.max_iteration = 1
    firmware.trace_format = 'qemudebug'
    if hasattr(args, 'trace'):
        firmware.path_to_trace = args.trace
    else:
        firmware.path_to_trace = '{}/{}-{}-{}.trace'.format(
            firmware.get_target_dir(), '0', firmware.get_arch(), firmware.get_endian()
        )
    firmware.debug = args.debug

    if hasattr(args, 'firmware'):
        images = project.attrs['images']
        components = firmware.get_components()
        if components is not None:
            if args.firmware is not None and args.firmware != components.get_path_to_raw():
                firmware.components = unpack(args.firmware, target_dir=firmware.target_dir)
        elif images is not None and len(images):
            firmware.components = unpack(images[0], target_dir=firmware.target_dir)
        elif args.firmware:
            firmware.components = unpack(args.firmware, target_dir=firmware.target_dir)
        else:
            print('-f/--firmware missing')

    if hasattr(args, 'dtb'):
        dtbs = project.attrs['dtbs']
        components = firmware.get_components()
        if components is not None:
            if args.dtb is not None:
                firmware.set_dtb(args.dtb)
            elif components.has_device_tree():
                firmware.set_dtb(components.get_path_to_dtb())
        elif args.dtb:
            firmware.set_dtb(args.dtb)
        elif dtbs is not None and len(dtbs):
            firmware.set_dtb(dtbs[0])
        else:
            print('neither dtb was found in tested firmware nor -dtb was assigned')
    return firmware


def project_standard_wrapup(firmware):
    firmware.snapshot()
    return archive(firmware)


def project_migrate(path_to_profile=None, components=None):
    project = get_current_project()
    if project is None:
        print('please open/create a new project')
        return None

    firmware = get_firmware('simple')
    firmware.target_dir =  project.attrs['target_dir']

    # load profile from path_to_profile
    if path_to_profile:
        firmware.set_profile(path_to_profile=path_to_profile)
        # change save-to-path to avoid modifing our well-defined profile
        firmware.path_to_profile = os.path.join(firmware.get_target_dir(), 'profile.yaml')
    else:
        firmware.set_profile(target_dir=firmware.get_target_dir(), first=True)

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

def archive(firmware):
    pass
