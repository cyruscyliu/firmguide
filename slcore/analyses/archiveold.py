import os

from slcore.amanager import Analysis
from slcore.database.dbf import get_database
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.common import load_dtb


class Archive2(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'archiveold'
        self.description = 'Archive the device tree blob/QEMU source.'
        self.required = []

    def run(self, **kwargs):
        """
        Must be called after entering user level.

        1. Only diagnose will update profile's runtime properties.
        2. We don't save profile.yaml directly.
        3. We save QEMU source as examples.
        4. We save the dtb as the most important reference.
        """
        # save QEMU source as examples
        machine_name = self.analysis_manager.firmware.get_machine_name()
        source = os.path.join(
            self.analysis_manager.project.attrs['path'], machine_name)
        if not os.path.exists(source):
            self.error_info = '{} doesn\'t exist'.format(source)
            return False

        target_machines = os.path.join(
            self.analysis_manager.project.attrs['base_dir'],
            'examples/machines/{}'.format(self.analysis_manager.firmware.get_machine_name()))
        os.makedirs(target_machines, exist_ok=True)
        os.system('cp -r {}/* {}'.format(source, target_machines))

        # only compatible can be updated automatically
        realdtb = self.analysis_manager.firmware.get_realdtb()
        if realdtb is None:
            self.error_info = 'there is no realdtb set'
            return False
        archivedtb = os.path.join(
            self.analysis_manager.project.attrs['base_dir'],
            'slcore/database/archivedtb',
            self.analysis_manager.firmware.get_machine_name() + '.dtb')
        os.system('cp {} {}'.format(realdtb, archivedtb))
        realdts = load_dtb(realdtb)
        compatible = find_compatible_in_fdt(realdts)

        # update database support
        support = get_database('support')
        board = support.select('board', arch=self.analysis_manager.firmware.get_arch(),
                               board=self.analysis_manager.firmware.get_board())
        if board is None:
            board = {'device_tree': True}

        if 'support_list' not in board:
            board['support_list'] = {}

        brand = self.analysis_manager.firmware.get_brand()
        target = self.analysis_manager.project.attrs['target']
        subtarget = self.analysis_manager.project.attrs['subtarget']

        l = len(self.analysis_manager.project.attrs['base_dir'])
        for cmptbl in compatible:
            board['support_list'][cmptbl] = {
                'brand': brand,
                'target': target,
                'subtarget': subtarget,
                'realdtb': archivedtb[l + 1:],
                'example': target_machines[l + 1:],
                'arch': self.analysis_manager.firmware.get_arch(),
                'endian': self.analysis_manager.firmware.get_endian(),
                'loaddr': self.analysis_manager.firmware.get_kernel_load_address(),
            }
            self.info('update {} {}'.format(
                cmptbl, board['support_list'][cmptbl]), 1)

        support = support.update(
            self.analysis_manager.firmware.get_board(),
            arch=self.analysis_manager.firmware.get_arch(), board=board)
        return True
