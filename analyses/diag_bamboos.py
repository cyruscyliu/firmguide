"""
Add bamboo devices after DataAbort and InitValue.
"""
from analyses.analysis import Analysis
from analyses.diag_dabt import DataAbort


class Bamboo(object):
    def __init__(self):
        self.name = None
        self.mmio_base = None
        self.mmio_size = None
        self.registers = {}

    def __str__(self):
        r = ''
        for k, v in self.registers.items():
            r = '{}/{}/{}'.format(k, v['offset'], v['value'])
        return '{} from 0x{:x} to 0x{:x} {}'.format(self.name, self.mmio_base, self.mmio_base + self.mmio_size, r)


class Bamboos(Analysis):
    def insert(self, bamboo):
        target = 0
        for i, exist in enumerate(self.bamboos):
            if bamboo.mmio_base < exist.mmio_base:
                target = i
                self.bamboos.insert(i, bamboo)
                break
        if target == 0:
            self.bamboos.append(bamboo)

        bamboo.name = 'stub{}'.format(len(self.bamboos) - 1)

    def init_registers(self, bamboo):
        bamboo.registers = {
            'stub_reserved{}'.format(self.variable): {
                'offset': "0x0 ... 0x{:x}".format(bamboo.mmio_size),
                'value': "0x0"
            }}

    def print_pretty(self):
        for bamboo in self.bamboos:
            yield bamboo.__str__()

    def run(self, firmware):
        dabt = self.analysis_manager.get_analysis('data_abort')
        assert isinstance(dabt, DataAbort)

        # load bamboo devices
        if firmware.profile is None:
            # in diagnosis mode
            bamboo_devices = {}
        else:
            bamboo_devices = firmware.get_bamboo_devices()

        for name, parameters in bamboo_devices.items():
            bamboo = Bamboo()
            bamboo.name = name
            bamboo.mmio_base = parameters['mmio_base']
            bamboo.mmio_size = parameters['mmio_size']
            bamboo.registers = parameters['registers']
            self.bamboos.append(bamboo)

        # get dead addresses
        for dead_address in dabt.dead_addresses:
            bamboo = Bamboo()
            bamboo.mmio_base = int(dead_address, 16) & 0xFFFFFF00
            bamboo.mmio_size = 0x100
            self.insert(bamboo)
            self.init_registers(bamboo)

        for message in self.print_pretty():
            self.info(firmware, message, 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'bamboos'
        self.description = 'add bamboo devices after DataAbort and InitValue'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['data_abort', 'init_value']
        #
        self.bamboos = []
        self.variable = 0
