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
from analyses.uart import get_uart_info

import logging
import math

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


def trace_diagnosis(path_to_trace, trace_format):
    if trace_format == 'qemudebug':
        trace = QEMUDebug(path_to_trace)
    else:  # 'ktracer'
        trace = KTracer(path_to_trace)
    if trace.scan_user_level():
        logger.info('GOOD! Have entered the user level!')
    trace.load()
    trace.detect_dead_loop()
    ratio = len(trace.suspicious_loops) / len(trace.loops)
    if ratio > 0.2:
        logger.info('BAD! Have {:.4f}% suspicious infinite loops!'.format(ratio * 100))
    else:
        logger.info('GOOD! Have {} suspicious infinite loops!'.format(len(trace.suspicious_loops)))
    if not len(trace.suspicious_loops):
        return
    for uuid, suspicious_loop in trace.suspicious_loops.items():
        reg_offset = trace.cpus[uuid]['offset']
        c = math.floor(math.log(reg_offset, 10)) + 1
        iteration = suspicious_loop['iteration']
        length = suspicious_loop['length']
        logger.info('This suspicious log starts at line {}, repeated {} times!'.format(
            reg_offset, iteration))
        for i in range(uuid, uuid + length + 1):
            pc = trace.cpus[i]['pc']
            bb_offset = trace.bbs[pc]['offset']
            for j, line in enumerate(trace.bbs[pc]['content']):
                logger.info('{} {}'.format('-' * c, line))
            for j, line in enumerate(trace.cpus[i]['content']):
                reg_offset = trace.cpus[i]['offset']
                logger.info('{} {}'.format(reg_offset, line))
        break
