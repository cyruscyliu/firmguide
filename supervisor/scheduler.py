from analyses.manager import AnalysesManager
from generation.compilerf import get_compiler
from profile.firmwaref import get_firmware_in_profile
from profile.stats import statistics

from supervisor.logging_setup import logger_info, logger_warning
from supervisor.save_and_restore import \
    check_and_restore, save_analysis, \
    setup_diagnosis, setup_code_generation, setup_single_analysis, setup_print_profile, setup_statistics


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_dynamic_analysis(tracing=False)
    analyses_manager.run_dynamic_analyses()


def run_single_analysis(firmware):
    analysis_wrapper(firmware)


def run_code_generation(firmware):
    analysis_wrapper(firmware, static_analysis=False, check_only=True)


def run_print_profile(firmware):
    firmware.print_profile()


def run_statistics(firmware):
    statistics(firmware)


def run(parser, args):
    firmware = get_firmware_in_profile(args.profile)
    if args.print_profile:
        setup_print_profile(args, firmware)
        run_print_profile(firmware)
    elif args.statistics:
        setup_statistics(args, firmware)
        run_statistics(firmware)
    elif args.trace:
        setup_diagnosis(args, firmware)
        run_diagnosis(firmware)
    elif args.generation:
        setup_code_generation(args, firmware)
        run_code_generation(firmware)
    elif args.uuid:
        setup_single_analysis(args, firmware)
        run_single_analysis(firmware)
    else:
        parser.print_help()


def static_analysis_wrapper(analyses_manager):
    analyses_manager.run_static_analysis()


def analysis_wrapper(firmware, static_analysis=True, check_only=False):
    # restore first
    check_and_restore(firmware)

    analyses_manager = AnalysesManager(firmware)

    if static_analysis:
        analyses_manager.register_static_analysis()
        analyses_manager.run_static_analysis()

    # save advance
    save_analysis(firmware)

    analyses_manager.register_dynamic_analysis(check_only=check_only)

    while not firmware.do_not_diagnosis:  # exit early
        # perform code generation
        machine_compiler = get_compiler(firmware)
        try:
            machine_compiler.solve()
        except NotImplementedError as e:
            logger_warning(firmware.get_uuid(), 'analysis', 'exception', e.__str__(), 0)
            exit(-1)
        machine_compiler.link_and_install()
        machine_compiler.make()

        # perform dynamic checking
        analyses_manager.run_dynamic_analyses()
        save_analysis(firmware)
