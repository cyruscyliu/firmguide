"""
source code at
    /root/openwrt-build-docker/share/19.07.1-ath79-generic/openwrt-19.07.1/build_dir/target-mips_24kc_musl/linux-ath79_generic/linux-4.14.167

def FUNCTION__CALLER(config):
    return [FUNCTION_TO_BE_ANALYZED]
"""
##### of_irq_init #####
def of_irq_init__irqchip_init(config):
    # compatible = "qca,ar7100-cpu-intc"
    # compatible = "qca,ar9340-intc"
    # compatible = "qca,ar7240-misc-intc"
    return ['ar79_cpu_intc_of_init', 'ath79_intc_of_init', 'ar7240_misc_intc_of_init']


#####

##### irq_set_chip_and_handler_name #####
def irq_set_chip_and_handler_name__mips_cpu_intc_map(config):
    # drivers/irqchip/irq-mips-cpu.c
    # irq_set_chip_and_handler(irq, chip, handle_percpu_irq);
    if 'qca,ar7100-cpu-intc' not in config:
        config['qca,ar7100-cpu-intc'] = {}
    config['qca,ar7100-cpu-intc']['handler'] = 'handler_percpu_irq'
    config['qca,ar7100-cpu-intc']['actions'] = {}
    return []


def irq_set_chip_and_handler_name__ath79_intc_map(config):
    # drivers/irqchip/irq-ath79-intc.c
    # irq_set_chip_and_handler(irq, &intc->chip, handle_level_irq);
    if 'qca,ar9340-intc' not in config:
        config['qca,ar9340-intc']
    config['qca,ar9340-intc']['handler'] = 'handle_level_irq'
    # intc->chip = dummy_irq_chip // nothing to do
    config['qca,ar9340-intc']['actions'] = {}
    return []


def irq_set_chip_and_handler_name__misc_map(config):
    # drivers/irqchip/irq-ath79-misc.c
    # irq_set_chip_and_handler(irq, &ath79_misc_irq_chip, handle_level_irq);
    if 'qca,ar7240-misc-intc' not in config:
        config['qca,ar7240-misc-intc'] = {}
    config['qca,ar7240-misc-intc']['actions'] = {
        'mask': {'action': '(1 << irqn)', 'rname': 'r1'}, # r1=0x04
        'unmask': {'action': '(1 << irqn)', 'rname': 'r1'}
    }
    return []


##### irq_set_handler #####
##### irq_set_chained_handler_and_data #####
def irq_set_handler__ath79_intc_of_init(config):
    # drivers/irqchip/irq-ath79-intc.c
    # irq_set_chained_handler_and_data(intc->irq, ath79_intc_irq_handler, domain);
    # in ath70_intc_irq_handler, this will be very hard
    # we'll ignore this intc because it has nothing to do with uarts
    # pending = ath79_reset_rr(intc->int_status); # 0xac, load from dt
    # pending &= intc->pending_mask;
    # if (pending) {
    #   for (i = 0; i < domain->hwirq_max; i++)
    #     if (pending & intc->irq_mask[i]) { # all load from dt
    #       if (intc->irq_wb_chan[i] != 0xffffffff)
    #         ath79_ddr_wb_flush(intc->irq_wb_chan[i]);
    #         generic_handle_irq(irq_find_mapping(domain, i));
    if 'qca,ar9340-intc' not in config:
        config['qca,ar9340-intc'] = {}
    config['qca,ar9340-intc']['irqn_to_regs'] = [
        {'irqn': 0, 'set_body': ['s->r43 = 0x1f000;'], 'clear_body': ['s->r43 = 0;']},
        {'irqn': 1, 'set_body': ['s->r43 = 0x01000000;'], 'clear_body': ['s->r43 = 0;']},
        {'irqn': 2, 'set_body': ['s->r43 = 0x10000000;'], 'clear_body': ['s->r43 = 0;']},
    ]
    config['qca,ar9340-intc']['get_registers'] = []
    config['qca,ar9340-intc']['get_registers'].append({'rname': 'r43', 'offset': '0xac'})
    return []


def irq_set_handler__ath79_misc_intc_domain_init(config):
    # drivers/irqchip/irq-ath79-misc.c
    # irq_set_chained_handler_and_data(irq, ath79_misc_irq_handler, domain);
    # in ath79_misc_irq_handler
    if 'qca,ar7240-misc-intc' not in config:
        config['qca,ar7240-misc-intc'] = {}
    # panding __ffs(*(base+0x0)&*(base+0x4))
    config['qca,ar7240-misc-intc']['irqn_to_regs'] = {
        'irqn': 'i', 'set_body': ['s->r0 |= (1 << i);'], 'clear_body': ['s->r0 &= ~(1 << i);']}
    config['qca,ar7240-misc-intc']['get_registers'] = []
    config['qca,ar7240-misc-intc']['get_registers'].append({'rname': 'r0', 'offset': '0x00'})
    config['qca,ar7240-misc-intc']['get_registers'].append({'rname': 'r1', 'offset': '0x04'})
    return []


##### irq_domain_add_legacy #####
def irq_domain_add_legacy____mips_cpu_irq_init(config):
    # qca,ar7100-cpu-intc is as a matter of fact mips internal intc
    # irq_domain = irq_domain_add_legacy(of_node, 8, 0, 0, &mips_cpu_intc_irq_domain_ops, ((void *)0));
    if 'qca,ar7100-cpu-intc' not in config:
        config['qca,ar7100-cpu-intc'] = {}
    config['qca,ar7100-cpu-intc']['extend'] = 'mti,cpu-interrupt-controller'
    return ['mips_cpu_intc_map']


def irq_domain_add_legacy__ath79_intc_of_init(config):
    # qca,ar9340-intc
    # domain = irq_domain_add_linear(node, cnt, &ath79_irq_domain_ops, intc); # LINERALY
    if 'qca,ar9340-intc' not in config:
        config['qca,ar9340-intc'] = {}
    return ['ath79_intc_map']


def irq_domain_add_legacy__ath79_misc_intc_of_init(config):
    # qca,ar7240-misc-intc
    # domain = irq_domain_add_linear(node, 32, &misc_irq_domain_ops, base);
    return ['misc_map']


##### of_clk_init #####
def of_clk_init__irqchip_init(config):
    # [+] [bingo] ('CLK_OF_DECLARE', 'fixed-clock', 'of_fixed_clk_setup') in ...sl/linux-ath79_generic/linux-4.14.167/drivers/clk/clk-fixed-rate.c
    # [+] [bingo] ('CLK_OF_DECLARE', 'qca,qca9530-pll', 'ath79_clocks_init_dt') in ...sl/linux-ath79_generic/linux-4.14.167/arch/mips/ath79/clock.c
    return ['of_fixed_clk_setup', 'ath79_clocks_init_dt']


ath79_fcbs = {
    'plat_irq_dispatch':{
        'ignored': True
    }, 'of_irq_init': {
        'irqchip_init': of_irq_init__irqchip_init,
        'ignored': False,
    },'irq_set_chip_and_handler_name': {
        'mips_cpu_intc_map': irq_set_chip_and_handler_name__mips_cpu_intc_map,
        'ath79_intc_map': irq_set_chip_and_handler_name__ath79_intc_map,
        'misc_map': irq_set_chip_and_handler_name__misc_map,
        'ignored': False
    }, 'irq_set_chained_handler_and_data': {
        'ath79_misc_intc_domain_init': irq_set_handler__ath79_misc_intc_domain_init,
        'ath79_intc_of_init': irq_set_handler__ath79_intc_of_init,
        'ignored': False
    }, 'irq_domain_add_legacy': {
        '__mips_cpu_irq_init': irq_domain_add_legacy____mips_cpu_irq_init,
        'ignored': False
    }, '__irq_domain_add': {
        'ath79_intc_of_init': irq_domain_add_legacy__ath79_intc_of_init,
        'ath79_misc_intc_of_init': irq_domain_add_legacy__ath79_misc_intc_of_init,
        'ignored': False
    }, 'panic': {
        'ignored': True
    }, 'of_clk_init': {
        'plat_time_init': of_clk_init__irqchip_init,
        'ignored': True
    }, 'r4k_clockevent_init': {
        'ignored': True
    }, 'init_r4k_clocksource': {
        'ignored': True
    }
}
