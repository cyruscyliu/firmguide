from analyses.cpu import get_cpu_model_info
from analyses.extraction import extract_kernel_and_dtb
from analyses.flash import get_flash_info
from analyses.ic import get_ic_info
from analyses.metadata import get_metadata
from analyses.ram import get_ram_info
from analyses.srcode import get_source_code
from analyses.timer import get_timer_info
from analyses.trace.collection import trace_collection
from analyses.trace.format import QEMUDebug, KTracer
from analyses.trace.policies import policy_checking
from analyses.uart import get_uart_info

import logging

logger = logging.getLogger()


def analysis(firmware):
    # let's start
    extract_kernel_and_dtb(firmware)
    get_metadata(firmware)
    get_source_code(firmware)
    get_cpu_model_info(firmware)
    get_ram_info(firmware)
    get_ic_info(firmware)
    get_timer_info(firmware)
    get_uart_info(firmware)
    get_flash_info(firmware)


def dynamic_analysis(firmware):
    trace_collection(firmware)
    policy_checking(firmware)


def trace_diagnosis(path_to_trace, trace_format):
    if trace_format == 'qemudebug':
        trace = QEMUDebug(path_to_trace)
    else:  # 'ktracer'
        trace = KTracer(path_to_trace)
    if trace.scan_user_level():
        logger.info('GOOD! Have entered the user level!')
    trace.load()
    trace.cycle_detection_all()
    trace.scan_suspicious_loop()
    ratio = len(trace.suspicious_loops) / len(trace.loops)
    if ratio > 0.2:
        logger.info('BAD! Have {:.4f}% suspicious infinite loops!'.format(ratio * 100))
    else:
        logger.info('GOOD! Have {} suspicious infinite loops!'.format(len(trace.suspicious_loops)))
    if not len(trace.suspicious_loops):
        return
    for suspicious_loop in trace.suspicious_loops.values():
        logger.info('This suspicious starts at line {}, repeated {} times!'.format(
            suspicious_loop['start'], suspicious_loop['iteration']))
        start = suspicious_loop['start']
        length = suspicious_loop['length']
        for i in range(start, start + length + 1):
            pc = '0x' + trace.cpus[i]['pc']
            bb = trace.bbs[pc]
            for line in bb['lines']:
                logger.info(line)
            for line in trace.cpus[i]['lines']:
                logger.info(line)
            logger.info('')
        break
