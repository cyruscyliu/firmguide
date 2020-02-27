import os

from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.compatible import *

# from linux-5.3
builtin_timers = [
    'snps,archs-timer-gfrc', 'snps,archs-timer-rtc', 'snps,arc-timer',
    'arm,armv7m-systick', 'arm,armv7-timer', 'arm,armv8-timer', 'arm,armv7-timer-mem',
    'arm,cortex-a9-global-timer', 'alphascale,asm9260-timer', 'brcm,bcm2835-system-timer',
    'brcm,kona-timer', 'bcm,kona-timer', 'stericsson,db8500-prcmu-timer-4', 'st,stih407-lpc',
    'cirrus,ep7209-timer', 'picochip,pc3x2-timer', 'snps,dw-apb-timer-osc', 'snps,dw-apb-timer-sp',
    'snps,dw-apb-timer', 'samsung,exynos4210-mct', 'samsung,exynos4412-mct', 'renesas,16bit-timer',
    'renesas,8bit-timer', 'renesas,tpu', 'jcore,pit', 'mti,gic-timer', 'arm,mps2-timer', 'fsl,timrot',
    'st,nomadik-mtu', 'renesas,ostm', 'samsung,s3c2410-pwm', 'samsung,s3c6400-pwm', 'samsung,s5p6440-pwm',
    'samsung,s5pc100-pwm', 'marvell,armada-xp-timer', 'marvell,armada-375-timer', 'marvell,armada-370-timer',
    'andestech,atcpit100', 'sirf,atlas7-tick', 'atmel,at91sam9260-pit', 'atmel,at91rm9200-st',
    'atmel,tcb-timer', 'cdns,ttc', 'ti,da830-timer', 'cnxt,cx92755-timer', 'efm32,timer',
    'energymicro,efm32-timer', 'fsl,ftm-timer', 'faraday,fttmr010', 'cortina,gemini-timer',
    'moxa,moxart-timer', 'aspeed,ast2400-timer', 'aspeed,ast2500-timer', 'csky,gx6605s-timer',
    'fsl,imx1-gpt', 'fsl,imx21-gpt', 'fsl,imx27-gpt', 'fsl,imx31-gpt', 'fsl,imx25-gpt', 'fsl,imx50-gpt',
    'fsl,imx51-gpt', 'fsl,imx53-gpt', 'fsl,imx6q-gpt', 'fsl,imx6dl-gpt', 'fsl,imx6sl-gpt',
    'fsl,imx6sx-gpt', 'nxp,sysctr-timer', 'fsl,imx7ulp-tpm', 'arm,integrator-timer', 'intel,ixp4xx-timer',
    'ti,keystone-timer', 'nxp,lpc3220-timer', 'mediatek,mt6577-timer', 'mediatek,mt6765-timer',
    'amlogic,meson6-timer', 'socionext,milbeaut-timer', 'csky,mptimer', 'nuvoton,npcm750-timer',
    'ezchip,nps400-timer', 'ezchip,nps400-timer1', 'ezchip,nps400-timer0', 'marvell,orion-timer',
    'actions,s500-timer', 'actions,s700-timer', 'actions,s900-timer', 'oxsemi,ox810se-rps-timer',
    'oxsemi,ox820-rps-timer', 'img,pistachio-gptimer', 'sirf,prima2-tick', 'marvell,pxa-timer',
    'qcom,kpss-timer', 'qcom,scss-timer', 'rda,8810pl-timer', 'riscv', 'rockchip,rk3288-timer',
    'rockchip,rk3399-timer', 'arm,sp804', 'arm,integrator-cp-timer', 'sprd,sc9860-timer',
    'sprd,sc9860-suspend-timer', 'st,stm32-timer', 'allwinner,sun4i-a10-timer', 'allwinner,suniv-f1c100s-timer',
    'allwinner,sun5i-a13-hstimer', 'allwinner,sun7i-a20-hstimer', 'sigma,tick-counter', 'nvidia,tegra210-timer',
    'nvidia,tegra20-timer', 'nvidia,tegra20-rtc', 'ti,omap-counter32k', 'stericsson,u300-apptimer', 'arm,vexpress-sysreg',
    'arm,versatile-sysreg', 'fsl,vf610-pit', 'via,vt8500-timer', 'lsi,zevio-timer'
]


def __is_timer(dts, path):
    if path.find('timer') != -1:
        # yes, this is a timer
        return True
    if dts.exist_property('compatible', path):
        for cmptbl in dts.get_property('compatible', path).data:
            if cmptbl in builtin_timers:
                # yes, this is a timer
                return True
            if cmptbl.find('timer') != -1:
                # yes, this is a timer
                return True
    return False


def find_flatten_timer_in_fdt(dts, intc=False):
    """
    compatible always, the compatible of the node
    path: always, the path of the node
    reg: always, see find_mmio_by_path for details
    intcp: condit, the phandle of the parent interrupt controller, if the slave is true
    irqn: condit, the irq number to which the slave device connect, if the slave is true
    irqns: condit, the irq numbers to which the slave device connect, if the slave is true
    """
    flatten_timers = {}
    for pa, no, pros in dts.walk():
        if len(no):
            continue
        if not __is_timer(dts, pa):
            continue
        compatible = dts.get_property('compatible', pa).data
        flatten_timers[pa] = {'compatible': compatible}

        mmio = find_mmio_by_path(dts, pa)
        if mmio is not None:
            # only you need is the base address
            flatten_timers[pa]['reg'] = mmio['reg'][0]

        if dts.exist_property('interrupts', pa):
            interrupt_parent = find_interrupt_parent_by_path(dts, pa)
            interrupts = dts.get_property('interrupts', pa).data
            irqns = find_irqnc_by_pphandle(dts, interrupt_parent, interrupts)
            flatten_timers[pa]['intcp'] = interrupt_parent
            flatten_timers[pa]['irqns'] = irqns
            flatten_timers[pa]['irqn'] = None
            flatten_timers[pa]['irqc'] = len(irqns)
        else:
            if not intc:
                # by default we don't return the timers which are free running
                flatten_timers.pop(pa)

    ft = []
    for k, v in flatten_timers.items():
        v['path'] = k
        ft.append(v)

    return ft

