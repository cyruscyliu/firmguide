"""
source code at
    ...

def FUNCTION__CALLER(config):
    return [FUNCTION_TO_BE_ANALYZED]
"""
##### of_irq_init #####


##### irq_set_chip_and_handler_name #####


##### irq_set_handler #####
##### irq_set_chained_handler_and_data #####


##### irq_domain_add_legacy #####


##### of_clk_init #####


##### clockevents_register_device #####


#### init_r4k_clocksource #####


uuid_fcbs = {
    'plat_irq_dispatch':{
        'ignored': True
    }, 'of_irq_init': {
        'ignored': False,
    },'irq_set_chip_and_handler_name': {
        'ignored': False
    }, 'irq_set_chained_handler_and_data': {
        'ignored': False
    }, 'irq_domain_add_legacy': {
        'ignored': False
    }, '__irq_domain_add': {
        'ignored': False
    }, 'panic': {
        'ignored': True
    }, 'of_clk_init': {
        'ignored': True
    }, 'r4k_clockevent_init': {
        'ignored': False
    }, 'init_r4k_clocksource': {
        'ignored': False
    }
}
