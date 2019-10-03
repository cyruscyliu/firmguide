from unittest import TestCase

import os
import fdt


class TestByDeviceTree(TestCase):
    def test_by_device_tree(self):
        with open(os.path.join(os.getcwd(), 'test.dtb'), 'rb') as f:
            dtb = f.read()
        dtc = fdt.parse_dtb(dtb)
        compatible = dtc.get_property('compatible', '/')
        self.assertListEqual(['plxtech,nas7820', 'plxtech,nas782x'], compatible.data)
        model = dtc.get_property('model', '/')
        self.assertListEqual(['Shuttle KD20'], model.data)
        cpus = dtc.get_node('/cpus')
        for cpu in cpus.nodes:
            self.assertListEqual(
                ['arm,arm11mpcore'],
                dtc.get_property('compatible', '/cpus/{}'.format(cpu.name)).data)
        self.assertListEqual([0, 0], dtc.get_property('reg', '/memory').data)
