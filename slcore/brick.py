import os
import copy

from slcore.render import Template
from slcore.database.dbf import get_database


EXTERNAL_TEMPLATE_VERSION = os.getenv('EXTERNAL_TEMPLATE_VERSION', 2)


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
    def __init__(self, t, compatible,
            cast=None, effi=None,
            autoboard=False, autoboard_all=False):
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
        if cast:
            self.compatible = cast
            self.old_compatible = compatible
        else:
            self.compatible = compatible
            self.old_compatible = None
        self.supported = False
        self.model = None
        self.extend = None
        self.actual = {}
        self.effic_compatible = effi
        self.buddy_compatible = []
        self.autoboard = autoboard
        self.autoboard_all = autoboard_all
        if self.autoboard_all:
            self.autoboard = True

        self.source = None
        self.template_to_source = None
        self.header = None
        self.template_to_header = None
        self.external_type = t

        self.unique = False
        self.fix_size = None
        self.disable = False
        self.builtin = None
        self.get_connection_repeated = True

        for cmptb in self.compatible:
            model = self.__load_model(cmptb)
            if model is None:
                self.buddy_compatible.append(cmptb)
                continue
            if self.supported:
                self.buddy_compatible.append(cmptb)
                continue
            if self.old_compatible:
                self.buddy_compatible.extend(self.old_compatible)
            if self.effic_compatible is None:
                self.effic_compatible = cmptb
            self.model = self.__expand_model(model)
            self.supported = True
            if 'buddy_compatible' in model:
                self.buddy_compatible.extend(model['buddy_compatible'])
            if 'unique' in model:
                self.unique = True
            if 'disable' in model:
                self.disable = True
            if 'builtin' in model:
                self.builtin = model['builtin']
            if 'get_connection_repeated' in model:
                self.get_connection_repeated = model['get_connection_repeated']
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
                if 'external_type' in model:
                    self.external_type = model['external_type']

        self.context = None

    def render(self, context):
        """low level render."""
        if self.disable:
            return {}

        self.context = context

        if 'fix_size' in self.model:
            self.fix_size = self.model['fix_size']

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
            if 'get_reserved' in self.model:
                self.__render_get_reserved(context, n=len(context['regs']))
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
                    k == 'get_reserved' or k == 'get_suite':
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
        # sucking code that should be removed in the future
        if self.compatible == ['marvell,orion-timer']:
            context['irqns'] = [2]
            n = 1
        if not self.get_connection_repeated:
            n = 1
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
            if self.fix_size:
                context['reg']['size'] = self.fix_size
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
            if self.fix_size:
                context['reg']['size'] = self.fix_size
            actual = self.__render('get_field', context)
            self.actual['get_field'].extend(actual)

    def __render_get_reserved(self, context, n=1):
        self.actual['get_reserved'] = []
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            if self.fix_size:
                context['reg']['size'] = self.fix_size
            actual = self.__render('get_reserved', context)
            self.actual['get_reserved'].extend(actual)

    def __render_get_reset(self, context, n=1):
        self.actual['get_reset'] = []
        for i in range(0, n):
            context['id'] = i
            context['reg'] = context['regs'][i]
            if self.fix_size:
                context['reg']['size'] = self.fix_size
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
            if self.fix_size:
                context['reg']['size'] = self.fix_size
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
        if self.disable:
            return None, None

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
        model_autoboard, model_autoboard_all = None, None
        if self.autoboard:
            c = compatible + ',autoboard'
            model_autoboard = qemu_devices.select('model', compatible=c)
        if self.autoboard_all:
            c = compatible + ',autoboard,all'
            model_autoboard_all = qemu_devices.select('model', compatible=c)
        if model is None:
            return None
        if model_autoboard_all is not None:
            return model_autoboard_all
        if model_autoboard is not None:
            return model_autoboard
        return model

    def update_model(self, arch):
        """Update the low level template to the database."""
        qemu_devices = get_database('qemu.{}'.format(self.t))

        if self.t == 'cpu':
            if arch == 'arm':
                extend = 'arm'
            else:
                extend = 'mips(el)'
        else:
            extend = self.t

        model = {
            'buddy_compatible': self.buddy_compatible[:-1],
            'extend': '{},generic'.format(extend)
        }
        qemu_devices.add(self.buddy_compatible[-1], **model)
        return True

    def __expand_model(self, model):
        """Expand the low level template if extend exists."""
        if 'extend' in model:
            extend = self.__load_model(model['extend'])
            self.extend = model.pop('extend')
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

    def get_statistics(self, supported=None, iv=None):
        entry = {
            'compatible': self.compatible,
            'type': self.t,
            'iv': {}
        }
        if iv is not None:
            for xxx, yyy in iv.items():
                entry['iv'][xxx] = yyy
        if supported is not None:
            entry['supported'] = supported
        else:
            entry['supported'] = self.supported

        if not entry['supported']:
            return entry

        if self.builtin is not None:
            entry['mtype'] = 'code_reuse'
            entry['code_reuse_count'] = self.builtin
            return entry

        if self.t in ['cpu', 'ram', 'serial', 'misc']:
            entry['mtype'] = 'code_reuse'
            entry['code_reuse_count'] = 1
        elif self.t in ['intc', 'timer']:
            entry['mtype'] = 'state_machine'
        else:
            entry['mtype'] = 'memory_region'
        return entry
