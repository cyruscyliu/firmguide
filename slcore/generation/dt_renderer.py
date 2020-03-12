import os

from slcore.dt_parsers.cpu import *
from slcore.dt_parsers.serial import *
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.common import *
from slcore.dt_parsers.timer import *
from slcore.dt_parsers.flash import *
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt
from slcore.database.dbf import get_database
from slcore.generation.render import Template
from slcore.generation.common import *
from slcore.generation.gllrender import Model
from slcore.logger import logger_info, logger_debug, logger_warning
from settings import *


class DTRenderer(object):
    def __init__(self, firmware):
        self.firmware = firmware

        self.context = {}
        self.context['machine_name'] = firmware.get_machine_name()
        self.context['machine_description'] = self.context['machine_name']
        self.context['arch'] = firmware.get_arch()
        self.context['endian'] = firmware.get_endian()
        self.context['board_id'] = firmware.get_board_id()
        self.context['ram_get_priority'] = firmware.get_ram_priority()
        self.context['ram_get_size'] = firmware.get_ram_size()
        self.context['license'] = '/*\n * automatically generated, don\'t change\n */'
        self.context['upper'] = lambda x: x.upper()
        self.context['range'] = lambda x: range(0, x)

        self.rendering_handlers = {
            'cpu': find_flatten_cpu_in_fdt,
            'intc': find_flatten_intc_in_fdt,
            'serial': find_flatten_serial_in_fdt,
            'timer': find_flatten_timer_in_fdt,
            'flash': find_flatten_flash_in_fdt,
        }

        self.machine = None
        self.location = {
            'arm': 'hw/arm', 'mips': 'hw/mips',
            'intc': 'hw/intc', 'timer': 'hw/timer'}
        self.external = {}
        self.skipped_bdevices = []

    def info(self, message, action):
        logger_info(self.firmware.get_uuid(), 'dt_renderer', action, message, 0)

    def debug(self, message, action):
        logger_debug(self.firmware.get_uuid(), 'dt_renderer', action, message, 0)

    def warning(self, message, action):
        logger_warning(self.firmware.get_uuid(), 'dt_renderer', action, message, 0)

    def __render_bamboo_devices(self):
        self.context['reset_get_field'] = []
        #
        bamboos = self.firmware.get_bamboo_devices()
        bamboo_suite = """
static void {0}_update(void *opaque)
{{
    /* {{{{ machine_name|upper }}}}State *s = opaque; */
}}

static uint64_t {0}_read(void *opaque, hwaddr offset, unsigned size)
{{
    {{{{ machine_name|upper }}}}State *s = opaque;
    uint32_t res = 0;

    switch (offset) {{
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\\n", __func__, offset);
        return 0;
    case {1}:
        res = s->{2}[offset >> 2];
        break;
    }}
    return res;
}}

static void {0}_write(void *opaque, hwaddr offset, uint64_t val, unsigned size)
{{
    {{{{ machine_name|upper }}}}State *s = opaque;

    switch (offset) {{
    default:
        qemu_log_mask(LOG_GUEST_ERROR, "%s: Bad offset %"HWADDR_PRIx"\\n", __func__, offset);
        return;
    case {1}:
        s->{2}[offset >> 2] = val;
        break;
    }}
    {0}_update(s);
}}

static const MemoryRegionOps {0}_ops = {{
    .read = {0}_read,
    .write = {0}_write,
    .endianness = {3},
}};"""
        for name, bamboo in bamboos.items():
            # 4th check, skip bdevices in skipped_bdevices
            if self.__skip(bamboo['compatible']):
                continue

            m_context = {'bamboo_get_field': [], 'bamboo_get_body': [], 'bamboo_get_suite': []}
            mmio_size = bamboo['mmio_size']
            mmio_base = bamboo['mmio_base']
            registers = bamboo['registers']
            #
            m_context['bamboo_get_field'].append('MemoryRegion {};'.format(to_mmio(name)))
            #
            for rname, register in registers.items():
                m_context['bamboo_get_field'].append('uint32_t {}[{} >> 2];'.format(rname, mmio_size))
                # self.context['reset_get_field'].append('s->{} = {};'.format(rname, register['value']))
            if 'mmio_priority' in bamboo:
                mmio_priority = bamboo['mmio_priority']
            else:
                mmio_priority = 0
            m_context['bamboo_get_body'].extend([
                'memory_region_init_io(&s->{}, NULL, &{}, s, TYPE_{{{{ machine_name|upper }}}}, {});'.format(to_mmio(name), to_ops(name), mmio_size),
                'memory_region_add_subregion_overlap(get_system_memory(), {}, &s->{}, {});'.format(bamboo['mmio_base'], to_mmio(name), mmio_priority)
            ])
            m_context['bamboo_get_field'] = ['\n    '.join(m_context['bamboo_get_field'])]
            m_context['bamboo_get_body'] = ['\n    '.join(m_context['bamboo_get_body'])]
            m_context['bamboo_get_suite'].append(bamboo_suite.format(name, register['offset'], rname, self.__get_endian()))
            self.__add_context(m_context)

    def __skip(self, compatible):
        for cmptb in compatible:
            if cmptb in self.skipped_bdevices:
                return True

    def render(self):
        path_to_dtb = self.firmware.get_dtb()
        dts = load_dtb(path_to_dtb)

        # all intcp should replaced by a real intc
        intcp = {}
        flatten_intc = find_flatten_intc_in_fdt(dts)
        if flatten_intc is not None:
            for intc in flatten_intc:
                m = Model('intc', intc['compatible'])
                if not m.supported:
                    continue
                if 'phandle' not in intc:
                    continue
                intcp[intc['phandle']] = m
        flatten_cpu = find_flatten_cpu_in_fdt(dts)
        if flatten_cpu is not None:
            for cpu in flatten_cpu:
                m = Model('cpu', cpu['compatible'])
                if not m.supported:
                    continue
                intcp[-1] = m

        for k, v in self.rendering_handlers.items():
            if k == 'flash' and self.firmware.get_arch() == 'arm':
                continue
            if k == 'flash' and self.firmware.get_components() \
                    and self.firmware.get_components().has_device_tree():
                dts = load_dtb(self.firmware.get_components().get_path_to_dtb())
            flatten_ks = v(dts)
            if flatten_ks is None:
                self.warning('no {} found'.format(k), 'parse')
                continue
            if self.firmware.get_arch() == 'mips' and k == 'flash' and \
                    not len(flatten_ks):
                # mips will have a default flash if no flash is detected
                flatten_ks = [{'compatible': ['flash,generic'], 'reg': {'base': 0x1fc00000, 'size': 0x400000}}]
            if k == 'serial':
                self.firmware.set_uart_num(len(flatten_ks))
            for context in flatten_ks:
                if k != 'serial' and self.__skip(context['compatible']):
                    self.debug('skip {}'.format(context['compatible']))
                    continue
                # the 1st check, compatible check
                m = Model(k, context['compatible'])
                if not m.supported:
                    self.warning('cannot support {} {}'.format(k, context['compatible']), 'parse')
                    continue

                # the 2nd check, parameters check
                context['name'] = m.effic_compatible.replace(',', '_').replace('-', '_')
                if 'intcp' in context:
                    phandle = context['intcp']
                    if phandle not in intcp:
                        self.warning('cannot support {} {}, {}'.format(k, m.effic_compatible, 'intcp is missing'), 'parse')
                        continue
                    context['intcp'] = intcp[phandle].model
                    context['intcp']['name'] = intcp[phandle].effic_compatible.replace(',', '_').replace('-', '_')

                context['upper'] = self.context['upper']
                context['range'] = self.context['range']
                context['endian'] = self.__get_endian()

                if k == 'flash' and self.firmware.get_arch() == 'mips':
                    if context['reg']['base'] > 0x20000000:
                        context['reg']['base'] &= 0x1FFFFFF
                    context['reg']['size'] = 0x20000000 - context['reg']['base']
                m_context = m.render(context)
                if isinstance(m_context, str):
                    self.warning('cannot suport {} {}, {} is missing'.format(k, m.effic_compatible, m_context), 'parse')
                    continue
                self.__add_context(m_context)

                # the 3rd check, external check
                for x, y in m_context.items():
                    context[x] = y
                context['license'] = self.context['license']
                m.load_template()
                source, header = m.render_qdev(context)
                if isinstance(source, KeyError):
                    self.warning('cannot suport {} {}, {} is missing'.format(k, m.effic_compatible, source), 'parse')
                    return False
                if m.external:
                    self.external[context['name']] = {'type': k, 'source': source, 'header': header}

                # update the skipped_bdevices
                self.skipped_bdevices.append(m.effic_compatible)
                self.skipped_bdevices.extend(m.buddy_compatible)

        # bamboo devices have to be processed in a special way
        self.__render_bamboo_devices()
        if 'timer_get_header' not in self.context:
            self.context['timer_get_header'] = []
            self.context['timer_get_body'] = []
            self.context['timer_get_field'] = []
        if 'flash_get_header' not in self.context:
            self.context['flash_get_header'] = []
            self.context['flash_get_body'] = []
            self.context['flash_get_field'] = []
        try:
            a = Template(self.machine).render(self.context)
            source = Template(a).render(self.context)
        except KeyError as e:
            self.warning('error in parsing, missing {}'.format(e), 'render')
            return False

        # save machine.c
        base = os.path.join(self.firmware.get_target_dir(), 'qemu-4.0.0')
        location = self.location[self.context['arch']]
        fname =  self.context['machine_name'] + '.c'
        self.__save(source, base, location, fname)
        self.info('save at {}/{}/{}'.format(base, location, fname), 'link')

        # save model.c
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

    def __get_endian(self):
        if self.context['endian'] == 'l':
            return 'DEVICE_LITTLE_ENDIAN'
        else:
            return 'DEVICE_BIG_ENDIAN'

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
        with open(os.path.join(GENERATION_DIR, 'machine.c')) as f:
            self.machine = ''.join(f.readlines())

