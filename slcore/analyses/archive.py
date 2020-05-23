import os

from slcore.amanager import Analysis
from slcore.database.dbf import get_database
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.common import load_dtb


class Archive(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'archive'
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
        source = os.path.join(
            self.analysis_manager.project.attrs['path'], 'qemu-4.0.0')
        target_machines = os.path.join(
            self.analysis_manager.project.attrs['base_dir'],
            'examples/machines/{}'.format(self.firmware.get_machine_name()))
        os.makedirs(target_machines, exist_ok=True)
        os.system('cp -r {}/* {}'.format(source, target_machines))

        # only compatible can be updated automatically
        realdtb = self.firmware.get_realdtb()
        archivedtb = os.path.join(
            self.analysis_manager.project.attrs['base_dir'],
            'slcore/database/archivedtb',
            self.firmware.get_machine_name() + '.dtb')
        os.system('cp {} {}'.format(realdtb, archivedtb))
        realdts = load_dtb(realdtb)
        compatible = find_compatible_in_fdt(realdts)

        # update database support
        support = get_database('support')
        board = support.select('board', arch=self.firmware.get_arch(),
                               board=self.firmware.get_board())
        if board is None:
            board = {'device_tree': True, 'support_list': {}}

        brand = self.firmware.get_brand()
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
                'arch': self.firmware.get_arch(),
                'endian': self.firmware.get_endian(),
            }
            self.info('update {} {}'.format(
                cmptbl, board['support_list'][cmptbl]), 1)

        support = support.update(
            self.firmware.get_board(),
            arch=self.firmware.get_arch(), board=board)
        return True
