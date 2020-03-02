from slcore.dt_parsers.mmio import *
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.compatible import *

# from linux-5.3
builtin_flashes = [
    'm-systems,diskonchip-g3',
    # 'jedec,spi-nor',
    'microchip,mchp23k256', 'microchip,mchp23lcv1024', 'atmel,at45', 'atmel,dataflash',
    'ibm,opal-flash', 'st,spear600-smi', 'st,spi-fsm', 'ti,am654-hbmc', 'lantiq,nor', 'cfi-flash', 'jedec-flash',
    'mtd-ram', 'mtd-rom', 'direct-mapped', 'cortina,gemini-syscon', 'arm,integrator-ap-syscon',
    'arm,integrator-cp-syscon', 'arm,core-module-versatile', 'arm,realview-eb-syscon',
    'arm,realview-pb1176-syscon', 'arm,realview-pb11mp-syscon', 'arm,realview-pba8-syscon',
    'arm,realview-pbx-syscon', 'arm,external-bus-interface', 'ti,omap2-onenand', 'atmel,at91sam9260-matrix',
    'atmel,at91sam9261-matrix', 'atmel,at91sam9263-matrix', 'atmel,at91sam9rl-matrix', 'atmel,at91sam9g45-matrix',
    'atmel,at91sam9n12-matrix', 'atmel,at91sam9x5-matrix', 'microchip,sam9x60-sfr', 'atmel,at91rm9200-nand-controller',
    'atmel,at91sam9260-nand-controller', 'atmel,at91sam9261-nand-controller', 'atmel,at91sam9g45-nand-controller',
    'atmel,sama5d3-nand-controller', 'microchip,sam9x60-nand-controller', 'atmel,at91rm9200-nand', 'atmel,sama5d4-nand',
    'atmel,sama5d2-nand', 'atmel,sama5d4-nand', 'atmel,sama5d2-nand', 'atmel,at91sam9g45-pmecc', 'atmel,sama5d4-pmecc',
    'atmel,sama5d2-pmecc', 'brcm,nand-bcm63138', 'brcm,nand-bcm6368', 'brcm,brcmnand-v4.0', 'brcm,brcmnand-v5.0',
    'brcm,brcmnand-v6.0', 'brcm,brcmnand-v6.1', 'brcm,brcmnand-v6.2', 'brcm,brcmnand-v7.0', 'brcm,brcmnand-v7.1',
    'brcm,brcmnand-v7.2', 'brcm,brcmnand-v7.3', 'brcm,brcmnand', 'brcm,nand-iproc', 'ti,davinci-nand',
    'ti,keystone-nand', 'altr,socfpga-denali-nand', 'socionext,uniphier-denali-nand-v5a', 'socionext,uniphier-denali-nand-v5b',
    'fsl,elbc-fcm-nand', 'fsl,ifc-nand', 'fsl,upm-nand', 'st,spear600-fsmc-nand', 'stericsson,fsmc-nand', 'gpio-control-nand',
    'fsl,imx23-gpmi-nand', 'fsl,imx28-gpmi-nand', 'fsl,imx6q-gpmi-nand', 'fsl,imx6sx-gpmi-nand', 'fsl,imx7d-gpmi-nand',
    'hisilicon,504-nfc', 'ingenic,jz4740-nand', 'ingenic,jz4725b-nand', 'ingenic,jz4780-nand', 'ingenic,jz4725b-bch',
    'ingenic,jz4740-ecc', 'ingenic,jz4780-bch', 'nxp,lpc3220-mlc', 'nxp,lpc3220-slc', 'marvell,armada-8k-nand-controller',
    'marvell,armada370-nand-controller', 'marvell,pxa3xx-nand-controller', 'marvell,armada-8k-nand', 'marvell,armada370-nand',
    'marvell,pxa3xx-nand', 'amlogic,meson-gxl-nfc', 'amlogic,meson-axg-nfc', 'fsl,mpc5121-nfc', 'mediatek,mt2701-ecc',
    'mediatek,mt2712-ecc', 'mediatek,mt7622-ecc', 'mediatek,mt2701-nfc', 'mediatek,mt2712-nfc', 'mediatek,mt7622-nfc',
    'fsl,imx21-nand', 'fsl,imx27-nand', 'fsl,imx25-nand', 'fsl,imx51-nand', 'fsl,imx53-nand', 'ibm,ndfc', 'ti,omap2-nand',
    'ti,am3352-elm', 'marvell,orion-nand', 'oxsemi,ox820-nand', 'pasemi,localbus-nand', 'gen_nand', 'qcom,ipq806x-nand',
    'qcom,ipq4019-nand', 'qcom,ipq8074-nand', 'samsung,s3c2410-nand', 'samsung,s3c2412-nand', 'samsung,s3c2440-nand',
    'renesas,shmobile-flctl-sh7372', 'abb,socrates-nand', 'st,stm32mp15-fmc2', 'allwinner,sun4i-a10-nand',
    'allwinner,sun8i-a23-nand-controller', 'sigma,smp8758-nand', 'nvidia,tegra20-nand', 'fsl,vf610-nfc', 'lantiq,nand-xway',
    'spi-nand', 'arm,arm-firmware-suite', 'brcm,bcm963xx-imagetag', 'brcm,trx', 'redboot-fis',
    'aspeed,ast2400-fmc', 'aspeed,ast2400-spi', 'aspeed,ast2500-fmc', 'aspeed,ast2500-spi', 'cdns,qspi-nor', 'ti,k2g-qspi',
    'ti,am654-ospi', 'hisilicon,fmc-spi-nor', 'mediatek,mt8173-nor', 'nxp,lpc1773-spifi'
]


def __is_flash(dts, path):
    if dts.exist_property('compatible', path):
        for cmptbl in dts.get_property('compatible', path).data:
            if cmptbl in builtin_flashes:
                # yes, this is a flash
                return True
            if cmptbl.find('flash') != -1:
                # yes, this is a flash
                return True
    return False


def find_flatten_flash_in_fdt(dts):
    """
    compatible always, the compatible of the node
    path: always, the path of the node
    reg: always, see find_mmio_by_path for details
    intcp: condit, the phandle of the parent interrupt controller, if the slave is true
    irqn: condit, the irq number to which the slave device connect, if the slave is true
    irqns: condit, the irq numbers to which the slave device connect, if the slave is true
    """
    flatten_flashs = {}
    for pa, no, pros in dts.walk():
        if not __is_flash(dts, pa):
            continue
        compatible = dts.get_property('compatible', pa).data
        flatten_flashs[pa] = {'compatible': compatible}

        mmio = find_mmio_by_path(dts, pa)
        if mmio is not None:
            # only you need is the base address
            flatten_flashs[pa]['reg'] = mmio['reg'][0]
        else:
            continue

    ft = []
    for k, v in flatten_flashs.items():
        v['path'] = k
        ft.append(v)

    return ft

