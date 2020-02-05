"""
source code controller
"""
from settings import *
from logger import logger_info
from pycparser import c_parser, c_ast, parse_file

import os
import qmp
import pydot
import subprocess

BACKUP, PATCH, COMPILE, LINK = 0, 1, 2, 3

class SRCodeController(object):
    def __init__(self, srcode, arch, prefix, cpu=4):
        self.srcode = srcode
        self.arch = arch
        self.prefix = prefix

        self.makeout = None
        self.cpu = cpu

        # mode
        self.llvm = False
        self.sparse = not os.system('which graph >/dev/null')

    def get_system_map(self):
        path = os.path.join(self.srcode, 'System.map')

        system_map = {}
        with open(path) as f:
            for line in f:
                # ffffffff803687e8 T arch_init_irq
                addr, type_, sym = line.strip().split()
                system_map[sym] = {'addr': addr, 'type': type_}
        return system_map

    def symbol2address(self, symbol):
        system_map = os.path.join(self.srcode, 'System.map')

        with open(system_map) as f:
            for line in f:
                # ffffffff803687e8 T arch_init_irq
                addr, type_, sym = line.strip().split()
                if sym == symbol:
                    return int(addr, 16) & 0xFFFFFFFF

        return None

    def addr2file(self, address):
        path_to_vmlinux = os.path.join(self.srcode, 'vmlinux')

        output = os.popen('addr2line -e {} {}'.format(path_to_vmlinux, hex(address))).readlines()
        if len(output):
            # /abs/path/to/linux-3.18.20/arch/mips/bcm47xx/irq.c:69
            f, l = output[0].split(':')
            s = f
            while s != '/':
                s, _ = os.path.split(s)
                if os.path.realpath(s) == os.path.realpath(self.srcode):
                    break
            return f[len(s)+1:]

        return None

    def get_cmdline(self, path):
        """
        get_cmdline('arch/arm/mm/proc-xxx.c')

        """
        full_path = os.path.join(self.srcode, path)
        full_dir = os.path.dirname(full_path)
        base = os.path.basename(full_path)
        full_cmd = os.path.join(full_dir, '.{}.cmd'.format(base.replace('.c', '.o')))

        cmdline = None
        if os.path.exists(full_cmd):
            with open(full_cmd) as f:
                cmdline = f.readline().strip().split(':=')[1]
        return cmdline

    def run(self, command):
        cwd = os.getcwd()
        os.chdir(self.srcode)
        status = os.system(command + '>/dev/null 2>&1')
        os.chdir(cwd)
        return status

    def set_makeout(self, makeout):
        self.makeout = makeout

    def get_makeout(self):
        if self.makeout is not None:
            return self.makeout

        self.makeout = os.path.join(self.srcode, 'makeout.txt')
        self.run('make -j{} ARCH={} CROSS_COMPILE={}'.format(self.cpu, self.arch, self.prefix))

        return self.makeout

    def __backup(compress=True, copy=False):
        pass

    def __patch():
        if self.patch:
            return
        self.patch = True

    def __build():
        if self.build:
            return
        self.build = True
        pass

    def __link():
        pass

    def apply_to_llvm(self, backup=True, patch=True, build=True, link=True):
        self.__backup()
        self.__patch()
        if build:
            self.__build()
        if link:
            self.__link()

    def __has_gcc(self, line):
        gcc = [os.path.basename(self.prefix) + 'gcc', 'ccache_cc']
        for i in gcc:
            if line.split()[0].endswith(i):# or line.split()[1].endswith(gcc):
                return True
        return False

    def __correct_gcc(self, command):
        items = command.split()
        items[0] = self.prefix + 'gcc'
        return ' '.join(items)

    def __adjuct_to_preprocess(self, command):
        items = command.split()
        items[-2] = items[-2].replace('.o', '.i')
        items[-4] = '-E'
        return ' '.join(items)

    def preprocess(self, path, cmdline=None):
        """
        preprocess('arch/arm/mm/proc-xxx.c')
        """
        if self.makeout is None:
            return

        command = None
        target = os.path.basename(path)
        with open(self.makeout) as f:
            for line in f:
                if not self.__has_gcc(line):
                    continue
                if line.strip().endswith(target):
                    command = line
                    break
        if command is None:
            if cmdline is not None:
                command = cmdline
            else:
                return None

        command = self.__correct_gcc(command)
        command = self.__adjuct_to_preprocess(command)
        status = self.run(command)
        if status == 0:
            return path.replace('.c', '.i')
        else:
            return None

        return funccalls

    def __get_funccalls_by_sparse(self, path, funcname):
        path = os.path.join(self.srcode, path)
        output = os.popen('graph {}'.format(path)).readlines()
        output = ''.join(output)

        graphs = pydot.graph_from_dot_data(output)
        assert len(graphs) == 1, 'something wrong in graph'
        graph = graphs[0]

        # 1st, find the subgraph you want to analyze
        eps = {}
        cfg = None
        for subgraph in graph.get_subgraph_list():
            attributes = subgraph.get_attributes()
            if attributes['fun'].strip('"') == funcname:
                cfg = subgraph
            eps[attributes['ep']] = attributes['fun'].strip('"')
        if cfg is None:
            return []

        # 2nd, traverse the subgraph and log all nodes
        nodes = []
        for node in cfg.get_node_list():
            nodes.append(node.get_name())

        # 3rd, find callgraph edge by nodes we logged
        funccalls = []
        for edge in graph.get_edge_list():
            if edge.get_source() in nodes:
                if edge.get_attributes()['op'] == 'call':
                    funccalls.append(eps[edge.get_destination()])
                else:
                    funccalls.append(edge.get_destination().strip('"'))

        return funccalls

    def __get_funccalls_by_llvm(self, path, funcname):
        pass

    def get_funccalls(self, path, funcname, mode='sparse'):
        if self.sparse and mode == 'sparse':
            return self.__get_funccalls_by_sparse(path, funcname)
        elif self.llvm and mode == 'kerberos':
            return self.__get_funccalls_by_kerberos(path, funcname)
        return []

