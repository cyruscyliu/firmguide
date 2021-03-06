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
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt, \
    merge_flatten_mmio
from slcore.render import Template
from slcore.brick import Brick, to_offset, to_upper, to_hex, \
    to_qemu_endian, to_range
from slcore.database.dbf import get_database


class SynthesisDT(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'synthesisdt'
        self.description = 'Convert device tree to QEMU virtual machine.'
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
            'intc': 'hw/intc', 'timer': 'hw/timer', 'net': 'hw/net'}
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
        self.context['endian'] = self.analysis_manager.firmware.get_endian()
        self.context['arch'] = self.analysis_manager.firmware.get_arch()
        self.context['machine_name'] = self.analysis_manager.firmware.get_machine_name()
        self.context['machine_description'] = self.analysis_manager.firmware.get_machine_name()
        self.context['board_id'] = self.analysis_manager.firmware.get_board_id()

    def clear_legacy_code(self):
        local_qemu = os.path.join(
            self.analysis_manager.project.attrs['path'],
            self.analysis_manager.firmware.get_machine_name())
        os.system('rm -rf {}'.format(local_qemu))

    def instantiate_intc(self, dts, autoboard, autoboard_all):
        intcp = {}
        flatten_intc = find_flatten_intc_in_fdt(dts)
        if flatten_intc is not None:
            for intc in flatten_intc:
                b = Brick('intc', intc['compatible'], autoboard=autoboard,
                          autoboard_all=autoboard_all)
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
        return intcp

    def run(self, **kwargs):
        # Parse arguments
        path_to_dtb = self.analysis_manager.firmware.get_realdtb()
        if path_to_dtb is None:
            self.error_info = 'there is no real dtb available.'
            return False

        autoboard = kwargs.pop('autoboard')
        autoboard_all = kwargs.pop('autoboard_all')

        dts = load_dtb(path_to_dtb)

        # Initialize
        self.init_context()
        self.clear_statistics()
        self.clear_legacy_code()
        intcp = self.instantiate_intc(dts, autoboard, autoboard_all) # intc table

        # Let's begin
        for k, v in self.rendering_handlers.items():
            flatten_ks = v(dts)
            if flatten_ks is None:
                self.warning('no {} found'.format(k), 0)
                continue
            # ######### handle ram ########
            if k == 'ram':
                if len(flatten_ks[0]['regs']) == 0:
                    self.context['ram_default_size'] = 256
                else:
                    self.context['ram_default_size'] = \
                        flatten_ks[0]['regs'][0]['size'] // 1024 // 1024
            # ######### handle flash ########
            cast, effi = None, None
            if self.analysis_manager.firmware.get_arch() == 'mips' and k == 'flash' and \
                    not len(flatten_ks):
                # mips will have a default flash if no flash is detected
                flatten_ks = [{'compatible': ['flash,generic'],
                               'regs': [{'base': 0x1fc00000, 'size': 0x400000}]}]
            elif self.analysis_manager.firmware.get_arch() == 'arm' and k == 'flash' and \
                    len(flatten_ks):
                # arm flash treated as mmio region
                k = 'mmio'
                cast = ['mmio,generic']
                effi = 'plxtech,nand-nas782x'
            # ######### handle mmio ########
            if k == 'mmio':
                flatten_ks = merge_flatten_mmio(flatten_ks)
            # ######### !!!!!!!!!!!! ########
            for context in flatten_ks:
                if k != 'serial' and self.__skip(context['compatible']):
                    self.debug('skip {}'.format(context['compatible']), 0)
                    continue
                # ######## the 1st check, (type, compatible) check ########
                b = Brick(k, context['compatible'],
                        cast=cast, effi=effi,
                        autoboard=autoboard, autoboard_all=autoboard_all)
                if not b.supported:
                    self.warning('cannot support {} {}'.format(
                        k, context['compatible']), 0)
                    self.update_new_statistics(b, supported=False)
                    continue
                # ######## the 2nd check, parameters check ########
                context['name'] = b.effic_compatible.replace(',', '_').replace('-', '_')
                if 'intcp' in context:
                    phandle = context['intcp']
                    if phandle not in intcp:
                        self.warning('cannot support {} {}, {}'.format(
                            k, b.effic_compatible, 'intcp is missing'), 0)
                        self.update_new_statistics(b, supported=False)
                        continue
                    context['intcp'] = intcp[phandle].model
                    context['intcp']['name'] = \
                        intcp[phandle].effic_compatible.replace(',', '_').replace('-', '_')
                # ######## update generic parameters ########
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
                # ######### handle flash ########
                if k == 'flash' and self.analysis_manager.firmware.get_arch() == 'mips':
                    if context['regs'][0]['base'] > 0x20000000:
                        context['regs'][0]['base'] &= 0x1FFFFFF
                    context['regs'][0]['size'] = \
                        0x20000000 - context['regs'][0]['base']
                # ######### load and render ########
                iv = None
                fix_parameters = self.load_fix_parameters(k, b.effic_compatible)
                if fix_parameters is not None:
                    for x, y in fix_parameters.items():
                        if x != 'regs_index':
                            b.model[x] = y
                        else:
                            iv = {}
                            for index, yy in y.items():
                                for xxx, yyy in yy.items():
                                    context['regs'][index][xxx] = yyy
                                    iv[index] = yyy
                                    self.analysis_manager.firmware.inc_iv_num()
                                    self.debug('iv+1 {} {}'.format(k, b.effic_compatible), 1)
                m_context = b.render(context)
                if isinstance(m_context, str):
                    self.warning('cannot suport {} {}, {} is missing'.format(
                        k, b.effic_compatible, m_context), 0)
                    self.update_new_statistics(b, supported=False)
                    continue
                self.__add_context(m_context)
                # ######### the 3rd check, external check ########
                for x, y in m_context.items():
                    context[x] = y
                context['license'] = self.context['license']
                b.load_template()
                # ######### load and render ########
                source, header = b.render_qdev(context)
                if isinstance(source, KeyError):
                    self.error_info = 'cannot suport {} {}, {} is missing'.format(
                        k, b.effic_compatible, source)
                    self.update_new_statistics(b, supported=False)
                    return False
                if b.external:
                    self.external[context['name']] = \
                        {'type': b.external_type, 'source': source, 'header': header}
                # ########## update the skipped_bdevices ########
                self.skipped_bdevices.append(b.effic_compatible)
                self.skipped_bdevices.extend(b.buddy_compatible)
                self.debug('{} done'.format(context['compatible']), 1)
                self.update_statistics(k, crm=b.builtin, debug=context['compatible'])
                self.update_new_statistics(b, supported=True, iv=iv)
        # ########## update parameters might be empty ########
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
        # ######## load and render ########
        try:
            self.load_template()
            a = Template(self.machine).render(self.context)
            source = Template(a).render(self.context)
        except KeyError as e:
            self.error_info = 'error in parsing, missing {}'.format(e)
            return False
        # ######## save machine.c ########
        base = os.path.join(
                self.analysis_manager.project.attrs['path'],
                self.analysis_manager.firmware.get_machine_name())
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

    def clear_statistics(self):
        self.analysis_manager.firmware.set_crm_num(0)
        self.analysis_manager.firmware.set_smm_num(0)
        self.analysis_manager.firmware.set_mrm_num(0)
        self.analysis_manager.firmware.set_iv_num(0)

    def update_statistics(self, t, crm=None, debug=None):
        if t in ['cpu', 'ram', 'serial', 'misc']:
            self.analysis_manager.firmware.inc_crm_num()
            self.debug('crm+1 {} {}'.format(t, debug), 1)
        elif t in ['intc', 'timer'] and crm is None:
            self.analysis_manager.firmware.inc_smm_num()
            self.debug('smm+1 {} {}'.format(t, debug), 1)
        elif t in ['intc', 'timer'] and crm is not None:
            self.analysis_manager.firmware.set_crm_num(
                self.analysis_manager.firmware.get_crm_num() + crm)
            self.debug('crm+{} {} {}'.format(crm, t, debug), 1)
        else:
            self.analysis_manager.firmware.inc_mrm_num()
            self.debug('mrm+1 {} {}'.format(t, debug), 1)

    def update_new_statistics(self, brick, supported=None, iv=None):
        entry = brick.get_statistics(supported=supported, iv=iv)
        self.analysis_manager.firmware.add_entry(entry)
        self.debug('add {}'.format(entry), 1)

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
