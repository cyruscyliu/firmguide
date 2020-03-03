import os
import tempfile

from slcore.compositor import unpack
from slcore.project import get_current_project, update_current_project


def project_add_firmware(images, **kwargs):
    """
    Sometimes we'd like to add a batch of firmware and test them all.
    """
    project = get_current_project()
    if project is None:
        return

    if 'images' not in project.attrs:
        project.attrs['images'] = []
    elif project.attrs['images'] is None:
        project.attrs['images'] = []
    project.attrs['images'].extend(images)
    update_current_project(project)


def project_scan_firmware(path, **kwargs):
    """
    Mostly, we'd like to add a batch of firmware automated.
    """
    has_device_tree = kwargs.pop('dt', True)
    count = kwargs.pop('count', 1)

    project = get_current_project()
    if project is None:
        return

    if 'images' not in project.attrs:
        project.attrs['images'] = []
    elif project.attrs['images'] is None:
        project.attrs['images'] = []

    candidates = []
    for f in os.listdir(path):
        firmware = os.path.join(path, f)
        if firmware in project.attrs['images']:
            print('[+] {} existed'.format(firmware))
            continue
        if not os.path.isfile(firmware):
            continue
        components = unpack(firmware, target_dir=tempfile.gettempdir())
        if not components.supported:
            continue
        if has_device_tree and not components.has_device_tree():
            continue
        print('[+] {} added'.format(firmware))
        candidates.append(firmware)
        if len(candidates) >= count:
            break

    project.attrs['images'].extend(candidates)
    update_current_project(project)

