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


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_dynamic_analysis(tracing=False)
    analyses_manager.run_dynamic_analyses()


def run_statistics(firmware):
    statistics(firmware)


def run_dynamic_analysis(firmware):
    # restore what we have done

    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_dynamic_analysis()

    # for the iteration we have to set a bound in case of stopless
    max_iteration = firmware.max_iteration
    iteration = 0

    try:
        while max_iteration:
            # perform code generation
            machine_compiler = get_compiler(firmware)
            machine_compiler.solve()
            machine_compiler.link_and_install()
            machine_compiler.make()

            # perform dynamic checking
            status = analyses_manager.run_dynamic_analyses()
            if not status:
                break
            max_iteration -= 1
            iteration += 1
    except NotImplementedError as e:
        logger_warning(firmware.get_uuid(), 'analysis', 'exception', e.__str__(), 0)
    except SystemExit as e:
        iteration += 1

    firmware.set_iteration(iteration)
