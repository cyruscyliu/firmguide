import os
import abc


class Trace(object):
    def __init__(self, *args, **kwargs):
        self.trace_tool = None
        self.path_to_trace = args[0]
        self.cpus = {}  # 1: {'id': 1, 'ln': 0, 'pc': '00000000'}
        self.loops = {}  # 1: {'id': 1, 'start': 0, 'length':1, 'iteration': 1}

    @abc.abstractmethod
    def load(self, *args, **kwargs):
        """
        Load trace file fast.
        :return:
        """
        pass

    @abc.abstractmethod
    def scan_user_level(self, *args, **kwargs):
        pass

    def brent_cycle_detection(self, start):
        """
        The lam (length of cycle) found may not be the least.
        But this one is obviously faster than Floyd's one.
        """

        def f(cpu):
            if cpu['id'] + 1 >= self.cpus.__len__():
                raise OverflowError('no more registers files')
            return self.cpus[cpu['id'] + 1]

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
        mu = start['id']
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
            if cpu['id'] + 1 >= self.cpus.__len__():
                raise OverflowError('no more registers files')
            return self.cpus[cpu['id'] + 1]

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
        mu = start['id']
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

    def cycle_detection_all(self):
        try:
            x0 = self.cpus[0]
            while 1:
                start, length, iteration = self.cycle_detection(x0)
                self.loops[x0['id']] = {'id': x0['id'], 'start': start, 'length': length, 'iteration': iteration}
                x0 = self.cpus[start + length * iteration + 2]
        except OverflowError:
            pass


class QEMUDebug(Trace):
    def scan_user_level(self, *args, **kwargs):
        cmd = 'grep usr {} >/dev/null 2>&1'.format(self.path_to_trace)
        not_find_user_level = os.system(cmd)
        return not not_find_user_level

    def load_in_asm(self, *args, **kwargs):
        pass

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
                    self.cpus[id_] = {'id': id_, 'ln': ln}
                if new == 4:
                    self.cpus[id_]['pc'] = line.strip().split()[-1].partition('=')[2]
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.trace_tool = 'ktracer'
