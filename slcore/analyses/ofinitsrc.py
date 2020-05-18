import re
import os

from slcore.database.dbf import get_database
from slcore.dt_parsers.common import load_dtb
from slcore.amanager import Analysis


def re_scan(path, declare='.*?', compatible='.*?', depress=False):
    # XXX_DECLARE(arc_gfrc, "snps,archs-timer-gfrc", arc_cs_setup_gfrc);
    string = ''
    with open(path) as f:
        for line in f:
            string += line.strip()
    # DECLARE\(\s*[_a-zA-Z0-9]+\s*,\s*(.*?)\s*,\s*([_a-zA-Z0-9]+)\s*\)
    match = re.findall(
        r'({})\(\s*[_a-zA-Z0-9]+\s*,\s*({})\s*,\s*([_a-zA-Z0-9]+)\s*\);'.format(
            declare, compatible), string)
    # one match is (xxx_declare, compatible, cb)

    # TODO fix me, how to detect this one?
    # IRQCHIP_DECLARE(gic_400, "arm,gic-400",IRQCHIP_DECLARE(cortex_a15_gic, "arm,cortex-a15-gic", gic_of_init);
    # We get the result 'arm,gic-400",IRQCHIP_DECLARE(cortex_a15_gic, "arm,cortex-a15-gic', but it is not the truth.

    # for print
    if len(path) > 120:
        path = '...' + path[100:]

    if not len(match):
        if not depress:
            print('[-] cannot find {}/{} in {}'.format(declare, compatible, path))
        return None

    # fix compatible
    match_fix = []
    for m in match:
        # TODO fix me, how to detect this one?
        if m[-2].find('DECLARE') != -1:
            print('[-] cannot recognize {} in {}'.format(m[-2], path))
            continue
        if m[-2].startswith('"'):
            a = m[-2].strip('"')
            match_fix.append((m[0], a, m[-1]))
        else:
            print('[-] cannot recognize {} in {}'.format(m[-2], path))
    return match_fix


def __scan_dtcb(declare, path_to_source):
    cbs = []
    # path:XXX_DECLARE(id, "compatible", cb);
    with os.popen('grep -r {} {}//'.format(declare, path_to_source)) as f:
        for line in f:
            path = line.split(':')[0]
            cb = re_scan(path, declare=declare)
            if cb is None:
                continue
            cbs.extend(cb)
    cbs = list(set(cbs))
    return cbs


def scan_clk_dtcb(path_to_source):
    a = []
    # CLK_OF_DECLARE
    # CLK_OF_DECLARE_DRIVER
    a.extend(__scan_dtcb('CLK_OF_DECLARE_DRIVER', path_to_source))
    a.extend(__scan_dtcb('CLK_OF_DECLARE', path_to_source))
    return a


def scan_timer_dtcb(path_to_source):
    # CLOCKSOURCE_OF_DECLARE'
    # CLOCKSOURCE_ACIP_DECLARE
    # TIMER_OF_DECLARE
    # TIMER_ACPI_DECLARE
    a = []
    a.extend(__scan_dtcb('CLOCKSOURCE_OF_DECLARE', path_to_source))
    a.extend(__scan_dtcb('CLOCKSOURCE_ACIP_DECLARE', path_to_source))
    a.extend(__scan_dtcb('TIMER_OF_DECLARE', path_to_source))
    a.extend(__scan_dtcb('TIMER_ACPI_DECLARE', path_to_source))
    return a


def scan_intc_dtcb(path_to_source):
    # IRQCHIP_ACPI_DECLARE
    # IRQCHIP_DECLARE
    a = []
    a.extend(__scan_dtcb('IRQCHIP_DECLARE', path_to_source))
    # a.extend(__scan_dtcb('IRQCHIP_ACPI_DECLARE', path_to_source))
    return a


def scan_serial_dtcb(path_to_source):
    # OF_EARLYCON_DECLARE
    # EARLYCON_DECLARE(a wrapper of OF_EARLYCON_DECLARE)
    return __scan_dtcb('OF_EARLYCON_DECLARE', path_to_source)


candidates = [
    'CPUIDLE_METHOD_OF_DECLARE',  # UNKNOWN
    'CLK_OF_DECLARE_DRIVER',
    'CLK_OF_DECLARE',
    'TIMER_ACPI_DECLARE',
    'TIMER_OF_DECLARE',
    'CLOCKSOURCE_ACIP_DECLARE',
    'CLOCKSOURCE_OF_DECLARE',
    'IRQCHIP_ACPI_DECLARE',
    'IRQCHIP_DECLARE',
    'OF_EARLYCON_DECLARE',
    'EARLYCON_DECLARE',
    'RESERVEDMEM_OF_DECLARE',  # DMA
    'IOMMU_OF_DECLARE',
]


class UpdateCompatibleDB(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'updatecompatibledb'
        self.description = 'Update hardware in new source.'

    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False
        path_to_source = srcodec.get_path_to_source_code()
        self.info('checking unexpected XXX_DECLARE in {}'.format(path_to_source), 1)
        self.info('expected: {}'.format(' '.join(candidates)), 1)

        unexpected = []
        # grep "_DECLARE(" -nir ./")"
        search_in = os.path.join('{}'.format(path_to_source))
        with os.popen('grep "_DECLARE(" -nir {}'.format(search_in)) as f:
            # rivers/clk/mvebu/clk-corediv.c:337:CLK_OF_DECLARE(mv98dx3
            for line in f:
                if line.find('"') == -1:
                    continue
                if line.find('#define') != -1:
                    continue
                path = line.split(':')[0]
                declare = line.split(':')[2].split('(')[0].strip()
                if declare not in candidates:
                    if len(path) > 160:
                        line = '...' + line[150:].strip()
                    print('[-] unexpected line: {}'.format(line))
                    unexpected.append(declare)
        if len(unexpected):
            self.info('unexpected macro: {}'.format(' '.join(list(set(unexpected)))), 1)
        else:
            self.info('nothing unexpected', 1)

        jobs = {
            'clk': scan_clk_dtcb,
            'timer': scan_timer_dtcb,
            'intc': scan_intc_dtcb,
            'serial': scan_serial_dtcb,
        }

        def do_job(t, job, path_to_source):
            cbs = job(path_to_source)

            qdevices = get_database('qemu.{}'.format(t))
            we_have = qdevices.select('*')

            for cb in cbs:
                if we_have is not None and cb[1] in we_have:
                    continue
                qdevices.add(cb[1], extend='{},generic'.format(t))
                self.info('new {} {} updated'.format(t, cb), 1)

        for t, job in jobs.items():
            do_job(t, job, path_to_source)

        return True


class OfInitSrc(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'ofinitsrc'
        self.description = \
            'Find of_init callbacks w.s.t compatibles in given device tree.'

    def run(self, **kwargs):
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False
        path_to_source = srcodec.get_path_to_source_code()

        # let's traverse the device tree
        path_to_dtb = self.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no device tree blob available.'
            return False

        dts = load_dtb(path_to_dtb)
        c_cb = []
        for path, nodes, pros in dts.walk():
            if not dts.exist_property('compatible', path):
                continue
            compatible = dts.get_property('compatible', path)
            self.info('searching {}'.format(compatible), 1)
            for cmptb in compatible:
                with os.popen('grep -r \\"{}\\" {}/'.format(cmptb, path_to_source)) as f:
                    for line in f:
                        path = line.split(':')[0]
                        if not os.path.exists(path):
                            continue
                        cb = re_scan(path, declare='[_A-Z]+_DECLARE', depress=True)
                        if len(path) > 160:
                            path = '...' + path[150:]
                        if (cb) is not None:
                            for i in cb:
                                if i[1] != cmptb:
                                    continue
                                self.info('[bingo] {} in {}'.format(i, path), 1)
                                c_cb.append(i)
        return True
