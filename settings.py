"""
settings for the whole project
"""
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TESTS_DIR = os.path.join(BASE_DIR, 'tests')

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

# LLVM-9
LLVM_OPT='opt'
LLVM_LINK='llvm-link'
LLVM_CLANG='clang'
