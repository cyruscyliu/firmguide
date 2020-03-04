import os
import yaml
from settings import BASE_DIR
from logger import logger_info2, logger_debug2, logger_warning2
from slcore.environment import setup_target_dir, get_target_dir
from slcore.srcodec import SRCodeController
from slcore.qemuc import QEMUController


class Project(object):
    def __init__(self, uuid=None, arch=None, endian=None, target_dir=None,
                 brand=None, target=None, subtarget=None, images=None,
                 source=None, cross_compile=None, makeout=None):
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
        print('please close current project {}'.format(project.attrs['uuid']))
        return False

    project = Project(target_dir=target_dir)
    if project.exists():
        project.load()
    else:
        print('please create a project first')
        return False

    __project_set_current(project)
    logger_info2('project', 'open', uuid, 1)
    return True


def project_create(uuid, arch, endian,
                   brand=None, target=None, subtarget=None,
                   source=None, cross_compile=None, makeout=None,
                   mode='cmdline'):
    project = __project_get_current()
    if project is not None:
        print('please close current project {}'.format(project.attrs['uuid']))
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
    logger_info2('project', 'create', uuid, 1)
    return True


def project_rename(uuid):
    new_target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is None:
        print('please open/create a new project')
        return False

    old_target_dir = project.attrs['uuid']
    project.rename(new_target_dir)
    __project_set_current(project)
    logger_info2('project', 'rename', '{}->{}'.format(old_target_dir, new_target_dir), 1)
    return True

def project_close():
    project = __project_get_current()
    if project is None:
        print('please open/create a new project')
        return False

    uuid = project.attrs['uuid']
    __project_clear_current()
    logger_info2('project', 'close', uuid, 1)
    return True


def project_show():
    project = __project_get_current()
    if project is None:
        print('please open/create a new project')
        return False

    for k, v in project.attrs.items():
        if isinstance(v, list):
            for vv in v:
                logger_info2('project', 'show', '{}: {}'.format(k, vv), 1)
        else:
            logger_info2('project', 'show', '{}: {}'.format(k, v), 1)
    return True


def update_current_project(project):
    __project_set_current(project)


def get_current_project():
    project = __project_get_current()
    if project is None:
        print('please open/create a new project')
        return None
    return project


def project_delete(uuid):
    target_dir = get_target_dir(uuid)
    project = __project_get_current()
    if project is not None:
        if os.path.realpath(project.target_dir) == os.path.realpath(target_dir):
            __project_clear_current()
    os.system('rm -r {}'.format(target_dir))
    logger_info2('project', 'delete', uuid, 1)
    return True


def project_get_srcodec():
    project = __project_get_current()
    if project is None:
        print('please open/create a new project')
        return None

    srcodec = SRCodeController()
    path_to_source_code = project.attrs['source']
    srcodec.set_path_to_source_code(path_to_source_code)
    srcodec.set_path_to_vmlinux(os.path.join(path_to_source_code, 'vmlinux'))
    srcodec.set_path_to_dot_config(os.path.join(path_to_source_code, '.config'))
    srcodec.set_path_to_cross_compile(project.attrs['cross_compile'])
    srcodec.set_endian(project.attrs['endian'])
    srcodec.set_arch(project.attrs['arch'])
    srcodec.set_path_to_makeout(project.attrs['makeout'])
    return srcodec


def project_get_qemuc():
    from settings import WORKING_DIR, QEMU_DIR_NAME
    return QEMUController(os.path.join(WORKING_DIR, QEMU_DIR_NAME))

