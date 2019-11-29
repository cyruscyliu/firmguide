import os

from pyquery import PyQuery as pq
from analyses.common.analysis import AnalysisGroup, Analysis
from database.db import DatabaseOpenWRTMapping
from database.dbf import get_database


def find_urls_in_openwrt_homepage(homepage):
    """
    The url for ImageBuilder must include "ImageBuilder".
    The url for config includes, OpenWrt.config(10.03), config.diff(15.05).
    """
    html = pq(url=homepage)
    a = html('a')
    image_builder = None
    dot_config = None
    for item in a.items():
        href = item.attr('href')
        if image_builder is None and href.find('ImageBuilder') != -1:
            image_builder = os.path.join(homepage, href)
        if dot_config is None and (href.find('config.diff') != -1 or href.find('OpenWrt.config') != -1):
            dot_config = os.path.join(homepage, href)
    return image_builder, dot_config


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
        self.info(firmware, 'download page found {}'.format(homepage), 1)
        firmware.set_target(target)
        self.info(firmware, 'get the most possible target {}'.format(target), 1)
        firmware.set_subtarget(subtarget)
        self.info(firmware, 'get the most possible subtarget {}'.format(subtarget), 1)
        firmware.set_revision(revision)
        self.info(firmware, 'get the revision {}'.format(revision), 1)
        _, dot_config = find_urls_in_openwrt_homepage(homepage)  # 2, 4
        path_to_dot_config = os.path.join(firmware.working_dir, 'openwrt.config')
        os.system('wget -nc {} -O {} >/dev/null 2>&1'.format(url, path_to_dot_config))
        if dot_config is None:
            self.context['input'] = 'you must find the source code for this new openwrt version'
            return False
        firmware.set_path_to_dot_config(path_to_dot_config)
        self.info(firmware, 'get the openwrt config at {}'.format(path_to_dot_config), 1)
        return True

    def __init__(self):
        super().__init__()
        self.name = 'url'
        self.description = 'parse OpenWRT firmware download url'
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
        self.info(firmware, 'get the revision {}'.format(openwrt_revision), 1)
        if openwrt_revision is None:
            self.context['input'] = 'update the database to handle this kernel version'
            return False
        return True

    def __init__(self):
        super().__init__()
        self.name = 'revision'
        self.description = 'parse OpenWRT revision by kernel version'
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
            self.info(firmware, 'get the toh {}'.format(toh), 1)
            return True
        else:
            self.context['input'] = 'information for toh is not enough'
            return False

    def get_cpu_by_openwrt_toh(self, firmware):
        cpu, soc = firmware.get_toh('packagearchitecture', 'cpu')
        if cpu is not None and cpu != '':
            firmware.set_cpu_model(cpu)
            self.info(firmware, 'get cpu model: {}'.format(cpu), 1)
        if soc is not None and cpu != '':
            firmware.set_soc_model(soc)
            self.info(firmware, 'get soc model: {}'.format(soc), 1)
        [ram] = firmware.get_toh('rammb')
        if ram is not None and ram != '':
            firmware.set_ram(0, ram, unit='MiB')
            self.info(firmware, 'get memory info, base: {}, size: {}MB'.format(0, ram), 1)
        return True

    def get_ram_by_openwrt_toh(self, firmware):
        [ram] = firmware.get_toh('rammb')
        if ram is not None and ram != '':
            firmware.set_ram(0, ram, unit='MiB')
            self.info(firmware, 'get memory info, base: {}, size: {}MB'.format(0, ram), 1)
        return True

    def get_flash_by_openwrt_toh(self, firmware):
        [flash] = firmware.get_toh('flashmb')
        if flash is not None and flash != '' and flash != '?':
            # microSD, NAND, CF card, microSDXC, SDHC, eMMC
            if flash.find('NAND') != -1:
                firmware.set_flash_type('nand')
                self.info(firmware, 'flash type {} found'.format('nand flash'), 1)
            else:
                firmware.set_flash_type('nor')
                self.info(firmware, 'flash type {} found'.format('nor flash'), 1)
        return True

    def run(self, firmware):
        if self.get_openwrt_toh(firmware) and \
                self.get_cpu_by_openwrt_toh(firmware) and \
                self.get_ram_by_openwrt_toh(firmware) and \
                self.get_flash_by_openwrt_toh(firmware):
            return True
        else:
            return False

    def __init__(self):
        super().__init__()
        self.description = 'extract information from OpenWRT table of hardware'
        self.name = 'toh'
        self.required = ['kernel', 'url']
        self.context['hint'] = ''
        self.critical = False
