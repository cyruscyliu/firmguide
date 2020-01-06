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
        # this is a simple `insert interval` problem
        # because we have a fix interval 0x100
        # and we will not merge adjacent intervals
        bamboos = []

        insert_pos = 0
        for exist in self.bamboos:
            if exist.mmio_base + exist.mmio_size <= bamboo.mmio_base:
                bamboos.append(exist)
                insert_pos += 1
            elif exist.mmio_base >= bamboo.mmio_base + bamboo.mmio_size:
                bamboos.append(exist)
            else:
                # find an identity bamboo
                insert_pos = -1

        if insert_pos != -1:
            bamboo.name = 'stub{}'.format(len(self.bamboos) - 1)
            bamboos.insert(insert_pos, bamboo)
            self.bamboos = bamboos

        return True

    def init_registers(self, bamboo):
        bamboo.registers = {
            'stub_reserved{}'.format(self.variable): {
                'offset': "0x0 ... 0x{:x}".format(bamboo.mmio_size),
                'value': "0x0"
            }}
        self.variable += 1

    def print_pretty(self):
        for bamboo in self.bamboos:
            yield bamboo.__str__()

    def convert_address(self, address):
        if isinstance(address, str):
            address = int(address, 16)
        for k, mapping in self.mapping.items():
            va = int(mapping['va'], 16)
            size = int(mapping['size'], 16)
            if va < address < va + size:
                pa = int(mapping['pa'], 16)
                return pa + (address - va)
        return address

    def run(self, firmware):
        self.bamboos = []  # clear otherwise dupicated mmio regions
        dabt = self.analysis_manager.get_analysis('data_abort')
        assert isinstance(dabt, DataAbort)

        # load bamboo devices
        if firmware.profile is None:
            # in diagnosis mode
            bamboo_devices = {}
            # load va/pa mapping
            self.mapping = {}
        else:
            bamboo_devices = firmware.get_bamboo_devices()
            self.mapping = firmware.get_va_pa_mapping()

        for name, parameters in bamboo_devices.items():
            bamboo = Bamboo()
            bamboo.name = name
            bamboo.mmio_base = int(parameters['mmio_base'], 16)
            bamboo.mmio_size = int(parameters['mmio_size'], 16)
            bamboo.registers = parameters['registers']
            self.variable += len(bamboo.registers)
            self.bamboos.append(bamboo)

        # get dead addresses
        for dead_address in dabt.dead_addresses:
            bamboo = Bamboo()
            bamboo.mmio_base = self.convert_address(int(dead_address, 16) & 0xFFFFFF00)
            bamboo.mmio_size = 0x100
            if self.insert(bamboo):
                self.init_registers(bamboo)

        for message in self.print_pretty():
            self.info(firmware, message, 1)

        # update bamboos
        if firmware.profile is None:
            return True
        latest_bamboo_devices = {}
        for bamboo in self.bamboos:
            latest_bamboo_devices[bamboo.name] = {
                'mmio_base': hex(bamboo.mmio_base),
                'mmio_size': hex(bamboo.mmio_size),
                'registers': bamboo.registers
            }
        firmware.set_bamboo_devices(latest_bamboo_devices)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'bamboos'
        self.description = 'add bamboo devices after DataAbort and InitValue'
        self.context['hint'] = 'bad bad bad trace'
        self.critical = False
        self.required = ['data_abort', 'init_value']
        self.type = 'diag'
        #
        self.bamboos = []
        self.variable = 0
        self.mapping = {}
