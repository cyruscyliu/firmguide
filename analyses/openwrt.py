import os

from analyses.common.analysis import AnalysisGroup, Analysis
from analyses.common.display import print_table
from database.db import DatabaseOpenWRTMapping
from database.dbf import get_database


class OpenWRTURL(Analysis):
    def run(self, firmware):
        """
        Example:
            http://archive.openwrt.org/chaos_calmer/15.05/ar71xx/generic/openwrt-15.05-ar71xx-generic-bxu2000n-2-a1-kernel.bin
                                                      ^     ^       ^
                                                  revision      subtarget
                                                          target
            http://archive.openwrt.org/backfire/10.03/orion/openwrt-wrt350nv2-squashfs-recovery.bin
                                                  ^     ^
                                                revision
                                                      target
        """
        if not firmware.get_brand() == 'openwrt':
            return True
        url = firmware.get_url()
        if url is None:
            self.context['input'] = 'assign the download url for this firmware'
            return False
        homepage = os.path.dirname(url)

        items = homepage.split('/')
        revision = items[4]
        target = items[5]
        subtarget = None
        if len(items) == 7:
            subtarget = items[6]

        firmware.set_homepage(homepage)
        self.info('\033[32mdownload page found {}\033[0m'.format(homepage))
        firmware.set_target(target)
        self.info('\033[32mget the most possible target {}\033[0m'.format(target))
        firmware.set_subtarget(subtarget)
        self.info('\033[32mget the most possible subtarget {}\033[0m'.format(subtarget))
        firmware.set_revision(revision)
        self.info('\033[32mget the revision {}\033[0m'.format(revision))
        return True

    def __init__(self):
        super().__init__()
        self.name = 'url'
        self.description = 'parse OpenWRT firmware download url'
        self.log_suffix = '[URL]'
        self.required = []
        self.context['hint'] = 'update download url for this firmware'
        self.critical = False


class OpenWRTRevision(Analysis):
    def run(self, firmware):
        kernel_version = firmware.get_kernel_version()
        if kernel_version is None:
            self.context['input'] = 'kernel version is not available'
            return False
        openwrt_mapping = DatabaseOpenWRTMapping()
        openwrt_revision = openwrt_mapping.select('revision', kernel_version=kernel_version)
        firmware.set_revision(openwrt_revision)
        if openwrt_revision is None:
            self.context['input'] = 'update the database to handle this kernel version'
            return False

    def __init__(self):
        super().__init__()
        self.name = 'revision'
        self.description = 'parse OpenWRT revision by kernel version'
        self.log_suffix = '[KERNEL VERSION]'
        self.required = ['kernel']
        self.context['hint'] = 'no kernel version available or no handler for this kernel version'
        self.critical = False


class OpenWRTToH(Analysis):
    def get_openwrt_toh(self, firmware):
        revision = firmware.get_revision()
        target = firmware.get_target()
        subtarget = firmware.get_subtarget()
        openwrt = get_database('openwrt')
        results = openwrt.select('*', supportedcurrentrel=revision, target=target, subtarget=subtarget)
        if len(results) == 1:
            toh = results[0]
            header = openwrt.header_last_selected
        else:
            toh = None
            header = None
        if toh:
            firmware.set_toh(toh, header=header)
            self.info('\033[32mget the toh {}\033[0m'.format(toh))
            print_table(header, toh)

    def get_cpu_by_openwrt_toh(self, firmware):
        cpu, soc = firmware.get_toh('packagearchitecture', 'cpu')
        if cpu is not None and cpu != '':
            firmware.set_cpu_model(cpu)
            self.info('\033[32mget cpu model: {}\033[0m'.format(cpu))
        if soc is not None and cpu != '':
            firmware.set_soc_model(soc)
            self.info('\033[32mget soc model: {}\033[0m'.format(soc))
        [ram] = firmware.get_toh('rammb')
        if ram is not None and ram != '':
            firmware.set_ram(0, ram, unit='MiB')
            self.info('\033[32mget memory info, base: {}, size: {}MB\033[0m'.format(0, ram))

    def get_ram_by_openwrt_toh(self, firmware):
        [ram] = firmware.get_toh('rammb')
        if ram is not None and ram != '':
            firmware.set_ram(0, ram, unit='MiB')
            self.info('\033[32mget memory info, base: {}, size: {}MB\033[0m'.format(0, ram))

    def get_flash_by_openwrt_toh(self, firmware):
        [flash] = firmware.get_toh('flashmb')
        if flash is not None and flash != '' and flash != '?':
            # microSD, NAND, CF card, microSDXC, SDHC, eMMC
            if flash.find('NAND') != -1:
                firmware.set_flash_type('nand')
                self.info('\033[32mflash type {} found\033[0m'.format('nand flash'))
            else:
                firmware.set_flash_type('nor')
                self.info('\033[32mflash type {} found\033[0m'.format('nor flash'))

    def run(self, firmware):
        self.get_openwrt_toh(firmware)
        self.get_cpu_by_openwrt_toh(firmware)
        self.get_flash_by_openwrt_toh(firmware)

    def __init__(self):
        super().__init__()
        self.description = 'extract information from OpenWRT table of hardware'
        self.name = 'toh'
        self.log_suffix = '[OpenWRT ToH]'
        self.required = ['kernel', 'url']
        self.context['hint'] = ''
        self.critical = False
