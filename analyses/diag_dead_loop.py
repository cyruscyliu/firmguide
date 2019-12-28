import math
import networkx as nx

from analyses.analysis import Analysis


class DeadLoop(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        # A basic block should be indexed by its first PC.
        # PC string must start with 0x.
        # For string trace, `content` is `lines`,
        # `offset` is `start line number`, `length` is `count of lines`.
        # '0x000000000': {'content': [], 'offset':0, 'length':0, 'pc': '0x00000000'}
        # For binary trace, `content` is `blob`,
        # `offset` is `offset of the blob`, `length` is `size of the blob`.
        # 0x000000000: {'content': [], 'offset':0, 'length':0, 'pc': 0x00000000}
        self.bbs = {}

        # A CPU register file should be indexed by its enumerated id.
        # CPU register file always has fixed lines.
        # 0: {'content':[], 'offset':0, 'length':4, 'uuid': 0, 'pc': 0x00000000}
        self.cpus = {}

        # A loop is detected by register files not by basic blocks,
        # so the loop can be indexed by its first register file's uuid.
        # 0: {'length':1, 'iteration': 1, 'uuid': 0}
        self.loops = {}
        self.suspicious_loops = {}

        self.flags = []
        self.trace_tool = None

        self.name = 'dead_loop'
        self.description = 'find dead loop in the given trace'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['check']

    def brent_cycle_detection(self, start):
        """
        The lam (length of cycle) found may not be the least.
        But this one is obviously faster than Floyd's one.
        """

        def f(cpu):
            if cpu['uuid'] + 1 >= self.cpus.__len__():
                raise OverflowError('no more registers files')
            return self.cpus[cpu['uuid'] + 1]

        # main phase: search successive powers of two
        power = lam = 1
        tortoise = start
        hare = f(start)  # f(start) is the element/node next to start.
        while tortoise != hare:
            if power == lam:  # time to start a new power of two?
                tortoise = hare
                power *= 2
                lam = 0
            hare = f(hare)
            lam += 1

        # Find the position of the first repetition of length λ
        tortoise = hare = start
        for i in range(lam):
            # range(lam) produces a list with the values 0, 1, ... , lam-1
            hare = f(hare)
        # The distance between the hare and tortoise is now λ.

        # Next, the hare and tortoise move at same speed until they agree
        mu = start['uuid']
        while tortoise != hare:
            tortoise = f(tortoise)
            hare = f(hare)
            mu += 1

        # Find the length of all cycles.
        iteration = lam
        while tortoise['pc'] == hare['pc']:
            iteration += 1
            tortoise = f(tortoise)
            hare = f(hare)

        return mu, lam, iteration // lam

    def floyd_cycle_detection(self, start):
        def f(cpu):
            if cpu['uuid'] + 1 >= self.cpus.__len__():
                raise OverflowError('no more registers files')
            return self.cpus[cpu['uuid'] + 1]

        # Main phase of algorithm: finding a repetition x_i = x_2i.
        # The hare moves twice as quickly as the tortoise and
        # the distance between them increases by 1 at each step.
        # Eventually they will both be inside the cycle and then,
        # at some point, the distance between them will be
        # divisible by the period λ.
        tortoise = f(start)  # f(start) is the element/node next to start.
        hare = f(f(start))
        while tortoise['pc'] != hare['pc']:
            tortoise = f(tortoise)
            hare = f(f(hare))

        # At this point the tortoise position, ν, which is also equal
        # to the distance between hare and tortoise, is divisible by
        # the period λ. So hare moving in circle one step at a time,
        # and tortoise (reset to x0) moving towards the circle, will
        # intersect at the beginning of the circle. Because the
        # distance between them is constant at 2ν, a multiple of λ,
        # they will agree as soon as the tortoise reaches index μ.

        # Find the position μ of first repetition.
        mu = start['uuid']
        tortoise = start
        while tortoise['pc'] != hare['pc']:
            tortoise = f(tortoise)
            hare = f(hare)
            mu += 1

        # Find the length of the shortest cycle starting from x_μ
        # The hare moves one step at a time while tortoise is still.
        # lam is incremented until λ is found.
        lam = 1
        hare = f(tortoise)
        while tortoise['pc'] != hare['pc']:
            hare = f(hare)
            lam += 1

        # Find the length of all cycles.
        iteration = lam
        while tortoise['pc'] == hare['pc']:
            iteration += 1
            tortoise = f(tortoise)
            hare = f(hare)

        return mu, lam, iteration // lam

    def cycle_detection(self, start, algorithm='floyd'):
        if algorithm == 'floyd':
            return self.floyd_cycle_detection(start)
        elif algorithm == 'brent':
            return self.brent_cycle_detection(start)
        else:
            # TODO add incremental cycle detection
            raise NotImplementedError('only support floyd and brent\'s cycle detection algorithms')

    def detect_dead_loop_by_graph(self):
        # construct the weighted graph
        graph = nx.DiGraph()
        last_pc = None
        for register_file in self.cpus.values():
            pc = register_file['pc']
            if last_pc is not None:
                edge = graph.get_edge_data(last_pc, pc)
                if edge is None:
                    graph.add_edge(last_pc, pc, weight=1)
                else:
                    graph.add_edge(last_pc, pc, weight=edge['weight'] + 1)
            last_pc = pc

        # find heavy edge
        dead_loop_candidates = []
        for edge in graph.edges:
            weight = graph.get_edge_data(*edge)['weight']
            if weight > 2000:
                dead_loop_candidates.append([edge[0], edge[1], weight])

    def detect_dead_loop(self):
        try:
            start = self.cpus[0]
            while 1:
                offset, length, iteration = self.cycle_detection(start)
                uuid = offset
                self.loops[uuid] = {
                    'uuid': uuid, 'length': length, 'iteration': iteration}
                start = self.cpus[offset + length * iteration]
        except OverflowError:
            pass

        for k, v in self.loops.items():
            if v['iteration'] > 2000:
                self.suspicious_loops[k] = v

    def analyze_ud_chain(self):
        pass

    def solve_constraints(self):
        pass

    def run(self, firmware):
        if firmware.trace_format == 'qemudebug':
            self.trace_tool = 'qemu debug'
            self.flags = ['in_asm', 'cpu']
            if 'in_asm' in self.flags:
                self.load_in_asm(firmware)
            if 'cpu' in self.flags:
                self.load_cpu(firmware)
        else:  # 'ktracer'
            self.trace_tool = 'ktracer'

        self.detect_dead_loop()  # does not work well
        # self.detect_dead_loop_by_graph() # does not work well
        ratio = len(self.suspicious_loops) / len(self.loops)
        if ratio > 0.2:
            self.info(firmware, 'BAD! Have {:.4f}% suspicious infinite loops!'.format(ratio * 100), 0)
        else:
            self.info(firmware, 'HH! Have {} suspicious infinite loops!'.format(len(self.suspicious_loops)), 1)
        if not len(self.suspicious_loops):
            return
        for uuid, suspicious_loop in self.suspicious_loops.items():
            reg_offset = self.cpus[uuid]['offset']
            c = math.floor(math.log(reg_offset, 10)) + 1
            iteration = suspicious_loop['iteration']
            length = suspicious_loop['length']
            self.info(firmware, 'This suspicious log starts at line {}, repeated {} times!'.format(
                reg_offset, iteration), 1)
            for i in range(uuid, uuid + length):
                pc = self.cpus[i]['pc']
                bb_offset = self.bbs[pc]['offset']
                for j, line in enumerate(self.bbs[pc]['content']):
                    self.info(firmware, '{} {}'.format('-' * c, line), 0)
                for j, line in enumerate(self.cpus[i]['content']):
                    reg_offset = self.cpus[i]['offset']
                    self.info(firmware, '{} {}'.format(reg_offset, line), 0)
        return True

    def load_in_asm(self, firmware):
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
        with open(firmware.path_to_trace) as f:
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

    def load_cpu(self, firmware):
        """
        R00=00000000 R01=00000000 R02=00000000 R03=00000000 1
        R04=00000000 R05=00000000 R06=00000000 R07=00000000 2
        R08=00000000 R09=00000000 R10=00000000 R11=00000000 3
        R12=00000000 R13=00000000 R14=00000000 R15=00000000 4
        PSR=400001d3 -Z-- A svc32                           5
        """
        ln = 0
        id_ = 0
        with open(firmware.path_to_trace) as f:
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
