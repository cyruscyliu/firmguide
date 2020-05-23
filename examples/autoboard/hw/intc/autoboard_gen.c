/*
 * autoboard maybe auto generated implementation
 */

#include "qemu/osdep.h"

#include "hw/intc/autoboard_intc.h"
#include "hw/intc/autoboard_edge_irq.h"
#include "hw/intc/autoboard_level_irq.h"
#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_utils.h"

// xxx_verify is untested & no use currently
static uint8_t bit_verify(auto_trifle *at, uint32_t bit_pos, uint32_t raise)
{
    uint32_t tmp;

    if (at->type == TRIFLE_KER_WRITE) {
        tmp = 1 << bit_pos;

        if (raise)
            return ((tmp & at->old_val) == 0) && ((tmp & at->new_val) == tmp);
        else
            return ((tmp & at->old_val) == tmp) && ((tmp & at->new_val) == 0);
    } else 
        return false;
}

static uint8_t constraint_verify(auto_trifle *at)
{
    return ACU_ST_MISMATCH;
}

uint8_t try_process_at_on_acu(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    switch (acu->type) {
        case ACU_DO_WATCH_READ:
        {
            if ((at->type != TRIFLE_KER_READ) || (at->off != acu->off))
                return ACU_ST_MISMATCH;
        }
            break;
        case ACU_DO_WATCH_WRITE:
        {
            if ((at->type != TRIFLE_KER_WRITE) || (at->off != acu->off))
                return ACU_ST_MISMATCH;

            if (!acu->match_write_cnt(s, acu, at))
                return ACU_ST_MISMATCH;
        }
            break;
        case ACU_DO_WATCH_HWEVT:
        {
            if ((at->type != TRIFLE_HW_EVT) || (at->hw_evt != acu->hw_evt))
                return ACU_ST_MISMATCH;
        }
            break;
        case ACU_DO_REACT:
        {
            acu->do_react(s, acu, at);
        }
            break;
        default:
            assert(false && "this should not be executed");
            break;
    }

    return (acu->next) ? (ACU_ST_NEXT) : (ACU_ST_DONE);
}

/*
 * generic configs for convenient reuse
 */

static auto_config_action wait_hw_evt_lvl_evt_reset_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = LVL_EVT_RESET,
            .next = 0,
        }
    }
};

static auto_config_action wait_hw_evt_lvl_evt_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = LVL_EVT_ACT,
            .next = 0,
        }
    }
};

static auto_config_action wait_hw_evt_lvl_evt_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = LVL_EVT_DEACT,
            .next = 0,
        }
    }
};

static auto_config_action wait_hw_evt_edge_evt_reset_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = EDGE_EVT_RESET,
            .next = 0,
        }
    }
};

static auto_config_action wait_hw_evt_edge_evt_pulse_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = EDGE_HW_EVT_PULSE_UP,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_HWEVT,
            .hw_evt = EDGE_HW_EVT_PULSE_DOWN,
            .next = 0,
        },
    }
};

/*
 * for ramips.rt3883
 *
 * we only need 1 irq for uart
 * 
 * for the ramips.rt3883:
 *  0x0  - status 1
 *  0x34 - enable
 *  0x38 - disable
 * 
 * static u32 rt_intc_regs[] = {
 *     [INTC_REG_STATUS0] = 0x00,
 *     [INTC_REG_STATUS1] = 0x04,
 *     [INTC_REG_TYPE] = 0x20,
 *     [INTC_REG_RAW_STATUS] = 0x30,
 *     [INTC_REG_ENABLE] = 0x34,
 *     [INTC_REG_DISABLE] = 0x38,
 * };
 *
 * for the bit 31 of enable/disable, it controls the global enable/disable
 * see more details, in https://cdn.sparkfun.com/datasheets/Wireless/WiFi/RT5350.pdf
 *
 */

#define RAMIPS_RT3883_MMIO_LEN 0x100
#define RAMIPS_RT3883_AUTOBOARD_IRQ_NUM 32

static uint8_t ramips_rt3883_uart_is_init_func_0(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)0xffffffff);
}

static uint8_t ramips_rt3883_uart_is_init_func_1(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)0x0);
}

static uint8_t ramips_rt3883_uart_is_init_func_2(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)(0x1 << 31));
}

static auto_config_action ramips_rt3883_uart_is_init_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x38,
            .match_write_cnt = ramips_rt3883_uart_is_init_func_0,
            .next = 1,
        },{
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x20,
            .match_write_cnt = ramips_rt3883_uart_is_init_func_1,
            .next = 2,
        },{
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x34,
            .match_write_cnt = ramips_rt3883_uart_is_init_func_2,
            .next = 0,
        }
    }
};

static uint8_t ramips_rt3883_uart_is_msk_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at) 
{
    return at->new_val == ((uint32_t)(0x1 << acu->irq));
}

static auto_config_action ramips_rt3883_uart_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x38,
            .irq = 12,
            .match_write_cnt = ramips_rt3883_uart_is_msk_func,
            .next = 0,
        }
    },
};

static uint8_t ramips_rt3883_uart_is_unmsk_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at) 
{
    return at->new_val == ((uint32_t)(0x1 << acu->irq));
}

static auto_config_action ramips_rt3883_uart_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x34,
            .irq = 12,
            .match_write_cnt = ramips_rt3883_uart_is_unmsk_func,
            .next = 0,
        }
    }
};

static uint8_t ramips_rt3883_uart_do_act_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    //uint32_t val = s->aummio->read(s->aummio, acu->off);
    //printf("[+] uart act write before 0x%x, size %d, value 0x%x\n", acu->off, 4, val);
    //s->aummio->write(s->aummio, acu->off, val | (uint32_t)(1 << acu->irq));
    s->aummio->write(s->aummio, acu->off, (uint32_t)(1 << acu->irq));
    //printf("[+] uart act write after 0x%x, size %d, value 0x%x\n", acu->off, 4, val | (uint32_t)(1 << acu->irq));
    return 0;
}

static auto_config_action ramips_rt3883_uart_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .off = 0x0,
            .irq = 12,
            .do_react = ramips_rt3883_uart_do_act_func,
            .next = 0,
        }
    }
};

static uint8_t ramips_rt3883_uart_do_deact_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    //uint32_t val = s->aummio->read(s->aummio, acu->off);
    //printf("[+] uart de-act write before 0x%x, size %d, value 0x%x\n", acu->off, 4, val);
    //s->aummio->write(s->aummio, acu->off, val & (~((uint32_t) (1 << acu->irq))));
    s->aummio->write(s->aummio, acu->off, 0);
    //printf("[+] uart de-act write after 0x%x, size %d, value 0x%x\n", acu->off, 4, val & (~((uint32_t) (1 << acu->irq))));
    return 0;
}

static auto_config_action ramips_rt3883_uart_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .off = 0x0,
            .irq = 12,
            .do_react = ramips_rt3883_uart_do_deact_func,
            .next = 0,
        }
    }
};

static level_irq_cfg ramips_rt3883_uart_level_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_act = &wait_hw_evt_lvl_evt_act_cfg,
    .is_deact = &wait_hw_evt_lvl_evt_deact_cfg,
    .is_msk = &ramips_rt3883_uart_is_msk_cfg,
    .is_unmsk = &ramips_rt3883_uart_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_lvl_evt_reset_cfg,
    .is_init = &ramips_rt3883_uart_is_init_cfg,
    .do_act = &ramips_rt3883_uart_do_act_cfg,
    .do_deact = &ramips_rt3883_uart_do_deact_cfg,
};

static auto_config_one_irq ramips_rt3883_irq_cfgs[RAMIPS_RT3883_AUTOBOARD_IRQ_NUM] = {
    [12] = {
        .irq_type = STAT_MACH_LEVEL_IRQ,
        .irq_stat_mach_cfg = &ramips_rt3883_uart_level_irq_cfg,
    }
};


/*
 * for oxnas.generic
 *
 * we only need 1 irq for uart, and will use qemu arm's gic instead of our ic
 * 
 * TODO: we could find a way converting gic to our ic config
 *
 */

#define OXNAS_GENERIC_MMIO_LEN 0x0
#define OXNAS_GENERIC_AUTOBOARD_IRQ_NUM 0


/*
 * for orion.generic
 *
 * we only need 2 irqs for timer & uart, and also need an extra timer device
 *
 */

#define ORION_GENERIC_MMIO_LEN 0x100
#define ORION_GENERIC_AUTOBOARD_IRQ_NUM 1

// TODO

/*
 * for ath79.generic
 *
 * we only need 1 irq for uart, this is also a level irq
 * 
 */

#define ATH79_GENERIC_MMIO_LEN 0x100
#define ATH79_GENERIC_AUTOBOARD_IRQ_NUM 32

static uint8_t ath79_generic_uart_is_msk_func0(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    // This endian swap may due to the uart serial initializes with BIG ENDIAN
    //if (at->new_val == ((at->old_val) & (__swap32(~(uint32_t)(1 << acu->irq)))))
    //    printf("[+] match the msk of irq %d\n", acu->irq);
    return at->new_val == ((at->old_val) & (__swap32(~(uint32_t)(1 << acu->irq))));
}

static auto_config_action ath79_generic_uart_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_READ,
            .off = 0x4,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 3,
            .match_write_cnt = ath79_generic_uart_is_msk_func0,
            .next = 2,
        },
        {
            .type = ACU_DO_WATCH_READ,
            .off = 0x4,
            .next = 0,
        }
    }
};

static uint8_t ath79_generic_uart_is_unmsk_func0(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    // This endian swap may due to the uart serial initializes with BIG ENDIAN
    //if (at->new_val == ((at->old_val) | (__swap32((uint32_t)(1 << acu->irq)))))
    //    printf("[+] match the unmsk of irq %d\n", acu->irq);
    return at->new_val == ((at->old_val) | (__swap32((uint32_t)(1 << acu->irq))));
}

static auto_config_action ath79_generic_uart_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_READ,
            .off = 0x4,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 3,
            .match_write_cnt = ath79_generic_uart_is_unmsk_func0,
            .next = 2,
        },
        {
            .type = ACU_DO_WATCH_READ,
            .off = 0x4,
            .next = 0,
        }
    }
};

static uint8_t ath79_generic_uart_do_act_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    uint32_t status = 0, enable = 4;
    //uint32_t val = s->aummio->read(s->aummio, acu->off);
    //printf("[+] uart act write before 0x%x, size %d, value 0x%x\n", acu->off, 4, val);
    //s->aummio->write(s->aummio, acu->off, val | (uint32_t)(1 << acu->irq));
    // This endian swap may due to the uart serial initializes with BIG ENDIAN
    s->aummio->write(s->aummio, status, __swap32((uint32_t)(1 << acu->irq)));
    s->aummio->write(s->aummio, enable, __swap32((uint32_t)(1 << acu->irq)));
    //printf("[+] uart act write after 0x%x, size %d, value 0x%x\n", acu->off, 4, val | (uint32_t)(1 << acu->irq));
    return 0;
}

static auto_config_action ath79_generic_uart_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 3,
            .do_react = ath79_generic_uart_do_act_func,
            .next = 0,
        }
    }
};

static uint8_t ath79_generic_uart_do_deact_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    uint32_t status = 0, enable = 4;
    //uint32_t val = s->aummio->read(s->aummio, acu->off);
    //printf("[+] uart de-act write before 0x%x, size %d, value 0x%x\n", acu->off, 4, val);
    //s->aummio->write(s->aummio, acu->off, val & (~((uint32_t) (1 << acu->irq))));
    s->aummio->write(s->aummio, status, 0);
    s->aummio->write(s->aummio, enable, 0);
    //printf("[+] uart de-act write after 0x%x, size %d, value 0x%x\n", acu->off, 4, val & (~((uint32_t) (1 << acu->irq))));
    return 0;
}

static auto_config_action ath79_generic_uart_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 3,
            .do_react = ath79_generic_uart_do_deact_func,
            .next = 0,
        }
    }
};

static uint8_t ath79_generic_uart_is_init_func_0(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)0x0);
}

static uint8_t ath79_generic_uart_is_init_func_1(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)0x0);
}

static auto_config_action ath79_generic_uart_is_init_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .match_write_cnt = ath79_generic_uart_is_init_func_0,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x0,
            .match_write_cnt = ath79_generic_uart_is_init_func_1,
            .next = 0,
        }
    }
};

static level_irq_cfg ath79_generic_uart_level_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_act = &wait_hw_evt_lvl_evt_act_cfg,
    .is_deact = &wait_hw_evt_lvl_evt_deact_cfg,
    .is_msk = &ath79_generic_uart_is_msk_cfg,
    .is_unmsk = &ath79_generic_uart_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_lvl_evt_reset_cfg,
    .is_init = &ath79_generic_uart_is_init_cfg,
    .do_act = &ath79_generic_uart_do_act_cfg,
    .do_deact = &ath79_generic_uart_do_deact_cfg,
};

static auto_config_one_irq ath79_generic_irq_cfgs[ATH79_GENERIC_AUTOBOARD_IRQ_NUM] = {
    [3] = {
        .irq_type = STAT_MACH_LEVEL_IRQ,
        .irq_stat_mach_cfg = &ath79_generic_uart_level_irq_cfg,
    }
};

/*
 * for kirkwood.generic
 * 
 * we have 2 intc, orion & bridge
 * 
 */

/*
 * for kirkwood.generic orion intc
 * 
 * we have 3 irqs connected to it, bridge intc & uart0 & uart1
 */

#define KIRKWOOD_GENERIC_ORION_MMIO_LEN 0x20
#define KIRKWOOD_GENERIC_ORION_AUTOBOARD_IRQ_NUM 64

static uint8_t kirkwood_generic_common_is_msk_func(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (at->old_val & (~(uint32_t)(1 << (acu->irq % 32)))));
}

static uint8_t kirkwood_generic_common_is_unmsk_func(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (at->old_val | ((uint32_t)(1 << (acu->irq % 32)))));
}

static uint8_t kirkwood_generic_common_do_act_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    uint32_t cause, mask;
    //uint32_t val = s->aummio->read(s->aummio, acu->off);
    //printf("[+] uart act write before 0x%x, size %d, value 0x%x\n", acu->off, 4, val);
    cause = (acu->irq / 32) * 0x10 + 0;
    mask = (acu->irq / 32) * 0x10 + 4;
    s->aummio->write(s->aummio, cause, (uint32_t)(1 << (acu->irq % 32)));
    s->aummio->write(s->aummio, mask, (uint32_t)(1 << (acu->irq % 32)));
    //printf("[+] uart act write after 0x%x, size %d, value 0x%x\n", acu->off, 4, val | (uint32_t)(1 << acu->irq));
    return 0;
}

static uint8_t kirkwood_generic_common_do_deact_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, auto_trifle *at)
{
    uint32_t cause, mask;
    //uint32_t val = s->aummio->read(s->aummio, acu->off);
    //printf("[+] uart act write before 0x%x, size %d, value 0x%x\n", acu->off, 4, val);
    cause = (acu->irq / 32) * 0x10 + 0;
    mask = (acu->irq / 32) * 0x10 + 4;
    s->aummio->write(s->aummio, cause, (uint32_t)(0));
    s->aummio->write(s->aummio, mask, (uint32_t)(0));
    //printf("[+] uart act write after 0x%x, size %d, value 0x%x\n", acu->off, 4, val | (uint32_t)(1 << acu->irq));
    return 0;
}

static uint8_t kirkwood_generic_orion_common_is_init_func0(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)(0x0));
}

static uint8_t kirkwood_generic_orion_common_is_init_func1(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)(0x0));
}

static auto_config_action kirkwood_generic_orion_common_is_init_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .match_write_cnt = kirkwood_generic_orion_common_is_init_func0,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x14,
            .match_write_cnt = kirkwood_generic_orion_common_is_init_func1,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_orion_bridge_intc_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 1,
            .match_write_cnt = kirkwood_generic_common_is_msk_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_orion_bridge_intc_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 1,
            .match_write_cnt = kirkwood_generic_common_is_unmsk_func,
            .next = 0,
        },
    },
};

static auto_config_action kirkwood_generic_orion_bridge_intc_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 1,
            .off = 0,
            .do_react = kirkwood_generic_common_do_act_func,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_orion_bridge_intc_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 1,
            .do_react = kirkwood_generic_common_do_deact_func,
            .next = 0,
        }
    }
};

static level_irq_cfg kirkwood_generic_orion_bridge_intc_level_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_act = &wait_hw_evt_lvl_evt_act_cfg,
    .is_deact = &wait_hw_evt_lvl_evt_deact_cfg,
    .is_msk = &kirkwood_generic_orion_bridge_intc_is_msk_cfg,
    .is_unmsk = &kirkwood_generic_orion_bridge_intc_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_lvl_evt_reset_cfg,
    .is_init = &kirkwood_generic_orion_common_is_init_cfg,
    .do_act = &kirkwood_generic_orion_bridge_intc_do_act_cfg,
    .do_deact = &kirkwood_generic_orion_bridge_intc_do_deact_cfg,
};

static auto_config_action kirkwood_generic_orion_uart0_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x14,
            .irq = 33,
            .match_write_cnt = kirkwood_generic_common_is_msk_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_orion_uart0_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x14,
            .irq = 33,
            .match_write_cnt = kirkwood_generic_common_is_unmsk_func,
            .next = 0,
        },
    },
};

static auto_config_action kirkwood_generic_orion_uart0_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 33,
            .off = 0x10,
            .do_react = kirkwood_generic_common_do_act_func,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_orion_uart0_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 33,
            .off = 0x10,
            .do_react = kirkwood_generic_common_do_deact_func,
            .next = 0,
        }
    }
};

static level_irq_cfg kirkwood_generic_orion_uart0_level_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_act = &wait_hw_evt_lvl_evt_act_cfg,
    .is_deact = &wait_hw_evt_lvl_evt_deact_cfg,
    .is_msk = &kirkwood_generic_orion_uart0_is_msk_cfg,
    .is_unmsk = &kirkwood_generic_orion_uart0_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_lvl_evt_reset_cfg,
    .is_init = &kirkwood_generic_orion_common_is_init_cfg,
    .do_act = &kirkwood_generic_orion_uart0_do_act_cfg,
    .do_deact = &kirkwood_generic_orion_uart0_do_deact_cfg,
};

static auto_config_action kirkwood_generic_orion_uart1_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x14,
            .irq = 34,
            .match_write_cnt = kirkwood_generic_common_is_msk_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_orion_uart1_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x14,
            .irq = 34,
            .match_write_cnt = kirkwood_generic_common_is_unmsk_func,
            .next = 0,
        },
    },
};

static auto_config_action kirkwood_generic_orion_uart1_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 34,
            .off = 0x10,
            .do_react = kirkwood_generic_common_do_act_func,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_orion_uart1_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 34,
            .off = 0x10,
            .do_react = kirkwood_generic_common_do_deact_func,
            .next = 0,
        }
    }
};

static level_irq_cfg kirkwood_generic_orion_uart1_intc_level_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_act = &wait_hw_evt_lvl_evt_act_cfg,
    .is_deact = &wait_hw_evt_lvl_evt_deact_cfg,
    .is_msk = &kirkwood_generic_orion_uart1_is_msk_cfg,
    .is_unmsk = &kirkwood_generic_orion_uart1_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_lvl_evt_reset_cfg,
    .is_init = &kirkwood_generic_orion_common_is_init_cfg,
    .do_act = &kirkwood_generic_orion_uart1_do_act_cfg,
    .do_deact = &kirkwood_generic_orion_uart1_do_deact_cfg,
};

static auto_config_one_irq kirkwood_generic_orion_irq_cfgs[KIRKWOOD_GENERIC_ORION_AUTOBOARD_IRQ_NUM] = {
    [1] = {
        .irq_type = STAT_MACH_LEVEL_IRQ,
        .irq_stat_mach_cfg = &kirkwood_generic_orion_bridge_intc_level_irq_cfg,
    },
    [33] = {
        .irq_type = STAT_MACH_LEVEL_IRQ,
        .irq_stat_mach_cfg = &kirkwood_generic_orion_uart0_level_irq_cfg,
    },
    [34] = {
        .irq_type = STAT_MACH_LEVEL_IRQ,
        .irq_stat_mach_cfg = &kirkwood_generic_orion_uart1_intc_level_irq_cfg,
    },
};

/*
 * for kirkwood.generic bridge intc
 * 
 * we have 2 irqs connected to it in timer
 */

#define KIRKWOOD_GENERIC_BRIDGE_MMIO_LEN 0x8
#define KIRKWOOD_GENERIC_BRIDGE_AUTOBOARD_IRQ_NUM 6

static uint8_t kirkwood_generic_bridge_common_is_init_func0(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)(0x0));
}

static uint8_t kirkwood_generic_bridge_common_is_init_func1(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (uint32_t)(0x0));
}

static auto_config_action kirkwood_generic_bridge_common_is_init_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .match_write_cnt = kirkwood_generic_bridge_common_is_init_func0,
            .next = 1,
        },
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x0,
            .match_write_cnt = kirkwood_generic_bridge_common_is_init_func1,
            .next = 0,
        }
    }
};

static uint8_t kirkwood_generic_bridge_common_is_ack_func(AUTOBOARD_INTCState *s, struct auto_config_unit *acu, auto_trifle *at)
{
    return (at->new_val == (~(uint32_t)(1 << (acu->irq % 32))));
}

static auto_config_action kirkwood_generic_bridge_timer1_is_ack_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x0,
            .irq = 1,
            .match_write_cnt = kirkwood_generic_bridge_common_is_ack_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_bridge_timer1_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 1,
            .match_write_cnt = kirkwood_generic_common_is_msk_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_bridge_timer1_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 1,
            .match_write_cnt = kirkwood_generic_common_is_unmsk_func,
            .next = 0,
        },
    },
};

static auto_config_action kirkwood_generic_bridge_timer1_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 1,
            .do_react = kirkwood_generic_common_do_act_func,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_bridge_timer1_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 1,
            .do_react = kirkwood_generic_common_do_deact_func,
            .next = 0,
        }
    }
};

static edge_irq_cfg kirkwood_generic_bridge_timer1_edge_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_pulse = &wait_hw_evt_edge_evt_pulse_cfg,
    .is_ack = &kirkwood_generic_bridge_timer1_is_ack_cfg,
    .is_msk = &kirkwood_generic_bridge_timer1_is_msk_cfg,
    .is_unmsk = &kirkwood_generic_bridge_timer1_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_edge_evt_reset_cfg,
    .is_init = &kirkwood_generic_bridge_common_is_init_cfg,
    .do_act = &kirkwood_generic_bridge_timer1_do_act_cfg,
    .do_deact = &kirkwood_generic_bridge_timer1_do_deact_cfg,
};

static auto_config_action kirkwood_generic_bridge_timer2_is_ack_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x0,
            .irq = 2,
            .match_write_cnt = kirkwood_generic_bridge_common_is_ack_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_bridge_timer2_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 2,
            .match_write_cnt = kirkwood_generic_common_is_msk_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_bridge_timer2_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 2,
            .match_write_cnt = kirkwood_generic_common_is_unmsk_func,
            .next = 0,
        },
    },
};

static auto_config_action kirkwood_generic_bridge_timer2_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 2,
            .do_react = kirkwood_generic_common_do_act_func,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_bridge_timer2_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 2,
            .do_react = kirkwood_generic_common_do_deact_func,
            .next = 0,
        }
    }
};

static edge_irq_cfg kirkwood_generic_bridge_timer2_intc_edge_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    .is_pulse = &wait_hw_evt_edge_evt_pulse_cfg,
    .is_ack = &kirkwood_generic_bridge_timer2_is_ack_cfg,
    .is_msk = &kirkwood_generic_bridge_timer2_is_msk_cfg,
    .is_unmsk = &kirkwood_generic_bridge_timer2_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_edge_evt_reset_cfg,
    .is_init = &kirkwood_generic_bridge_common_is_init_cfg,
    .do_act = &kirkwood_generic_bridge_timer2_do_act_cfg,
    .do_deact = &kirkwood_generic_bridge_timer2_do_deact_cfg,
};

static auto_config_action kirkwood_generic_bridge_wdt_is_ack_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x0,
            .irq = 3,
            .match_write_cnt = kirkwood_generic_bridge_common_is_ack_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_bridge_wdt_is_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 3,
            .match_write_cnt = kirkwood_generic_common_is_msk_func,
            .next = 0,
        },
    }
};

static auto_config_action kirkwood_generic_bridge_wdt_is_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_WATCH_WRITE,
            .off = 0x4,
            .irq = 3,
            .match_write_cnt = kirkwood_generic_common_is_unmsk_func,
            .next = 0,
        },
    },
};

static auto_config_action kirkwood_generic_bridge_wdt_do_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 3,
            .do_react = kirkwood_generic_common_do_act_func,
            .next = 0,
        }
    }
};

static auto_config_action kirkwood_generic_bridge_wdt_do_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_DO_REACT,
            .irq = 3,
            .do_react = kirkwood_generic_common_do_deact_func,
            .next = 0,
        }
    }
};

static edge_irq_cfg kirkwood_generic_bridge_wdt_intc_edge_irq_cfg = {
    .is_off = NULL,
    .is_on = NULL,
    //.is_pulse = NULL,
    //.is_ack = NULL,
    //.is_msk = NULL,
    //.is_unmsk = NULL,
    //.is_reset = NULL,
    //.is_init = NULL,
    //.do_act = NULL,
    //.do_deact = NULL,
    .is_pulse = &wait_hw_evt_edge_evt_pulse_cfg,
    .is_ack = &kirkwood_generic_bridge_wdt_is_ack_cfg,
    .is_msk = &kirkwood_generic_bridge_wdt_is_msk_cfg,
    .is_unmsk = &kirkwood_generic_bridge_wdt_is_unmsk_cfg,
    .is_reset = &wait_hw_evt_edge_evt_reset_cfg,
    .is_init = &kirkwood_generic_bridge_common_is_init_cfg,
    .do_act = &kirkwood_generic_bridge_wdt_do_act_cfg,
    .do_deact = &kirkwood_generic_bridge_wdt_do_deact_cfg,
};

static auto_config_one_irq kirkwood_generic_bridge_irq_cfgs[KIRKWOOD_GENERIC_BRIDGE_AUTOBOARD_IRQ_NUM] = {
    [1] = {
        .irq_type = STAT_MACH_EDGE_IRQ,
        .irq_stat_mach_cfg = &kirkwood_generic_bridge_timer1_edge_irq_cfg,
    },
    [2] = {
        .irq_type = STAT_MACH_EDGE_IRQ,
        .irq_stat_mach_cfg = &kirkwood_generic_bridge_timer2_intc_edge_irq_cfg,
    },
    [3] = {
        .irq_type = STAT_MACH_EDGE_IRQ,
        //.irq_type = STAT_MACH_EMPTY,
        .irq_stat_mach_cfg = &kirkwood_generic_bridge_wdt_intc_edge_irq_cfg,
    },
};


/*
 * Config Panel
 */

static auto_one_intc_cfg all_irq_cfgs[AUTOBOARD_INTC_NUM] = {
    [AUTOBOARD_INTC_RAMIPS_RT3883] = {
        .irq_cfgs = ramips_rt3883_irq_cfgs,
        .mmio_len = RAMIPS_RT3883_MMIO_LEN,
        .irq_num = RAMIPS_RT3883_AUTOBOARD_IRQ_NUM,
    },
    [AUTOBOARD_INTC_ATH79_GENERIC] = {
        .irq_cfgs = ath79_generic_irq_cfgs,
        .mmio_len = ATH79_GENERIC_MMIO_LEN,
        .irq_num = ATH79_GENERIC_AUTOBOARD_IRQ_NUM,
    },
    [AUTOBOARD_INTC_KIRKWOOD_GENERIC_ORION] = {
        .irq_cfgs = kirkwood_generic_orion_irq_cfgs,
        .mmio_len = KIRKWOOD_GENERIC_ORION_MMIO_LEN,
        .irq_num = KIRKWOOD_GENERIC_ORION_AUTOBOARD_IRQ_NUM,
    },
    [AUTOBOARD_INTC_KIRKWOOD_GENERIC_BRIDGE] = {
        .irq_cfgs = kirkwood_generic_bridge_irq_cfgs,
        .mmio_len = KIRKWOOD_GENERIC_BRIDGE_MMIO_LEN,
        .irq_num = KIRKWOOD_GENERIC_BRIDGE_AUTOBOARD_IRQ_NUM,
    },
};

auto_one_intc_cfg *get_autoboard_intc_config(autoboard_intc_cfg_id id)
{
    assert(id > AUTOBOARD_INTC_INVALID && id < AUTOBOARD_INTC_NUM && "invalid autoboard intc cfg id");
    return &all_irq_cfgs[id];
}