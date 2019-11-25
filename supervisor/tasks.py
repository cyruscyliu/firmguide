import logging
import math

from analyses.device_tree import DeviceTree
from analyses.dot_config import DotConfig
from analyses.extraction import Extraction
from analyses.format import Format
from analyses.kernel import Kernel
from analyses.common.analysis import AnalysesManager
from analyses.openwrt import OpenWRTURL, OpenWRTRevision, OpenWRTToH
from analyses.srcode import SRCode
from analyses.strings import Strings

logger = logging.getLogger()


def static_analysis(firmware):
    analyses_manager = AnalysesManager()
    # format <- extraction
    analyses_manager.register_analysis(Format())
    analyses_manager.register_analysis(Extraction())
    # extraction <- kernel
    analyses_manager.register_analysis(Kernel())
    # extraction <- dt
    analyses_manager.register_analysis(DeviceTree())
    # extraction, revision <- strings
    analyses_manager.register_analysis(Strings())
    # kernel <- revision
    analyses_manager.register_analysis(OpenWRTRevision())
    # revision, url <- toh
    analyses_manager.register_analysis(OpenWRTURL())
    analyses_manager.register_analysis(OpenWRTToH())
    # srcode <- .config
    analyses_manager.register_analysis(SRCode())
    analyses_manager.register_analysis(DotConfig())
    # run them all
    analyses_manager.run(firmware)


def dynamic_analysis(firmware):
    trace_collection(firmware)


def trace_diagnosis(trace):
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
