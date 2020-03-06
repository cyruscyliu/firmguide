import os
import yaml

from slcore.parser import get_candidates, get_all_strings


def find_machine_dir_s(strings, arch):
    """Find which Linux kernel board the image belongs to.

    Args:
        strings (list): Strings from the image.
        arch (str)    : The architecture. It's required because of the db interface.

    Returns:
        list: A list of Linux kernel boards the image may belongs to.
    """
    # TODO the signature should be refined because of too much FP
    signature = yaml.safe_load(
        open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'signature.{}.yaml'.format(arch))))

    # construct
    target_strings = {}
    votes = {}
    for k, strings in signature.items():
        target_strings[k] = strings
        votes[k] = 0

    # search
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1

    # vote
    target_machine_dir = []
    max_to_min = sorted(votes, key=votes.get, reverse=True)
    for vote in max_to_min:
        if votes[vote] > 1:
            target_machine_dir.append(vote)

    return target_machine_dir


def find_machine_dir(path_to_kernel, arch):
    """Find which Linux kernel board the image belongs to.

    Args:
        path_to_kernel(str): Path to the kernel. We will get strings from it.
        arch (str)         : The architecture. It's required because of the db interface.

    Returns:
        list: A list of Linux kernel boards the image may belongs to.
    """
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_machine_dir_s(strings, arch)


sig = {
    # mips 5.3
    "0x10000000": {
        "machine_description": [
            "Alchemy Bosporus Gateway Reference",
            "Alchemy Bosporus Gateway Reference",
            "Alchemy Db1x00",
            "Alchemy Pb1000",
            "Alchemy Pb1100",
            "Alchemy Pb1200",
            "Alchemy Pb1500",
            "Alchemy Pb1550",
            "DB1000",
            "DB1500",
            "DB1100",
            "PB1500",
            "PB1100",
            "PB1200",
            "DB1200",
            "DB1300",
            "DB1550",
            "PB1550",
            "MTX-1",
            "XXS1500",
            "GPR"
        ],
        "number": "0x10000000",
        "machine_type": "alchemy"
    },
    "0x10000010": {
        "machine_description": [
            "TI AR7 (TNETD7300)",
            "TI AR7 (TNETD7100)",
            "TI AR7 (TNETD7200)",
            "TI AR7 (Unknown)",
            "TI AR7 (TNETV1050)",
            "TI AR7 (TNETV1055)",
            "TI AR7 (TNETV1056)",
            "TI AR7 (TNETV1060)"
        ],
        "number": "0x10000010",
        "machine_type": "ar7"
    },
    "0x10000020": {
        "machine_description": "Basler eXcite",
        "number": "0x10000020",
        "machine_type": "basler"
    },
    "0x10000030": {
        "machine_description": "Broadcom BCM47XX",
        "number": "0x10000030",
        "machine_type": "bcm47xx"
    },
    "0x10000040": {
        "machine_description": [
            "bcm63xx/%s (0x%04x/0x%04X)",
            "bcm63xx/%s (0x%04x/0x%02X)"
        ],
        "number": "0x10000040",
        "machine_type": "bcm63xx"
    },
    "0x10000050": {
        "machine_description": "octeon_board_type_string",
        "number": "0x10000050",
        "machine_type": "cavium-octeon"
    },
    "0x10000060": {
        "machine_description": [
            "Cobalt Qube",
            "Cobalt RaQ",
            "Cobalt Qube2",
            "Cobalt RaQ2",
            "MIPS Cobalt"
        ],
        "number": "0x10000060",
        "machine_type": "cobalt"
    },
    "0x10000070": {
        "machine_description": [
            "unknown DECstation",
            "DECstation 2100/3100",
            "DECsystem 5100",
            "DECstation 5000/200",
            "DECstation 5000/1xx",
            "Personal DECstation 5000/xx",
            "DECstation 5000/2x0",
            "DECsystem 5400",
            "DECsystem 5500",
            "DECsystem 5800",
            "DECsystem 5900",
        ],
        "number": "0x10000070",
        "machine_type": "dec"
    },
    "0x10000080": {
        "machine_description": [
            "NEC EMMA2RH Mark-eins",
            "Unknown NEC board"
        ],
        "number": "0x10000080",
            "machine_type": "emma"
        },
        "0x10000090": {
            "machine_description": [
                 "SGI Indy",
                 "SGI Origin",
                 "SGI IP28",
                 "SGI Octane",
                 "SGI O2",
                 "Jazz MIPS_Magnum_4000",
                 "Jazz Acer_PICA_61",
                 "SNI RM200_PCI",
                 "SNI RM200_PCI-R5K",
            ],
            "number": "0x10000090",
            "machine_type": "fw"
        },
        "0x100000a0": {
            "machine_description": "Wind River PPMC (GT64120)",
            "number": "0x100000a0",
            "machine_type": "gt64120"
        },
        "0x100000a0": {
            "machine_description": [
                "MQ 2",
                "MQ Pro",
                "SP 25",
                "SP 50",
                "SP 100",
                "SP 5000",
                "SP 7000",
                "SP 1000"
            ],
            "number": "0x100000a0",
            "machine_type": "lasat"
        },
        "0x100000b0": {
            "machine_description": [
                 "unknown loongson machine",
                 "lemote-fuloong-2e-box",
                 "lemote-fuloong-2f-box",
                 "lemote-mengloong-2f-7inches",
                 "lemote-yeeloong-2f-8.9inches",
                 "dexxon-gidum-2f-10inches"
            ],
            "number": "0x100000b0",
            "machine_type": "loongson"
        },
        "0x100000c0": {
            "machine_description": "MIPSsim",
            "number": "0x100000c0",
            "machine_type": "mipssim"
        },
        "0x100000d0": {
            "machine_description": "MIPS Malta",
            "number": "0x100000d0",
            "machine_type": "mti-malta"
        },
        "0x100000e0": {
            "machine_description": [
                "NXP STB22x",
                "NXP PNX8550/JBS",
                "NXP PNX8950/STB810"
            ],
            "number": "0x100000e0",
            "machine_type": "nxp"
        },
        "0x100000f0": {
            "machine_description": [
                "PMC-Sierra MSP4200 Eval Board",
                "PMC-Sierra MSP4200 VoIP Gateway",
                "PMC-Sierra MSP7120 Eval Board",
                "PMC-Sierra MSP7120 Residential Gateway",
                "PMC-Sierra MSP7120 FPGA",
                "PMC-Sierra Yosemite"
            ],
            "number": "0x100000a0",
            "machine_type": "pmc-sierra"
        },
        "0x10000100": {
            "machine_description": [
                "Mikrotik RB532A",
                "Mikrotik RB532"
            ],
            "number": "0x10000100",
            "machine_type": "rb532"
        },
        "0x10000110": {
            "machine_description": "SiByte",
            "number": "0x10000110",
            "machine_type": "sibyte"
        },
        "0x10000120": {
            "machine_description": [
                "Toshiba JMR_TX3927",
                "Toshiba RBTX4927",
                "Toshiba RBTX4937",
                "Toshiba RBTX4938",
                "Toshiba RBTX4939"
            ],
            "number": "0x10000120",
            "machine_type": "txx9"
        },
        "0x10000130": {
            "machine_description": "NEC VR4100 series",
            "number": "0x10000130",
            "machine_type": "vr41xx"
        },
        "0x10000140": {
            "machine_description": [
                "Atheros AR5312",
                "Atheros AR2312",
                "Atheros AR2313",
                "Atheros AR2315",
                "Atheros AR2316",
                "Atheros AR2317",
                "Atheros AR2318",
                "Atheros (unknown)",
            ],
            "number": "0x10000140",
            "machine_type": "ath25"
        },
        "0x10000150": {
            "machine_description": [
                 "Qualcomm Atheros QCA%s ver %u rev %u",
                 "Qualcomm Atheros TP%s rev %u",
                 "Atheros AR%s rev %u"
            ],
            "number": "0x10000150",
            "machine_type": "ath79"
        },
        "0x10000150": {
            "machine_description": "Generic BMIPS kernel",
            "number": "0x10000150",
            "machine_type": "bmips"
        },
        "0x10000160": {
            "machine_description": [
                "JZ4780",
                "JZ4770",
                "JZ4740",
            ],
            "number": "0x10000160",
            "machine_type": "jz4740"
        },
        "0x10000170": {
            "machine_description": [
                "LOONGSON LS1B",
                "LOONGSON LS1C",
                "LOONGSON (unknown)"
            ],
            "number": "0x10000160",
            "machine_type": "loongson32"
        },
        "0x10000170": {
            "machine_description": [
                "unknown loongson machine",
                "lemote-fuloong-2e-box",
                "lemote-fuloong-2f-box",
                "lemote-mengloong-2f-7inches",
                "lemote-yeeloong-2f-8.9inches",
                "dexxon-gdium-2f",
                "lemote-nas-2f",
                "lemote-lynloong-2f",
                "generic-loongson-machine",
            ],
            "number": "0x10000170",
            "machine_type": "loongson64"
        },
        "0x10000180": {
            "machine_description": [
                "Broadcom XLPII Series",
                "Netlogic XLP Series",
                "Netlogic XLR/XLS Series"
            ],
            "number": "0x10000180",
            "machine_type": "netlogic"
        },
        "0x10000190": {
            "machine_description": "MIPS Para-Virtualized Guest",
            "number": "0x10000190",
            "machine_type": "paravirt"
        },
        "0x100001a0": {
            "machine_description": "PIC32MZDA",
            "number": "0x100001a0",
            "machine_type": "pic32"
        },
        "0x100001b0": {
            "machine_description": [
                "IMG Pistachio SoC (B0)",
                "IMG Pistachio SoC (A1)",
                "IMG Pistachio SoC"
            ],
            "number": "0x100001b0",
            "machine_type": "pistachio"
        },
        "0x100001c0": {
            "machine_description": [
                "Ralink %s ver:%u eco:%u",
                "Ralink %s id:%u rev:%u",
                "MediaTek %s ver:%u eco:%u",
                "MediaTek %s ver:%u eco:%u"
            ],
            "number": "0x100001c0",
            "machine_type": "ralink"
        },
        "0x100001d0": {
            "machine_description": [
                "lantiq,danube"
                "lantiq,twinpass"
                "lantiq,ase"
                "lantiq,ar9"
                "lantiq,gr9"
                "lantiq,vr9"
                "lantiq,ar10"
                "lantiq,grx390"
            ],
            "number": "0x100001d0",
            "machine_type": "lantiq"
        }
    }

