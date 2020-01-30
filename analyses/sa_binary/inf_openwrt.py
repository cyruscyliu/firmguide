import os

from analyses.analysis import Analysis
from slcore.database.dbf import get_database
from slcore.naive_parsers.openwrt import *
from slcore.parser import get_candidates, get_all_strings


class OpenWRT(Analysis):
    def run(self, firmware):
        if firmware.get_brand() is None:
            self.context['input'] = 'run with -b BRAND'
            return True

        if firmware.get_brand() != 'openwrt':
            return True

        path_to_kernel = firmware.get_path_to_kernel()
        # TODO get from analysis strings
        candidates = get_candidates(path_to_kernel)
        strings = get_all_strings(candidates)

        # revision, target, subtarget
        revision = find_openwrt_revision(firmware.get_kernel_version())
        self.info(firmware, 'get openwrt revision: {}'.format(revision), 1)
        target = search_most_possible_target(strings)
        self.info(firmware, 'get openwrt target: {}'.format(target), 1)
        subtarget = search_most_possible_subtarget(target,strings)
        self.info(firmware, 'get openwrt subtarget: {}'.format(target), 1)
        if firmware.get_url():
            revision, target, subtarget = parse_openwrt_url(firmware.get_url()) # the most precise way
            self.info(firmware, 'get openwrt revision: {}'.format(revision), 1)
            self.info(firmware, 'get openwrt target: {}'.format(target), 1)
            self.info(firmware, 'get openwrt subtarget: {}'.format(target), 1)

        # toh
        # search_most_possible_toh_record(strings)
        toh = find_openwrt_toh(revision, target, subtarget)
        self.info(firmware, 'get openwrt revision: {}'.format(toh), 1)
        if toh:
            machine_name = find_machine_name_by_openwrt_toh(toh, header)
            self.info(firmware, 'get machine name: {}'.format(toh), 1)
            cpu = find_cpu_by_openwrt_toh(toh, header)
            self.info(firmware, 'get cpu: {}'.format(toh), 1)
            ram_size = find_ram_size_by_openwrt_toh(toh, header)
            self.info(firmware, 'get ram size: {}'.format(toh), 1)

        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'openwrt'
        self.description = 'handle openwrt firmware'
        self.required = []
        self.context['hint'] = 'not openwrt firmware'
        self.critical = False
        self.settings = ['target', 'subtarget', 'revision', 'toh', 'machine_name', 'cpu', 'ram_size']

