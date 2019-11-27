import abc
import math
import logging

from analyses.dead_loop import DynamicAnalysis

logger = logging.getLogger()


class Trace(DynamicAnalysis):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.trace_tool = None
        self.path_to_trace = args[0]
        self.logger = logging.getLogger()

    @abc.abstractmethod
    def load(self, *args, **kwargs):
        """
        Load trace file fast.
        :return:
        """
        pass

    def diagnosis(self):
        self.load()
        self.detect_dead_loop()
        ratio = len(self.suspicious_loops) / len(self.loops)
        if ratio > 0.2:
            self.logger.info('BAD! Have {:.4f}% suspicious infinite loops!'.format(ratio * 100))
        else:
            self.logger.info('GOOD! Have {} suspicious infinite loops!'.format(len(self.suspicious_loops)))
        if not len(self.suspicious_loops):
            return
        for uuid, suspicious_loop in self.suspicious_loops.items():
            reg_offset = self.cpus[uuid]['offset']
            c = math.floor(math.log(reg_offset, 10)) + 1
            iteration = suspicious_loop['iteration']
            length = suspicious_loop['length']
            self.logger.info('This suspicious log starts at line {}, repeated {} times!'.format(
                reg_offset, iteration))
            for i in range(uuid, uuid + length + 1):
                pc = self.cpus[i]['pc']
                bb_offset = self.bbs[pc]['offset']
                for j, line in enumerate(self.bbs[pc]['content']):
                    self.logger.info('{} {}'.format('-' * c, line))
                for j, line in enumerate(self.cpus[i]['content']):
                    reg_offset = self.cpus[i]['offset']
                    self.logger.info('{} {}'.format(reg_offset, line))


class QEMUDebug(Trace):
    def load_in_asm(self, *args, **kwargs):
        """
        ----------------                                1
        IN:                                             2
        0x00000000:  e3a00000  mov      r0, #0          3
        0x00000004:  e59f1004  ldr      r1, [pc, #4]    4
        0x00000008:  e59f2004  ldr      r2, [pc, #4]    4
        0x0000000c:  e59ff004  ldr      pc, [pc, #4]    4
                                                        4
        """
        ln = 0
        with open(self.path_to_trace) as f:
            new = 0
            for line in f:
                if new == 0 and line.startswith('---'):
                    new = 1
                if new == 3:
                    bb_id = line.strip().split(':')[0]
                    self.bbs[bb_id] = {'content': [line.strip()], 'offset': ln + 1}
                if new == 4 and len(line.strip()):
                    self.bbs[bb_id]['content'].append(line.strip())
                if new in [1, 2, 3]:
                    new += 1
                if new == 4 and not len(line.strip()):
                    new = 0
                ln += 1

    def load_cpu(self, *args, **kwargs):
        """
        R00=00000000 R01=00000000 R02=00000000 R03=00000000 1
        R04=00000000 R05=00000000 R06=00000000 R07=00000000 2
        R08=00000000 R09=00000000 R10=00000000 R11=00000000 3
        R12=00000000 R13=00000000 R14=00000000 R15=00000000 4
        PSR=400001d3 -Z-- A svc32                           5
        """
        ln = 0
        id_ = 0
        with open(self.path_to_trace) as f:
            new = 0
            for line in f:
                if new == 0 and line.startswith('R00'):
                    new = 1
                    self.cpus[id_] = {'uuid': id_, 'offset': ln + 1, 'content': []}
                if new in [1, 2, 3, 4, 5]:
                    self.cpus[id_]['content'].append(line.strip())
                if new == 4:
                    self.cpus[id_]['pc'] = '0x' + line.strip().split()[-1].partition('=')[2]
                if new in [1, 2, 3, 4]:
                    new += 1
                if new == 5:
                    new = 0
                    id_ += 1
                ln += 1

    def load(self, *args, **kwargs):
        if 'in_asm' in self.flags:
            self.load_in_asm()
        if 'cpu' in self.flags:
            self.load_cpu()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trace_tool = 'qemu debug'
        self.flags = ['in_asm', 'cpu']


class KTracer(Trace):
    def load(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trace_tool = 'ktracer'
