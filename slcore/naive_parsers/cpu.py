import os
import yaml

from slcore.parser import get_candidates, get_all_strings


# fetch from linux-5.3
cpu_list = {
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
         'cpu_name': 'XScale-PXA270'}]
}


def find_cpu_in_strings(strings):
    """Find which CPU model the image runs on.

    :param strings: Strings from the image.
    :type  strings: str
    :returns      : A list of CPU modes the image may runs on.
    :rtype        : list
    """
    # construct
    target_strings = {}
    votes = {}
    for k, cpus in cpu_list.items():
        target_strings[k] = []
        votes[k] = 0
        for cpu in cpus:
            target_strings[k].append(cpu['cpu_arch_name'])
            target_strings[k].append(cpu['cpu_name'])
        target_strings[k] = list(set(target_strings[k]))

    # search
    for string in strings:
        string = string.strip()
        for k, v in target_strings.items():
            if string in v:
                votes[k] += 1
    # vote
    vote = 0
    model = None
    for k, v in votes.items():
        if v > vote:
            vote = v
            model = k

    if model is None:
        return []

    arm_cpus = yaml.safe_load(
        open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'cpu.arm.yaml')))
    target_cpus = []
    for candidate in cpu_list[model]:
        for arm_cpu, properties in arm_cpus.items():
            cpu_id = int(properties['cpu_id'], 16)
            if cpu_id & int(candidate['cpu_mask'], 16) == int(candidate['cpu_id'], 16):
                target_cpus.append(arm_cpu)

    wanted_cpus = ['arm11mpcore', 'cortex-a9', 'cortex-a15']
    if len(target_cpus):
        for target_cpu in target_cpus:
            if target_cpu in wanted_cpus:
                 return target_cpu

    return target_cpus


def find_cpu(path_to_kernel):
    """"Find which CPU model the image runs on.

    :param path_to_kernel: Path to the kernel. We will get strings from it.
    :type  path_to_kernel: str
    :returns             : A list of CPU modes the image may runs on.
    :rtype               : list
    """
    candidates = get_candidates(path_to_kernel)
    strings = get_all_strings(candidates)
    return find_cpu_in_strings(strings)

