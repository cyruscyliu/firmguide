"""
BINWALK controller
"""
from core.externalc import ExternalPackage
from settings import *

import os


class BINWALKController(ExternalPackage):
    def install(self):
        os.system(
            'wget -nc {0} -O {1}/{2} || true &&'
            'tar --skip-old-files -zxf {1}/{2} -C {1} &&'
            'cp -r {3}/* {1}/{4}/src/'.format(
                BINWALK_PACKAGE_URL, WORKING_DIR, BINWALK_PACKAGE_NAME,
                BINWALK_PATCH_DIR, BINWALK_DIR_NAME))
        os.system(
            'cd {}/{} && sudo $(PYTHON) setup.py -q install'.format(
                WORKING_DIR, BINWALK_DIR_NAME))

    def clean(self):
        os.system('rm -rf {}/{}'.format(WORKING_DIR, BINWALK_DIR_NAME))

    def clear(self):
        os.system('rm -rf {0}/{1} {0}/{2}'.format(
            WORKING_DIR, BINWALK_DIR_NAME, BINWALK_PACKAGE_NAME))
