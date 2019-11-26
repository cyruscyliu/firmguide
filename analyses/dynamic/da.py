class DynamicAnalysis(object):
    def __init__(self):
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

    def detect_dead_loop(self):
        try:
            start = self.cpus[0]
            while 1:
                offset, length, iteration = self.cycle_detection(start)
                uuid = start['uuid'] + offset
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
