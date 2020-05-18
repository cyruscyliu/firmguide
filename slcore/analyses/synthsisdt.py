import os

from slcore.amanager import Analysis
from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.misc import find_flatten_misc_in_fdt
from slcore.dt_parsers.memory import find_flatten_ram_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.render import Template
from slcore.brick import Brick, to_offset, to_upper, to_hex, \
    to_qemu_endian, to_range
from slcore.database.dbf import get_database


class SynthesisDT(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'synthesisdt'
        self.description = 'Synthesize bricks to QEMU machines.'
        self.required = ['preprocdt']

        self.context = {}
        self.rendering_handlers = {
            'cpu': find_flatten_cpu_in_fdt,
            'ram': find_flatten_ram_in_fdt,
            'intc': find_flatten_intc_in_fdt,
            'serial': find_flatten_serial_in_fdt,
            'timer': find_flatten_timer_in_fdt,
            'flash': find_flatten_flash_in_fdt,
            'misc': find_flatten_misc_in_fdt,
            'mmio': find_flatten_mmio_in_fdt,
        }

        self.machine = None
        self.location = {
            'arm': 'hw/arm', 'mips': 'hw/mips',
            'intc': 'hw/intc', 'timer': 'hw/timer'}
        self.external = {}
        self.skipped_bdevices = []

    def __skip(self, compatible):
        for cmptb in compatible:
            if cmptb in self.skipped_bdevices:
                return True

    def init_context(self):
        self.context['license'] = \
            '/*\n * automatically generated, don\'t change\n */'
        self.context['to_upper'] = to_upper
        self.context['to_range'] = to_range
        self.context['to_hex'] = to_hex
        self.context['to_offset'] = to_offset
        self.context['to_endian'] = to_qemu_endian
        self.context['endian'] = self.firmware.get_endian()
        self.context['arch'] = self.firmware.get_arch()
        self.context['machine_name'] = self.firmware.get_machine_name()
        self.context['machine_description'] = self.firmware.get_machine_name()
        self.context['board_id'] = self.firmware.get_board_id()

    def run(self, **kwargs):
        path_to_dtb = self.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no device tree blob available.'
            return False

        dts = load_dtb(path_to_dtb)

        self.init_context()

        # all intcp should replaced by a real intc
        intcp = {}
        flatten_intc = find_flatten_intc_in_fdt(dts)
        if flatten_intc is not None:
            for intc in flatten_intc:
                b = Brick('intc', intc['compatible'])
                if not b.supported:
                    continue
                if 'phandle' not in intc:
                    continue
                intcp[intc['phandle']] = b
        flatten_cpu = find_flatten_cpu_in_fdt(dts)
        if flatten_cpu is not None:
            for cpu in flatten_cpu:
                b = Brick('cpu', cpu['compatible'])
                if not b.supported:
                    continue
                intcp[-1] = b

        # let's begin
        for k, v in self.rendering_handlers.items():
            # ######### handle flash ########
            if k == 'flash' and self.firmware.get_arch() == 'arm':
                continue
            if k == 'flash' and self.firmware.get_components() \
                    and self.firmware.get_components().has_device_tree():
                dts = load_dtb(self.firmware.get_components().get_path_to_dtb())
            # ######### !!!!!!!!!!!! ########
            flatten_ks = v(dts)
            if flatten_ks is None:
                self.warning('no {} found'.format(k), 0)
                continue
            # ######### handle flash ########
            if self.firmware.get_arch() == 'mips' and k == 'flash' and \
                    not len(flatten_ks):
                # mips will have a default flash if no flash is detected
                flatten_ks = [{'compatible': ['flash,generic'],
                               'regs': [{'base': 0x1fc00000, 'size': 0x400000}]}]
            # ######### !!!!!!!!!!!! ########
            for context in flatten_ks:
                if k != 'serial' and self.__skip(context['compatible']):
                    self.debug('skip {}'.format(context['compatible']), 0)
                    continue
                # ######## the 1st check, (type, compatible) check ########
                # ######### !!!!!!!!!!!! ########
                b = Brick(k, context['compatible'])
                if not b.supported:
                    self.warning('cannot support {} {}'.format(
                        k, context['compatible']), 0)
                    continue
                # ######## the 2nd check, parameters check ########
                context['name'] = b.effic_compatible.replace(',', '_').replace('-', '_')
                if 'intcp' in context:
                    phandle = context['intcp']
                    if phandle not in intcp:
                        self.warning('cannot support {} {}, {}'.format(
                            k, b.effic_compatible, 'intcp is missing'), 0)
                        continue
                    context['intcp'] = intcp[phandle].model
                    context['intcp']['name'] = \
                        intcp[phandle].effic_compatible.replace(',', '_').replace('-', '_')

                context['to_upper'] = self.context['to_upper']
                context['to_range'] = self.context['to_range']
                context['to_endian'] = self.context['to_endian']
                context['to_hex'] = self.context['to_hex']
                context['to_offset'] = self.context['to_offset']
                context['endian'] = self.context['endian']
                context['arch'] = self.context['arch']
                context['machine_name'] = self.context['machine_name']
                context['machine_description'] = self.context['machine_description']
                context['board_id'] = self.context['board_id']

                if k == 'flash' and self.firmware.get_arch() == 'mips':
                    if context['regs'][0]['base'] > 0x20000000:
                        context['regs'][0]['base'] &= 0x1FFFFFF
                    context['regs'][0]['size'] = \
                        0x20000000 - context['regs'][0]['base']
                # ######### !!!!!!!!!!!! ########
                fix_parameters = self.load_fix_parameters(k, b.effic_compatible)
                if fix_parameters is not None:
                    if k != 'mmio':
                        for x, y in fix_parameters.items():
                            b.model[x] = y
                    else:
                        for x, y in fix_parameters.items():
                            context['regs'][x]['registers'] = y
                m_context = b.render(context)
                if isinstance(m_context, str):
                    self.warning('cannot suport {} {}, {} is missing'.format(
                        k, b.effic_compatible, m_context), 0)
                    continue
                self.__add_context(m_context)
                # ######### the 3rd check, external check ########
                for x, y in m_context.items():
                    context[x] = y
                context['license'] = self.context['license']
                b.load_template()
                # ######### !!!!!!!!!!!! ########
                source, header = b.render_qdev(context)
                if isinstance(source, KeyError):
                    self.error_info = 'cannot suport {} {}, {} is missing'.format(
                        k, b.effic_compatible, source)
                    return False
                if b.external:
                    self.external[context['name']] = \
                        {'type': k, 'source': source, 'header': header}
                # update the skipped_bdevices
                self.skipped_bdevices.append(b.effic_compatible)
                self.skipped_bdevices.extend(b.buddy_compatible)
        # let's go on
        if 'timer_get_header' not in self.context:
            self.context['timer_get_header'] = []
            self.context['timer_get_body'] = []
            self.context['timer_get_field'] = []
            self.context['timer_get_connection'] = []
        if 'flash_get_header' not in self.context:
            self.context['flash_get_header'] = []
            self.context['flash_get_body'] = []
            self.context['flash_get_field'] = []
        if 'misc_get_header' not in self.context:
            self.context['misc_get_header'] = []
            self.context['misc_get_body'] = []
            self.context['misc_get_field'] = []
        # ######## !!!!!!!! ########
        try:
            self.load_template()
            a = Template(self.machine).render(self.context)
            source = Template(a).render(self.context)
        except KeyError as e:
            self.error_info = 'error in parsing, missing {}'.format(e)
            return False
        # ######## save machine.c ########
        base = os.path.join(self.analysis_manager.project.attrs['path'], 'qemu-4.0.0')
        location = self.location[self.context['arch']]
        fname = self.context['machine_name'] + '.c'
        self.__save(source, base, location, fname)
        self.info('save at {}/{}/{}'.format(base, location, fname), 'link')
        # ######## save model.c ########
        for k, v in self.external.items():
            location = self.location[v['type']]
            fname = k + '.c'
            self.__save(v['source'], base, location, fname)
            self.info('save at {}/{}/{}'.format(base, location, fname), 'link')

            location = os.path.join('include', self.location[v['type']])
            fname = k + '.h'
            self.__save(v['header'], base, location, fname)
            self.info('save at {}/{}/{}'.format(base, location, fname), 'link')
        return True

    def __save(self, s, base, location, fname):
        os.makedirs(base, exist_ok=True)

        source_target = os.path.join(base, location, fname)
        os.makedirs(os.path.dirname(source_target), exist_ok=True)
        with open(source_target, 'w') as f:
            f.write(s)
            f.flush()

    def __add_context(self, context):
        for k, v in context.items():
            if k in self.context:
                if isinstance(v, list):
                    self.context[k].extend(v)
                else:
                    self.context[k] = [self.context[k], v]
            else:
                self.context[k] = v

    def load_template(self):
        generate_dir = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(generate_dir, 'machine.c')) as f:
            self.machine = ''.join(f.readlines())

    def load_fix_parameters(self, t, compatible):
        qemu_devices = get_database('qemu.{}'.format(t))
        fix_parameters = qemu_devices.select('fix_parameters', compatible=compatible)
        return fix_parameters
