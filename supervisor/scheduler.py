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


def analysis_wrapper(firmware, static_analysis=True, tracing=True, check_only=False):
    # restore first, load what we have done
    check_and_restore(firmware)

    analyses_manager = AnalysesManager(firmware)

    # static analysis is not always necessary
    # but is prone to abort due to critical analysis
    # it's very important to save its status such
    # that we can save analysis results for this time
    status = True
    if static_analysis:
        analyses_manager.register_static_analysis()
        status = analyses_manager.run_static_analysis()

    # save advance
    save_analysis(firmware)
    if not status:
        exit(-1)

    # if -q assigned, exit early
    if firmware.do_not_diagnosis:
        exit(-1)

    # dynamic analysis is always necessary
    # but we'd like to choose part of them for specific task
    # we can ignore tracing and ignore several advanced analysis
    # only keep `check` analysis to tell us whether we have
    # entered the user mode or not
    analyses_manager.register_dynamic_analysis(tracing=tracing, check_only=check_only)

    # for iteration we must set a limit otherwise we might not stop
    max_iteration = firmware.max_iteration
    iteration = 0
    # because complication is not analysis,
    # so we handle its exception here, maybe
    # there are some surprising tricks?
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
        pass

    firmware.set_iteration(iteration)
    save_analysis(firmware)
