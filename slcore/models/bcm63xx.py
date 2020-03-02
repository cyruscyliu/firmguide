"""
source code at
    /mnt/iscsi/openwrt-build-docker/share/15.05-0af6774c7e18315cb7b5479646f33141/./chaos_calmer-15.05/build_dir/target-mips_mips32_uClibc-0.9.33.2/linux-brcm63xx_smp/linux-3.18.20

def FUNCTION__CALLER(config):
    return [FUNCTION_TO_BE_ANALYZED]
"""
##### of_irq_init #####
def of_irq_init__irqchip_init(config):
    # [+] [bingo] ('IRQCHIP_DECLARE', 'brcm,bcm6345-ext-intc', 'bcm6345_ext_intc_of_init') in ...d_dir/target-mips_mips32_uClibc-0.9.33.2/linux-brcm63xx_smp/linux-3.18.20/drivers/irqchip/irq-bcm6345-ext.c
    # [+] [bingo] ('IRQCHIP_DECLARE', 'brcm,bcm6345-periph-intc', 'bcm6345_periph_of_init') in ...d_dir/target-mips_mips32_uClibc-0.9.33.2/linux-brcm63xx_smp/linux-3.18.20/drivers/irqchip/irq-bcm6345-periph.c
    return ['bcm6345_ext_intc_of_init', 'bcm6345_periph_of_init']


##### irq_set_chip_and_handler_name #####
def irq_set_chip_and_handler_name__bcm6345_periph_map(config):
    # drivers/irqchip/irq-bcm6345-periph.c
    if 'brcm,bcm6345-periph-intc' not in config:
        config['brcm,bcm6345-periph-intc'] = {}
    # irq_set_chip_and_handler(irq, &priv->chip, handle_level_irq);
    config['brcm,bcm6345-periph-intc']['handler'] = 'handle_level_irq'
    # data->chip.irq_mask = bcm6345_periph_irq_mask;
    # data->chip.irq_unmask = bcm6345_periph_irq_unmask;
    config['brcm,bcm6345-periph-intc']['actions'] = {
        'mask': '(1 << irqn)',
        'unmask': '(1 << irqn)'
    }
    return []


##### irq_set_handler #####
##### irq_set_chained_handler_and_data #####
def irq_set_handler____bcm6345_periph_intc_init(config):
    # drivers/irqchip/irq-bcm6345-periph.c
    if 'brcm,bcm6345-periph-intc' not in config:
        config['brcm,bcm6345-periph-intc'] = {}
    # irq_set_chained_handler(block->parent_irq, bcm6345_periph_irq_handle);
    # in bcm6345_periph_irq_handle
    # pending = __raw_readl(block->en_reg[idx]) & __raw_readl(block->status_reg[idx]);
    # hw_irq = find_next_bit(((&pending)))
    config['brcm,bcm6345-periph-intc']['irq_to_regs'] = {
        'irqn': 'i', 'set_body': '(1 << irqn)', 'clear_body': '(1 << irqn)'
    }
    return []


def irq_set_handler____bcm6345_ext_intc_init(config):
    # drivers/irqchip/irq-bcm6345-ext.c
    if 'brcm,bcm6345-ext-intc' not in config:
        config['brcm,bcm6345-ext-intc'] = {}
    # irq_set_chained_handler(irqs[i], bcm6345_ext_intc_irq_handle);
    # in bcm6345_ext_intc_irq_handle, it will never read from MMIO
    config['brcm,bcm6345-ext-intc']['irq_to_regs'] = {}
    return []

##### irq_domain_add_simple #####
##### irq_domain_add_simple(of_node, size, first_irq, ops, ...) #####
##### irq_domain_add_legacy #####
def irq_domain_add_simple____bcm6345_periph_intc_init(config):
    # drivers/irqchip/irq-bcm6345-periph.c
    if 'brcm,bcm6345-periph-intc' not in config:
        config['brcm,bcm6345-periph-intc'] = {}
    # data->domain = irq_domain_add_simple(node, 32 * num_words, 8, &bcm6345_periph_domain_ops, data);
    return ['bcm6345_periph_map']


def irq_domain_add_simple____bcm6345_ext_intc_init(config):
    # drivers/irqchip/irq-bcm6345-periph.c
    if 'brcm,bcm6345-periph-intc' not in config:
        config['brcm,bcm6345-periph-intc'] = {}
    # data->domain = irq_domain_add_simple(node, num_irqs, start, &bcm6345_ext_domain_ops, data);
    return ['bcm6345_ext_intc_map']


##### of_clk_init #####


bcm63xx_fcbs = {
    'plat_irq_dispatch':{
        'ignored': True
    }, 'of_irq_init': {
        'irqchip_init': of_irq_init__irqchip_init,
        'ignored': False,
    }, 'mips_cpu_irq_init': {
        'ignored': True
    }, '__irq_set_handler': {
        '__bcm6345_periph_intc_init': irq_set_handler____bcm6345_periph_intc_init,
        '__bcm6345_ext_intc_init': irq_set_handler____bcm6345_ext_intc_init,
        'ignored': False
    } ,'irq_set_chip_and_handler_name': {
        'bcm6345_periph_map': irq_set_chip_and_handler_name__bcm6345_periph_map,
        'ignored': False
    }, 'irq_set_chained_handler_and_data': {
        'ignored': False
    }, 'irq_domain_add_legacy': {
        'ignored': False
    }, '__irq_domain_add': {
        'ignored': False
    }, 'irq_domain_add_simple': {
        '__bcm6345_periph_intc_init': irq_domain_add_simple____bcm6345_periph_intc_init,
        '__bcm6345_ext_intc_init': irq_domain_add_simple____bcm6345_ext_intc_init,
        'ignored': False
    }, 'panic': {
        'ignored': True
    }, 'of_clk_init': {
        'ignored': True
    }, 'r4k_clockevent_init': {
        'ignored': True
    }, 'init_r4k_clocksource': {
        'ignored': True
    }
}
