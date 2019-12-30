from analyses.analysis import Analysis
from pyqemulog import *

from analyses.diag_tracing import LoadTrace


def get_instruction(address, bb):
    instruction = None
    for instruction in bb['instructions']:
        if int(instruction['address'], 16) == address:
            break
    return ' '.join([instruction['opcode'], ' '.join(instruction['operand'])])


class DataAbort(Analysis):
    def run(self, firmware):
        trace = self.analysis_manager.get_analysis('load_trace')
        assert isinstance(trace, LoadTrace)

        dabts = []
        for k, cpurf in trace.cpurfs.items():
            if 'exception' in cpurf and 'type' in cpurf['exception'] and cpurf['exception']['type'] == 'dabt':
                dabts.append(cpurf)

        if not len(dabts):
            self.context['input'] = 'no more data abort, maybe there are some heavy loops?'
            return False

        for cpurf in dabts:
            # dabt
            # current bb has where to abort -> next bb has where to return
            if get_exception_return_cpurf(cpurf, trace.cpurfs) is None:
                self.info(firmware, 'line {} has a data abort at {}, return abnormally'.format(
                    cpurf['ln'], cpurf['register_files']['DFAR']), 1)
            else:
                self.info(firmware, 'line {} has a data abort at {}, return normally'.format(
                    cpurf['ln'], cpurf['register_files']['DFAR']), 1)
                next_cpurf = get_next_cpurf(cpurf, trace.cpurfs)
                where_to_return = int(next_cpurf['register_files']['R14'], 16) - 8
                self.info(firmware, 'the program should re-entry 0x{:x} {}'.format(
                    where_to_return, get_instruction(where_to_return, get_bb(cpurf, trace.bbs))), 1)
                if int(cpurf['register_files']['DFAR'], 16) == 0:
                    self.info(firmware, 'kernel panic by accessing 0', 1)
                    continue
                self.dead_addresses.append(cpurf['register_files']['DFAR'])

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'data_abort'
        self.description = 'find data abort info'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = True
        self.required = ['callstack']
        #
        self.dead_addresses = []
