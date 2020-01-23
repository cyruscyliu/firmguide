"""
settings for the whole project
"""
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# ====== core =====

# default working dir
# WORKING_DIR = os.path.join(BASE_DIR, 'build')
WORKING_DIR = os.path.join(BASE_DIR, '../build')

# python
PYTHON = 'python3.7'

# QEMU
QEMU_PATCH_DIR = 'patches/qemu/files'
QEMU_PACKAGE_URL = 'https://download.qemu.org/qemu-4.0.0.tar.xz'
QEMU_PACKAGE_NAME = 'qemu-4.0.0.tar.xz'
QEMU_DIR_NAME = 'qemu-4.0.0'
QEMU_GLOBAL = False

# BINWALK
BINWALK_PATCH_DIR = 'patches/binwalk/files'
BINWALK_PACKAGE_URL = 'https://github.com/ReFirmLabs/binwalk/archive/v2.1.1.tar.gz'
BINWALK_PACKAGE_NAME = 'v2.1.1.tar.gz'
BINWALK_DIR_NAME = 'binwalk-2.1.1'
BINWALK_GLOBAL = True

