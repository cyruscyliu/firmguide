import os

from slcore.dt_parsers.cpu import *
from slcore.dt_parsers.serial import *
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.common import *
from slcore.database.dbf import get_database
from slcore.generation.render import Template
from slcore.generation.common import *
from logger import logger_info, logger_debug
from settings import *


class Model(object):
    def __init__(self, t, compatible):
        self.t = t
        self.compatible = compatible
        self.supported = False
        self.model = None
        self.effictive_compatible = None
        self.buddy_compatbile = []

        for cmptb in self.compatible:
            model = self.__load_model(cmptb)
            if model is None:
                self.buddy_compatbile.append(cmptb)
                continue
            self.effictive_compatible = cmptb
            self.model = self.__expand_model(model)
            self.supported = True

    def render(self, context):
        # 2nd check, parameters check
        if 'parameters' in self.model:
            for param in self.model['parameters']:
                if param not in context:
                    return '{} is missing'.format(param)

        # change address from int to hex
        if 'reg' in context:
            if isinstance(context['reg'], dict):
                context['reg']['base'] = hex(context['reg']['base'])
                context['reg']['size'] = hex(context['reg']['size'])
            else:
                for i, (base, size) in enumerate(context['reg']):
                    context['reg'][i]['base'] = hex(base)
                    context['reg'][i]['size'] = hex(size)

        self.__render('get_header', context)
        self.__render('get_field', context)
        self.__render('get_body', context)

        # rendering was done so we could concat them all
        # get_header LIST -> [str]
        # get_filed  LIST -> [str]
        # get_body   LIST -> [str]
        # others      str ->  str
        context = {}
        for k, v in self.model.items():
            if k == 'get_body' or k == 'get_header':
                if len(v) > 1:
                    context['{}_{}'.format(self.t, k)] = ['\n    '.join(v)]
                else:
                    context['{}_{}'.format(self.t, k)] = v
            else:
                context['{}_{}'.format(self.t, k)] = v
        return context

    def __render(self, key, context):
        actual = []
        for line in self.model[key]:
            a = Template(line).render(context or {})
            actual.append(Template(a).render(context or {}))
        self.model[key] = actual

    def __load_model(self, compatible):
        qemu_devices = get_database('qemu.{}'.format(self.t))
        model = qemu_devices.select('model', compatible=compatible)
        if model is None:
            return None
        return model

    def __expand_model(self, model):
        if 'extend' in model:
            extend = self.__load_model(model['extend'])
            model.pop('extend')
            for k, v in extend.items():
                model[k] = v
        return model


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
        self.context['license'] = '/* \n * automatically generated, don\'t change\n */\n'
        self.context['upper'] = lambda x: x.upper()

        self.rendering_handlers = {
            'cpu': find_flatten_cpu_in_fdt,
            'intc': find_flatten_intc_in_fdt,
            'serial': find_flatten_serial_in_fdt,
        }

        self.location = {
            'machine': {'arm': 'hw/arm', 'mips': 'hw/mips', 'interrupt_controller': 'hw/intc'},
        }

    def info(self, message, action):
        logger_info(self.firmware.get_uuid(), 'dt_renderer', action, message, 0)

    def debug(self, message, action):
        logger_debug(self.firmware.get_uuid(), 'dt_renderer', action, message, 0)

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
        res = s->{2}
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
        s->{2} = val;
        break;
    }}
    {0}_update(s);
}}

static const MemoryRegionOps {0}_ops = {{
    .read = {0}_read,
    .write = {0}_write,
    .endianness = {3},
}};
"""
        for name, bamboo in bamboos.items():
            m_context = {'bamboo_get_field': [], 'bamboo_get_body': [], 'bamboo_get_suite': []}
            mmio_size = bamboo['mmio_size']
            mmio_base = bamboo['mmio_base']
            registers = bamboo['registers']
            #
            m_context['bamboo_get_field'].append('MemoryRegion {};'.format(to_mmio(name)))
            #
            for rname, register in registers.items():
                m_context['bamboo_get_field'].append('uint32_t {};'.format(rname))
                self.context['reset_get_field'].append('s->{} = {};'.format(rname, register['value']))
            if 'mmio_priority' in bamboo:
                mmio_priority = bamboo['mmio_priority']
            else:
                mmio_priority = 0
            m_context['bamboo_get_body'].extend([
                'memory_region_init_io(&s->{}, NULL, &{}, s, TYEP_{{{{ machine_name|upper }}}}, {});'.format(to_mmio(name), to_ops(name), mmio_size),
                'memory_region_add_subregion_overlap(get_system_memory(), {}, &s->{}, {});'.format(bamboo['mmio_base'], to_mmio(name), mmio_priority)
            ])
            m_context['bamboo_get_field'] = ['\n    '.join(m_context['bamboo_get_field'])]
            m_context['bamboo_get_body'] = ['\n    '.join(m_context['bamboo_get_body'])]
            m_context['bamboo_get_suite'].append(bamboo_suite.format(name, register['offset'], rname, self.__get_endian()))
            self.__add_context(m_context)

    def render(self):
        path_to_dtb = self.firmware.get_dtb()
        with open(os.path.join(BASE_DIR, 'slcore/generation/machine.c')) as f:
            self.machine = ''.join(f.readlines())
        dts = load_dtb(path_to_dtb)

        # all intcp should replaced by a real intc
        intcp = {}
        flatten_intc = find_flatten_intc_in_fdt(dts)
        for intc in flatten_intc:
            m = Model('intc', intc['compatible'])
            if not m.supported:
                continue
            intcp[intc['phandle']] = m

        for k, v in self.rendering_handlers.items():
            flatten_ks = v(dts)
            for flatten_k in flatten_ks:
                # 1st check, compatible check
                m = Model(k, flatten_k['compatible'])
                if not m.supported:
                    # print('!suport {} {}'.format(k, flatten_k['compatible']))
                    continue

                # 2nd check, parameters check
                flatten_k['name'] = m.effictive_compatible.replace(',', '_').replace('-', '_')
                if 'intcp' in flatten_k:
                    phandle = flatten_k['intcp']
                    if phandle not in intcp:
                        # print('!cannot suport {} {}, {}'.format(k, m.effictive_compatible, 'intcp is missing'))
                        continue
                    flatten_k['intcp'] = intcp[phandle].model
                    flatten_k['name'] = intcp[phandle].effictive_compatible.replace(',', '_').replace('-', '_')

                flatten_k['upper'] = lambda x: x.upper()
                flatten_k['endian'] = self.__get_endian()
                # print('\ncontext:', flatten_k)
                m_context = m.render(flatten_k)
                if isinstance(m_context, str):
                    # print('!cannot suport {} {}, {}'.format(k, m.effictive_compatible, m_context))
                    continue
                self.__add_context(m_context)

        # bamboo devices have to be processed in a special way
        self.__render_bamboo_devices()
        a = Template(self.machine).render(self.context)
        source = Template(a).render(self.context)

        os.makedirs(os.path.join(self.firmware.get_target_dir(), 'qemu-4.0.0'), exist_ok=True)
        source_target = os.path.join(
            self.firmware.get_target_dir(), 'qemu-4.0.0', self.location['machine'][self.context['arch']],
            self.context['machine_name'] + '.c')
        os.makedirs(os.path.dirname(source_target), exist_ok=True)
        with open(source_target, 'w') as f:
            f.write(source)
            f.flush()
        self.info('save at {}'.format(source_target.split('qemu-4.0.0')[1][1:]), 'link')

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


def contain(aa, b):
    """
    aa contains b
    """
    for a in aa:
        if a['path'] == b['path']:
            return True
    return False

def run_dt_renderer(firmware):
    path_to_dtb = firmware.get_dtb()
    if path_to_dtb is None:
        return True

    # 1. load the dtb
    dts = load_dtb(path_to_dtb)

    # 2. create bdevices
    # 2.1 get the intc/serail/mmio list
    flatten_intc = find_flatten_intc_in_fdt(dts)
    flatten_serial = find_flatten_serial_in_fdt(dts)
    flatten_mmio = find_flatten_mmio_in_fdt(dts)
    # 2.2 create bamboo devices
    for mmio in flatten_mmio:
        if contain(flatten_intc, mmio):
            continue
        if contain(flatten_serial, mmio):
            continue
        for reg in mmio['reg']:
            firmware.insert_bamboo_devices(
                reg['base'], reg['size'], value=0)
    firmware.update_bamboo_devices()

    # 3. render
    dt_renderer = DTRenderer(firmware)
    dt_renderer.render()

