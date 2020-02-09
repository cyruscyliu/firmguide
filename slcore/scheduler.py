from logger import logger_info, logger_warning
from analyses.manager import AnalysesManager
from slcore.generation.compilerf import get_compiler
from slcore.environment import restore_analysis, save_analysis


def run_binary_analysis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_tree = analyses_manager.register_binary_analysis()
    status = analyses_manager.run(target_analyses_tree=analyses_tree)

    return False


def run_static_analysis(firmware, binary=True):
    # restore what we have done
    restore_analysis(firmware)

    analyses_manager = AnalysesManager(firmware)
    analyses_tree = analyses_manager.register_static_analysis()
    status = analyses_manager.run(target_analyses_tree=analyses_tree)

    save_analysis(firmware)
    return status


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_tree = analyses_manager.register_diagnosis()

    max_iteration = firmware.max_iteration

    status = False
    while max_iteration:
        max_iteration -= 1
        try:
            status = analyses_manager.run(target_analyses_tree=analyses_tree)
        except SystemExit:
            break

    firmware.set_iteration(firmware.max_iteration - max_iteration)

    return status

