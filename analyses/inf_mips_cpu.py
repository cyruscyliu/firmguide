import os
import yaml

from analyses.analysis import Analysis
from database.dbf import get_database


class MIPSCPU(Analysis):
    def run(self, firmware):
        # only for mips
        if firmware.get_architecture() == 'arm':
            return True

        # find command
        path_to_srcode = firmware.get_path_to_source_code()
        path_to_mkout = firmware.get_path_to_makeout()

        results = os.popen('grep cpu-probe.c {}'.format(path_to_mkout)).readlines()
        if len(results) != 1:
            self.context['input'] = 'no cpu-probe in makeout {}'.format(path_to_mkout)
            path_to_cpu_probe_cmd = os.path.join(path_to_srcode, 'arch/mips/kernel/.cpu-probe.o.cmd')
            if not os.path.exists(path_to_cpu_probe_cmd):
                return False
            with open(path_to_cpu_probe_cmd) as f:
                results = f.readline()
            results = [' '.join(results.split()[2:])]

        command = results[0]
        path_to_gcc = firmware.get_path_to_gcc()
        if path_to_gcc is None:
            self.context['input'] = 'no gcc available'
            return False

        # alter -o to -E
        args = command.strip().split()
        args[0] = path_to_gcc  # always true
        args = [i.replace('/root/firmware', '/mnt/salamander/srcode/share') for i in args]
        args[-4] = '-E'
        path_to_cpu_probe = 'arch/mips/kernel/cpu-probe.'
        args[-2] = path_to_cpu_probe + 'i'
        args[-1] = path_to_cpu_probe + 'c'

        # run and parse
        cwd = os.getcwd()
        os.chdir(path_to_srcode)
        status = os.system('{} >/dev/null 2>&1'.format(' '.join(args)))
        path_to_cpu_probei = os.path.join(path_to_srcode, args[-2])
        os.chdir(cwd)

        if status:
            self.context['input'] = 'error in pre-processing'
            return False

        state = 0
        candidates = []
        no_critial_check = False
        with open(path_to_cpu_probei) as f:
            for line in f:
                if state == 0 and line.find('__get_cpu_type(const int cpu_type)') != -1:
                    state = 1
                if state == 1 and line.find('case CPU') != -1:
                    candidates.append(line.strip().strip(':').split()[1])
                if state == 1 and line.find('break') != -1:
                    state = 0
                if line.find('cpu_data[0].cputype != c->cputype') != -1:
                    no_critial_check = True

        # mapping
        ref = {
            "CPU_R2000": {
                "comp_id": "0x000000",
                "imp_id": "0x0100"
            },
            "CPU_R3080E": {
                "comp_id": "0x000000",
                "imp_id": "0x0200"
            },
            "CPU_R3000A": {
                "comp_id": "0x000000",
                "imp_id": "0x0200"
            },
            "CPU_R3080": {
                "comp_id": "0x000000",
                "imp_id": "0x0200"
            },
            "CPU_R4400PC": {
                "comp_id": "0x000000",
                "imp_id": "0x0400"
            },
            "CPU_R4400MC": {
                "comp_id": "0x000000",
                "imp_id": "0x0400"
            },
            "CPU_R4400SC": {
                "comp_id": "0x000000",
                "imp_id": "0x0400"
            },
            "CPU_R4000MC": {
                "comp_id": "0x000000",
                "imp_id": "0x0400"
            },
            "CPU_R4000SC": {
                "comp_id": "0x000000",
                "imp_id": "0x0400"
            },
            "CPU_VR4111": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_VR4121": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_VR4122": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_VR4182A": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_VR4131": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_VR4133": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_VR41XX": {
                "comp_id": "0x000000",
                "imp_id": "0x0c00"
            },
            "CPU_R4300": {
                "comp_id": "0x000000",
                "imp_id": "0x0b00"
            },
            "CPU_R4600": {
                "comp_id": "0x000000",
                "imp_id": "0x2000"
            },
            "CPU_TX3927": {
                "comp_id": "0x000000",
                "imp_id": "0x2200"
            },
            "CPU_TX3912": {
                "comp_id": "0x000000",
                "imp_id": "0x2200"
            },
            "CPU_TX3922": {
                "comp_id": "0x000000",
                "imp_id": "0x2200"
            },
            "CPU_R4700": {
                "comp_id": "0x000000",
                "imp_id": "0x2100"
            },
            "CPU_TX49XX": {
                "comp_id": "0x000000",
                "imp_id": "0x2d00"
            },
            "CPU_R5000": {
                "comp_id": "0x000000",
                "imp_id": "0x2300"
            },
            "CPU_R5432": {
                "comp_id": "0x000000",
                "imp_id": "0x5400"
            },
            "CPU_R5500": {
                "comp_id": "0x000000",
                "imp_id": "0x5500"
            },
            "CPU_NEVADA": {
                "comp_id": "0x000000",
                "imp_id": "0x2800"
            },
            "CPU_R6000": {
                "comp_id": "0x000000",
                "imp_id": "0x0300"
            },
            "CPU_R6000A": {
                "comp_id": "0x000000",
                "imp_id": "0x0600"
            },
            "CPU_RM7000": {
                "comp_id": "0x000000",
                "imp_id": "0x2700"
            },
            "CPU_R8000": {
                "comp_id": "0x000000",
                "imp_id": "0x1000"
            },
            "CPU_R10000": {
                "comp_id": "0x000000",
                "imp_id": "0x0900"
            },
            "CPU_R12000": {
                "comp_id": "0x000000",
                "imp_id": "0x0e00"
            },
            "CPU_R14000": {
                "comp_id": "0x000000",
                "imp_id": "0x0f00"
            },
            "CPU_LOONGSON2": {
                "comp_id": "0x000000",
                "imp_id": "0x6300"
            },
            "CPU_LOONGSON3": {
                "comp_id": "0x000000",
                "imp_id": "0x6300"
            },
            "CPU_LOONGSON1": {
                "comp_id": "0x000000",
                "imp_id": "0x4200"
            },
            "CPU_4KC": {
                "comp_id": "0x010000",
                "imp_id": "0x8000"
            },
            "CPU_4KEC": {
                "comp_id": "0x010000",
                "imp_id": [
                    "0x8400",
                    "0x9000"
                ]
            },
            "CPU_4KSC": {
                "comp_id": "0x010000",
                "imp_id": [
                    "0x8600",
                    "0x9200"
                ]
            },
            "CPU_5KC": {
                "comp_id": "0x010000",
                "imp_id": "0x8100"
            },
            "CPU_5KE": {
                "comp_id": "0x010000",
                "imp_id": "0x8900"
            },
            "CPU_20KC": {
                "comp_id": "0x010000",
                "imp_id": "0x8200"
            },
            "CPU_24K": {
                "comp_id": "0x010000",
                "imp_id": [
                    "0x9300",
                    "0x9600"
                ]
            },
            "CPU_25KF": {
                "comp_id": "0x010000",
                "imp_id": "0x8800"
            },
            "CPU_34K": {
                "comp_id": "0x010000",
                "imp_id": "0x9500"
            },
            "CPU_74K": {
                "comp_id": "0x010000",
                "imp_id": "0x9700"
            },
            "CPU_M14KC": {
                "comp_id": "0x010000",
                "imp_id": "0x9c00"
            },
            "CPU_M14KEC": {
                "comp_id": "0x010000",
                "imp_id": "0x9e00"
            },
            "CPU_1004K": {
                "comp_id": "0x010000",
                "imp_id": "0x9900"
            },
            "CPU_1074K": {
                "comp_id": "0x010000",
                "imp_id": "0x9a00"
            },
            "CPU_INTERAPTIV": {
                "comp_id": "0x010000",
                "imp_id": [
                    "0xa000",
                    "0xa100"
                ]
            },
            "CPU_PROAPTIV": {
                "comp_id": "0x010000",
                "imp_id": [
                    "0xa200",
                    "0xa300"
                ]
            },
            "CPU_P5600": {
                "comp_id": "0x010000",
                "imp_id": "0xa800"
            },
            "CPU_M5150": {
                "comp_id": "0x010000",
                "imp_id": "0xa700"
            },
            "CPU_BMIPS32": {
                "comp_id": "0x020000",
                "imp_id": [
                    "0x4000",
                    "0x8000"
                ]
            },
            "CPU_BMIPS3300": {
                "comp_id": "0x020000",
                "imp_id": [
                    "0x9000",
                    "0x9100",
                    "0x0000"
                ]
            },
            "CPU_BMIPS4380": {
                "comp_id": "0x020000",
                "imp_id": "0xa000"
            },
            "CPU_BMIPS4350": {
                "comp_id": "0x020000",
                "imp_id": "0xa000"
            },
            "CPU_BMIPS5000": {
                "comp_id": "0x020000",
                "imp_id": "0x5a00"
            },
            "CPU_ALCHEMY": [
                {
                    "comp_id": "0x030000",
                    "imp_id": [
                        "0x0100",
                        "0x0200"
                    ]
                },
                {
                    "comp_id": "0x0c0000",
                    "imp_id": "0x8000"
                }
            ],
            "CPU_SB1": {
                "comp_id": "0x40000",
                "imp_id": "0x0100"
            },
            "CPU_SB1A": {
                "comp_id": "0x40000",
                "imp_id": "0x1100"
            },
            "CPU_SR71000": {
                "comp_id": "0x050000",
                "imp_id": "0x0400"
            },
            "CPU_PR4450": {
                "comp_id": "0x060000",
                "imp_id": "0x1200"
            },
            "CPU_XLR": {
                "comp_id": "0x0c0000",
                "imp_id": [
                    "0x1200",
                    "0x1500",
                    "0x1300",
                    "0x1000",
                    "0x1100",
                    "0x0000",
                    "0x0200",
                    "0x0900",
                    "0x0600",
                    "0x0800",
                    "0x0a00",
                    "0x0b00",
                    "0x0f00",
                    "0x8000",
                    "0x8800",
                    "0x8c00",
                    "0x8e00",
                    "0x8f00",
                    "0xce00",
                    "0xcf00",
                    "0x4000",
                    "0x4a00",
                    "0x4400",
                    "0x4c00",
                    "0x4e00",
                    "0x4f00"
                ]
            },
            "CPU_CAVIUM_OCTEON": {
                "comp_id": "0x0d0000",
                "imp_id": [
                    "0x0000",
                    "0x0100",
                    "0x0200"
                ]
            },
            "CPU_CAVIUM_OCTEON_PLUS": {
                "comp_id": "0x0d0000",
                "imp_id": [
                    "0x0300",
                    "0x0400",
                    "0x0600",
                    "0x0700"
                ]
            },
            "CPU_CAVIUM_OCTEON2": {
                "comp_id": "0x0d0000",
                "imp_id": [
                    "0x9300",
                    "0x9000",
                    "0x9200",
                    "0x9100",
                    "0x9400"
                ]
            },
            "CPU_CAVIUM_OCTEON3": {
                "comp_id": "0x0d0000",
                "imp_id": [
                    "0x9600",
                    "0x9500"
                ]
            },
            "CPU_JZRISC": {
                "comp_id": "0xd00000",
                "imp_id": "0x0200"
            }
        }

        targets = []
        for candidate in candidates:
            rs = ref[candidate]
            if isinstance(rs, dict):
                cmp_id = rs['comp_id']
                imp_id = rs['imp_id']  # maybe a list
                target = self.has_matched_mips_cpu(cmp_id, imp_id)
                if target:
                    targets.extend(target)
            elif isinstance(rs, list):
                for r in rs:
                    cmp_id = r['comp_id']
                    imp_id = r['imp_id']
                    target = self.has_matched_mips_cpu(cmp_id, imp_id)
                    if target:
                        targets.extend(target)

        if not len(candidates):
            self.context['input'] = 'no __get_cpu_type in {}'.format(path_to_cpu_probei)
            if not no_critial_check:
                return False
            else:
                targets = ['74Kf']

        # choose the one has private peripheral
        wanted_cpus = ['74Kf']
        if len(targets):
            for target_cpu in targets:
                if target_cpu in wanted_cpus:
                    firmware.set_cpu_model(target_cpu)
                    self.info(firmware, 'get cpu model: {} which has private peripheral'.format(target_cpu), 1)
                    cpu_pp_name = self.qemu_devices.select('cpu_private', like=target_cpu)
                    if cpu_pp_name is not None:
                        firmware.set_cpu_pp_name(cpu_pp_name)
                        self.info(firmware, 'cpu private peripheral {} found'.format(cpu_pp_name), 1)
                    return True
            firmware.set_cpu_model(targets[0])
            self.info(firmware, 'get cpu model: {}, take the first one by default'.format(targets), 1)
            return True
        else:
            return False

    def has_matched_mips_cpu(self, cmp_id, imp_id):
        matched_cpus = []

        cmp_id = int(cmp_id, 16)
        for cpu_name, properties in self.mips_cpus.items():
            prid = properties['prid']
            if isinstance(imp_id, list):
                for ii in imp_id:
                    if prid & 0xff0000 == cmp_id and prid & 0xff00 == int(ii, 16):
                        matched_cpus.append(cpu_name)
            else:
                if prid & 0xff0000 == cmp_id and prid & 0xff00 == int(imp_id, 16):
                    matched_cpus.append(cpu_name)
        return matched_cpus

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'mips_cpu'
        self.description = 'infer supported mips cpus'
        self.context['hint'] = 'problem in mips cpus inference'
        self.critical = False
        self.required = ['srcode']
        #
        self.mips_cpus = yaml.safe_load(open(os.path.join(os.getcwd(), 'database/cpu.mips.yaml')))
        self.qemu_devices = get_database('qemu.devices')
