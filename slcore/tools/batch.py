import os

from slcore.project import get_current_project, update_current_project


def project_add_firmware(images, **kwargs):
    """
    Somethings we'd like to add a batch of firmware and test them all.
    """
    project = get_current_project()
    if project is None:
        project

    if 'images' not in project.attrs:
        project.attrs['images'] = []
    elif project.attrs['images'] is None:
        project.attrs['images'] = []
    project.attrs['images'].extend(images)
    update_current_project(project)

