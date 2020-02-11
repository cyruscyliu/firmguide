from unittest import TestCase
from slcore.srcodec import SRCodeController
from settings import *

import os
import sys

class TestSRCodeController(TestCase):
    def test_get_funccalls(self):
        srcodec = SRCodeController()
        srcodec.set_path_to_source_code(BASE_DIR)

        # test 1
        test_1 = os.path.join('tests/srcodec_setup.i')

        test_1_1 = srcodec.get_funccalls(test_1, 'plat_time_init', mode='sparse')
        self.assertEqual(
            ['ath79_clocks_init', 'ath79_get_sys_clk_rate', 'ath79_get_sys_clk_rate',
             'ath79_get_sys_clk_rate', 'ath79_get_sys_clk_rate', 'printk'],
            test_1_1
        )

        test_1_2 = srcodec.get_funccalls(test_1, 'ath79_setup', mode='sparse')
        self.assertEqual(
            ['ath79_gpio_init', 'ath79_register_uart', 'ath79_register_wdt', 'mips_machine_setup'],
            test_1_2
        )

        # test 2
        test_2 = os.path.join('tests/srcodec_irq.i')
        test_2_1 = srcodec.get_funccalls(test_2, 'arch_init_irq', mode='sparse')
        self.assertEqual(
            ['__builtin_unreachable', 'ath79_misc_irq_init', 'ar934x_ip2_irq_init',
             'qca955x_irq_init', 'qca956x_irq_init', 'mips_cpu_irq_init'],
            test_2_1
        )

    def test_get_globals(self):
        srcodec = SRCodeController()
        srcodec.set_path_to_source_code(BASE_DIR)

        # test 2
        test_2 = os.path.join('tests/srcodec_irq.i')
        test_2_1 = srcodec.get_globals(test_2, 'arch_init_irq', mode='sparse')
        self.assertEqual({
            'dummy_irq_chip': ['load'],
            'ip2_chip': ['store', 'store', 'store'],
            'ip3_chip': ['store', 'store', 'store'],
            'ath79_soc': ['load', 'load'],
            'ath79_ip2_handler': ['store', 'store', 'store', 'store', 'store', 'store', 'store', 'store'],
            'ath79_ip3_handler': ['store', 'store', 'store', 'store', 'store', 'store', 'store', 'store'],
            'cp0_perfcount_irq': ['store']
        }, test_2_1)

