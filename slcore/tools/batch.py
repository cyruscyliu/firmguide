import os
import tempfile

from slcore.compositor import unpack
from slcore.project import get_current_project, update_current_project


def project_plugin_batch(args):
    if args.add:
        project_add_image(args.add)
    elif args.extend:
        project_scan_images(args.extend, dt=args.dt, count=args.count)
    elif args.show:
        project_show_images()


def project_show_images():
    project = get_current_project()
    if project is None:
        return

    __project_init_image(project)
    images = project.attrs['images']
    if not len(images):
        print('[+] no images in current project')
        return
    for image in images:
        print('[+] {}'.format(image))


def __project_init_image(project):
    if 'images' not in project.attrs:
        project.attrs['images'] = []
    elif project.attrs['images'] is None:
        project.attrs['images'] = []


def project_add_image(images, **kwargs):
    """
    Sometimes we'd like to add a batch of firmware and test them all.
    """
    project = get_current_project()
    if project is None:
        return

    __project_init_image(project)
    for image in images:
        if image in project.attrs['images']:
            print('[+] {} existed'.format(image))
            continue
        project.attrs['images'].append(image)
    update_current_project(project)


def project_scan_images(path, **kwargs):
    """
    Mostly, we'd like to add a batch of firmware automated.
    """
    has_device_tree = kwargs.pop('dt', True)
    count = kwargs.pop('count', 1)

    project = get_current_project()
    if project is None:
        return

    __project_init_image(project)

    candidates = []
    for f in os.listdir(path):
        firmware = os.path.join(path, f)
        if not os.path.isfile(firmware):
            continue
        if firmware.endswith('.tar.gz') or firmware.endswith('.tar.xz') or \
                firmware.endswith('.tar') or firmware.endswith('.tar.bz2'):
            print('[+] skip {}'.format(firmware))
            continue
        if firmware in project.attrs['images']:
            print('[+] {} existed'.format(firmware))
            continue
        print('[+] unpacking {}'.format(firmware))
        components = unpack(firmware, target_dir=tempfile.gettempdir())
        if not components.supported:
            print('[+] {} unsupported'.format(firmware))
            continue
        if has_device_tree and not components.has_device_tree():
            continue
        print('[+] add {}'.format(firmware))
        candidates.append(firmware)
        if len(candidates) >= count:
            break

    project.attrs['images'].extend(candidates)
    update_current_project(project)

