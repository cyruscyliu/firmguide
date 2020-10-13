from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.dt_parsers.memory import find_flatten_ram_in_fdt
from slcore.dt_parsers.common import load_dtb
from slcore.amanager import Analysis


class DiscloseDT(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'disclosedt'
        self.description = 'Disclose device tree blob.'

    def run(self, **kwargs):
        mmio = kwargs.pop('mmio', False)
        flash = kwargs.pop('flash', False)

        path_to_dtb = kwargs.pop('dtb')
        self.firmware.set_realdtb(path_to_dtb)

        dts = load_dtb(path_to_dtb)
        path_to_dts = path_to_dtb + '.dts'
        with open(path_to_dts, 'w') as f:
            f.write(dts.to_dts())

        for cpu in find_flatten_cpu_in_fdt(dts):
            message = '[CPU] of {}/{}'.format(cpu['path'], cpu['compatible'])
            self.info(message, 1)

        for mem in find_flatten_ram_in_fdt(dts):
            for reg in mem['regs']:
                message =  \
                    '[MEM] base 0x{:08x} size 0x{:08x} of {}/{}'.format(
                        reg['base'], reg['size'],
                        mem['path'], mem['compatible'])
                self.info(message, 1)

        for timer in find_flatten_timer_in_fdt(dts):
            for reg in timer['regs']:
                message =  \
                    '[TIMER] base 0x{:08x} size 0x{:08x} of {}/{}'.format(
                        reg['base'], reg['size'],
                        timer['path'], timer['compatible'])
                self.info(message, 1)

        for serial in find_flatten_serial_in_fdt(dts) or []:
            for reg in serial['regs']:
                message =  \
                    '[SERIAL] base 0x{:08x} size 0x{:08x} of {}/{}'.format(
                        reg['base'], reg['size'],
                        serial['path'], serial['compatible'])
                self.info(message, 1)

        flatten_mmio = find_flatten_mmio_in_fdt(dts)
        def memory_overlapping_detection(compatible, start, end):
            for mmio in flatten_mmio:
                if mmio['compatible'] == compatible:
                    continue
                for reg in mmio['regs']:
                    if reg['base'] <= start and start < reg['base'] + reg['size']:
                        return mmio['compatible']
                    if reg['base'] < end and end <= reg['base'] + reg['size']:
                        return mmio['compatible']
            return None

        if mmio:
            sorted_mmio = []
            for mmio in flatten_mmio:
                if len(mmio['regs']):
                    sorted_mmio.append(mmio)
            for mmio in sorted(
                    sorted_mmio, key=lambda x: x['regs'][0]['base']):
                for reg in mmio['regs']:
                    base, size = reg['base'], reg['size']
                    compatible = mmio['compatible']
                    overlap = memory_overlapping_detection(compatible, base, base + size)
                    message =  \
                        '[MMIO] base 0x{:08x} size 0x{:08x} of {}/{} overlap:{}'.format(
                            base, size, mmio['path'], compatible, overlap)
                    self.info(message, 1)

        if flash:
            for flash in find_flatten_flash_in_fdt(dts):
                for reg in flash['regs']:
                    message = \
                        '[FLASH] base 0x{:08x} size 0x{:08x} of {}/{}'.format(
                            reg['base'], reg['size'],
                            flash['path'], flash['compatible'])
                    self.info(message, 1)

        self.info('save dts at {}'.format(path_to_dts), 1)
        return True
