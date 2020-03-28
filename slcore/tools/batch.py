import os
import tempfile

from slcore.compositor import unpack
from slcore.project import get_current_project, update_current_project


def project_plugin_batch(args):
    """BATCH command interface."""
    if args.add:
        project_add('images', args.add)
    elif args.add_dtb:
        project_add('dtbs', args.add_dtb)
    elif args.extend:
        project_scan('images', args.extend, dt=args.dt, count=args.count, kernel=True)
    elif args.extend_dtb:
        project_scan('dtbs', args.extend_dtb, count=args.count)
    elif args.show:
        project_show('images')
        project_show('dtbs')


def project_show(t):
    """Show images/dtbs in current project."""
    project = get_current_project()
    if project is None:
        return

    __project_init(project, t)
    items = project.attrs[t]
    if not len(items):
        print('[+] no {} in current project'.format(t))
        return
    for item in items:
        print('[+] {}'.format(item))


def __project_init(project, t):
    if t not in project.attrs:
        project.attrs[t] = []
    elif project.attrs[t] is None:
        project.attrs[t] = []


def project_add(t, items, **kwargs):
    """Add a batch of things and test them all."""
    project = get_current_project()
    if project is None:
        return

    __project_init(project, t)
    for item in items:
        if item in project.attrs[t]:
            print('[+] {} existed'.format(item))
            continue
        project.attrs[t].append(item)
    update_current_project(project)


def project_scan(t, path, **kwargs):
    """Add a batch of things automated."""
    has_kernel = kwargs.pop('kernel', False)
    has_device_tree = kwargs.pop('dt', True)
    count = kwargs.pop('count', -1)

    project = get_current_project()
    if project is None:
        return

    __project_init(project, t)

    candidates = []
    for f in os.listdir(path):
        item = os.path.join(path, f)
        if not os.path.isfile(item):
            continue
        if item.endswith('.gz') or item.endswith('.xz') or \
                item.endswith('.tar') or item.endswith('.bz2') or \
                item.endswith('.dts') or item.endswith('.dtsi'):
            print('[+] skip {}'.format(item))
            continue
        if item in project.attrs[t]:
            print('[+] {} existed'.format(item))
            continue
        print('[+] unpacking {}'.format(item))
        components = unpack(item, target_dir=tempfile.gettempdir())
        if has_kernel and not components.supported:
            print('[+] {} unsupported'.format(item))
            continue
        if has_device_tree and not components.has_device_tree():
            print('[+] {} has no device tree'.format(item))
            continue
        print('[+] add {}'.format(item))
        candidates.append(item)
        if count != -1 and len(candidates) >= count:
            break

    project.attrs[t].extend(candidates)
    update_current_project(project)

