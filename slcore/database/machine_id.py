from slcore.parser import get_candidates, get_all_strings


def find_machine_id_s(strings):
    """Find the machine id in the image.

    Args:
        strings(list): The strings from the image.

    Returns:
        list: The list of machine ids the image supports.
    """
    machine_ids = {
        "1944": {
            "machine_description": "Palm Centro 685",
            "machine_name": "centro",
            "config": "MACH_CENTRO",
            "number": "1944",
            "machine_type": "CENTRO"
        },
        "0": {
            "machine_description": "EBSA110",
            "machine_name": "ebsa110",
            "config": "ARCH_EBSA110",
            "number": "0",
            "machine_type": "EBSA110"
        },
        "347": {
            "machine_description": "IPAQ-H1940",
            "machine_name": "h1940",
            "config": "ARCH_H1940",
            "number": "347",
            "machine_type": "H1940"
        },
        "811": {
            "machine_description": "Contec Micro9-High",
            "machine_name": "micro9",
            "config": "MACH_MICRO9",
            "number": "811",
            "machine_type": "MICRO9"
        },
        "812": {
            "machine_description": "Contec Micro9-Lite",
            "machine_name": "micro9l",
            "config": "MACH_MICRO9L",
            "number": "812",
            "machine_type": "MICRO9L"
        },
        "817": {
            "machine_description": "OMAP310 based Palm Tungsten E",
            "machine_name": "omap_palmte",
            "config": "MACH_OMAP_PALMTE",
            "number": "817",
            "machine_type": "OMAP_PALMTE"
        },
        "1799": {
            "machine_description": "AT2440EVB",
            "machine_name": "at2440evb",
            "config": "MACH_AT2440EVB",
            "number": "1799",
            "machine_type": "AT2440EVB"
        },
        "1798": {
            "machine_description": "Gumstix Overo",
            "machine_name": "overo",
            "config": "MACH_OVERO",
            "number": "1798",
            "machine_type": "OVERO"
        },
        "2853": {
            "machine_description": "Amlogic Meson platform",
            "machine_name": "meson",
            "config": "MACH_MESON",
            "number": "2853",
            "machine_type": "MESON"
        },
        "713": {
            "machine_description": "SHARP Spitz",
            "machine_name": "spitz",
            "config": "MACH_SPITZ",
            "number": "713",
            "machine_type": "SPITZ"
        },
        "1490": {
            "machine_description": "JIVE",
            "machine_name": "jive",
            "config": "MACH_JIVE",
            "number": "1490",
            "machine_type": "JIVE"
        },
        "2072": {
            "machine_description": "Phytec Phycore pcm043",
            "machine_name": "pcm043",
            "config": "MACH_PCM043",
            "number": "2072",
            "machine_type": "PCM043"
        },
        "423": {
            "machine_description": "SHARP Corgi",
            "machine_name": "corgi",
            "config": "MACH_CORGI",
            "number": "423",
            "machine_type": "CORGI"
        },
        "1994": {
            "machine_description": "Compulab eXeda",
            "machine_name": "exeda",
                "config": "MACH_EXEDA",
                "number": "1994",
                "machine_type": "EXEDA"
        },
        "1701": {
            "machine_description": "LogicPD i.MX27LITE",
            "machine_name": "imx27lite",
            "config": "MACH_IMX27LITE",
            "number": "1701",
            "machine_type": "IMX27LITE"
        },
        "1709": {
            "machine_description": "CALAO USB_A9260",
            "machine_name": "usb_a9260",
            "config": "MACH_USB_A9260",
            "number": "1709",
            "machine_type": "USB_A9260"
        },
        "299": {
            "machine_description": "Intel IXDP2401 Development Platform",
            "machine_name": "ixdp2401",
            "config": "ARCH_IXDP2401",
            "number": "299",
            "machine_type": "IXDP2401"
        },
        "290": {
            "machine_description": "ADI Engineering Coyote",
            "machine_name": "adi_coyote",
            "config": "ARCH_ADI_COYOTE",
            "number": "290",
            "machine_type": "ADI_COYOTE"
        },
        "1128": {
            "machine_description": "Cirrus Logic EDB9307A Evaluation Board",
            "machine_name": "edb9307a",
            "config": "MACH_EDB9307A",
            "number": "1128",
            "machine_type": "EDB9307A"
        },
        "592": {
            "machine_description": "IPAQ-RX3715",
            "machine_name": "rx3715",
            "config": "MACH_RX3715",
            "number": "592",
            "machine_type": "RX3715"
        },
        "597": {
            "machine_description": "Linksys NSLU2",
            "machine_name": "nslu2",
            "config": "MACH_NSLU2",
            "number": "597",
            "machine_type": "NSLU2"
        },
        "598": {
            "machine_description": "Toshiba e400",
            "machine_name": "e400",
            "config": "MACH_E400",
            "number": "598",
            "machine_type": "E400"
        },
        "629": {
            "machine_description": "Intel IQ80332",
            "machine_name": "iq80332",
            "config": "MACH_IQ80332",
            "number": "629",
            "machine_type": "IQ80332"
        },
        "193": {
            "machine_description": "SMDK2410",
            "machine_name": "smdk2410",
            "config": "ARCH_SMDK2410",
            "number": "193",
            "machine_type": "SMDK2410"
        },
        "1127": {
            "machine_description": "Cirrus Logic EDB9302A Evaluation Board",
            "machine_name": "edb9302a",
            "config": "MACH_EDB9302A",
            "number": "1127",
            "machine_type": "EDB9302A"
        },
        "275": {
            "machine_description": "ARM-IntegratorCP",
            "machine_name": "cintegrator",
            "config": "ARCH_CINTEGRATOR",
            "number": "275",
            "machine_type": "CINTEGRATOR"
        },
        "2820": {
            "machine_description": "Eukrea CPUIMX25",
            "machine_name": "eukrea_cpuimx25sd",
            "config": "MACH_EUKREA_CPUIMX25SD",
            "number": "2820",
            "machine_type": "EUKREA_CPUIMX25SD"
        },
        "2821": {
            "machine_description": "Eukrea CPUIMX35",
            "machine_name": "eukrea_cpuimx35sd",
            "config": "MACH_EUKREA_CPUIMX35SD",
            "number": "2821",
            "machine_type": "EUKREA_CPUIMX35SD"
        },
        "2548": {
            "machine_description": "DaVinci DM6467T EVM",
            "machine_name": "davinci_dm6467tevm",
            "config": "MACH_DAVINCI_DM6467TEVM",
            "number": "2548",
            "machine_type": "DAVINCI_DM6467TEVM"
        },
        "3020": {
            "machine_description": "Compulab CM-A510 Board",
            "machine_name": "cm_a510",
            "config": "MACH_CM_A510",
            "number": "3020",
            "machine_type": "CM_A510"
        },
        "526": {
            "machine_description": "Gateworks Avila Network Platform",
            "machine_name": "avila",
            "config": "MACH_AVILA",
            "number": "526",
            "machine_type": "AVILA"
        },
        "2382": {
            "machine_description": "Jasper Development Platform",
            "machine_name": "marvell_jasper",
            "config": "MACH_MARVELL_JASPER",
            "number": "2382",
            "machine_type": "MARVELL_JASPER"
        },
        "520": {
            "machine_description": "SHARP Tosa",
            "machine_name": "tosa",
            "config": "MACH_TOSA",
            "number": "520",
            "machine_type": "TOSA"
        },
        "1400": {
            "machine_description": "OpenGear/IM4004",
            "machine_name": "im4004",
            "config": "MACH_IM4004",
            "number": "1400",
            "machine_type": "IM4004"
        },
        "1407": {
            "machine_description": "ARM-RealView PB11MPCore",
            "machine_name": "realview_pb11mp",
            "config": "MACH_REALVIEW_PB11MP",
            "number": "1407",
            "machine_type": "REALVIEW_PB11MP"
        },
        "1236": {
            "machine_description": "LogicPD MX31 LITEKIT",
            "machine_name": "mx31lite",
            "config": "MACH_MX31LITE",
            "number": "1236",
            "machine_type": "MX31LITE"
        },
        "448": {
            "machine_description": "HTC Himalaya",
            "machine_name": "himalaya",
            "config": "MACH_HIMALAYA",
            "number": "448",
            "machine_type": "HIMALAYA"
        },
        "1230": {
            "machine_description": "Palm Treo 680",
            "machine_name": "treo680",
            "config": "MACH_TREO680",
            "number": "1230",
            "machine_type": "TREO680"
        },
        "1233": {
            "machine_description": "PXA3xx Platform Development Kit (aka Zylonite)",
            "machine_name": "zylonite",
            "config": "MACH_ZYLONITE",
            "number": "1233",
            "machine_type": "ZYLONITE"
        },
        "447": {
            "machine_description": "Freescale MX31ADS",
            "machine_name": "mx31ads",
            "config": "MACH_MX31ADS",
            "number": "447",
            "machine_type": "MX31ADS"
        },
        "3290": {
            "machine_description": "Compulab CM-T3730",
            "machine_name": "cm_t3730",
            "config": "MACH_CM_T3730",
            "number": "3290",
            "machine_type": "CM_T3730"
        },
        "106": {
            "machine_description": "Agilent AAED-2000 Development Platform",
            "machine_name": "aaed2000",
            "config": "ARCH_AAED2000",
            "number": "106",
            "machine_type": "AAED2000"
        },
        "107": {
            "machine_description": "Cirrus-CDB89712",
            "machine_name": "cdb89712",
            "config": "ARCH_CDB89712",
            "number": "107",
            "machine_type": "CDB89712"
        },
        "900": {
            "machine_description": "OMAP2430 sdp2430 board",
            "machine_name": "omap_2430sdp",
            "config": "MACH_OMAP_2430SDP",
            "number": "900",
            "machine_type": "OMAP_2430SDP"
        },
        "901": {
            "machine_description": "DaVinci DM644x EVM",
            "machine_name": "davinci_evm",
            "config": "MACH_DAVINCI_EVM",
            "number": "901",
            "machine_type": "DAVINCI_EVM"
        },
        "2042": {
            "machine_description": "PXA168-based Zylonite2 Development Platform",
            "machine_name": "zylonite2",
            "config": "MACH_ZYLONITE2",
            "number": "2042",
            "machine_type": "ZYLONITE2"
        },
        "2043": {
            "machine_description": "PXA168-based Aspenite Development Platform",
            "machine_name": "aspenite",
            "config": "MACH_ASPENITE",
            "number": "2043",
            "machine_type": "ASPENITE"
        },
        "904": {
            "machine_description": "Palm Zire72",
            "machine_name": "palmz72",
            "config": "MACH_PALMZ72",
            "number": "904",
            "machine_type": "PALMZ72"
        },
        "905": {
            "machine_description": "Hilscher nxdb500",
            "machine_name": "nxdb500",
            "config": "MACH_NXDB500",
            "number": "905",
            "machine_type": "NXDB500"
        },
        "32": {
            "machine_description": "BSE nanoEngine",
            "machine_name": "nanoengine",
            "config": "SA1100_NANOENGINE",
            "number": "32",
            "machine_type": "NANOENGINE"
        },
        "31": {
            "machine_description": "Intrinsyc CerfBoard/CerfCube",
            "machine_name": "cerf",
            "config": "SA1100_CERF",
            "number": "31",
            "machine_type": "CERF"
        },
        "641": {
            "machine_description": "Gemtek GTWX5715 (Linksys WRV54G)",
            "machine_name": "gtwx5715",
            "config": "MACH_GTWX5715",
            "number": "641",
            "machine_type": "GTWX5715"
        },
        "1535": {
            "machine_description": "OMAP3 EVM",
            "machine_name": "omap3evm",
            "config": "MACH_OMAP3EVM",
            "number": "1535",
            "machine_type": "OMAP3EVM"
        },
        "438": {
            "machine_description": "Compulab CM-X2XX",
            "machine_name": "armcore",
            "config": "MACH_ARMCORE",
            "number": "438",
            "machine_type": "ARMCORE"
        },
        "648": {
            "machine_description": "Cogent CSB637",
            "machine_name": "csb637",
            "config": "MACH_CSB637",
            "number": "648",
            "machine_type": "CSB637"
        },
        "2104": {
            "machine_description": "PXA168 Avengers lite Development Platform",
            "machine_name": "avengers_lite",
            "config": "MACH_AVENGERS_LITE",
            "number": "2104",
            "machine_type": "AVENGERS_LITE"
        },
        "2160": {
            "machine_description": "OMAP4430 4430SDP board",
            "machine_name": "omap_4430sdp",
            "config": "MACH_OMAP_4430SDP",
            "number": "2160",
            "machine_type": "OMAP_4430SDP"
        },
        "2162": {
            "machine_description": "Motorola Zn5",
            "machine_name": "magx_zn5",
            "config": "MACH_MAGX_ZN5",
            "number": "2162",
            "machine_type": "MAGX_ZN5"
        },
        "2612": {
            "machine_description": "Embedian CAPC-7117 evaluation kit based on the MXM-8x10 CoM",
            "machine_name": "capc7117",
            "config": "MACH_CAPC7117",
            "number": "2612",
            "machine_type": "CAPC7117"
        },
        "331": {
            "machine_description": "Simtec-BAST",
            "machine_name": "bast",
            "config": "ARCH_BAST",
            "number": "331",
            "machine_type": "BAST"
        },
        "3378": {
            "machine_description": "Xilinx Zynq Platform",
            "machine_name": "xilinx_ep107",
            "config": "MACH_XILINX_EP107",
            "number": "3378",
            "machine_type": "XILINX_EP107"
        },
        "1908": {
            "machine_description": "Teltonika RUT100",
            "machine_name": "rut100",
            "config": "MACH_RUT100",
            "number": "1908",
            "machine_type": "RUT100"
        },
        "1902": {
            "machine_description": "Contec Micro9-Slim",
            "machine_name": "micro9s",
            "config": "MACH_MICRO9S",
            "number": "1902",
            "machine_type": "MICRO9S"
        },
        "1901": {
            "machine_description": "ARM-RealView PBX",
            "machine_name": "realview_pbx",
            "config": "MACH_REALVIEW_PBX",
            "number": "1901",
            "machine_type": "REALVIEW_PBX"
        },
        "851": {
            "machine_description": "Freescale i.MX21ADS",
            "machine_name": "mx21ads",
            "config": "MACH_MX21ADS",
            "number": "851",
            "machine_type": "MX21ADS"
        },
        "6": {
            "machine_description": "Chalice-CATS",
            "machine_name": "cats",
            "config": "ARCH_CATS",
            "number": "6",
            "machine_type": "CATS"
        },
        "91": {
            "machine_description": "Cirrus Logic 7212/7312",
            "machine_name": "clep7212",
            "config": "ARCH_CLEP7212",
            "number": "91",
            "machine_type": "CLEP7212"
        },
        "97": {
            "machine_description": "Shannon (AKA: Tuxscreen)",
            "machine_name": "shannon",
            "config": "SA1100_SHANNON",
            "number": "97",
            "machine_type": "SHANNON"
        },
        "3207": {
            "machine_description": "Wolfson Cragganmore 6410",
            "machine_name": "wlf_cragg_6410",
            "config": "MACH_WLF_CRAGG_6410",
            "number": "3207",
            "machine_type": "WLF_CRAGG_6410"
        },
        "1627": {
            "machine_description": "Ericsson AB U300 S25/S26/B25/B26 Prototype Board",
            "machine_name": "u300",
            "config": "MACH_U300",
            "number": "1627",
            "machine_type": "U300"
        },
        "1626": {
            "machine_description": "SMDK6410",
            "machine_name": "smdk6410",
            "config": "MACH_SMDK6410",
            "number": "1626",
            "machine_type": "SMDK6410"
        },
        "1624": {
            "machine_description": "Atmel AT91SAM9G20-EK",
            "machine_name": "at91sam9g20ek",
            "config": "MACH_AT91SAM9G20EK",
            "number": "1624",
            "machine_type": "AT91SAM9G20EK"
        },
        "1999": {
            "machine_description": "MINI2440",
            "machine_name": "mini2440",
            "config": "MACH_MINI2440",
            "number": "1999",
            "machine_type": "MINI2440"
        },
        "744": {
            "machine_description": "SHARP Akita",
            "machine_name": "akita",
            "config": "MACH_AKITA",
            "number": "744",
            "machine_type": "AKITA"
        },
        "3062": {
            "machine_description": "PControl G20",
            "machine_name": "pcontrol_g20",
            "config": "MACH_PCONTROL_G20",
            "number": "3062",
            "machine_type": "PCONTROL_G20"
        },
        "2913": {
            "machine_description": "Buffalo Linkstation LiveV3 (LS-CHL)",
            "machine_name": "linkstation_lschl",
            "config": "MACH_LINKSTATION_LSCHL",
            "number": "2913",
            "machine_type": "LINKSTATION_LSCHL"
        },
        "234": {
            "machine_description": "TI-Innovator",
            "machine_name": "omap_innovator",
            "config": "MACH_OMAP_INNOVATOR",
            "number": "234",
            "machine_type": "OMAP_INNOVATOR"
        },
        "2341": {
            "machine_description": "Compulab CM-T35",
            "machine_name": "cm_t35",
            "config": "MACH_CM_T35",
            "number": "2341",
            "machine_type": "CM_T35"
        },
        "2342": {
            "machine_description": "LaCie 2Big Network",
            "machine_name": "net2big",
            "config": "MACH_NET2BIG",
            "number": "2342",
            "machine_type": "NET2BIG"
        },
        "1": {
            "machine_description": "Acorn-RiscPC",
            "machine_name": "riscpc",
            "config": "ARCH_RPC",
            "number": "1",
            "machine_type": "RISCPC"
        },
        "1693": {
            "machine_description": "HP Media Vault mv2120",
            "machine_name": "mv2120",
            "config": "MACH_MV2120",
            "number": "1693",
            "machine_type": "MV2120"
        },
        "1690": {
            "machine_description": "Wiliboard WBD-111",
            "machine_name": "wbd111",
            "config": "MACH_WBD111",
            "number": "1690",
            "machine_type": "WBD111"
        },
        "1757": {
            "machine_description": "Zipit Z2",
            "machine_name": "zipit2",
            "config": "MACH_ZIPIT2",
            "number": "1757",
            "machine_type": "ZIPIT2"
        },
        "1756": {
            "machine_description": "LaCie Ethernet Disk mini V2",
            "machine_name": "edmini_v2",
            "config": "MACH_EDMINI_V2",
            "number": "1756",
            "machine_type": "EDMINI_V2"
        },
        "146": {
            "machine_description": "Sharp-Collie",
            "machine_name": "collie",
            "config": "SA1100_COLLIE",
            "number": "146",
            "machine_type": "COLLIE"
        },
        "618": {
            "machine_description": "Intel IXDP465 Development Platform",
            "machine_name": "ixdp465",
            "config": "MACH_IXDP465",
            "number": "618",
            "machine_type": "IXDP465"
        },
        "619": {
            "machine_description": "Intel IXDP2351 Development Platform",
            "machine_name": "ixdp2351",
            "config": "MACH_IXDP2351",
            "number": "619",
            "machine_type": "IXDP2351"
        },
        "1270": {
            "machine_description": "SMDK6400",
            "machine_name": "smdk6400",
            "config": "MACH_SMDK6400",
            "number": "1270",
            "machine_type": "SMDK6400"
        },
        "1271": {
            "machine_description": "Nokia N800",
            "machine_name": "nokia_n800",
            "config": "MACH_NOKIA_N800",
            "number": "1271",
            "machine_type": "NOKIA_N800"
        },
        "148": {
            "machine_description": "Hewlett-Packard Laboratories BadgePAD 4",
            "machine_name": "badge4",
            "config": "SA1100_BADGE4",
            "number": "148",
            "machine_type": "BADGE4"
        },
        "1880": {
            "machine_description": "Liebherr controller BK3.1",
            "machine_name": "bk3",
            "config": "MACH_BK3",
            "number": "1880",
            "machine_type": "BK3"
        },
        "1281": {
            "machine_description": "Intel EP80219",
            "machine_name": "ep80219",
            "config": "MACH_EP80219",
            "number": "1281",
            "machine_type": "EP80219"
        },
        "949": {
            "machine_description": "IP Fabrics Double Espresso",
            "machine_name": "espresso",
            "config": "MACH_ESPRESSO",
            "number": "949",
            "machine_type": "ESPRESSO"
        },
        "941": {
            "machine_description": "Hilscher nxeb500hmi",
            "machine_name": "nxeb500hmi",
            "config": "MACH_NXEB500HMI",
            "number": "941",
            "machine_type": "NXEB500HMI"
        },
        "1578": {
            "machine_description": "Vision Engraving Systems EP9307",
            "machine_name": "vision_ep9307",
            "config": "MACH_VISION_EP9307",
            "number": "1578",
            "machine_type": "VISION_EP9307"
        },
        "1476": {
            "machine_description": "Simplemachines Sim.One Board",
            "machine_name": "sim_one",
            "config": "MACH_SIM_ONE",
            "number": "1476",
            "machine_type": "SIM_ONE"
        },
        "681": {
            "machine_description": "NexVision - Nexcoder 2440",
            "machine_name": "nexcoder_2440",
            "config": "MACH_NEXCODER_2440",
            "number": "681",
            "machine_type": "NEXCODER_2440"
        },
        "680": {
            "machine_description": "Nex Vision - Otom 1.1",
            "machine_name": "otom",
            "config": "MACH_OTOM",
            "number": "680",
            "machine_type": "OTOM"
        },
        "2534": {
            "machine_description": "SmartQ 5",
            "machine_name": "smartq5",
            "config": "MACH_SMARTQ5",
            "number": "2534",
            "machine_type": "SMARTQ5"
        },
        "1574": {
            "machine_description": "EPFL Mobots mx31moboard",
            "machine_name": "mx31moboard",
            "config": "MACH_MX31MOBOARD",
            "number": "1574",
            "machine_type": "MX31MOBOARD"
        },
        "1304": {
            "machine_description": "GTA02",
            "machine_name": "neo1973_gta02",
            "config": "MACH_NEO1973_GTA02",
            "number": "1304",
            "machine_type": "NEO1973_GTA02"
        },
        "2650": {
            "machine_description": "MityDSP-L138/MityARM-1808",
            "machine_name": "mityomapl138",
            "config": "MACH_MITYOMAPL138",
            "number": "2650",
            "machine_type": "MITYOMAPL138"
        },
        "136": {
            "machine_description": "Compaq iPAQ H3100",
            "machine_name": "h3100",
            "config": "SA1100_H3100",
            "number": "136",
            "machine_type": "H3100"
        },
        "496": {
            "machine_description": "Toshiba e800",
            "machine_name": "e800",
            "config": "MACH_E800",
            "number": "496",
            "machine_type": "E800"
        },
        "497": {
            "machine_description": "Toshiba e750",
            "machine_name": "e750",
            "config": "MACH_E750",
            "number": "497",
            "machine_type": "E750"
        },
        "491": {
            "machine_description": "OMAP730 Perseus2",
            "machine_name": "omap_perseus2",
            "config": "MACH_OMAP_PERSEUS2",
            "number": "491",
            "machine_type": "OMAP_PERSEUS2"
        },
        "24": {
            "machine_description": "ARM-Prospector720T",
            "machine_name": "p720t",
            "config": "ARCH_P720T",
            "number": "24",
            "machine_type": "P720T"
        },
        "25": {
            "machine_description": "Intel-Assabet",
            "machine_name": "assabet",
            "config": "SA1100_ASSABET",
            "number": "25",
            "machine_type": "ASSABET"
        },
        "1830": {
            "machine_description": "Atmel AT91SAM9M10G45-EK",
            "machine_name": "at91sam9m10g45ek",
            "config": "MACH_AT91SAM9M10G45EK",
            "number": "1830",
            "machine_type": "AT91SAM9M10G45EK"
        },
        "27": {
            "machine_description": "LART",
            "machine_name": "lart",
            "config": "SA1100_LART",
            "number": "27",
            "machine_type": "LART"
        },
        "20": {
            "machine_description": "PLEB",
            "machine_name": "pleb",
            "config": "SA1100_PLEB",
            "number": "20",
            "machine_type": "PLEB"
        },
        "21": {
            "machine_description": "ARM-Integrator",
            "machine_name": "integrator",
            "config": "ARCH_INTEGRATOR",
            "number": "21",
            "machine_type": "INTEGRATOR"
        },
        "22": {
            "machine_description": "Compaq iPAQ H3600",
            "machine_name": "h3600",
            "config": "SA1100_H3600",
            "number": "22",
            "machine_type": "H3600"
        },
        "3790": {
            "machine_description": "marzen",
            "machine_name": "marzen",
            "config": "MACH_MARZEN",
            "number": "3790",
            "machine_type": "MARZEN"
        },
        "406": {
            "machine_description": "Intel HCDDBBVA0 Development Platform (aka Mainstone)",
            "machine_name": "mainstone",
            "config": "MACH_MAINSTONE",
            "number": "406",
            "machine_type": "MAINSTONE"
        },
        "2157": {
            "machine_description": "DaVinci DA850/OMAP-L138 EVM",
            "machine_name": "davinci_da850_evm",
            "config": "MACH_DAVINCI_DA850_EVM",
            "number": "2157",
            "machine_type": "DAVINCI_DA850_EVM"
        },
        "930": {
            "machine_description": "LogicPD PXA270 Card Engine",
            "machine_name": "logicpd_pxa270",
            "config": "MACH_LOGICPD_PXA270",
            "number": "930",
            "machine_type": "LOGICPD_PXA270"
        },
        "2159": {
            "machine_description": "Atmel AT91SAM9G10-EK",
            "machine_name": "at91sam9g10ek",
            "config": "MACH_AT91SAM9G10EK",
            "number": "2159",
            "machine_type": "AT91SAM9G10EK"
        },
        "408": {
            "machine_description": "SecureComputing/SG300",
            "machine_name": "lite300",
            "config": "MACH_LITE300",
            "number": "408",
            "machine_type": "LITE300"
        },
        "1955": {
            "machine_description": "Nokia RX-51 board",
            "machine_name": "nokia_rx51",
            "config": "MACH_NOKIA_RX51",
            "number": "1955",
            "machine_type": "NOKIA_RX51"
        },
        "373": {
            "machine_description": "Gumstix",
            "machine_name": "gumstix",
            "config": "ARCH_GUMSTIX",
            "number": "373",
            "machine_type": "GUMSTIX"
        },
        "704": {
            "machine_description": "ADI Engineering RoadRunner Development Platform",
            "machine_name": "roadrunner",
            "config": "MACH_ROADRUNNER",
            "number": "704",
            "machine_type": "ROADRUNNER"
        },
        "705": {
            "machine_description": "Atmel AT91RM9200-EK",
            "machine_name": "at91rm9200ek",
            "config": "MACH_AT91RM9200EK",
            "number": "705",
            "machine_type": "AT91RM9200EK"
        },
        "702": {
            "machine_description": "eco920",
            "machine_name": "eco920",
            "config": "MACH_ECO920",
            "number": "702",
            "machine_type": "ECO920"
        },
        "89": {
            "machine_description": "Intel DBPXA250 Development Platform (aka Lubbock)",
            "machine_name": "lubbock",
            "config": "ARCH_LUBBOCK",
            "number": "89",
            "machine_type": "LUBBOCK"
        },
        "399": {
            "machine_description": "Cogent CSB337",
            "machine_name": "csb337",
            "config": "MACH_CSB337",
            "number": "399",
            "machine_type": "CSB337"
        },
        "87": {
            "machine_description": "Simpad",
            "machine_name": "simpad",
            "config": "SA1100_SIMPAD",
            "number": "87",
            "machine_type": "SIMPAD"
        },
        "1711": {
            "machine_description": "CALAO QIL_A9260",
            "machine_name": "qil_a9260",
            "config": "MACH_QIL_A9260",
            "number": "1711",
            "machine_type": "QIL_A9260"
        },
        "1710": {
            "machine_description": "CALAO USB_A9263",
            "machine_name": "usb_a9263",
            "config": "MACH_USB_A9263",
            "number": "1710",
            "machine_type": "USB_A9263"
        },
        "799": {
            "machine_description": "Intel IQ81340SC",
            "machine_name": "iq81340sc",
            "config": "MACH_IQ81340SC",
            "number": "799",
            "machine_type": "IQ81340SC"
        },
        "612": {
            "machine_description": "KB920x",
            "machine_name": "kb9200",
            "config": "MACH_KB9200",
            "number": "612",
            "machine_type": "KB9200"
        },
        "613": {
            "machine_description": "OMAP310 based Siemens SX1",
            "machine_name": "sx1",
            "config": "MACH_SX1",
            "number": "613",
            "machine_type": "SX1"
        },
        "1652": {
            "machine_description": "Technologic Systems TS-78xx SBC",
            "machine_name": "ts78xx",
            "config": "MACH_TS78XX",
            "number": "1652",
            "machine_type": "TS78XX"
        },
        "2415": {
            "machine_description": "Raumfeld Speaker",
            "machine_name": "raumfeld_speaker",
            "config": "MACH_RAUMFELD_SPEAKER",
            "number": "2415",
            "machine_type": "RAUMFELD_SPEAKER"
        },
        "1657": {
            "machine_description": "Lyrtech SFFSDR",
            "machine_name": "sffsdr",
            "config": "MACH_SFFSDR",
            "number": "1657",
            "machine_type": "SFFSDR"
        },
        "2288": {
            "machine_description": "Atmel AT91SAM9G20-EK 2 MMC Slot Mod",
            "machine_name": "at91sam9g20ek_2mmc",
            "config": "MACH_AT91SAM9G20EK_2MMC",
            "number": "2288",
            "machine_type": "AT91SAM9G20EK_2MMC"
        },
        "2289": {
            "machine_description": "BCMRING",
            "machine_name": "bcmring",
            "config": "MACH_BCMRING",
            "number": "2289",
            "machine_type": "BCMRING"
        },
        "1138": {
            "machine_description": "OMAP3430 3430SDP board",
            "machine_name": "omap_3430sdp",
            "config": "MACH_OMAP_3430SDP",
            "number": "1138",
            "machine_type": "OMAP_3430SDP"
        },
        "2282": {
            "machine_description": "LaCie d2 Network",
            "machine_name": "d2net",
            "config": "MACH_D2NET",
            "number": "2282",
            "machine_type": "D2NET"
        },
        "2283": {
            "machine_description": "LaCie Big Disk Network",
            "machine_name": "bigdisk",
            "config": "MACH_BIGDISK",
            "number": "2283",
            "machine_type": "BIGDISK"
        },
        "245": {
            "machine_description": "Intel IXDP425 Development Platform",
            "machine_name": "ixdp425",
            "config": "ARCH_IXDP425",
            "number": "245",
            "machine_type": "IXDP425"
        },
        "1179": {
            "machine_description": "BugLabs BUGBase",
            "machine_name": "bug",
            "config": "MACH_BUG",
            "number": "1179",
            "machine_type": "BUG"
        },
        "243": {
            "machine_description": "Intel IXDP2800 Development Platform",
            "machine_name": "ixdp2800",
            "config": "ARCH_IXDP2800",
            "number": "243",
            "machine_type": "IXDP2800"
        },
        "242": {
            "machine_description": "Intel IXDP2400 Development Platform",
            "machine_name": "ixdp2400",
            "config": "ARCH_IXDP2400",
            "number": "242",
            "machine_type": "IXDP2400"
        },
        "1430": {
            "machine_description": "Freescale MX27PDK",
            "machine_name": "mx27_3ds",
            "config": "MACH_MX27_3DS",
            "number": "1430",
            "machine_type": "MX27_3DS"
        },
        "2272": {
            "machine_description": "ARM-Versatile Express",
            "machine_name": "vexpress",
            "config": "MACH_VEXPRESS",
            "number": "2272",
            "machine_type": "VEXPRESS"
        },
        "2885": {
            "machine_description": "Omicron DEVIXP",
            "machine_name": "devixp",
            "config": "MACH_DEVIXP",
            "number": "2885",
            "machine_type": "DEVIXP"
        },
        "1439": {
            "machine_description": "Halibut Board (QCT SURF7200A)",
            "machine_name": "halibut",
            "config": "MACH_HALIBUT",
            "number": "1439",
            "machine_type": "HALIBUT"
        },
        "1009": {
            "machine_description": "SMDK2412",
            "machine_name": "smdk2412",
            "config": "MACH_SMDK2412",
            "number": "1009",
            "machine_type": "SMDK2412"
        },
        "510": {
            "machine_description": "OMAP2420 H4 board",
            "machine_name": "omap_h4",
            "config": "MACH_OMAP_H4",
            "number": "510",
            "machine_type": "OMAP_H4"
        },
        "515": {
            "machine_description": "TI-OSK",
            "machine_name": "omap_osk",
            "config": "MACH_OMAP_OSK",
            "number": "515",
            "machine_type": "OMAP_OSK"
        },
        "1227": {
            "machine_description": "Voipac PXA270",
            "machine_name": "vpac270",
            "config": "MACH_VPAC270",
            "number": "1227",
            "machine_type": "VPAC270"
        },
        "624": {
            "machine_description": "OpenGear/CM4008",
            "machine_name": "cm4008",
            "config": "MACH_CM4008",
            "number": "624",
            "machine_type": "CM4008"
        },
        "1340": {
            "machine_description": "Toradex Colibri PXA320",
            "machine_name": "colibri320",
            "config": "MACH_COLIBRI320",
            "number": "1340",
            "machine_type": "COLIBRI320"
        },
        "451": {
            "machine_description": "Cirrus Logic EDB9312 Evaluation Board",
            "machine_name": "edb9312",
            "config": "MACH_EDB9312",
            "number": "451",
            "machine_type": "EDB9312"
        },
        "452": {
            "machine_description": "Generic OMAP1510/1610/1710",
            "machine_name": "omap_generic",
            "config": "MACH_OMAP_GENERIC",
            "number": "452",
            "machine_type": "OMAP_GENERIC"
        },
        "1084": {
            "machine_description": "SMDK2443",
            "machine_name": "smdk2443",
            "config": "MACH_SMDK2443",
            "number": "1084",
            "machine_type": "SMDK2443"
        },
        "2886": {
            "machine_description": "Omicron MICCPT",
            "machine_name": "miccpt",
            "config": "MACH_MICCPT",
            "number": "2886",
            "machine_type": "MICCPT"
        },
        "2887": {
            "machine_description": "Omicron MIC256",
            "machine_name": "mic256",
            "config": "MACH_MIC256",
            "number": "2887",
            "machine_type": "MIC256"
        },
        "4828": {
            "machine_description": "BCM2835",
            "machine_name": "bcm2835",
            "config": "MACH_BCM2835",
            "number": "4828",
            "machine_type": "BCM2835"
        },
        "970": {
            "machine_description": "OMAP730 F-Sample",
            "machine_name": "omap_fsample",
            "config": "MACH_OMAP_FSAMPLE",
            "number": "970",
            "machine_type": "OMAP_FSAMPLE"
        },
        "656": {
            "machine_description": "Acer-N30",
            "machine_name": "n30",
            "config": "MACH_N30",
            "number": "656",
            "machine_type": "N30"
        },
        "180": {
            "machine_description": "KS8695 Centaur Development Board",
            "machine_name": "ks8695",
            "config": "ARCH_KS8695",
            "number": "180",
            "machine_type": "KS8695"
        },
        "1501": {
            "machine_description": "Olimex SAM9-L9260",
            "machine_name": "sam9_l9260",
            "config": "MACH_SAM9_L9260",
            "number": "1501",
            "machine_type": "SAM9_L9260"
        },
        "1507": {
            "machine_description": "uCdragon YL-9200",
            "machine_name": "yl9200",
            "config": "MACH_YL9200",
            "number": "1507",
            "machine_type": "YL9200"
        },
        "1504": {
            "machine_description": "ARM-RealView PB1176",
            "machine_name": "realview_pb1176",
            "config": "MACH_REALVIEW_PB1176",
            "number": "1504",
            "machine_type": "REALVIEW_PB1176"
        },
        "1508": {
            "machine_description": "Marvell Orion-NAS Reference Design",
            "machine_name": "rd88f5182",
            "config": "MACH_RD88F5182",
            "number": "1508",
            "machine_type": "RD88F5182"
        },
        "1509": {
            "machine_description": "Buffalo/Revogear Kurobox Pro",
            "machine_name": "kurobox_pro",
            "config": "MACH_KUROBOX_PRO",
            "number": "1509",
            "machine_type": "KUROBOX_PRO"
        },
        "659": {
            "machine_description": "MobilePro900/C",
            "machine_name": "nec_mp900",
            "config": "MACH_NEC_MP900",
            "number": "659",
            "machine_type": "NEC_MP900"
        },
        "2627": {
            "machine_description": "QCT QSD8X50A ST1.5",
            "machine_name": "qsd8x50a_st1_5",
            "config": "MACH_QSD8X50A_ST1_5",
            "number": "2627",
            "machine_type": "QSD8X50A_ST1_5"
        },
        "2624": {
            "machine_description": "iControl/SafeTcam boards using Embedian MXM-8x10 CoM",
            "machine_name": "icontrol",
            "config": "MACH_ICONTROL",
            "number": "2624",
            "machine_type": "ICONTROL"
        },
        "2625": {
            "machine_description": "PXA168-based GuruPlug Display (gplugD) Platform",
            "machine_name": "gplugd",
            "config": "MACH_GPLUGD",
            "number": "2625",
            "machine_type": "GPLUGD"
        },
        "3087": {
            "machine_description": "VPR200",
            "machine_name": "vpr200",
            "config": "MACH_VPR200",
            "number": "3087",
            "machine_type": "VPR200"
        },
        "15": {
            "machine_description": "Shark",
            "machine_name": "shark",
            "config": "ARCH_SHARK",
            "number": "15",
            "machine_type": "SHARK"
        },
        "17": {
            "machine_description": "Compaq-PersonalServer",
            "machine_name": "personal_server",
            "config": "ARCH_PERSONAL_SERVER",
            "number": "17",
            "machine_type": "PERSONAL_SERVER"
        },
        "19": {
            "machine_description": "LinkUp Systems L7200",
            "machine_name": "l7200",
            "config": "ARCH_L7200",
            "number": "19",
            "machine_type": "L7200"
        },
        "862": {
            "machine_description": "Amstrad E3 (Delta)",
            "machine_name": "ams_delta",
            "config": "MACH_AMS_DELTA",
            "number": "862",
            "machine_type": "AMS_DELTA"
        },
        "865": {
            "machine_description": "Iomega NAS 100d",
            "machine_name": "nas100d",
            "config": "MACH_NAS100D",
            "number": "865",
            "machine_type": "NAS100D"
        },
        "2753": {
            "machine_description": "Wiliboard WBD-222",
            "machine_name": "wbd222",
            "config": "MACH_WBD222",
            "number": "2753",
            "machine_type": "WBD222"
        },
        "2750": {
            "machine_description": "Compulab CM-T3517",
            "machine_name": "cm_t3517",
            "config": "MACH_CM_T3517",
            "number": "2750",
            "machine_type": "CM_T3517"
        },
        "2697": {
            "machine_description": "Buffalo Nas WXL",
            "machine_name": "terastation_wxl",
            "config": "MACH_TERASTATION_WXL",
            "number": "2697",
            "machine_type": "TERASTATION_WXL"
        },
        "880": {
            "machine_description": "Hilscher nxdkn",
            "machine_name": "nxdkn",
            "config": "MACH_NXDKN",
            "number": "880",
            "machine_type": "NXDKN"
        },
        "887": {
            "machine_description": "S3C2413",
            "machine_name": "s3c2413",
            "config": "MACH_S3C2413",
            "number": "887",
            "machine_type": "S3C2413"
        },
        "885": {
            "machine_description": "Palm T|X",
            "machine_name": "palmtx",
            "config": "MACH_PALMTX",
            "number": "885",
            "machine_type": "PALMTX"
        },
        "3234": {
            "machine_description": "GS_IA18_S",
            "machine_name": "gsia18s",
            "config": "MACH_GSIA18S",
            "number": "3234",
            "machine_type": "GSIA18S"
        },
        "1616": {
            "machine_description": "CM-X300 module",
            "machine_name": "cm_x300",
            "config": "MACH_CM_X300",
            "number": "1616",
            "machine_type": "CM_X300"
        },
        "1967": {
            "machine_description": "OMAP Zoom2 board",
            "machine_name": "omap_zoom2",
            "config": "MACH_OMAP_ZOOM2",
            "number": "1967",
            "machine_type": "OMAP_ZOOM2"
        },
        "327": {
            "machine_description": "Intel IQ31244",
            "machine_name": "iq31244",
            "config": "ARCH_IQ31244",
            "number": "327",
            "machine_type": "IQ31244"
        },
        "775": {
            "machine_description": "IMOTE 2",
            "machine_name": "intelmote2",
            "config": "MACH_INTELMOTE2",
            "number": "775",
            "machine_type": "INTELMOTE2"
        },
        "774": {
            "machine_description": "Stargate 2",
            "machine_name": "stargate2",
            "config": "MACH_STARGATE2",
            "number": "774",
            "machine_type": "STARGATE2"
        },
        "776": {
            "machine_description": "Keith und Koep Trizeps IV module",
            "machine_name": "trizeps4",
            "config": "MACH_TRIZEPS4",
            "number": "776",
            "machine_type": "TRIZEPS4"
        },
        "772": {
            "machine_description": "Cirrus Logic EDB9315A Evaluation Board",
            "machine_name": "edb9315a",
            "config": "MACH_EDB9315A",
            "number": "772",
            "machine_type": "EDB9315A"
        },
        "2239": {
            "machine_description": "INCO startec LILLY-1131",
            "machine_name": "lilly1131",
            "config": "MACH_LILLY1131",
            "number": "2239",
            "machine_type": "LILLY1131"
        },
        "1681": {
            "machine_description": "Marvell RD-88F6192-NAS Development Board",
            "machine_name": "rd88f6192_nas",
            "config": "MACH_RD88F6192_NAS",
            "number": "1681",
            "machine_type": "RD88F6192_NAS"
        },
        "1680": {
            "machine_description": "Marvell DB-88F6281-BP Development Board",
            "machine_name": "db88f6281_bp",
            "config": "MACH_DB88F6281_BP",
            "number": "1680",
            "machine_type": "DB88F6281_BP"
        },
        "1683": {
            "machine_description": "Marvell DB-78x00-BP Development Board",
            "machine_name": "db78x00_bp",
            "config": "MACH_DB78X00_BP",
            "number": "1683",
            "machine_type": "DB78X00_BP"
        },
        "1769": {
            "machine_description": "Marvell LB88RC8480 Development Board",
            "machine_name": "lb88rc8480",
            "config": "MACH_LB88RC8480",
            "number": "1769",
            "machine_type": "LB88RC8480"
        },
        "1685": {
            "machine_description": "SMDK2416",
            "machine_name": "smdk2416",
            "config": "MACH_SMDK2416",
            "number": "1685",
            "machine_type": "SMDK2416"
        },
        "1761": {
            "machine_description": "Pandora Handheld Console",
            "machine_name": "omap3_pandora",
            "config": "MACH_OMAP3_PANDORA",
            "number": "1761",
            "machine_type": "OMAP3_PANDORA"
        },
        "1766": {
            "machine_description": "Maxtor Shared Storage II",
            "machine_name": "mss2",
            "config": "MACH_MSS2",
            "number": "1766",
            "machine_type": "MSS2"
        },
        "1788": {
            "machine_description": "Marvell DB-MV88AP510-BP Development Board",
            "machine_name": "dove_db",
            "config": "MACH_DOVE_DB",
            "number": "1788",
            "machine_type": "DOVE_DB"
        },
        "1140": {
            "machine_description": "VSTMS",
            "machine_name": "vstms",
            "config": "MACH_VSTMS",
            "number": "1140",
            "machine_type": "VSTMS"
        },
        "1260": {
            "machine_description": "Armadillo-500",
            "machine_name": "armadillo5x0",
            "config": "MACH_ARMADILLO5X0",
            "number": "1260",
            "machine_type": "ARMADILLO5X0"
        },
        "662": {
            "machine_description": "Sperry-Sun KAFA",
            "machine_name": "kafa",
            "config": "MACH_KAFA",
            "number": "662",
            "machine_type": "KAFA"
        },
        "1264": {
            "machine_description": "Digi ConnectCore 9P 9360 on an JSCC9P9360 Devboard",
            "machine_name": "cc9p9360js",
            "config": "MACH_CC9P9360JS",
            "number": "1264",
            "machine_type": "CC9P9360JS"
        },
        "2097": {
            "machine_description": "Marvell SheevaPlug Reference Board",
            "machine_name": "sheevaplug",
            "config": "MACH_SHEEVAPLUG",
            "number": "2097",
            "machine_type": "SHEEVAPLUG"
        },
        "1546": {
            "machine_description": "OMAP3 Beagle Board",
            "machine_name": "omap3_beagle",
            "config": "MACH_OMAP3_BEAGLE",
            "number": "1546",
            "machine_type": "OMAP3_BEAGLE"
        },
        "1542": {
            "machine_description": "D-Link DNS-323",
            "machine_name": "dns323",
            "config": "MACH_DNS323",
            "number": "1542",
            "machine_type": "DNS323"
        },
        "2520": {
            "machine_description": "MINI6410",
            "machine_name": "mini6410",
            "config": "MACH_MINI6410",
            "number": "2520",
            "machine_type": "MINI6410"
        },
        "2383": {
            "machine_description": "Flint Development Platform",
            "machine_name": "flint",
            "config": "MACH_FLINT",
            "number": "2383",
            "machine_type": "FLINT"
        },
        "1548": {
            "machine_description": "Nokia N810",
            "machine_name": "nokia_n810",
            "config": "MACH_NOKIA_N810",
            "number": "1548",
            "machine_type": "NOKIA_N810"
        },
        "543": {
            "machine_description": "SHARP Husky",
            "machine_name": "husky",
            "config": "MACH_HUSKY",
            "number": "543",
            "machine_type": "HUSKY"
        },
        "545": {
            "machine_description": "SHARP Shepherd",
            "machine_name": "shepherd",
            "config": "MACH_SHEPHERD",
            "number": "545",
            "machine_type": "SHEPHERD"
        },
        "1461": {
            "machine_description": "HTC Herald",
            "machine_name": "herald",
            "config": "MACH_HERALD",
            "number": "1461",
            "machine_type": "HERALD"
        },
        "1460": {
            "machine_description": "TCT_HAMMER",
            "machine_name": "tct_hammer",
            "config": "MACH_TCT_HAMMER",
            "number": "1460",
            "machine_type": "TCT_HAMMER"
        },
        "2708": {
            "machine_description": "QCT QSD8X50 SURF",
            "machine_name": "qsd8x50_surf",
            "config": "MACH_QSD8X50_SURF",
            "number": "2708",
            "machine_type": "QSD8X50_SURF"
        },
        "993": {
            "machine_description": "OMAP310 based Palm Zire71",
            "machine_name": "omap_palmz71",
            "config": "MACH_OMAP_PALMZ71",
            "number": "993",
            "machine_type": "OMAP_PALMZ71"
        },
        "2212": {
            "machine_description": "Atmel AT91SAM9G45-EKES",
            "machine_name": "at91sam9g45ekes",
            "config": "MACH_AT91SAM9G45EKES",
            "number": "2212",
            "machine_type": "AT91SAM9G45EKES"
        },
        "2707": {
            "machine_description": "QCT MSM7X30 FFA",
            "machine_name": "msm7x30_ffa",
            "config": "MACH_MSM7X30_FFA",
            "number": "2707",
            "machine_type": "MSM7X30_FFA"
        },
        "1828": {
            "machine_description": "PXA930 Handheld Platform (aka SAAR)",
            "machine_name": "saar",
            "config": "MACH_SAAR",
            "number": "1828",
            "machine_type": "SAAR"
        },
        "1824": {
            "machine_description": "taskit Stamp9G20",
            "machine_name": "stamp9g20",
            "config": "MACH_STAMP9G20",
            "number": "1824",
            "machine_type": "STAMP9G20"
        },
        "1827": {
            "machine_description": "PXA910 Evaluation Board (aka TavorEVB)",
            "machine_name": "tavorevb",
            "config": "MACH_TAVOREVB",
            "number": "1827",
            "machine_type": "TAVOREVB"
        },
        "1826": {
            "machine_description": "SMDKC100",
            "machine_name": "smdkc100",
            "config": "MACH_SMDKC100",
            "number": "1826",
            "machine_type": "SMDKC100"
        },
        "414": {
            "machine_description": "Arcom/Eurotech Vulcan",
            "machine_name": "arcom_vulcan",
            "config": "MACH_ARCOM_VULCAN",
            "number": "414",
            "machine_type": "ARCOM_VULCAN"
        },
        "2413": {
            "machine_description": "Raumfeld Controller",
            "machine_name": "raumfeld_rc",
            "config": "MACH_RAUMFELD_RC",
            "number": "2413",
            "machine_type": "RAUMFELD_RC"
        },
        "1388": {
            "machine_description": "Marvell Form Factor Development Platform (aka Littleton)",
            "machine_name": "littleton",
            "config": "MACH_LITTLETON",
            "number": "1388",
            "machine_type": "LITTLETON"
        },
        "2414": {
            "machine_description": "Raumfeld Connector",
            "machine_name": "raumfeld_connector",
            "config": "MACH_RAUMFELD_CONNECTOR",
            "number": "2414",
            "machine_type": "RAUMFELD_CONNECTOR"
        },
        "413": {
            "machine_description": "Iskratel XCEP",
            "machine_name": "xcep",
            "config": "MACH_XCEP",
            "number": "413",
            "machine_type": "XCEP"
        },
        "923": {
            "machine_description": "Embest ATEB9200",
            "machine_name": "ateb9200",
            "config": "MACH_ATEB9200",
            "number": "923",
            "machine_type": "ATEB9200"
        },
        "1380": {
            "machine_description": "DaVinci DM646x EVM",
            "machine_name": "davinci_dm6467_evm",
            "config": "MACH_DAVINCI_DM6467_EVM",
            "number": "1380",
            "machine_type": "DAVINCI_DM6467_EVM"
        },
        "1381": {
            "machine_description": "DaVinci DM355 EVM",
            "machine_name": "davinci_dm355_evm",
            "config": "MACH_DAVINCI_DM355_EVM",
            "number": "1381",
            "machine_type": "DAVINCI_DM355_EVM"
        },
        "2149": {
            "machine_description": "phyCARD-i.MX27",
            "machine_name": "pca100",
            "config": "MACH_PCA100",
            "number": "2149",
            "machine_type": "PCA100"
        },
        "927": {
            "machine_description": "Acer-N35",
            "machine_name": "n35",
            "config": "MACH_N35",
            "number": "927",
            "machine_type": "N35"
        },
        "1921": {
            "machine_description": "W90P910EVB",
            "machine_name": "w90p910evb",
            "config": "MACH_W90P910EVB",
            "number": "1921",
            "machine_type": "W90P910EVB"
        },
        "1923": {
            "machine_description": "W90P950EVB",
            "machine_name": "w90p950evb",
            "config": "MACH_W90P950EVB",
            "number": "1923",
            "machine_type": "W90P950EVB"
        },
        "1924": {
            "machine_description": "W90N960EVB",
            "machine_name": "w90n960evb",
            "config": "MACH_W90N960EVB",
            "number": "1924",
            "machine_type": "W90N960EVB"
        },
        "831": {
            "machine_description": "SHARP Borzoi",
            "machine_name": "borzoi",
            "config": "MACH_BORZOI",
            "number": "831",
            "machine_type": "BORZOI"
        },
        "835": {
            "machine_description": "Palm LifeDrive",
            "machine_name": "palmld",
            "config": "MACH_PALMLD",
            "number": "835",
            "machine_type": "PALMLD"
        },
        "838": {
            "machine_description": "Intel IXDP2805/2855 Development Platform",
            "machine_name": "ixdp28x5",
            "config": "MACH_IXDP28X5",
            "number": "838",
            "machine_type": "IXDP28X5"
        },
        "839": {
            "machine_description": "OMAP1510 based Palm Tungsten|T",
            "machine_name": "omap_palmtt",
            "config": "MACH_OMAP_PALMTT",
            "number": "839",
            "machine_type": "OMAP_PALMTT"
        },
        "362": {
            "machine_description": "SMDK2440",
            "machine_name": "s3c2440",
            "config": "ARCH_S3C2440",
            "number": "362",
            "machine_type": "S3C2440"
        },
        "2932": {
            "machine_description": "AM3517/05 CRANEBOARD",
            "machine_name": "craneboard",
            "config": "MACH_CRANEBOARD",
            "number": "2932",
            "machine_type": "CRANEBOARD"
        },
        "382": {
            "machine_description": "TI-H2",
            "machine_name": "omap_h2",
            "config": "MACH_OMAP_H2",
            "number": "382",
            "machine_type": "OMAP_H2"
        },
        "384": {
            "machine_description": "Toshiba e740",
            "machine_name": "e740",
            "config": "MACH_E740",
            "number": "384",
            "machine_type": "E740"
        },
        "385": {
            "machine_description": "Intel IQ80331",
            "machine_name": "iq80331",
            "config": "ARCH_IQ80331",
            "number": "385",
            "machine_type": "IQ80331"
        },
        "387": {
            "machine_description": "ARM-Versatile PB",
            "machine_name": "versatile_pb",
            "config": "ARCH_VERSATILE_PB",
            "number": "387",
            "machine_type": "VERSATILE_PB"
        },
        "1645": {
            "machine_description": "Freescale MX35PDK",
            "machine_name": "mx35_3ds",
            "config": "MACH_MX35_3DS",
            "number": "1645",
            "machine_type": "MX35_3DS"
        },
        "1647": {
            "machine_description": "Neuros OSD2",
            "machine_name": "neuros_osd2",
            "config": "MACH_NEUROS_OSD2",
            "number": "1647",
            "machine_type": "NEUROS_OSD2"
        },
        "787": {
            "machine_description": "Eukrea",
            "machine_name": "cpuat91",
            "config": "MACH_CPUAT91",
            "number": "787",
            "machine_type": "CPUAT91"
        },
        "1773": {
            "machine_description": "OMAP Logic 3530 LV SOM board",
            "machine_name": "omap3530_lv_som",
            "config": "MACH_OMAP3530_LV_SOM",
            "number": "1773",
            "machine_type": "OMAP3530_LV_SOM"
        },
        "782": {
            "machine_description": "Philips PNX4008",
            "machine_name": "pnx4008",
            "config": "MACH_PNX4008",
            "number": "782",
            "machine_type": "PNX4008"
        },
        "1729": {
            "machine_description": "sapphire",
            "machine_name": "sapphire",
            "config": "MACH_SAPPHIRE",
            "number": "1729",
            "machine_type": "SAPPHIRE"
        },
        "1727": {
            "machine_description": "Nokia N810 WiMAX",
            "machine_name": "nokia_n810_wimax",
            "config": "MACH_NOKIA_N810_WIMAX",
            "number": "1727",
            "machine_type": "NOKIA_N810_WIMAX"
        },
        "1649": {
            "machine_description": "Keith und Koep Trizeps IV-WL module",
            "machine_name": "trizeps4wl",
            "config": "MACH_TRIZEPS4WL",
            "number": "1649",
            "machine_type": "TRIZEPS4WL"
        },
        "1743": {
            "machine_description": "Motorola EZX E6",
            "machine_name": "ezx_e6",
            "config": "MACH_EZX_E6",
            "number": "1743",
            "machine_type": "EZX_E6"
        },
        "2191": {
            "machine_description": "taskit PortuxG20",
            "machine_name": "portuxg20",
            "config": "MACH_PORTUXG20",
            "number": "2191",
            "machine_type": "PORTUXG20"
        },
        "152": {
            "machine_description": "ARM-FortuNet",
            "machine_name": "fortunet",
            "config": "ARCH_FORTUNET",
            "number": "152",
            "machine_type": "FORTUNET"
        },
        "2800": {
            "machine_description": "ti8168evm",
            "machine_name": "ti8168evm",
            "config": "MACH_TI8168EVM",
            "number": "2800",
            "machine_type": "TI8168EVM"
        },
        "254": {
            "machine_description": "HackKit Cpu Board",
            "machine_name": "hackkit",
            "config": "SA1100_HACKKIT",
            "number": "254",
            "machine_type": "HACKKIT"
        },
        "2200": {
            "machine_description": "OMAP3517/AM3517 EVM",
            "machine_name": "omap3517evm",
            "config": "MACH_OMAP3517EVM",
            "number": "2200",
            "machine_type": "OMAP3517EVM"
        },
        "1584": {
            "machine_description": "Buffalo Terastation Pro II/Live",
            "machine_name": "terastation_pro2",
            "config": "MACH_TERASTATION_PRO2",
            "number": "1584",
            "machine_type": "TERASTATION_PRO2"
        },
        "1585": {
            "machine_description": "Buffalo Linkstation Pro/Live",
            "machine_name": "linkstation_pro",
            "config": "MACH_LINKSTATION_PRO",
            "number": "1585",
            "machine_type": "LINKSTATION_PRO"
        },
        "731": {
            "machine_description": "Gateway 7001 AP",
            "machine_name": "gateway7001",
            "config": "MACH_GATEWAY7001",
            "number": "731",
            "machine_type": "GATEWAY7001"
        },
        "732": {
            "machine_description": "Phytec Messtechnik GmbH phyCORE-PXA270",
            "machine_name": "pcm027",
            "config": "MACH_PCM027",
            "number": "732",
            "machine_type": "PCM027"
        },
        "734": {
            "machine_description": "Simtec-Anubis",
            "machine_name": "anubis",
            "config": "MACH_ANUBIS",
            "number": "734",
            "machine_type": "ANUBIS"
        },
        "508": {
            "machine_description": "Synertronixx scb9328",
            "machine_name": "scb9328",
            "config": "MACH_SCB9328",
            "number": "508",
            "machine_type": "SCB9328"
        },
        "509": {
            "machine_description": "TI OMAP1710 H3 board",
            "machine_name": "omap_h3",
            "config": "MACH_OMAP_H3",
            "number": "509",
            "machine_type": "OMAP_H3"
        },
        "1212": {
            "machine_description": "Lanner EM7210",
            "machine_name": "em7210",
            "config": "MACH_EM7210",
            "number": "1212",
            "machine_type": "EM7210"
        },
        "1359": {
            "machine_description": "Cogent CSB726",
            "machine_name": "csb726",
            "config": "MACH_CSB726",
            "number": "1359",
            "machine_type": "CSB726"
        },
        "1358": {
            "machine_description": "Marvell Orion-2 Development Board",
            "machine_name": "db88f5281",
            "config": "MACH_DB88F5281",
            "number": "1358",
            "machine_type": "DB88F5281"
        },
        "1351": {
            "machine_description": "KwikByte CAM60",
            "machine_name": "cam60",
            "config": "MACH_CAM60",
            "number": "1351",
            "machine_type": "CAM60"
        },
        "463": {
            "machine_description": "Cirrus Logic EDB9315 Evaluation Board",
            "machine_name": "edb9315",
            "config": "MACH_EDB9315",
            "number": "463",
            "machine_type": "EDB9315"
        },
        "1354": {
            "machine_description": "Atmel AT91 EB01",
            "machine_name": "at91eb01",
            "config": "MACH_AT91EB01",
            "number": "1354",
            "machine_type": "AT91EB01"
        },
        "2045": {
            "machine_description": "PXA910-based TTC_DKB Development Platform",
            "machine_name": "ttc_dkb",
            "config": "MACH_TTC_DKB",
            "number": "2045",
            "machine_type": "TTC_DKB"
        },
        "169": {
            "machine_description": "Intel IQ80321",
            "machine_name": "iq80321",
            "config": "ARCH_IQ80321",
            "number": "169",
            "machine_type": "IQ80321"
        },
        "906": {
            "machine_description": "Armadeus APF9328",
            "machine_name": "apf9328",
            "config": "MACH_APF9328",
            "number": "906",
            "machine_type": "APF9328"
        },
        "160": {
            "machine_description": "Freescale MX1ADS",
            "machine_name": "mx1ads",
            "config": "ARCH_MX1ADS",
            "number": "160",
            "machine_type": "MX1ADS"
        },
        "161": {
            "machine_description": "Hynix GMS30C7201",
            "machine_name": "h7201",
            "config": "ARCH_H7201",
            "number": "161",
            "machine_type": "H7201"
        },
        "162": {
            "machine_description": "Hynix HMS30C7202",
            "machine_name": "h7202",
            "config": "ARCH_H7202",
            "number": "162",
            "machine_type": "H7202"
        },
        "964": {
            "machine_description": "D-Link DSM-G600 RevA",
            "machine_name": "dsmg600",
            "config": "MACH_DSMG600",
            "number": "964",
            "machine_type": "DSMG600"
        },
        "963": {
            "machine_description": "picotux 200",
            "machine_name": "picotux2xx",
            "config": "MACH_PICOTUX2XX",
            "number": "963",
            "machine_type": "PICOTUX2XX"
        },
        "1105": {
            "machine_description": "OpenGear/IM42xx",
            "machine_name": "im42xx",
            "config": "MACH_IM42XX",
            "number": "1105",
            "machine_type": "IM42XX"
        },
        "1100": {
            "machine_description": "GLAN Tank",
            "machine_name": "glantank",
            "config": "MACH_GLANTANK",
            "number": "1100",
            "machine_type": "GLANTANK"
        },
        "1101": {
            "machine_description": "Thecus N2100",
            "machine_name": "n2100",
            "config": "MACH_N2100",
            "number": "1101",
            "machine_type": "N2100"
        },
        "1511": {
            "machine_description": "Freescale MX31PDK (3DS)",
            "machine_name": "mx31_3ds",
            "config": "MACH_MX31_3DS",
            "number": "1511",
            "machine_type": "MX31_3DS"
        },
        "1108": {
            "machine_description": "QT2410",
            "machine_name": "qt2410",
            "config": "MACH_QT2410",
            "number": "1108",
            "machine_type": "QT2410"
        },
        "1109": {
            "machine_description": "Intel KIXRP435 Reference Platform",
            "machine_name": "kixrp435",
            "config": "MACH_KIXRP435",
            "number": "1109",
            "machine_type": "KIXRP435"
        },
        "1722": {
            "machine_description": "Kyoto Microcomputer Co., Ltd. KZM-ARM11-01",
            "machine_name": "kzm_arm11_01",
            "config": "MACH_KZM_ARM11_01",
            "number": "1722",
            "machine_type": "KZM_ARM11_01"
        },
        "1812": {
            "machine_description": "Marvell Orion-VoIP GE Reference Design",
            "machine_name": "rd88f5181l_ge",
            "config": "MACH_RD88F5181L_GE",
            "number": "1812",
            "machine_type": "RD88F5181L_GE"
        },
        "876": {
            "machine_description": "OpenGear/CM4002",
            "machine_name": "cm4002",
            "config": "MACH_CM4002",
            "number": "876",
            "machine_type": "CM4002"
        },
        "875": {
            "machine_description": "HTC Magician",
            "machine_name": "magician",
            "config": "MACH_MAGICIAN",
            "number": "875",
            "machine_type": "MAGICIAN"
        },
        "1818": {
            "machine_description": "Marvell Orion-VoIP FXO Reference Design",
            "machine_name": "rd88f5181l_fxo",
            "config": "MACH_RD88F5181L_FXO",
            "number": "1818",
            "machine_type": "RD88F5181L_FXO"
        },
        "2741": {
            "machine_description": "QCT MSM7X30 FLUID",
            "machine_name": "msm7x30_fluid",
            "config": "MACH_MSM7X30_FLUID",
            "number": "2741",
            "machine_type": "MSM7X30_FLUID"
        },
        "2031": {
            "machine_description": "Eukrea CPU9G20",
            "machine_name": "cpuat9g20",
            "config": "MACH_CPUAT9G20",
            "number": "2031",
            "machine_type": "CPUAT9G20"
        },
        "2038": {
            "machine_description": "Raidsonic NAS IB-4220-B",
            "machine_name": "nas4220b",
            "config": "MACH_NAS4220B",
            "number": "2038",
            "machine_type": "NAS4220B"
        },
        "890": {
            "machine_description": "Netgear WG302 v2 / WAG302 v2",
            "machine_name": "wg302v2",
            "config": "MACH_WG302V2",
            "number": "890",
            "machine_type": "WG302V2"
        },
        "1601": {
            "machine_description": "QNAP TS-409",
            "machine_name": "ts409",
            "config": "MACH_TS409",
            "number": "1601",
            "machine_type": "TS409"
        },
        "1973": {
            "machine_description": "Eukrea CPU9260",
            "machine_name": "cpuat9260",
            "config": "MACH_CPUAT9260",
            "number": "1973",
            "machine_type": "CPUAT9260"
        },
        "356": {
            "machine_description": "Radisys ENP-2611 PCI network processor board",
            "machine_name": "enp2611",
            "config": "ARCH_ENP2611",
            "number": "356",
            "machine_type": "ENP2611"
        },
        "809": {
            "machine_description": "SecureComputing/SE4200",
            "machine_name": "se4200",
            "config": "MACH_SE4200",
            "number": "809",
            "machine_type": "SE4200"
        },
        "801": {
            "machine_description": "Intel IQ81340MC",
            "machine_name": "iq81340mc",
            "config": "MACH_IQ81340MC",
            "number": "801",
            "machine_type": "IQ81340MC"
        },
        "2965": {
            "machine_description": "Flexibity Connect",
            "machine_name": "flexibity",
            "config": "MACH_FLEXIBITY",
            "number": "2965",
            "machine_type": "FLEXIBITY"
        },
        "769": {
            "machine_description": "Carmeva",
            "machine_name": "carmeva",
            "config": "MACH_CARMEVA",
            "number": "769",
            "machine_type": "CARMEVA"
        },
        "2849": {
            "machine_description": "Income s.r.o. SH-Dmaster PXA270 SBC",
            "machine_name": "income",
            "config": "MACH_INCOME",
            "number": "2849",
            "machine_type": "INCOME"
        },
        "1781": {
            "machine_description": "DaVinci DA830/OMAP L137 EVM",
            "machine_name": "davinci_da830_evm",
            "config": "MACH_DAVINCI_DA830_EVM",
            "number": "1781",
            "machine_type": "DAVINCI_DA830_EVM"
        },
        "218": {
            "machine_description": "VoiceBlue OMAP5910",
            "machine_name": "voiceblue",
            "config": "MACH_VOICEBLUE",
            "number": "218",
            "machine_type": "VOICEBLUE"
        },
        "1771": {
            "machine_description": "Freescale MX25PDK (3DS)",
            "machine_name": "mx25_3ds",
            "config": "MACH_MX25_3DS",
            "number": "1771",
            "machine_type": "MX25_3DS"
        },
        "2325": {
            "machine_description": "Marvell OpenRD Base Board",
            "machine_name": "openrd_base",
            "config": "MACH_OPENRD_BASE",
            "number": "2325",
            "machine_type": "OPENRD_BASE"
        },
        "1075": {
            "machine_description": "Ajeco 1ARM single board computer",
            "machine_name": "onearm",
            "config": "MACH_ONEARM",
            "number": "1075",
            "machine_type": "ONEARM"
        },
        "1072": {
            "machine_description": "emQbit's ECB_AT91",
            "machine_name": "ecbat91",
            "config": "MACH_ECBAT91",
            "number": "1072",
            "machine_type": "ECBAT91"
        },
        "4": {
            "machine_description": "EBSA285",
            "machine_name": "ebsa285",
            "config": "ARCH_EBSA285",
            "number": "4",
            "machine_type": "EBSA285"
        },
        "283": {
            "machine_description": "Arcom/Eurotech VIPER SBC",
            "machine_name": "viper",
            "config": "ARCH_VIPER",
            "number": "283",
            "machine_type": "VIPER"
        },
        "1673": {
            "machine_description": "Phytec Phycore pcm037",
            "machine_name": "pcm037",
            "config": "MACH_PCM037",
            "number": "1673",
            "machine_type": "PCM037"
        },
        "1091": {
            "machine_description": "Freecom FSG-3",
            "machine_name": "fsg",
            "config": "MACH_FSG",
            "number": "1091",
            "machine_type": "FSG"
        },
        "1099": {
            "machine_description": "Atmel AT91SAM9260-EK",
            "machine_name": "at91sam9260ek",
            "config": "MACH_AT91SAM9260EK",
            "number": "1099",
            "machine_type": "AT91SAM9260EK"
        },
        "672": {
            "machine_description": "OpenGear/CM41xx",
            "machine_name": "cm41xx",
            "config": "MACH_CM41XX",
            "number": "672",
            "machine_type": "CM41XX"
        },
        "673": {
            "machine_description": "Technologic Systems TS-72xx SBC",
            "machine_name": "ts72xx",
            "config": "MACH_TS72XX",
            "number": "673",
            "machine_type": "TS72XX"
        },
        "262": {
            "machine_description": "Atmel AT91RM9200-DK",
            "machine_name": "at91rm9200dk",
            "config": "ARCH_AT91RM9200DK",
            "number": "262",
            "machine_type": "AT91RM9200DK"
        },
        "260": {
            "machine_description": "Intel IXCDP1100 Development Platform",
            "machine_name": "ixcdp1100",
            "config": "ARCH_IXCDP1100",
            "number": "260",
            "machine_type": "IXCDP1100"
        },
        "1551": {
            "machine_description": "phyCORE-i.MX27",
            "machine_name": "pcm038",
            "config": "MACH_PCM038",
            "number": "1551",
            "machine_type": "PCM038"
        },
        "3004": {
            "machine_description": "ti8148evm",
            "machine_name": "ti8148evm",
            "config": "MACH_TI8148EVM",
            "number": "3004",
            "machine_type": "TI8148EVM"
        },
        "2990": {
            "machine_description": "REAL6410",
            "machine_name": "real6410",
            "config": "MACH_REAL6410",
            "number": "2990",
            "machine_type": "REAL6410"
        },
        "2495": {
            "machine_description": "AM18x/OMAP-L138 Hawkboard",
            "machine_name": "omapl138_hawkboard",
            "config": "MACH_OMAPL138_HAWKBOARD",
            "number": "2495",
            "machine_type": "OMAPL138_HAWKBOARD"
        },
        "50": {
            "machine_description": "CL-EDB7211 (EP7211 eval board)",
            "machine_name": "edb7211",
            "config": "ARCH_EDB7211",
            "number": "50",
            "machine_type": "EDB7211"
        },
        "1565": {
            "machine_description": "QNAP TS-109/TS-209",
            "machine_name": "ts209",
            "config": "MACH_TS209",
            "number": "1565",
            "machine_type": "TS209"
        },
        "2393": {
            "machine_description": "OMAP3 touchbook Board",
            "machine_name": "touchbook",
            "config": "MACH_TOUCHBOOK",
            "number": "2393",
            "machine_type": "TOUCHBOOK"
        },
        "2254": {
            "machine_description": "Airgoo-HMT",
            "machine_name": "hmt",
            "config": "MACH_HMT",
            "number": "2254",
            "machine_type": "HMT"
        },
        "538": {
            "machine_description": "Cirrus Logic EDB9302 Evaluation Board",
            "machine_name": "edb9302",
            "config": "MACH_EDB9302",
            "number": "538",
            "machine_type": "EDB9302"
        },
        "1326": {
            "machine_description": "Atmel AT91SAM9RL-EK",
            "machine_name": "at91sam9rlek",
            "config": "MACH_AT91SAM9RLEK",
            "number": "1326",
            "machine_type": "AT91SAM9RLEK"
        },
        "200": {
            "machine_description": "CEIVA/Polaroid Photo MAX Digital Picture Frame",
            "machine_name": "ceiva",
            "config": "ARCH_CEIVA",
            "number": "200",
            "machine_type": "CEIVA"
        },
        "986": {
            "machine_description": "Bluewater Systems Snapper CL15",
            "machine_name": "snapper_cl15",
            "config": "MACH_SNAPPER_CL15",
            "number": "986",
            "machine_type": "SNAPPER_CL15"
        },
        "2776": {
            "machine_description": "Cavium Networks CNS3420 Validation Board",
            "machine_name": "cns3420vb",
            "config": "MACH_CNS3420VB",
            "number": "2776",
            "machine_type": "CNS3420VB"
        },
        "110": {
            "machine_description": "Vibren PXA255 IDP",
            "machine_name": "pxa_idp",
            "config": "ARCH_PXA_IDP",
            "number": "110",
            "machine_type": "PXA_IDP"
        },
        "118": {
            "machine_description": "autronix autcpu12",
            "machine_name": "autcpu12",
            "config": "ARCH_AUTCPU12",
            "number": "118",
            "machine_type": "AUTCPU12"
        },
        "1858": {
            "machine_description": "Buffalo Linkstation Mini",
            "machine_name": "linkstation_mini",
            "config": "MACH_LINKSTATION_MINI",
            "number": "1858",
            "machine_type": "LINKSTATION_MINI"
        },
        "1859": {
            "machine_description": "Custom afeb9260 board",
            "machine_name": "afeb9260",
            "config": "MACH_AFEB9260",
            "number": "1859",
            "machine_type": "AFEB9260"
        },
        "1851": {
            "machine_description": "Freescale MXLADS",
            "machine_name": "mxlads",
            "config": "MACH_MXLADS",
            "number": "1851",
            "machine_type": "MXLADS"
        },
        "1524": {
            "machine_description": "Dave/DENX QongEVB-LITE",
            "machine_name": "qong",
            "config": "MACH_QONG",
            "number": "1524",
            "machine_type": "QONG"
        },
        "1257": {
            "machine_description": "MIO A701",
            "machine_name": "mioa701",
            "config": "MACH_MIOA701",
            "number": "1257",
            "machine_type": "MIOA701"
        },
        "919": {
            "machine_description": "OMAP24xx Apollon",
            "machine_name": "omap_apollon",
            "config": "MACH_OMAP_APOLLON",
            "number": "919",
            "machine_type": "OMAP_APOLLON"
        },
        "918": {
            "machine_description": "Palm Tungsten|C",
            "machine_name": "palmtc",
            "config": "MACH_PALMTC",
            "number": "918",
            "machine_type": "PALMTC"
        },
        "420": {
            "machine_description": "NHK8815",
            "machine_name": "nomadik",
            "config": "MACH_NOMADIK",
            "number": "420",
            "machine_type": "NOMADIK"
        },
        "917": {
            "machine_description": "Palm Tungsten|T5",
            "machine_name": "palmt5",
            "config": "MACH_PALMT5",
            "number": "917",
            "machine_type": "PALMT5"
        },
        "424": {
            "machine_description": "SHARP Poodle",
            "machine_name": "poodle",
            "config": "MACH_POODLE",
            "number": "424",
            "machine_type": "POODLE"
        },
        "300": {
            "machine_description": "Intel IXDP2801 Development Platform",
            "machine_name": "ixdp2801",
            "config": "ARCH_IXDP2801",
            "number": "300",
            "machine_type": "IXDP2801"
        },
        "1933": {
            "machine_description": "NCP",
            "machine_name": "ncp",
            "config": "MACH_NCP",
            "number": "1933",
            "machine_type": "NCP"
        },
        "1932": {
            "machine_description": "Marvell 88F6281 GTW GE Board",
            "machine_name": "mv88f6281gtw_ge",
            "config": "MACH_MV88F6281GTW_GE",
            "number": "1932",
            "machine_type": "MV88F6281GTW_GE"
        },
        "1939": {
            "machine_description": "DaVinci DM365 EVM",
            "machine_name": "davinci_dm365_evm",
            "config": "MACH_DAVINCI_DM365_EVM",
            "number": "1939",
            "machine_type": "DAVINCI_DM365_EVM"
        },
        "827": {
            "machine_description": "ARM-RealView EB",
            "machine_name": "realview_eb",
            "config": "MACH_REALVIEW_EB",
            "number": "827",
            "machine_type": "REALVIEW_EB"
        },
        "846": {
            "machine_description": "Freescale i.MX27ADS",
            "machine_name": "mx27ads",
            "config": "MACH_MX27ADS",
            "number": "846",
            "machine_type": "MX27ADS"
        },
        "844": {
            "machine_description": "Palm Tungsten|E2",
            "machine_name": "palmte2",
            "config": "MACH_PALMTE2",
            "number": "844",
            "machine_type": "PALMTE2"
        },
        "842": {
            "machine_description": "Simtec-OSIRIS",
            "machine_name": "osiris",
            "config": "MACH_OSIRIS",
            "number": "842",
            "machine_type": "OSIRIS"
        },
        "841": {
            "machine_description": "Arcom/Eurotech ZEUS",
            "machine_name": "arcom_zeus",
            "config": "MACH_ARCOM_ZEUS",
            "number": "841",
            "machine_type": "ARCOM_ZEUS"
        },
        "3503": {
            "machine_description": "TI-NSPIRE",
            "machine_name": "nspire",
            "config": "MACH_NSPIRE",
            "number": "3503",
            "machine_type": "NSPIRE"
        },
        "849": {
            "machine_description": "Giant Shoulder Inc Loft board",
            "machine_name": "loft",
            "config": "MACH_LOFT",
            "number": "849",
            "machine_type": "LOFT"
        },
        "848": {
            "machine_description": "Atmel AT91SAM9261-EK",
            "machine_name": "at91sam9261ek",
            "config": "MACH_AT91SAM9261EK",
            "number": "848",
            "machine_type": "AT91SAM9261EK"
        },
        "2679": {
            "machine_description": "QCT MSM7X30 SURF",
            "machine_name": "msm7x30_surf",
            "config": "MACH_MSM7X30_SURF",
            "number": "2679",
            "machine_type": "MSM7X30_SURF"
        },
        "1987": {
            "machine_description": "Bluewater Systems Snapper 9260/9G20 module",
            "machine_name": "snapper_9260",
            "config": "MACH_SNAPPER_9260",
            "number": "1987",
            "machine_type": "SNAPPER_9260"
        },
        "1633": {
            "machine_description": "Linksys WRT350N v2",
            "machine_name": "wrt350n_v2",
            "config": "MACH_WRT350N_V2",
            "number": "1633",
            "machine_type": "WRT350N_V2"
        },
        "1982": {
            "machine_description": "Brivo Systems LLC ACS-5000 Master board",
            "machine_name": "acs5k",
            "config": "MACH_ACS5K",
            "number": "1982",
            "machine_type": "ACS5K"
        },
        "1639": {
            "machine_description": "OMAP LDP board",
            "machine_name": "omap_ldp",
            "config": "MACH_OMAP_LDP",
            "number": "1639",
            "machine_type": "OMAP_LDP"
        },
        "1733": {
            "machine_description": "STMP378X",
            "machine_name": "stmp378x",
            "config": "MACH_STMP378X",
            "number": "1733",
            "machine_type": "STMP378X"
        },
        "1732": {
            "machine_description": "STMP37XX",
            "machine_name": "stmp37xx",
            "config": "MACH_STMP37XX",
            "number": "1732",
            "machine_type": "STMP37XX"
        },
        "1988": {
            "machine_description": "D-Link DSM-320 Wireless Media Player",
            "machine_name": "dsm320",
            "config": "MACH_DSM320",
            "number": "1988",
            "machine_type": "DSM320"
        },
        "753": {
            "machine_description": "Toshiba e330",
            "machine_name": "e330",
            "config": "MACH_E330",
            "number": "753",
            "machine_type": "E330"
        },
        "2330": {
            "machine_description": "OMAP3 Devkit8000",
            "machine_name": "devkit8000",
            "config": "MACH_DEVKIT8000",
            "number": "2330",
            "machine_type": "DEVKIT8000"
        },
        "2816": {
            "machine_description": "PXA168-based Teton BGA Development Platform",
            "machine_name": "teton_bga",
            "config": "MACH_TETON_BGA",
            "number": "2816",
            "machine_type": "TETON_BGA"
        },
        "755": {
            "machine_description": "Nokia 770",
            "machine_name": "nokia770",
            "config": "MACH_NOKIA770",
            "number": "755",
            "machine_type": "NOKIA770"
        },
        "2178": {
            "machine_description": "Logic OMAP3 Torpedo board",
            "machine_name": "omap3_torpedo",
            "config": "MACH_OMAP3_TORPEDO",
            "number": "2178",
            "machine_type": "OMAP3_TORPEDO"
        },
        "562": {
            "machine_description": "HP iPAQ HX4700",
            "machine_name": "h4700",
            "config": "MACH_H4700",
            "number": "562",
            "machine_type": "H4700"
        },
        "2183": {
            "machine_description": "A&W6410",
            "machine_name": "anw6410",
            "config": "MACH_ANW6410",
            "number": "2183",
            "machine_type": "ANW6410"
        },
        "1596": {
            "machine_description": "Toshiba e350",
            "machine_name": "e350",
            "config": "MACH_E350",
            "number": "1596",
            "machine_type": "E350"
        },
        "2187": {
            "machine_description": "Vista Silicon Visstrim_M10",
            "machine_name": "imx27_visstrim_m10",
            "config": "MACH_IMX27_VISSTRIM_M10",
            "number": "2187",
            "machine_type": "IMX27_VISSTRIM_M10"
        },
        "2479": {
            "machine_description": "SmartQ 7",
            "machine_name": "smartq7",
            "config": "MACH_SMARTQ7",
            "number": "2479",
            "machine_type": "SMARTQ7"
        },
        "2957": {
            "machine_description": "Brownstone Development Platform",
            "machine_name": "brownstone",
            "config": "MACH_BROWNSTONE",
            "number": "2957",
            "machine_type": "BROWNSTONE"
        },
        "220": {
            "machine_description": "HP iPAQ H5000",
            "machine_name": "h5400",
            "config": "ARCH_H5400",
            "number": "220",
            "machine_type": "H5400"
        },
        "1024": {
            "machine_description": "AML_M5900",
            "machine_name": "aml_m5900",
            "config": "MACH_AML_M5900",
            "number": "1024",
            "machine_type": "AML_M5900"
        },
        "1022": {
            "machine_description": "SMDK2413",
            "machine_name": "smdk2413",
            "config": "MACH_SMDK2413",
            "number": "1022",
            "machine_type": "SMDK2413"
        },
        "1029": {
            "machine_description": "Balloon3",
            "machine_name": "balloon3",
            "config": "MACH_BALLOON3",
            "number": "1029",
            "machine_type": "BALLOON3"
        },
        "723": {
            "machine_description": "ADS Sphere board",
            "machine_name": "adssphere",
            "config": "MACH_ADSSPHERE",
            "number": "723",
            "machine_type": "ADSSPHERE"
        },
        "1744": {
            "machine_description": "Motorola EZX E2",
            "machine_name": "ezx_e2",
            "config": "MACH_EZX_E2",
            "number": "1744",
            "machine_type": "EZX_E2"
        },
        "1745": {
            "machine_description": "Motorola EZX A910",
            "machine_name": "ezx_a910",
            "config": "MACH_EZX_A910",
            "number": "1745",
            "machine_type": "EZX_A910"
        },
        "1740": {
            "machine_description": "Motorola EZX A780",
            "machine_name": "ezx_a780",
            "config": "MACH_EZX_A780",
            "number": "1740",
            "machine_type": "EZX_A780"
        },
        "1741": {
            "machine_description": "Motorola EZX E680",
            "machine_name": "ezx_e680",
            "config": "MACH_EZX_E680",
            "number": "1741",
            "machine_type": "EZX_E680"
        },
        "1742": {
            "machine_description": "Motorola EZX A1200",
            "machine_name": "ezx_a1200",
            "config": "MACH_EZX_A1200",
            "number": "1742",
            "machine_type": "EZX_A1200"
        },
        "729": {
            "machine_description": "Toradex Colibri PXA270",
            "machine_name": "colibri",
            "config": "MACH_COLIBRI",
            "number": "729",
            "machine_type": "COLIBRI"
        },
        "604": {
            "machine_description": "Intel IXDPG425",
            "machine_name": "ixdpg425",
            "config": "MACH_IXDPG425",
            "number": "604",
            "machine_type": "IXDPG425"
        },
        "607": {
            "machine_description": "Cirrus Logic EDB9307 Evaluation Board",
            "machine_name": "edb9307",
            "config": "MACH_EDB9307",
            "number": "607",
            "machine_type": "EDB9307"
        },
        "606": {
            "machine_description": "ARM-Versatile AB",
            "machine_name": "versatile_ab",
            "config": "MACH_VERSATILE_AB",
            "number": "606",
            "machine_type": "VERSATILE_AB"
        },
        "1169": {
            "machine_description": "Contec Micro9-Mid",
            "machine_name": "micro9m",
            "config": "MACH_MICRO9M",
            "number": "1169",
            "machine_type": "MICRO9M"
        },
        "1202": {
            "machine_description": "Atmel AT91SAM9263-EK",
            "machine_name": "at91sam9263ek",
            "config": "MACH_AT91SAM9263EK",
            "number": "1202",
            "machine_type": "AT91SAM9263EK"
        },
        "1894": {
            "machine_description": "Marvell Orion-1-90 AP GE Reference Design",
            "machine_name": "rd88f6183ap_ge",
            "config": "MACH_RD88F6183AP_GE",
            "number": "1894",
            "machine_type": "RD88F6183AP_GE"
        },
        "1897": {
            "machine_description": "ARM-RealView PB-A8",
            "machine_name": "realview_pba8",
            "config": "MACH_REALVIEW_PBA8",
            "number": "1897",
            "machine_type": "REALVIEW_PBA8"
        },
        "958": {
            "machine_description": "Glomation GESBC-9312-sx",
            "machine_name": "gesbc9312",
            "config": "MACH_GESBC9312",
            "number": "958",
            "machine_type": "GESBC9312"
        },
        "2135": {
            "machine_description": "Marvell RD-78x00-MASA Development Board",
            "machine_name": "rd78x00_masa",
            "config": "MACH_RD78X00_MASA",
            "number": "2135",
            "machine_type": "RD78X00_MASA"
        },
        "48": {
            "machine_description": "HP Jornada 720",
            "machine_name": "jornada720",
            "config": "SA1100_JORNADA720",
            "number": "48",
            "machine_type": "JORNADA720"
        },
        "952": {
            "machine_description": "HP iPAQ RX1950",
            "machine_name": "rx1950",
            "config": "MACH_RX1950",
            "number": "952",
            "machine_type": "RX1950"
        },
        "2138": {
            "machine_description": "DaVinci DM355 leopard",
            "machine_name": "dm355_leopard",
            "config": "MACH_DM355_LEOPARD",
            "number": "2138",
            "machine_type": "DM355_LEOPARD"
        },
        "2139": {
            "machine_description": "QNAP TS-119/TS-219",
            "machine_name": "ts219",
            "config": "MACH_TS219",
            "number": "2139",
            "machine_type": "TS219"
        },
        "1682": {
            "machine_description": "Marvell RD-88F6281 Reference Board",
            "machine_name": "rd88f6281",
            "config": "MACH_RD88F6281",
            "number": "1682",
            "machine_type": "RD88F6281"
        },
        "5": {
            "machine_description": "Rebel-NetWinder",
            "machine_name": "netwinder",
            "config": "ARCH_NETWINDER",
            "number": "5",
            "machine_type": "NETWINDER"
        },
        "1114": {
            "machine_description": "Digi ConnectCore 9P 9360 on an A9M9750 Devboard",
            "machine_name": "cc9p9360dev",
            "config": "MACH_CC9P9360DEV",
            "number": "1114",
            "machine_type": "CC9P9360DEV"
        },
        "1440": {
            "machine_description": "HTC Dream",
            "machine_name": "trout",
            "config": "MACH_TROUT",
            "number": "1440",
            "machine_type": "TROUT"
        },
        "1292": {
            "machine_description": "MultiLink",
            "machine_name": "goramo_mlr",
            "config": "MACH_GORAMO_MLR",
            "number": "1292",
            "machine_type": "GORAMO_MLR"
        },
        "1564": {
            "machine_description": "McAfee/SG310",
            "machine_name": "sg310",
            "config": "MACH_SG310",
            "number": "1564",
            "machine_type": "SG310"
        },
        "1297": {
            "machine_description": "Compulab EM-X270",
            "machine_name": "em_x270",
            "config": "MACH_EM_X270",
            "number": "1297",
            "machine_type": "EM_X270"
        },
        "1566": {
            "machine_description": "Atmel AT91CAP9A-DK",
            "machine_name": "at91cap9adk",
            "config": "MACH_AT91CAP9ADK",
            "number": "1566",
            "machine_type": "AT91CAP9ADK"
        },
        "2722": {
            "machine_description": "OMAP3 STALKER",
            "machine_name": "sbc3530",
            "config": "MACH_SBC3530",
            "number": "2722",
            "machine_type": "SBC3530"
        },
        "2005": {
            "machine_description": "Buffalo Linkstation LS-HGL",
            "machine_name": "linkstation_ls_hgl",
            "config": "MACH_LINKSTATION_LS_HGL",
            "number": "2005",
            "machine_type": "LINKSTATION_LS_HGL"
        },
        "462": {
            "machine_description": "Cirrus Logic EDB9301 Evaluation Board",
            "machine_name": "edb9301",
            "config": "MACH_EDB9301",
            "number": "462",
            "machine_type": "EDB9301"
        },
        "1801": {
            "machine_description": "Netgear WNR854T",
            "machine_name": "wnr854t",
            "config": "MACH_WNR854T",
            "number": "1801",
            "machine_type": "WNR854T"
        },
        "1800": {
            "machine_description": "ADENEO NEOCORE 926",
            "machine_name": "neocore926",
            "config": "MACH_NEOCORE926",
            "number": "1800",
            "machine_type": "NEOCORE926"
        },
        "4390": {
            "machine_description": "Keystone",
            "machine_name": "keystone",
            "config": "MACH_KEYSTONE",
            "number": "4390",
            "machine_type": "KEYSTONE"
        },
        "2000": {
            "machine_description": "Toradex Colibri PXA300",
            "machine_name": "colibri300",
            "config": "MACH_COLIBRI300",
            "number": "2000",
            "machine_type": "COLIBRI300"
        },
        "475": {
            "machine_description": "Thorcom-VR1000",
            "machine_name": "vr1000",
            "config": "MACH_VR1000",
            "number": "475",
            "machine_type": "VR1000"
        },
    }

    # construct
    target_strings = {}
    votes = {}
    for k, machine_properties in machine_ids.items():
        if isinstance(machine_properties['machine_description'], list):
            target_strings[k] = machine_properties['machine_description']
        else:
            target_strings[k] = [machine_properties['machine_description']]
        votes[k] = 0

    # search
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1

    # vote
    target_machine_id = []
    for k, vote in votes.items():
        if vote >= 1:
            if k.startswith('0x'):
                target_machine_id.append((k, machine_ids[k]))
            else:
                target_machine_id.append((hex(int(k)), machine_ids[k]))

    if len(target_machine_id):
        return [i[0] for i in target_machine_id]
    else:
        return None


def find_machine_id(path_to_kernel):
    """Find the machine id in the image.

    Args:
        path_to_kernel(str): The path to the image.

    Returns:
        list: The list of machine ids the image supports.
    """
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_machine_id_s(strings)
