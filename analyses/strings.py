import re
import os
import yaml

from prettytable import PrettyTable
from analyses.analysis import Analysis
from database.dbf import get_database
from supervisor.logging_setup import logger_info


class Strings(Analysis):
    def get_candidates(self, firmware):
        """
        We can find useful strings in uncompressed binary.

        :param firmware: the firmware.
        :return: [paths/to/candidates] or None
        """
        kernel = firmware.get_path_to_kernel()
        if kernel is None:
            return None
        working_dir = os.path.dirname(kernel)
        candidates = [kernel]
        for file_ in os.listdir(working_dir):
            if file_.endswith('7z') or file_.endswith('xz'):
                zimage = os.path.join(working_dir, file_[:-3])
                if os.path.exists(zimage):
                    candidates.append(zimage)
        return candidates

    def get_all_strings(self, firmware):
        """
        We get strings from uncompressed binary.

        :param firmware:
        :return: [strings] or None
        """
        strings = []
        # get candidate files which contain useful strings
        candidates = self.get_candidates(firmware)
        if candidates is None:
            self.strings = None
            return
        for candidate in candidates:
            info = os.popen('strings {} -n 2 | grep -E "^[a-zA-Z]+[a-zA-Z0-9_-]{{1,20}}"'.format(candidate))
            strings += info.readlines()
        self.strings = strings

    def get_toh_by_strings(self, firmware):
        search_most_possible_toh_record(firmware, self.strings)

    def search_most_possible_target(self, firmware, extent=None):
        # by default we search the target
        if extent is None:
            extent = ['target']
        # get the database
        openwrt = get_database('openwrt')
        results = openwrt.select(*extent, deduplicated=True, transpose=True)
        # the result would be [[all_record[0], [all_record[1]]
        targets = []
        for ext in extent:
            targets += results[openwrt.header_last_selected.index(ext)]
        # we would like to search target from strings
        target_searched = {}
        for string in self.strings:
            for target in targets:
                if target.startswith('?'):
                    target = target[1:]
                if len(target) > len(string) or len(target) < 2:
                    continue
                if target in string.split('_'):
                    if target not in target_searched:
                        target_searched[target] = {'count': 0, 'strings': []}
                    target_searched[target]['count'] += 1
                    target_searched[target]['strings'].append(string.strip())
                    break
        # find the most possible target
        sum_of_occurrence = 0
        for k, v in target_searched.items():
            sum_of_occurrence += v['count']
        most_possible = None
        max_count = 0
        for k, v in target_searched.items():
            count = v['count']
            confidence = round(count / sum_of_occurrence, 2)
            if count > max_count:
                most_possible = k
                max_count = count
        logger_info(firmware.get_uuid(), 'analysis', 'strings', 'get the most possible target {}'.format(most_possible),
                    1)
        firmware.set_target(most_possible)

    def search_most_possible_subtarget(self, firmware, extent=None):
        # no target, no subtarget
        if firmware.get_target() is None:
            return
        # we just search the subtarget
        if extent is None:
            extent = ['subtarget']
        # get the database
        openwrt = get_database('openwrt')
        results = openwrt.select(*extent, transpose=True, deduplicated=True, target=firmware.get_target())
        subtargets = []
        for ext in extent:
            subtargets += results[openwrt.header_last_selected.index(ext)]
        # let's start
        subtarget_searched = {}
        for string in self.strings:
            for subtarget in subtargets:
                if subtarget.startswith('?'):
                    subtarget = subtarget[1:]
                if len(subtarget) > len(string) or len(subtarget) < 2 or subtarget == 'generic':
                    continue
                if subtarget in string.split('_'):
                    if subtarget not in subtarget_searched:
                        subtarget_searched[subtarget] = {'count': 0, 'strings': []}
                    subtarget_searched[subtarget]['count'] += 1
                    subtarget_searched[subtarget]['strings'].append(string.strip())
                    break
        # find the most possible subtarget
        sum_of_occurrence = 0
        for k, v in subtarget_searched.items():
            sum_of_occurrence += v['count']
        if not sum_of_occurrence:
            # nothing, but we may filter the candidates
            results = openwrt.select('*', target=firmware.get_target())
            filtered_results = []
            for v in results:
                if v[openwrt.header_last_selected.index('supportedcurrentrel')] == '':
                    continue
                filtered_results.append(v)
            # use kernel version to infer supportedcurrentrel
            # logger.debug('filter out candidates by matching kernel version')
            if firmware.get_revision() is None:
                return
            filtered_results_2 = []
            for v in filtered_results:
                if firmware.get_revision() == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
                    filtered_results_2.append(v)
            if len(filtered_results_2) == 1:
                # logger.debug('only one left, choose it for you automatically')
                subtarget = filtered_results_2[0][openwrt.header_last_selected.index('subtarget')]
                if subtarget == '':
                    subtarget = None
                firmware.set_subtarget(subtarget)
                logger_info(
                    firmware.get_uuid(), 'analysis', 'strings', 'get the most possible subtarget {}'.format(subtarget),
                    1)
                firmware.set_toh(filtered_results_2[0], header=openwrt.header_last_selected)

                return
        most_possible = None
        max_count = 0
        for k, v in subtarget_searched.items():
            count = v['count']
            confidence = round(count / sum_of_occurrence, 2)
            if count > max_count:
                most_possible = k
                max_count = count
        firmware.set_subtarget(most_possible)
        logger_info(firmware.get_uuid(), 'analysis', 'strings',
                    'get the most possible subtarget {}'.format(most_possible), 1)

    def find_uart_model_by_strings(self, firmware):
        for string in self.strings:
            if string.find('8250') != -1 or string.find('16550') != -1:
                firmware.set_uart_name('ns16550A')
                self.info(firmware, 'uart model {} found'.format('ns16550A'), 1)
                break

    def find_uart_baud_rate_by_strings(self, firmware):
        for string in self.strings:
            if string.find('root=') != -1:
                # root=/dev/mtdblock1 rootfstype=squashfs,jffs2 noinitrd console=ttyS0,115200\n
                a, _, b = string.partition('console=')
                if _ is '':
                    continue
                else:
                    uart_baud = b.split(',')[1].strip()
                    firmware.set_uart_baud_rate(uart_baud)
                    self.info(firmware, 'uart baud {} found'.format(uart_baud), 1)
                    break

    def find_flash_type_by_strings(self, firmware):
        for string in self.strings:
            if string.find('physmap-flash') != -1:
                firmware.set_flash_type('nor')
                self.info(firmware, 'flash type {} flash found'.format('nor'), 1)
                break

    def find_cpu_model_by_strings(self, firmware):
        # fetch from linux-5.3
        candidates = {
            'proc-arm7tdmi': [
                {'cpu_id': '0x41007700', 'cpu_mask': '0xfff8ff00', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM7TDMI'},
                {'cpu_id': '0x0001d2ff', 'cpu_mask': '0x0001ffff', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'Triscend-A7x'},
                {'cpu_id': '0x0001d2ff', 'cpu_mask': '0x0001ffff', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'Atmel-AT91M40xxx'},
                {'cpu_id': '0x14000040', 'cpu_mask': '0xfff000e0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'Samsung-S3C3410'},
                {'cpu_id': '0x36365000', 'cpu_mask': '0xfffff000', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'Samsung-S3C44B0x'},
                {'cpu_id': '0x4c000000', 'cpu_mask': '0xfff000e0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'Samsung-S3C4510B'},
                {'cpu_id': '0x34100000', 'cpu_mask': '0xffff0000', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'Samsung-S3C4530'},
                {'cpu_id': '0x44b00000', 'cpu_mask': '0xffff0000', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'NETARM'}],
            'proc-arm9tdmi': [
                {'cpu_id': '0x41009900', 'cpu_mask': '0xfff8ff00', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM9TDMI'},
                {'cpu_id': '0x41029000', 'cpu_mask': '0xffffffff', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'P2001'}],
            'proc-arm720': [
                {'cpu_id': '0x41807100', 'cpu_mask': '0xffffff00', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM710T'},
                {'cpu_id': '0x41807200', 'cpu_mask': '0xffffff00', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM720T'}],
            'proc-arm740': [
                {'cpu_id': '0x41807400', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv4', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM740T'}],
            'proc-arm920': [
                {'cpu_id': '0x41009200', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM920T'}],
            'proc-arm922': [
                {'cpu_id': '0x41009220', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM922T'}],
            'proc-arm925': [
                {'cpu_id': '0x54029250', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM925T'},
                {'cpu_id': '0x54029150', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM925T'}],
            'proc-arm926': [
                {'cpu_id': '0x41069260', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv5tej', 'cpu_elf_name': 'v5',
                 'cpu_name': 'ARM926EJ-S'}],
            'proc-arm940': [
                {'cpu_id': '0x41009400', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv4t', 'cpu_elf_name': 'v4',
                 'cpu_name': 'ARM940T'}],
            'proc-arm946': [
                {'cpu_id': '0x41009460', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5t',
                 'cpu_name': 'ARM946E-S'}],
            'proc-arm1020': [
                {'cpu_id': '0x4104a200', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv5t', 'cpu_elf_name': 'v5',
                 'cpu_name': 'ARM1020'}],
            'proc-arm1020e': [
                {'cpu_id': '0x4105a200', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'ARM1020E'}],
            'proc-arm1022': [
                {'cpu_id': '0x4105a220', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'ARM1022'}],
            'proc-arm1026': [
                {'cpu_id': '0x4105a260', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv5tej', 'cpu_elf_name': 'v5',
                 'cpu_name': 'ARM1026EJ-S'}],
            'proc-fa526': [
                {'cpu_id': '0x66015261', 'cpu_mask': '0xff01fff1', 'cpu_arch_name': 'armv4', 'cpu_elf_name': 'v4',
                 'cpu_name': 'FA526'}],
            'proc-feroceon': [
                {'cpu_id': '0x41009260', 'cpu_mask': '0xff00fff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'Feroceon'},
                {'cpu_id': '0x56055310', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'Feroceon 88FR531-vd'},
                {'cpu_id': '0x56155710', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'Feroceon 88FR571-vd'},
                {'cpu_id': '0x56251310', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'Feroceon 88FR131'}],
            'proc-mohawk': [
                {'cpu_id': '0x56158000', 'cpu_mask': '0xfffff000', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'Marvell 88SV331x'}],
            'proc-sa110': [
                {'cpu_id': '0x4401a100', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv4', 'cpu_elf_name': 'v4',
                 'cpu_name': 'StrongARM-110'}],
            'proc-sa1100': [
                {'cpu_id': '0x4401a110', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv4', 'cpu_elf_name': 'v4',
                 'cpu_name': 'StrongARM-1100'},
                {'cpu_id': '0x6901b110', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv4', 'cpu_elf_name': 'v4',
                 'cpu_name': 'StrongARM-1110'}],
            'proc-v6': [
                {'cpu_id': '0x0007b000', 'cpu_mask': '0x0007f000', 'cpu_arch_name': 'armv6', 'cpu_elf_name': 'v6',
                 'cpu_name': 'ARMv6-compatible processor'}],
            'proc-v7': [
                {'cpu_id': '', 'cpu_mask': '', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc050', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc090', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc080', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x560f5800', 'cpu_mask': '0xff0fff00', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc170', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc180', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc070', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc0d0', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc0f0', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x420f00f0', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fc0e0', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fd090', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x410fd0a0', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x510f0400', 'cpu_mask': '0xff0ffc00', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'},
                {'cpu_id': '0x000f0000', 'cpu_mask': '0x000f0000', 'cpu_arch_name': 'armv7', 'cpu_elf_name': 'v7',
                 'cpu_name': 'ARMv7 Processor'}],
            'proc-v7m': [
                {'cpu_id': '0x410fc270', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7m', 'cpu_elf_name': 'v7m',
                 'cpu_name': 'ARMv7-M'},
                {'cpu_id': '0x410fc240', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7m', 'cpu_elf_name': 'v7m',
                 'cpu_name': 'ARMv7-M'},
                {'cpu_id': '0x410fc230', 'cpu_mask': '0xff0ffff0', 'cpu_arch_name': 'armv7m', 'cpu_elf_name': 'v7m',
                 'cpu_name': 'ARMv7-M'},
                {'cpu_id': '0x000f0000', 'cpu_mask': '0x000f0000', 'cpu_arch_name': 'armv7m', 'cpu_elf_name': 'v7m',
                 'cpu_name': 'ARMv7-M'}],
            'proc-xsc3': [
                {'cpu_id': '0x69056000', 'cpu_mask': '0xffffe000', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-V3 based processor'},
                {'cpu_id': '0x56056000', 'cpu_mask': '0xffffe000', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-V3 based processor'},
                {'cpu_id': '', 'cpu_mask': '', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-V3 based processor'}],
            'proc-xscale': [
                {'cpu_id': '0x69052000', 'cpu_mask': '0xfffffffe', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-80200'},
                {'cpu_id': '0x69052000', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-80200'},
                {'cpu_id': '0x69052e20', 'cpu_mask': '0xffffffe0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-80219'},
                {'cpu_id': '0x69052420', 'cpu_mask': '0xfffff7e0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IOP8032x Family'},
                {'cpu_id': '0x69054010', 'cpu_mask': '0xfffffd30', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IOP8033x Family'},
                {'cpu_id': '0x69052100', 'cpu_mask': '0xfffff7f0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-PXA250'},
                {'cpu_id': '0x69052120', 'cpu_mask': '0xfffff3f0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-PXA210'},
                {'cpu_id': '0x69054190', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IXP2400'},
                {'cpu_id': '0x690541a0', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IXP2800'},
                {'cpu_id': '0x690541c0', 'cpu_mask': '0xffffffc0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IXP42x Family'},
                {'cpu_id': '0x69054040', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IXP43x Family'},
                {'cpu_id': '0x69054200', 'cpu_mask': '0xffffff00', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-IXP46x Family'},
                {'cpu_id': '0x69052d00', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-PXA255'},
                {'cpu_id': '0x69054110', 'cpu_mask': '0xfffffff0', 'cpu_arch_name': 'armv5te', 'cpu_elf_name': 'v5',
                 'cpu_name': 'XScale-PXA270'}]}

        # construct
        target_strings = {}
        votes = {}
        for k, cpus in candidates.items():
            target_strings[k] = []
            votes[k] = 0
            for cpu in cpus:
                target_strings[k].append(cpu['cpu_arch_name'])
                target_strings[k].append(cpu['cpu_name'])
            target_strings[k] = list(set(target_strings[k]))
        # search
        for string in self.strings:
            string = string.strip()
            for k, v in target_strings.items():
                if string in v:
                    votes[k] += 1
        # vote
        vote = 0
        model = ''
        for k, v in votes.items():
            if v > vote:
                vote = v
                model = k

        arm32_cpus = yaml.safe_load(open(os.path.join(os.getcwd(), 'database/cpu.arm32.yaml')))
        target_cpus = []
        for candidate in candidates[model]:
            for arm32_cpu, properties in arm32_cpus.items():
                cpu_id = int(properties['cpu_id'], 16)
                if cpu_id & int(candidate['cpu_mask'], 16) == int(candidate['cpu_id'], 16):
                    target_cpus.append(arm32_cpu)
        if len(target_cpus):
            firmware.set_cpu_model(target_cpus[0])
            self.info(firmware, 'get cpu model: {}, take the first one by default'.format(target_cpus), 1)
            return True
        else:
            return False

    def run(self, firmware):
        self.get_all_strings(firmware)

        if self.strings is None:
            self.context['input'] = 'no strings at all'
            return False

        # kernel version is very critical
        for string in self.strings:
            string = string.strip()
            if len(string) < 20:
                continue
            r = re.search(r'[lL]inux version ([1-5]+\.\d+\.\d+).*', string)
            if r is not None:
                kernel_version = r.groups()[0]
                firmware.set_kernel_version(kernel_version)
                self.info(firmware, 'get the kernel version: {}'.format(kernel_version), 1)
                break

        self.search_most_possible_target(firmware)
        self.search_most_possible_subtarget(firmware)

        self.find_uart_model_by_strings(firmware)
        self.find_uart_baud_rate_by_strings(firmware)
        self.find_flash_type_by_strings(firmware)

        # cpu
        architecture = firmware.get_architecture()
        if architecture != 'arm':
            self.context['input'] = 'search strings to find CPU only valid for ARM'
            return False
        self.find_cpu_model_by_strings(firmware)

        return True

    def __init__(self):
        super().__init__()
        self.name = 'strings'
        self.description = 'handle strings'
        self.required = ['extraction', 'revision']
        self.context['hint'] = 'lack of strings'
        self.critical = False
        #
        self.strings = []


def search_most_possible_toh_record(firmware, strings, extent=None):
    LOG_SUFFIX = '[STRINGS for ToH]'
    if extent is None:
        extent = ['*']
    openwrt = get_database('openwrt')
    results = openwrt.select(*extent)
    table = PrettyTable(openwrt.header_last_selected)
    filterd_results = []
    for vs in results:
        possible = False
        for v in vs:
            for string in strings:
                if len(v) < len(string) or len(v) < 2 or v == 'generic':
                    continue
                if v.find(string) != -1:
                    filterd_results.append(vs)
                    table.add_row(vs)
                    possible = True
                    break
            if possible:
                break
    if len(filterd_results) == 0:
        # logger.info('nothing left {}'.format(LOG_SUFFIX))
        return

    # for line in table.__unicode__().split('\n'):
    #     logger.debug(line)

    # use kernel version to infer supportedcurrentrel
    # logger.debug('filter out candidates by matching kernel version {}'.format(LOG_SUFFIX))
    if firmware.get_revision() is None:
        return
    filterd_results_2 = []
    for v in filterd_results:
        if firmware.get_revision() == v[openwrt.header_last_selected.index('supportedcurrentrel')]:
            filterd_results_2.append(v)
    if len(filterd_results_2) == 1:
        # logger.info('only one left, choose it automatically {}'.format(LOG_SUFFIX))
        firmware.set_toh(filterd_results[0])
        return
    if len(filterd_results_2) == 0:
        # logger.info('nothing left {}'.format(LOG_SUFFIX))
        return
