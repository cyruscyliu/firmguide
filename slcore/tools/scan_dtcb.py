#!/usr/bin/python
import re
import os
import sys
sys.path.extend(['.', '..', '../..'])

from slcore.database.dbf import get_database
from slcore.dt_parsers.common import load_dtb


def __re_scan(path, declare='.*?', compatible='(.*?)', depress=False):
    # XXX_DECLARE(arc_gfrc, "snps,archs-timer-gfrc", arc_cs_setup_gfrc);
    string = ''
    with open(path) as f:
        for line in f:
            string += line.strip()
    # DECLARE\(\s*[_a-zA-Z0-9]+\s*,\s*(.*?)\s*,\s*([_a-zA-Z0-9]+)\s*\)
    match = re.findall(r'{}\(\s*[_a-zA-Z0-9]+\s*,\s*({})\s*,\s*([_a-zA-Z0-9]+)\s*\)'.format(declare, compatible), string)

    # for print
    if len(path) > 120:
         path =  '...' + path[100:]

    if not len(match):
        if not depress:
            print('[-] cannot find {}/{} in {}'.format(declare, compatible, path))
        return None

    # fix compatible
    match_fix = []
    for m in match:
        if m[-2].startswith('"'):
            a = m[-2].strip('"')
            match_fix.append((a, m[-1]))
        else:
            print('[-] cannot recognize {}/{} in {}'.format(m[-2], compatible, path))
    return match_fix


def __scan_dtcb(declare, path_to_source):
    cbs = []
    # path:XXX_DECLARE(id, "compatible", cb);
    with os.popen('grep -r {} {}//'.format(declare, path_to_source)) as f:
        for line in f:
            path = line.split(':')[0]
            cb = __re_scan(path, declare=declare)
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


def __do_job(t, job, path_to_source):
    cbs = job(path_to_source)

    qdevices = get_database('qemu.{}'.format(t))
    we_have = qdevices.select('*')

    for cb in cbs:
        if we_have is not None and cb[0] in we_have:
            continue
        qdevices.add(cb[0], extend='{},generic'.format(t))
        print('[+] new {} {} updated'.format(t, cb))


def scan_declare(path_to_source):
    # we want to know whether or not
    # there are declares we don't known
    print('[+] checking unexpected XXX_DECLARE in {}'.format(path_to_source))
    candidates = [
        'CPUIDLE_METHOD_OF_DECLARE', # UNKNOWN
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
        'RESERVEDMEM_OF_DECLARE', # DMA
        'IOMMU_OF_DECLARE',
    ]
    print('[+] expected: {}'.format(' '.join(candidates)))

    unexpected = []
    # grep "_DECLARE(" -nir ./")"
    search_in = os.path.join('{}'.format(path_to_source))
    with os.popen('grep "_DECLARE(" -nir {}'.format(search_in)) as f:
        # rivers/clk/mvebu/clk-corediv.c:337:CLK_OF_DECLARE(mv98dx3
        for line in f:
            if line.find('"') == -1:
                continue
            path = line.split(':')[0]
            declare = line.split(':')[2].split('(')[0]
            if declare not in candidates:
                if len(path) > 120:
                    line = '...' + line[100:]
                unexpected.append(declare)
    if len(unexpected):
        print('[+] unexpected: {}'.format(' '.join(unexpected)))
    else:
        print('[+] nothing unexpected')


def update_dtdb(path_to_source):
    jobs = {
        'clk': scan_clk_dtcb,
        'timer': scan_timer_dtcb,
        'intc': scan_intc_dtcb,
        'serial': scan_serial_dtcb,
    }

    for t, job in jobs.items():
        __do_job(t, job, path_to_source)


def scan_dtcb(path_to_dtb, path_to_source):
    # let's traverse the device tree
    dts = load_dtb(path_to_dtb)
    for path, nodes, pros in dts.walk():
        if not dts.exist_property('compatible', path):
            continue
        compatible = dts.get_property('compatible', path)
        print('[+] searching {}'.format(compatible))
        for cmptb in compatible:
            with os.popen('grep -r \\"{}\\" {}/'.format(cmptb, path_to_source)) as f:
                for line in f:
                    path = line.split(':')[0]
                    if not os.path.exists(path):
                        continue
                    cb = __re_scan(path, declare='DECLARE', depress=True)
                    if len(path) > 120:
                        path = '...' + path[100:]
                    if (cb) is not None:
                        for i in cb:
                            if i[0] != cmptb:
                                continue
                            print('[+] [bingo] {} -> {} in {}'.format(i[0], i[1], path))


if __name__ == '__main__':
    if len(sys.argv) == 3:
        path_to_dtb = sys.argv[1]
        path_to_source = sys.argv[2]
    else:
        print('usage: ./scan_dtcb.py path/to/dtb dir/to/linux_kernel_source')
        exit(-1)
    scan_declare(path_to_source)
    update_dtdb(path_to_source)
    scan_dtcb(path_to_dtb, path_to_source)

