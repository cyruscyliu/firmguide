/*
 * autoboard maybe auto generated implementation
 */

#include "qemu/osdep.h"

#include "hw/intc/autoboard_intc.h"
#include "hw/intc/autoboard_level_irq.h"
#include "hw/intc/autoboard_gen.h"
#include "hw/intc/autoboard_utils.h"

static uint8_t bit_verify(write_once *wo, uint32_t bit_pos, uint32_t raise)
{
    uint32_t tmp = 1 << bit_pos;
    if (raise)
        return ((tmp & wo->old_val) == 0) && ((tmp & wo->new_val) == tmp);
    else
        return ((tmp & wo->old_val) == tmp) && ((tmp & wo->new_val) == 0);
}

static uint8_t constraint_verify(write_once *wo)
{
    return ACU_MISMATCH;
}


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
#define RAMIPS_RT3883_AUTOBOARD_IRQ_NUM 1

static uint8_t ramips_rt3883_uart_init_func_0(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo)
{
    if ((wo->off == acu->off) && (wo->new_val == 0xffffffff))
        return ACU_NEXT;

    return ACU_MISMATCH;
}

static uint8_t ramips_rt3883_uart_init_func_1(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo)
{
    if ((wo->off == acu->off) && (wo->new_val == 0x0))
        return ACU_NEXT;

    return ACU_MISMATCH;
}

static uint8_t ramips_rt3883_uart_init_func_2(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo)
{
    if ((wo->off == acu->off) && (wo->new_val == (0x1 << 31)))
        return ACU_DONE;

    return ACU_MISMATCH;
}

static auto_config_action ramips_rt3883_uart_init_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_WATCH,
            .off = 0x38,
            .next = 1,
            .func = ramips_rt3883_uart_init_func_0,
        },{
            .type = ACU_WATCH,
            .off = 0x20,
            .next = 2,
            .func = ramips_rt3883_uart_init_func_1,
        },{
            .type = ACU_WATCH,
            .off = 0x34,
            .func = ramips_rt3883_uart_init_func_2,
        }
    }
};

static uint8_t ramips_rt3883_uart_msk_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo) 
{
    if ((wo->off == acu->off) && (wo->new_val == (0x1 << acu->irq)))
        return ACU_DONE;

    return ACU_MISMATCH;
}

static auto_config_action ramips_rt3883_uart_msk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_WATCH,
            .off = 0x38,
            .irq = 12,
            .func = ramips_rt3883_uart_msk_func,
        }
    },
};

static uint8_t ramips_rt3883_uart_unmsk_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo) 
{
    if ((wo->off == acu->off) && (wo->new_val == (0x1 << acu->irq)))
        return ACU_DONE;

    return ACU_MISMATCH;
}

static auto_config_action ramips_rt3883_uart_unmsk_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_WATCH,
            .off = 0x34,
            .irq = 12,
            .func = ramips_rt3883_uart_unmsk_func,
        }
    }
};

static uint8_t ramips_rt3883_uart_act_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo)
{
    uint32_t val = s->aummio->read(s->aummio, acu->off);
    s->aummio->write(s->aummio, acu->off, val | (1 << acu->irq));
    return ACU_DONE;
}

static auto_config_action ramips_rt3883_uart_act_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_REACT,
            .off = 0x0,
            .irq = 12,
            .func = ramips_rt3883_uart_act_func,
        }
    }
};

static uint8_t ramips_rt3883_uart_deact_func(AUTOBOARD_INTCState *s, auto_config_unit *acu, write_once *wo)
{
    uint32_t val = s->aummio->read(s->aummio, acu->off);
    s->aummio->write(s->aummio, acu->off, val | (~(1 << acu->irq)));
    return ACU_DONE;
}

static auto_config_action ramips_rt3883_uart_deact_cfg = {
    .prog = 0,
    .acus = {
        {
            .type = ACU_REACT,
            .off = 0x0,
            .irq = 12,
            .func = ramips_rt3883_uart_deact_func,
        }
    }
};

static level_irq_cfg ramips_rt3883_uart_level_irq_cfg = {
    .on = NULL,
    .off = NULL,
    .init = &ramips_rt3883_uart_init_cfg,
    .msk = &ramips_rt3883_uart_msk_cfg,
    .unmsk = &ramips_rt3883_uart_unmsk_cfg,
    .act = &ramips_rt3883_uart_act_cfg,
    .deact = &ramips_rt3883_uart_deact_cfg
};

auto_config_one_irq ramips_rt3883_irq_cfgs[] = {
    {
        .irq_type = STAT_MACH_LEVEL_IRQ,
        .irq_stat_mach_cfg = &ramips_rt3883_uart_level_irq_cfg
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
 *
 */

auto_config_one_irq *autoboard_irq_cfgs = NULL;
uint32_t mmio_len = 0;
uint32_t autoboard_irq_num = 0;

void init_autoboard_intc_config(void)
{
    /*
     * config for ramips rt3883
     */

    autoboard_irq_cfgs = ramips_rt3883_irq_cfgs;
    mmio_len = RAMIPS_RT3883_MMIO_LEN;
    autoboard_irq_num = RAMIPS_RT3883_AUTOBOARD_IRQ_NUM;
}