from unittest import TestCase

from slcore.environment import get_target_dir
from slcore.project import project_open, project_close, \
    project_create, project_rename, project_delete
from settings import BASE_DIR

import os


class TestProject(TestCase):
    def test_project_create_open(self):
        os.system('rm -f {}'.format(os.path.join(BASE_DIR, '.project')))
        # normal
        project_create('test_project', 'arm', 'l')
        self.assertTrue(
            os.path.exists(os.path.join(get_target_dir('test_project'), 'project.yaml')))
        self.assertTrue(
            os.path.exists(os.path.join(BASE_DIR, '.project')))
        project_close()
        self.assertTrue(
            os.path.exists(os.path.join(get_target_dir('test_project'), 'project.yaml')))
        self.assertFalse(
            os.path.exists(os.path.join(BASE_DIR, '.project')))
        project_delete('test_project')
        # normal
        project_create('test_project', 'arm', 'l')
        project_close()
        project_open('test_project')
        project_close()
        project_delete('test_project')

        # abnormal: open w/o create
        self.assertFalse(project_open('test_project'))

        # abnormal: open after create
        project_create('test_project', 'arm', 'l')
        self.assertFalse(project_open('test_project'))
        project_close()

        # abnormal: create after open
        project_open('test_project')
        self.assertFalse(project_create('test_project', 'arm', 'l'))
        project_close()
        project_delete('test_project')

    def test_project_rename(self):
        # normal
        project_create('test_project', 'arm', 'l')
        project_rename('new_test_project')
        project_close()

        project_open('new_test_project')
        project_rename('test_project')
        self.assertTrue(
            os.path.exists(os.path.join(get_target_dir('test_project'), 'project.yaml')))
        self.assertTrue(
            os.path.exists(os.path.join(BASE_DIR, '.project')))
        project_close()

        # abnormal: rename w/o open
        self.assertFalse(project_rename('test_project_rename'))

    def test_project_close(self):
        # normal
        project_create('test_project', 'arm', 'l')
        project_close()

        # abnormal: delete w/o open/create
        self.assertFalse(project_close())

