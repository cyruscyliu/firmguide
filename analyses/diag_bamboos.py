"""
Add bamboo devices after DataAbort and InitValue.
"""
from analyses.analysis import Analysis
from analyses.diag_dabt import DataAbort
from analyses.inf_libtooling import LibTooling


class Bamboos(Analysis):
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
        dabt = self.analysis_manager.get_analysis('data_abort')
        assert isinstance(dabt, DataAbort)
        libtooling = self.analysis_manager.get_analysis('kerberos')
        assert isinstance(libtooling, LibTooling)

        firmware.load_bamboo_devices()
        self.mapping = firmware.get_va_pa_mapping()

        # get dead addresses/bamboo
        target_addresses = dabt.dead_addresses + libtooling.bamboo_address
        for target_address in target_addresses:
            mmio_base = self.convert_address(int(target_address, 16) & 0xFFFFFFF0)
            not_overlapping = firmware.insert_bamboo_devices(mmio_base, 0x10, value=0)
            if not not_overlapping:
                self.info(firmware, 'check if there is overlapping for (0x{:x}, 0x{:x}'.format(
                    mmio_base, 0x10), 1)

        for bamboo_device in firmware.print_bamboo_devices():
            self.info(firmware, bamboo_device, 1)

        # update bamboos
        firmware.update_bamboo_devices()
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
        self.mapping = {}
