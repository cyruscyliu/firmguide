from analyses.manager import AnalysesManager
from generation.compilerf import get_compiler
from profile.firmwaref import get_firmware_in_profile

from supervisor.logging_setup import logger_info, logger_warning
from supervisor.save_and_restore import \
    check_and_restore, save_analysis, setup_diagnosis, setup_code_generation, setup_single_analysis


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_manager.register_dynamic_analysis(tracing=False)
    analyses_manager.run_dynamic_analyses()


def run_single_analysis(firmware):
    analysis_wrapper(firmware)


def run_code_generation(firmware):
    analysis_wrapper(firmware, static_analysis=False, check_only=True)


def run(parser, args):
    firmware = get_firmware_in_profile(args.profile)
    if args.trace:
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
        machine_compiler.solve()
        machine_compiler.link_and_install()
        machine_compiler.make()

        # perform dynamic checking
        analyses_manager.run_dynamic_analyses()
        break
