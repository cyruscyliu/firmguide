import os
import sys

sys.path.extend(['.', '..'])

from settings import *
from slcore.srcodec import SRCodeController


def srcodec_callgraph_test():
    srcodec = SRCodeController(BASE_DIR, '', '')

    # test 1
    test_1 = os.path.join('tests/srcodec_setup.i')

    test_1_1 = srcodec.get_funccalls(test_1, 'plat_time_init', mode='sparse')
    print(test_1_1)
    # ['ath79_clocks_init', 'ath79_get_sys_clk_rate', 'ath79_get_sys_clk_rate', 'ath79_get_sys_clk_rate', 'ath79_get_sys_clk_rate', 'printk']

    test_1_2 = srcodec.get_funccalls(test_1, 'ath79_setup', mode='sparse')
    print(test_1_2)
    # ['ath79_gpio_init', 'ath79_register_uart', 'ath79_register_wdt', 'mips_machine_setup']

    # test 2
    test_2 = os.path.join('tests/srcodec_irq.i')
    test_2_1 = srcodec.get_funccalls(test_2, 'arch_init_irq', mode='sparse')
    print(test_2_1)


if __name__ == '__main__':
    srcodec_callgraph_test()

