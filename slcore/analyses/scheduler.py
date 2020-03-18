from slcore.analyses.manager import AnalysesManager
from slcore.environment import restore_analysis, save_analysis
from slcore.analyses.mfilter import Filter
from slcore.analyses.ram import RAM
from slcore.analyses.loaddr import LoadAddr
from slcore.analyses.entrypoint import EntryPoint
from slcore.analyses.preparation import Preparation
from slcore.analyses.initvalue import InitValue
from slcore.analyses.preprocdt import DTPreprocessing
from slcore.analyses.trace import DoTracing, LoadTrace
from slcore.analyses.c_user_level import Checking
from slcore.analyses.c_user_level import FastChecking
from slcore.analyses.c_data_abort import DataAbort
from slcore.analyses.c_undef_inst import UndefInst
from slcore.analyses.machines import Machines


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

def run_bootup(firmware):
    analyses_manager = AnalysesManager(firmware)

    at = analyses_manager.new_analyses_tree()
    analyses_manager.register_analysis(Machines(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(Preparation(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DTPreprocessing(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(InitValue(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(DoTracing(analyses_manager), analyses_tree=at)
    analyses_manager.register_analysis(FastChecking(analyses_manager), analyses_tree=at)
    try:
        status = analyses_manager.run(target_analyses_tree=at)
    except SystemExit:
        status = True
        pass

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

