import os
import yaml

from slcore.models.ath79 import ath79_fcbs
from slcore.project import get_current_project
from slcore.environment import migrate, snapshot, archive
from slcore.srcodec import SRCodeController


def run_model(firmware):
    srcodec = firmware.get_srcodec()

    if firmware.uuid == 'ath79':
        fcbs = ath79_fcbs
    else:
        print('cannot support {0}, please add ./slcore/models/{0}.py'.format(firmware.uuid))
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


def project_model_ict():
    project = get_current_project()
    if project is None:
        return

    target_dir = project.attrs['target_dir']
    path_to_profile = os.path.join(target_dir, 'profile.yaml')
    if not os.path.exists(path_to_profile):
        path_to_profile = None

    firmware = migrate(project.attrs['uuid'], path_to_profile=path_to_profile)
    firmware.set_arch(project.attrs['arch'])
    firmware.set_endian(project.attrs['endian'])

    # 2.1 low level source code controller
    srcodec = SRCodeController()
    path_to_source_code = project.attrs['source']
    srcodec.set_path_to_source_code(path_to_source_code)
    srcodec.set_path_to_vmlinux(os.path.join(path_to_source_code, 'vmlinux'))
    srcodec.set_path_to_dot_config(os.path.join(path_to_source_code, '.config'))
    srcodec.set_path_to_cross_compile(project.attrs['cross_compile'])
    srcodec.set_endian(project.attrs['endian'])
    srcodec.set_arch(project.attrs['arch'])
    srcodec.set_path_to_makeout(project.attrs['makeout'])
    firmware.srcodec = srcodec

    # 3. analyze the source code
    status = run_model(firmware)

    # 4. take snapshots to save results
    status = snapshot(firmware)
    return archive(firmware)

