import os

from slcore.dt_parsers.cpu import *
from slcore.dt_parsers.serial import *
from slcore.dt_parsers.intc import *
from slcore.dt_parsers.common import *
from slcore.database.dbf import get_database
from slcore.generation.render import Template
from slcore.generation.common import *
from logger import logger_info, logger_debug, logger_warning
from settings import *


class Model(object):
    def __init__(self, t, compatible):
        """
        self.t               :type of the mode, e.g. cpu, intc, serial
        self.compatible      :compatible of the dt node
        self.effic_compatible:compatible of the model
        self.buddy_compatible:compatible of the dt node but not the compatible of the model
        self.supported       :whether or not this model is supported
        self.model           :metadata from the database which is used to
                              generate machine.c/peripheral.c etc.
        self.context         :metadata from the dt node like reg.base/reg.size
        self.external        :whether or not this model is not built-in qdev
        """
        self.t = t
        self.compatible = compatible
        self.supported = False
        self.model = None
        self.effic_compatible = None
        self.buddy_compatbile = []
        self.source = None
        self.header = None

        for cmptb in self.compatible:
            model = self.__load_model(cmptb)
            if model is None:
                self.buddy_compatbile.append(cmptb)
                continue
            self.effic_compatible = cmptb
            self.model = self.__expand_model(model)
            self.supported = True
            if 'externel' in model:
                self.external = model['externel']
            else:
                self.external = False
            break
        self.context = None

    def render(self, context):
        self.context = context

        # the 2nd check, parameters check
        # self.model['parameters'] tells us what should be in the context
        if 'parameters' in self.model:
            for param in self.model['parameters']:
                if param not in context:
                    return param

        # update int to hex, especially in reg
        # for a supported model, only base address is needed
        # intc/serial etc. should let context['reg'] = mmio['reg'][0]
        if 'reg' in context:
            context['reg']['base'] = hex(context['reg']['base'])
            context['reg']['size'] = hex(context['reg']['size'])

        self.__render('get_header', context)
        self.__render('get_field', context)
        self.__render('get_body', context)

        # rendering was done so we could concat them all
        # get_header LIST -> [str]
        # get_filed  LIST -> [str]
        # get_body   LIST -> [str]
        # others      str ->  str
        # at the same time, we add a prefix to all keys
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

    def render_qdev(self, context):
        try:
            if self.source:
                a = Template(self.source).render(context)
                self.source = Template(a).render(context)
            if self.header:
                a = Template(self.header).render(context)
                self.header = Template(a).render(context)
            return self.source, self.header
        except KeyError as e:
            return e, e

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

    def load_template(self):
        if not self.external:
            return
        psource = os.path.join(GENERATION_DIR, '{}2.c'.format(self.t))
        if os.path.exists(psource):
            with open(psource) as f:
                self.source = ''.join(f.readlines())
        pheader = os.path.join(GENERATION_DIR, '{}2.h'.format(self.t))
        if os.path.exists(pheader):
            with open(pheader) as f:
                self.header = ''.join(f.readlines())


class DTRenderer(object):
    def __init__(self, firmware):
        self.firmware = firmware

        self.context = {}
        firmware.set_machine_name(firmware.get_uuid())
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

        self.machine = None
        self.location = {'arm': 'hw/arm', 'mips': 'hw/mips', 'intc': 'hw/intc'}
        self.external = {}

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
        dts = load_dtb(path_to_dtb)

        # all intcp should replaced by a real intc
        intcp = {}
        flatten_intc = find_flatten_intc_in_fdt(dts)
        if flatten_intc is not None:
            for intc in flatten_intc:
                m = Model('intc', intc['compatible'])
                if not m.supported:
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
            flatten_ks = v(dts)
            if flatten_ks is None:
                self.warning('no {} found'.format(k), 'parse')
                continue
            for context in flatten_ks:
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

                context['upper'] = lambda x: x.upper()
                context['endian'] = self.__get_endian()

                m.load_template()
                m_context = m.render(context)
                if isinstance(m_context, str):
                    self.warning('cannot suport {} {}, {} is missing'.format(k, m.effic_compatible, m_context), 'parse')
                    continue
                self.__add_context(m_context)

                # the 3rd check, external check
                for x, y in m_context.items():
                    context[x] = y
                context['license'] = self.context['license']
                source, header = m.render_qdev(context)
                if isinstance(source, KeyError):
                    self.warning('cannot suport {} {}, {} is missing'.format(k, m.effic_compatible, m_context), 'parse')
                    return False
                if m.external:
                    self.external[context['name']] = {'type': k, 'source': source, 'header': header}

        # bamboo devices have to be processed in a special way
        self.__render_bamboo_devices()
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
        return False

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


def contain(aa, b):
    """
    aa contains b
    """
    if aa is None:
        return False

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
    exclusive_find_flatten_handlers = [
        find_flatten_intc_in_fdt,
        find_flatten_serial_in_fdt
    ]
    flatten_ks = []
    for effh in exclusive_find_flatten_handlers:
        context= effh(dts)
        if context is not None:
            flatten_ks.extend(context)
    flatten_mmio = find_flatten_mmio_in_fdt(dts)
    # 2.2 create bamboo devices
    for mmio in flatten_mmio:
        if contain(flatten_ks, mmio):
            continue
        for reg in mmio['reg']:
            firmware.insert_bamboo_devices(
                reg['base'], reg['size'], value=0)
    firmware.update_bamboo_devices()

    # 3. render
    dt_renderer = DTRenderer(firmware)
    dt_renderer.load_template()
    status = dt_renderer.render()
    if not status:
        return False

    # 4. compiler
    # 4.1 copy files to qemu/
    prefix = os.path.join(firmware.get_target_dir(), 'qemu-4.0.0')
    firmware.qemuc.install(prefix)
    # 4.2 update compilation targets
    firmware.qemuc.add_target(
        to_upper(firmware.get_machine_name()), firmware.get_machine_name(),
        type_='hw',arch=firmware.get_arch(), endian=firmware.get_endian())
    for k, v in dt_renderer.external.items():
        firmware.qemuc.add_target(to_upper(k), k, type_=v['type'])
    # 4.3 compile
    firmware.qemuc.compile(cflags='-Wmaybe-uninitialized', cpu=4)
    # 4.3 keep qemu clean
    firmware.qemuc.recover()
    return True

