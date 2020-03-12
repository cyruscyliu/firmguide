"""
General Low Level Render.

The GLLR(General Low Level Render) is a abstract layer of rendering
low level templates. We define the syntax of low level templates
as below. Let's take intc,generic as an example.

Example:
    intc,generic:
        paramters: [name, reg, intcp]
        get_header: ['hw/intc/{{ name }}.h']
        get_field: ['{{ name|upper }}State {{name}}']
        get_body:
            - 'object_initialize(&s->{{ name }}, sizeof(s->{{ name }}), TYPE_{{ name|upper }});'
            - 'qdev_set_parent_bus(DEVICE(&s->{{ name }}), sysbus_get_default());'
            - 'object_property_set_bool(OBJECT(&s->{{ name }}), true, "realized", &err);'
            - 'sysbus_mmio_map(SYS_BUS_DEVICE(&s->{{ name }}), 0, {{ reg.base }});',
        get_connection: ['qdev_connect_gpio_out(DEVICE(&s->{{ name }}), 0, {{ intcp.get_irqn }});']
        get_irqn: qdev_get_gpio_in(DEVICE(&s->{{ intcp.name }}), {{ irqn|__restore_irqn }})
        buddy_compatible: []

Note:
    1. You have to assign a key to a peripheral. Mostly, the key is the one of
    the compatibles of the peripheral and you can put the others into the
    buddy_compatible. To together with buddy_compatible, only the key compatible
    will be recognized, the others will be ignored, which is useful when we use
    integrated devices in QEMU, such as arm1mpcore-priv..
    2. Put all context keys used in parameters, say we will use `name` in get_header,
    then you put `name` in the parameters, in order to pre-check the context.
    3. Put all header templates into get_header.
    4. Put all soc field templates into get_field.
    5. Put all initialization templates into get_body.
    6. Put all connection templates into get_connection.
    7. Put all irq input templates into get_irqn.
"""
import os
import copy

from slcore.generation.render import Template
from slcore.database.dbf import get_database


EXTERNAL_TEMPLATE_VERSION = 2


class Model(object):
    def __init__(self, t, compatible):
        """
        Args:
            t(str)          : Type of the mode, e.g. cpu, intc, serial.
            compatible(list): Compatible of the dt node.

        Attributes:
            effic_compatible(str): The compatible of the model.
            buddy_compatible(str): The compatible of the dt node but not the compatible of the model.
            supported(bool)      : Whether or not this model is supported.
            model(dict)          : The metadata from the database is used to generate machine.c/peripheral.c etc.
            context(dict)        : The metadata from the dt node like reg.base/reg.size.
            external             : Whether or not this model is not built-in qdev.
        """
        self.t = t
        self.compatible = compatible
        self.supported = False
        self.model = None
        self.actual = {}
        self.effic_compatible = None
        self.buddy_compatible = []
        self.source = None
        self.header = None
        self.unique = False

        for cmptb in self.compatible:
            model = self.__load_model(cmptb)
            if model is None:
                self.buddy_compatible.append(cmptb)
                continue
            self.effic_compatible = cmptb
            self.model = self.__expand_model(model)
            self.supported = True
            if 'external' in model:
                self.external = model['external']
            else:
                self.external = False
            if 'buddy_compatible' in model:
                self.buddy_compatible.extend(model['buddy_compatible'])
            if 'unique' in model:
                self.unique = True
            break
        self.context = None

    def render(self, context):
        """low level render."""
        self.context = context

        # the 2nd check, parameters check
        # self.model['parameters'] tells us what should be in the context
        if 'parameters' in self.model:
            for param in self.model['parameters']:
                if param not in context:
                    return param

        # update int to hex, especially in reg
        if 'regs' in context:
            for reg in context['regs']:
                reg['base'] = hex(reg['base'])
                reg['size'] = hex(reg['size'])

        self.actual = copy.deepcopy(self.model)
        self.__render_get_header(context)
        if 'regs' in context:
            self.__render_get_field(context, n=len(context['regs']))
            self.__render_get_body(context, n=len(context['regs']))
        if 'irqns' in context:
            self.__render_get_connection(context, n=len(context['irqns']), p=len(context['regs']))

        # rendering was done so we could concat them all
        # get_field/body/connection  LIST -> [str]
        # at the same time, we add a prefix to all keys
        context = {}
        for k, v in self.actual.items():
            if k == 'get_body' or k == 'get_field' or k == 'get_connection':
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
                actual = self.__render('get_connection', context)
                self.actual['get_connection'].extend(actual)

    def __render_get_body(self, context, n=1):
        self.actual['get_body'] = []
        if self.unique:
            n = 1
        for i in range(0, n):
            context['reg'] = context['regs'][i]
            context['id'] = i
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
            actual = self.__render('get_field', context)
            self.actual['get_field'].extend(actual)

    def __render(self, key, context):
        actual = []
        for line in self.model[key]:
            a = Template(line).render(context or {})
            actual.append(Template(a).render(context or {}))
        return actual

    def render_qdev(self, context):
        """External template render."""
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
            return
        psource = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '{}{}.c'.format(self.t, EXTERNAL_TEMPLATE_VERSION))
        if os.path.exists(psource):
            with open(psource) as f:
                self.source = ''.join(f.readlines())
        pheader = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            '{}{}.h'.format(self.t, EXTERNAL_TEMPLATE_VERSION))
        if os.path.exists(pheader):
            with open(pheader) as f:
                self.header = ''.join(f.readlines())

