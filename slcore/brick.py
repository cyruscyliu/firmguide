import os
import copy

from slcore.render import Template
from slcore.database.dbf import get_database


EXTERNAL_TEMPLATE_VERSION = 2


def to_qemu_endian(endian):
    if endian == 'l':
        return 'DEVICE_LITTLE_ENDIAN'
    else:
        return 'DEVICE_BIG_ENDIAN'


def to_hex(number):
    return hex(number)


def to_offset(size):
    if size == 4:
        return '0x0'
    else:
        return '0x0 ... 0x{:x}'.format(size - 4)


def to_upper(string):
    return string.upper()


def to_range(n):
    return range(0, n)


class Brick(object):
    def __init__(self, t, compatible):
        """
        Args:
            t(str)          : Type of the mode, e.g. cpu, intc, serial.
            compatible(list): Compatible of the dt node.

        Attributes:
            effic_compatible(str): The compatible of the model.
            buddy_compatible(str): The compatible of the dt node
                                   but not the compatible of the model.
            supported(bool)      : Whether or not this model is supported.
            model(dict)          : The metadata from the database is used
                                   to generate machine.c/peripheral.c etc.
            context(dict)        : The metadata from the dt node like
                                   reg.base/reg.size.
            external             : Whether or not this model is not
                                   built-in qdev.
        """
        self.t = t
        self.compatible = compatible
        self.supported = False
        self.model = None
        self.actual = {}
        self.effic_compatible = None
        self.buddy_compatible = []

        self.source = None
        self.template_to_source = None
        self.header = None
        self.template_to_header = None

        self.unique = False
        self.fix_size = None

        for cmptb in self.compatible:
            model = self.__load_model(cmptb)
            if model is None:
                self.buddy_compatible.append(cmptb)
                continue
            self.effic_compatible = cmptb
            self.model = self.__expand_model(model)
            self.supported = True
            if 'buddy_compatible' in model:
                self.buddy_compatible.extend(model['buddy_compatible'])
            if 'unique' in model:
                self.unique = True
            if 'fix_size' in model:
                self.fix_size = model['fix_size']
            # external source and header
            if 'external' in model:
                self.external = model['external']
            else:
                self.external = False
            if self.external:
                if 'external_source' in model:
                    self.template_to_source = model['external_source']
                else:
                    self.template_to_source = os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        'qemutemplates',
                        '{}{}.c'.format(self.t, EXTERNAL_TEMPLATE_VERSION))
                if 'external_header' in model:
                    self.template_to_header = model['external_header']
                else:
                    self.template_to_header = os.path.join(
                        os.path.dirname(os.path.realpath(__file__)),
                        'qemutemplates',
                        '{}{}.h'.format(self.t, EXTERNAL_TEMPLATE_VERSION))
            break
        self.context = None

    def render(self, context):
        """low level render."""
        self.context = context

        # model['parameters'] tells us what should be in the context
        if 'parameters' in self.model:
            for param in self.model['parameters']:
                if param not in context:
                    return param

        self.actual = copy.deepcopy(self.model)
        self.__render_get_header(context)
        if 'regs' in context:
            self.__render_get_field(context, n=len(context['regs']))
            self.__render_get_body(context, n=len(context['regs']))
            if 'get_registers' in self.model:
                self.__render_get_registers(context, n=len(context['regs']))
            if 'get_reset' in self.model:
                self.__render_get_reset(context, n=len(context['regs']))
            if 'get_suite' in self.model:
                self.__render_get_suite(context, n=len(context['regs']))
        if 'irqns' in context:
            if 'regs' in context:
                self.__render_get_connection(
                    context, n=len(context['irqns']), p=len(context['regs']))
            else:
                self.__render_get_connection(
                    context, n=len(context['irqns']))

        # rendering was done so we could concat them all
        # get_field/body/connection  LIST -> [str]
        # at the same time, we add a prefix to all keys
        context = {}
        for k, v in self.actual.items():
            if k == 'get_body' or k == 'get_field' or \
                    k == 'get_connection' or k == 'get_reset' or \
                    k == 'get_registers' or k == 'get_suite':
                if len(v) > 1:
                    context['{}_{}'.format(self.t, k)] = ['\n    '.join(v)]
                else:
                    context['{}_{}'.format(self.t, k)] = v
            else:
                context['{}_{}'.format(self.t, k)] = v
        return context

    def __render_get_connection(self, context, n=1, p=1):
        self.actual['get_connection'] = []
        if self.unique:
            p = 1
        for i in range(0, n):
            context['irqn'] = context['irqns'][i]
            for j in range(0, p):
                context['id'] = j
                context['iid'] = context['irqn'] // context['intcp']['n_irq']
                context['irqn'] = context['irqn'] % context['intcp']['n_irq']
                context['siid'] = i
                actual = self.__render('get_connection', context)
                self.actual['get_connection'].extend(actual)

    def __render_get_body(self, context, n=1):
        self.actual['get_body'] = []
        if self.unique:
            n = 1
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            if 'irqn' in context:
                context['iid'] = context['irqn'] // context['intcp']['n_irq']
                context['irqn'] = context['irqn'] % context['intcp']['n_irq']
            actual = self.__render('get_body', context)
            self.actual['get_body'].extend(actual)

    def __render_get_header(self, context):
        actual = self.__render('get_header', context)
        self.actual['get_header'] = actual

    def __render_get_field(self, context, n=1):
        self.actual['get_field'] = []
        if self.unique:
            n = 1
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            actual = self.__render('get_field', context)
            self.actual['get_field'].extend(actual)

    def __render_get_registers(self, context, n=1):
        self.actual['get_registers'] = []
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            actual = self.__render('get_registers', context)
            self.actual['get_registers'].extend(actual)

    def __render_get_reset(self, context, n=1):
        self.actual['get_reset'] = []
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            if 'registers' in context['reg']:
                for register in context['reg']['registers']:
                    context['register'] = register
                    actual = self.__render('get_reset', context)
                    self.actual['get_reset'].extend(actual)

    def __render_get_suite(self, context, n=1):
        self.actual['get_suite'] = []
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            actual = self.__render('get_suite', context)
            self.actual['get_suite'].extend(actual)

    def __render(self, key, context):
        actual = []
        for line in self.model[key]:
            a = Template(line).render(context or {})
            actual.append(Template(a).render(context or {}))
        return actual

    def render_qdev(self, context):
        """External template render."""
        if self.fix_size:
            context['reg']['size'] = self.fix_size
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
        """Load the low level template from the database."""
        qemu_devices = get_database('qemu.{}'.format(self.t))
        model = qemu_devices.select('model', compatible=compatible)
        if model is None:
            return None
        return model

    def __expand_model(self, model):
        """Expand the low level template if extend exists."""
        if 'extend' in model:
            extend = self.__load_model(model['extend'])
            model.pop('extend')
            for k, v in extend.items():
                if k in model:
                    continue
                model[k] = v
        return model

    def load_template(self):
        """Load external templates if the external is true."""
        if not self.external:
            return False

        if os.path.exists(self.template_to_source):
            with open(self.template_to_source) as f:
                self.source = ''.join(f.readlines())
        if os.path.exists(self.template_to_header):
            with open(self.template_to_header) as f:
                self.header = ''.join(f.readlines())
