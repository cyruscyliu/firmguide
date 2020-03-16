import os
import yaml
import logging
import logging.config

from settings import BASE_DIR
from slcore.environment import setup_target_dir, get_target_dir
from slcore.srcodec import SRCodeController
from slcore.qemuc import QEMUController


class Project(object):
    def __init__(self, uuid=None, arch=None, endian=None, target_dir=None,
                 brand=None, target=None, subtarget=None, images=None, dtbs=None,
                 source=None, cross_compile=None, makeout=None):
        """
        Those arguments can be divided into 3 groups.
        1. basics: uuid/arch/endian/target_dir [required]
        2. brand related: brand, target, subtarget [optional]
        3. source related: source/cross_compile/makeout [optional]
        """
        self.target_dir = target_dir
        self.attrs = {
            'uuid': uuid,
            'arch': arch,
            'endian': endian,
            'target_dir': target_dir,
            'brand': brand,
            'target': target,
            'subtarget': subtarget,
            'source': source,
            'cross_compile': cross_compile,
            'makeout': makeout,
            'images': images,
            'dtbs': dtbs,
        }

    def exists(self):
        return os.path.exists(
            os.path.join(self.target_dir, 'project.yaml'))

    def rename(self, new_target_dir):
        os.system('mv {} {}'.format(self.target_dir, new_target_dir))
        self.attrs['target_dir'] = new_target_dir
        self.target_dir = new_target_dir

    def save(self):
        """
        save project.yaml
        """
        yaml.safe_dump(
            self.attrs,
            open(os.path.join(self.target_dir, 'project.yaml'), 'w'))

    def load(self):
        """
        load project.yaml
        """
        self.attrs = yaml.safe_load(
            open(os.path.join(self.target_dir, 'project.yaml')))
        self.target_dir = self.attrs['target_dir']


def __project_get_current():
    current = os.path.join(BASE_DIR, '.project')
    if os.path.exists(current):
        kwargs = yaml.safe_load(open(current))
        project = Project(**kwargs)
        return project
    else:
        return None


def __project_set_current(project):
    current = os.path.join(BASE_DIR, '.project')
    yaml.safe_dump(project.attrs, open(current, 'w'))


def __project_clear_current():
    current = os.path.join(BASE_DIR, '.project')
    os.remove(current)


def project_open(uuid):
    target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is not None:
        project_print('please close current project {}'.format(project.attrs['uuid']))
        return False

    project = Project(target_dir=target_dir)
    if project.exists():
        project.load()
    else:
        project_print('please create a project first')
        return False

    __project_set_current(project)
    return True


def project_config(uuid=None, arch=None, endian=None,
                   brand=None, target=None, subtarget=None,
                   source=None, cross_compile=None, makeout=None):
    project = __project_get_current()
    if project is None:
        project_print('please create/open a project {}'.format(project.attrs['uuid']))
        return False

    if uuid is not None:
        project.attrs['uuid'] = uuid
    if arch is not None:
        project.attrs['arch'] = arch
    if endian is not None:
        project.attrs['endian'] = endian
    if brand is not None:
        project.attrs['brand'] = brand
    if target is not None:
        project.attrs['target'] = target
    if subtarget is not None:
        project.attrs['subtarget'] = subtarget
    if source is not None:
        project.attrs['source'] = source
    if cross_compile is not None:
        project.attrs['cross_compile'] = cross_compile
    if makeout is not None:
        project.attrs['makeout'] = makeout
    __project_set_current(project)
    return True


def project_create(uuid, arch, endian,
                   brand=None, target=None, subtarget=None,
                   source=None, cross_compile=None, makeout=None,
                   mode='cmdline'):
    project = __project_get_current()
    if project is not None:
        project_print('please close current project {}'.format(project.attrs['uuid']))
        return False

    target_dir = setup_target_dir(uuid)
    if mode == 'cmdline':
        project = Project(
            uuid, arch, endian, target_dir=target_dir,
            brand=brand, target=target, subtarget=subtarget,
            source=source, cross_compile=cross_compile, makeout=makeout)
    else:
        raise NotImplementedError('cannot support wizard mode')

    project.save()
    __project_set_current(project)
    return True


def project_rename(uuid):
    new_target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return False

    project.rename(new_target_dir)
    project.attrs['uuid'] = uuid
    __project_set_current(project)
    return True

def project_close():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return False

    project.save()
    __project_clear_current()
    return True


def project_show():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return False

    for k, v in project.attrs.items():
        if isinstance(v, list):
            for vv in v:
                project_print('[+] {}: {}'.format(k, vv))
        else:
            project_print('[+] {}: {}'.format(k, v))
    return True


def update_current_project(project):
    __project_set_current(project)


def get_current_project():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return None
    return project


def project_delete(uuid):
    target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is not None:
        if os.path.realpath(project.target_dir) == os.path.realpath(target_dir):
            __project_clear_current()
    os.system('rm -r {}'.format(target_dir))
    return True


def project_get_srcodec():
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return None

    srcodec = SRCodeController()
    path_to_source_code = project.attrs['source'] # checked
    if path_to_source_code is None:
        return None
    srcodec.set_path_to_source_code(path_to_source_code)
    srcodec.set_path_to_vmlinux(os.path.join(path_to_source_code, 'vmlinux'))
    srcodec.set_path_to_dot_config(os.path.join(path_to_source_code, '.config'))

    cross_compile = project.attrs['cross_compile'] # checked
    if cross_compile is None:
        return None
    srcodec.set_path_to_cross_compile(cross_compile)
    srcodec.set_endian(project.attrs['endian'])
    srcodec.set_arch(project.attrs['arch'])
    srcodec.set_path_to_makeout(project.attrs['makeout'])
    return srcodec


def project_get_qemuc():
    from settings import WORKING_DIR, QEMU_DIR_NAME
    return QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))


def project_setup_logging(default_level=logging.INFO):
    project = __project_get_current()
    if project is None:
        project_print('please open/create a new project')
        return None

    uuid = project.attrs['uuid']
    target_dir = project.attrs['target_dir']

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'logging.yaml')
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        config['handlers']['file']['filename'] = os.path.join(target_dir, '{}.log'.format(uuid))
        config['root']['level'] = default_level
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def project_print(message):
    print('[-] {}'.format(message))

