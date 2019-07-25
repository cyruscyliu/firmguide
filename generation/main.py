from shutil import copyfile
import argparse
import yaml
import os

from machines.machine_loader import load_machines
from render import Template

TEMPLATE_DIR = 'template'


def get_config(path='config.yaml'):
    with open(path, encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config['install']


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
    parser = argparse.ArgumentParser()
    parser.add_argument('-os', help="assign your operating system, windows by default",
                        choices=['windows', 'linux'], default='windows')
    args = parser.parse_args()

    OS = args.os

    machines = load_machines('machines')
    config = get_config()
    for machine in machines:
        context_inv = {}
        context = get_context(machine, {})
        context['upper'] = lambda x: x.upper()
        context['concat'] = lambda x: concat(x)
        templates = os.listdir(TEMPLATE_DIR)
        MACHINE_DIR = context['machine_name']
        if not os.path.exists(MACHINE_DIR):
            os.mkdir(MACHINE_DIR)
        for template in templates:
            target = '{}.{}'.format(context[template[:-2]], template[-1])
            context_inv[target[:-2]] = template[:-2]
            print('generating {} ...'.format(target))
            with open(os.path.join(MACHINE_DIR, target), 'w') as f_target:
                with open(os.path.join(TEMPLATE_DIR, template), 'r') as f_template:
                    lines = ''
                    for line in f_template:
                        lines += line
                text_update = Template(lines).render(context)
                f_target.writelines(text_update)
                f_target.flush()

        print('\ninstalling ..')
        source_header_files = os.listdir(MACHINE_DIR)
        target_dir = config[OS]['root']
        for source_header_file in source_header_files:
            name = source_header_file[:-2]
            src = os.path.join(MACHINE_DIR, source_header_file)
            if source_header_file.endswith('c'):
                dst = os.path.join(target_dir, config[OS][context_inv[name]], source_header_file)
            elif source_header_file.endswith('h'):
                dst = os.path.join(target_dir, config['include'], config[OS][context_inv[name]], source_header_file)
            else:
                continue
            print(src, '->', dst)
            copyfile(src, dst)

        for root, dirs, files in os.walk('makefiles'):
            if not len(dirs):
                for file_ in files:
                    src = os.path.join(root, file_)
                    dst = os.path.join(target_dir, root.replace('makefiles\\', ''), file_)
                    print(src, '->', dst)
                    copyfile(src, dst)

        print('done!')
