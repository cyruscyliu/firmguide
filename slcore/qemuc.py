"""
QEMU controller

after several experiments, I conclude
    1) QEMU is likely to be supported on Windows with extra compilation efforts
    https://stackoverflow.com/questions/53084815/compile-qemu-under-windows-10-64-bit-for-windows-10-64-bit
    which is not elegant and not easy. I hope QEMU will be officially supported on Windows in the future.
    2) Multi-processing introduces more complexity than speed increment. Once you'd like to
    analyze more than one firmware at the same time, you must consider QEMU pollution(synchronization) problem.
    Modifying QEMU source code at the same time makes everything messy and embarrassing. JIT solution is one of
    the ideal ways to solve this problem. BTW, running in different directories looks quick and dirty but is
    really helpful.

finite state machine
                |<-----> RECOVER
    START --> PATCH <--> COMPILE
      |---------<----------|
      |---<----RUN----<----|
      |---<-- TRACE---<----|
"""
import os

START, PATCH, RECOVER, COMPILE, RUN, TRACE = 0, 1, 2, 3, 4, 5


class QEMUController(object):
    def __init__(self):
        self.state = START

    def patch(self, *args, **kwargs):
        pass

    def recover(self, *args, **kwargs):
        pass

    def compile(self, *args, **kwargs):
        pass

    def run(self, *args, **kwargs):
        pass

    def trace(self, *args, **kwargs):
        pass

