import os
import yaml

from analyses.manager import AnalysesManager
from slcore.environment import restore_analysis, save_analysis
from slcore.models.bcm63xx import bcm63xx_fcbs
from slcore.models.ath79 import ath79_fcbs


def run_binary_analysis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_tree = analyses_manager.register_binary_analysis()
    status = analyses_manager.run(target_analyses_tree=analyses_tree)

    return False


def run_static_analysis(firmware, binary=True):
    # restore what we have done
    restore_analysis(firmware)

    analyses_manager = AnalysesManager(firmware)
    analyses_tree = analyses_manager.register_static_analysis()
    status = analyses_manager.run(target_analyses_tree=analyses_tree)

    save_analysis(firmware)
    return status


def run_diagnosis(firmware):
    analyses_manager = AnalysesManager(firmware)
    analyses_tree = analyses_manager.register_diagnosis()

    max_iteration = firmware.max_iteration

    status = False
    while max_iteration:
        max_iteration -= 1
        try:
            status = analyses_manager.run(target_analyses_tree=analyses_tree)
        except SystemExit:
            break

    firmware.set_iteration(firmware.max_iteration - max_iteration)
    if not firmware.get_stage('user_mode') and firmware.debug:
        firmware.qemuc.debug(firmware.running_command, firmware.srcodec.get_path_to_vmlinux())

    return status


def run_model(firmware):
    srcodec = firmware.get_srcodec()

    if firmware.uuid == 'ath79':
        fcbs = ath79_fcbs
    elif firmware.uuid == 'bcm63xx':
        fcbs = bcm63xx_fcbs
    else:
        print('cannot support {0}, please add ./slcore/models/{0}.py and from slcore.models.{0} import {0}_fcbs'.format(firmware.uuid))
        return

    if firmware.uuid == 'ar71xx_generic':
        ## =========== from stinc.py =============
        firmware.insert_bamboo_devices(0x18060010, 0x4, value=0x10000000)
        firmware.insert_bamboo_devices(0x18060014, 0x4, value=0x10000000)
        ## =======================================
        ## =========== from stimer.py ==============
        firmware.insert_bamboo_devices(0x18050000, 0x4, value=0x10)
        ## =========================================

    # ===== intc subsystem =====
    # 1. get_irqnr_and_base/plat_irq_dispatch(not neccesory)
    if firmware.get_arch() == 'arm':
        # FOR ARM, we have get_irqnr_preamble, get irqnr_and_base
        # which together are also named arch_irq_handler_default after ?(at least >2.16)
        # and handler_arch_irq which is a global function pointer which is
        # defined by set_handle_irq separately.
        if firmware.uuid == 'oxnas_generic':
            # in of_gic_init, we have set_handle_irq(gic_handle_irq)
            ep = 'gic_handle_irq'
            # irqnr = readl(base+0xc) & 0x3ff
            irqn_to_reg = "[irqn: i, set_body: ['s->r0 = i;'], clear_body: ['s->r0 = 0xffffffff;']"
            get_register0 = "{rname: r0, offset: '0x0c', mask_ack: False, mask: False, unmask: False, ack: False}"
            get_register1 = "{rname: r1, offset: '0x10', mask_ack: False, mask: False, unmask: False, ack_action: (i), ack: True}"
            # self.info(firmware, 'irqn_to_reg: {}'.format(irqn_to_reg), 1)
            # self.info(firmware, 'get_register: {}'.format(get_register0), 1)
            # self.info(firmware, 'get_register: {}'.format(get_register1), 1)
    elif firmware.get_arch() == 'mips':
        # doesn't works well, ignore this one
        # srcodec.traverse_funccalls2(['plat_irq_dispatch'], caller='irq_handler', fcbs=fcbs)
        pass
    # 2 intc initilization
    ep = 'init_IRQ'
    srcodec.traverse_funccalls2([ep], caller='start_kernel', fcbs=fcbs)
    # for mips, you could skip plat_irq_dispatch because it is very general
    # mostly, timer interrupt is IRQ7 and you won't worry about it

    # ==== timer subsystem ====
    ep = 'time_init'
    # this is a simple implementation
    # For mips, time_init includes plat_time_init and
    # mips_clockevent_init, cpu_has_mfc0_count_bug, init_mips_clocksource.
    # Recursively, if time_init has r4k_clockevent_init, r4k_clockevent_init
    # this machine can use the r4k compatile counter as interrupt source
    # and clock source. At the same time, mips_hpt_frequency must be defined
    # to not zero in plat_time_init. Other cases can be discussed seperately.
    srcodec.traverse_funccalls2([ep], caller='start_kernel', fcbs=fcbs)

    path_to_config = os.path.join(firmware.get_target_dir(), 'config.yaml')
    with open(path_to_config, 'w') as f:
        yaml.safe_dump(srcodec.config, f)
    print('config save at {}'.format(path_to_config))

