import os
import yaml


class Project(object):
    def __init__(self, name=None, arch=None, endian=None, path=None,
                 brand=None, target=None, subtarget=None, images=None,
                 dtbs=None, source=None, cross_compile=None, makeout=None,
                 base_dir=None, rootfs_dir=None, build_dir=None, qemu_dir=None,
                 llvm_dir=None, sparse_dir=None):
        """
        Those arguments can be divided into 3 groups.
        1. basics: name/arch/endian/path/base_dir/rootfs_dir [required]
        2. brand related: brand, target, subtarget [optional]
        3. source related: source/cross_compile/makeout [optional]
        """
        self.attrs = {
            'name': name, 'arch': arch, 'endian': endian,
            'path': path, 'base_dir': base_dir,
            'rootfs_dir': rootfs_dir, 'qemu_dir': qemu_dir,
            'llvm_dir': llvm_dir, 'sparse_dir': sparse_dir,
            'brand': brand, 'target': target, 'subtarget': subtarget,
            'source': source, 'cross_compile': cross_compile,
            'makeout': makeout, 'images': images, 'dtbs': dtbs,
        }

    def exists(self):
        return os.path.exists(
            os.path.join(self.attrs['path'], 'project.yaml'))

    def rename(self, new_name):
        self.attrs['name'] = new_name

    def save(self):
        """
        save project.yaml
        """
        yaml.safe_dump(
            self.attrs,
            open(os.path.join(self.attrs['path'], 'project.yaml'), 'w'))

    def load(self):
        """
        load project.yaml
        """
        self.attrs = yaml.safe_load(
            open(os.path.join(self.attrs['path'], 'project.yaml')))


def project_print(message):
    print('[+] {}'.format(message))


def project_get_current(base_dir):
    """Get current project."""
    current = os.path.join(base_dir, '.project')
    if os.path.exists(current):
        kwargs = yaml.safe_load(open(current))
        project = Project(**kwargs)
        return project
    else:
        return None


def project_set_current(project):
    """Set current project to your own project."""
    current = os.path.join(project.attrs['base_dir'], '.project')
    yaml.safe_dump(project.attrs, open(current, 'w'))


def project_clear_current(base_dir):
    """Clear(remove) current project."""
    current = os.path.join(base_dir, '.project')
    os.remove(current)


def project_open(*args, **kwargs):
    """Open a project."""
    path = kwargs.pop('path')
    base_dir = kwargs.pop('base_dir')

    project = project_get_current(base_dir)
    if project is not None:
        project_print('please close current project {}'.format(
            project.attrs['name']))
        return False

    project = Project(path=path)
    if project.exists():
        project.load()
    else:
        project_print('please create a project first')
        return False

    project_set_current(project)
    return True


def project_config(*args, **kwargs):
    """Config current project."""
    base_dir = kwargs.pop('base_dir')
    project = project_get_current(base_dir)
    if project is None:
        project_print('please create/open a project.')
        return False

    for k, v in kwargs.items():
        if k not in project.attrs:
            continue
        if v is None:
            continue
        project.attrs[k] = v

    project_set_current(project)
    return True


def project_create(*args, **kwargs):
    base_dir = kwargs.pop('base_dir')
    project = project_get_current(base_dir)
    if project is not None:
        project_print('please close current project {}'.format(
            project.attrs['name']))
        return False

    rootfs_dir = kwargs.pop('rootfs_dir')
    qemu_dir = kwargs.pop('qemu_dir')
    llvm_dir = kwargs.pop('llvm_dir')
    sparse_dir = kwargs.pop('sparse_dir')

    path = kwargs.pop('path')
    os.makedirs(path, exist_ok=True)

    project = Project(
        name=kwargs.pop('name'), arch=kwargs.pop('arch'),
        endian=kwargs.pop('endian'), path=path,
        base_dir=base_dir, rootfs_dir=rootfs_dir,
        qemu_dir=qemu_dir, llvm_dir=llvm_dir, sparse_dir=sparse_dir,
        brand=kwargs.pop('brand', None),
        target=kwargs.pop('target', None),
        subtarget=kwargs.pop('subtarget', None),
        source=kwargs.pop('source', None),
        cross_compile=kwargs.pop('cross_compile', None),
        makeout=kwargs.pop('makeout', None))

    project.save()
    project_set_current(project)
    return True


def project_rename(*args, **kwargs):
    base_dir = kwargs.pop('base_dir')
    project = project_get_current(base_dir)
    if project is None:
        project_print('please open/create a new project')
        return False

    name = kwargs.pop('name')
    project.rename(name)

    project_set_current(project)
    return True


def project_close(*args, **kwargs):
    base_dir = kwargs.pop('base_dir')
    project = project_get_current(base_dir)
    if project is None:
        project_print('please open/create a new project')
        return False

    project.save()
    project_clear_current(base_dir)
    return True


def project_show(*args, **kwargs):
    base_dir = kwargs.pop('base_dir')
    project = project_get_current(base_dir)
    if project is None:
        project_print('please open/create a new project')
        return False

    for k, v in project.attrs.items():
        if isinstance(v, list):
            for vv in v:
                project_print('{}: {}'.format(k, vv))
        else:
            project_print('{}: {}'.format(k, v))
    return True


def project_delete(*args, **kwargs):
    base_dir = kwargs.pop('base_dir')
    path = kwargs.pop('path')

    project = project_get_current(base_dir)
    if project is not None:
        if os.path.realpath(project.attrs['path']) == \
                os.path.realpath(path):
            project_clear_current(base_dir)
            os.system('rm -r {}'.format(path))
            return True
    return False


def __project_add(container, items):
    if items is None:
        return
    for item in items:
        if item in container:
            print('[+] {} existed'.format(item))
            continue
        container.append(item)


def project_batch(*args, **kwargs):
    """BATCH command interface."""
    base_dir = kwargs.pop('base_dir')
    project = project_get_current(base_dir)
    if project is None:
        project_print('please create/open a project.')
        return False

    images = kwargs.pop('add')
    if project.attrs['images'] is None:
        project.attrs['images'] = []
    __project_add(project.attrs['images'], images)
    dtbs = kwargs.pop('add_dtb')
    if project.attrs['dtbs'] is None:
        project.attrs['dtbs'] = []
    __project_add(project.attrs['dtbs'], dtbs)
    project_set_current(project)


def get_project_callbacks():
    return {
        'project_open': project_open,
        'project_config': project_config,
        'project_create': project_create,
        'project_rename': project_rename,
        'project_close': project_close,
        'project_show': project_show,
        'project_delete': project_delete,
        'project_batch': project_batch
    }
