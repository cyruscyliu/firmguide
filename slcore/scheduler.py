from analyses.manager import AnalysesManager
from slcore.generation.compilerf import get_compiler
from profile.stats import statistics

from logger import logger_info, logger_warning
from slcore.environment import restore_analysis, save_analysis, \
    setup_diagnosis, setup_statistics


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_dynamic_analysis(tracing=False)
    status = analyses_manager.run_dynamic_analyses()


def run_static_analysis(firmware, binary=True):
    # restore what we have done
    # restore_analysis(firmware)

    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_static_analysis(binary=binary)
    status = analyses_manager.run_static_analysis()

    # save_analysis(firmware)


def run_statistics(firmware):
    statistics(firmware)


def run_dynamic_analysis(firmware, check_only=False):
    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_dynamic_analysis(check_only=check_only)

    max_iteration = firmware.max_iteration

    while max_iteration:
        max_iteration -= 1
        try:
            status = analyses_manager.run_dynamic_analyses()
        except SystemExit:
            break

    firmware.set_iteration(firmware.max_iteration - max_iteration)

