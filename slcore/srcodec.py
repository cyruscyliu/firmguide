"""
source code controller
"""
from settings import *
from logger import logger_info
from pycparser import c_parser, c_ast, parse_file
from slcore.compositor import Common
from slcore.naive_parsers.symbols import parse_system_map, addr2file

import os
import qmp
import pydot
import subprocess

BACKUP, PATCH, COMPILE, LINK = 0, 1, 2, 3

SOURCE_CODE_ATTRIBUTES = [
    'path_to_source_code', 'path_to_cross_compile',
    'path_to_makeout', 'arch', 'endian', 'path_to_vmlinux',
    'system_map', 'path_to_dot_config'
]

class SRCodeController(Common):
    def __init__(self):
        super().__init__()
        # mode
        self.sparse = not os.system('which graph >/dev/null')

        self.set_attributes(SOURCE_CODE_ATTRIBUTES)

    def symbol2file(self, symbol, relative=True):
        if self.system_map is None:
            path = os.path.join(self.srcode, 'System.map')
            self.system_map = parse_system_map(path)

        if symbol in self.system_map:
            address = self.system_map[symbol]['addr']
        else:
            return None

        f = addr2file(self.path_to_vmlinux, address)

        if f is None:
            return None
        if relative:
            return f[len(os.path.realpath(self.path_to_source_code)) + 1:]
        else:
            return f

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

    def get_funccalls(self, path, funcname, mode='sparse'):
        if self.sparse and mode == 'sparse':
            return self.__get_funccalls_by_sparse(path, funcname)
        return []

