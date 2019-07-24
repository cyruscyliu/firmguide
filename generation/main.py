import os

from machines.machine_loader import load_machines
from render import Template

ARM926 = 'arm926'
TEMPLATE_DIR = 'template'


def get_context(machine, context):
    for k, v in machine.items():
        if isinstance(v, dict):
            get_context(v, context)
        else:
            context[k] = v
    return context


def concat(x):
    return ''.join(x.split('_'))


if __name__ == '__main__':
    machines = load_machines('machines')
    for machine in machines:
        context = get_context(machine, {})
        context['upper'] = lambda x: x.upper()
        context['concat'] = lambda x: concat(x)
        templates = os.listdir(TEMPLATE_DIR)
        MACHINE_DIR = context['machine_name']
        if not os.path.exists(MACHINE_DIR):
            os.mkdir(MACHINE_DIR)
        for template in templates:
            target = '{}.{}'.format(context[template[:-2]], template[-1])
            print('generating {} ...'.format(target))
            with open(os.path.join(MACHINE_DIR, target), 'w') as f_target:
                with open(os.path.join(TEMPLATE_DIR, template), 'r') as f_template:
                    lines = ''
                    for line in f_template:
                        lines += line
                text_update = Template(lines).render(context)
                f_target.writelines(text_update)
                f_target.flush()
        print('installing ..')

        print('done!')
