"""
source code controller
+ symbol2file, symbol2fileg
+ cmdline/preprocess/compile/link one file
+ cfg/cg/gloabls
"""
from slcore.common import Common
from slcore.naive_parsers.symbols import parse_system_map, addr2file
from slcore.srcodeb import UNMODELED_SKIP_LIST

import os
import pydot

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
        self.config = {}

    def symbol2fileg(self, symbol, relative=True):
        search_in = os.path.join(self.path_to_source_code, 'arch/{}'.format(self.arch))
        search_in2 = os.path.join(self.path_to_source_code, 'drivers')

        f = None

        lines = []
        with os.popen('find {} -name "*.c" | xargs grep " {}"'.format(search_in, symbol)) as o:
            lines = o.readlines()
        if not len(lines):
            with os.popen('find {} -name "*.c" | xargs grep " {}"'.format(search_in2, symbol)) as o:
                lines = o.readlines()

        if not len(lines):
            return f;

        for line in lines:
            # arch/mips/kernel/setup.c: * arch_mem_init -
            # arch/mips/kernel/setup.c:static void __init arch_mem_init(char **cmdline_p)
            # arch/mips/kernel/setup.c:       arch_mem_init(cmdline_p);
            fs, c = line.strip().split(':')[0:2]
            if c.strip().startswith('*'):
                continue
            if c.strip().endswith(';'):
                continue
            fs_o = fs[:-1] + 'o'
            if not os.path.exists(fs_o):
                continue
            f = os.path.realpath(fs)

        if f is None:
            return f
        if relative:
            return f[len(os.path.realpath(self.path_to_source_code)) + 1:]
        else:
            return f

    def symbol2file(self, symbol, relative=True):
        if self.system_map is None:
            path = os.path.join(self.path_to_source_code, 'System.map')
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
        full_path = os.path.join(self.path_to_source_code, path)
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
        os.chdir(self.path_to_source_code)
        status = os.system(command + '>/dev/null 2>&1')
        os.chdir(cwd)
        return status

    def __has_gcc(self, line):
        gcc = [os.path.basename(self.path_to_cross_compile) + 'gcc', 'ccache_cc']

        items = line.split()
        if not len(items):
            return

        for i in gcc:
            if line.split()[0].endswith(i):# or line.split()[1].endswith(gcc):
                return True
        return False

    def __correct_gcc(self, command):
        items = command.split()
        items[0] = self.path_to_cross_compile + 'gcc'
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
        pathi = os.path.join(self.path_to_source_code, path).replace('.c', '-i')
        if os.path.exists(pathi):
            return path.replace('.c', '.i')
        if self.path_to_makeout is None:
            return

        command = None
        target = path
        with open(self.path_to_makeout) as f:
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

    def __get_graph(self, path):
        with os.popen('graph {} 2>/dev/null'.format(path)) as o:
            output= o.readlines()
        output = ''.join(output)

        graphs = pydot.graph_from_dot_data(output)
        assert len(graphs) == 1, 'something wrong in graph'
        return graphs[0]

    def __get_funccalls_by_sparse(self, path, funcname):
        path = os.path.join(self.path_to_source_code, path)
        graph = self.__get_graph(path)

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

    def __get_globals_by_sparse(self, path, funcname):
        path = os.path.join(self.path_to_source_code, path)
        graph = self.__get_graph(path)

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

        gs = {}
        def store(g):
            if g not in gs:
                gs[g] = []
            gs[g].append('store')

        def load(g):
            if g not in gs:
                gs[g] = []
            gs[g].append('load')

        # 2nd, traverse the subgraph and log all reading/writing operations
        for node in cfg.get_node_list():
            # 'ls': '"[ store(ath79_ip2_handler), store(ath79_ip3_handler) ]"'
            # '"[ store('ath79_ip2_handler'), store('ath79_ip3_handler') ]"'
            attrs = node.get_attributes()
            if 'ls' in attrs:
                eval(attrs['ls'].strip('"').replace('(', '(\'').replace(')', '\')'))

        return gs

    def parse_funcalls2(self, caller, funccalls, fcbs={}, depth=0):
        def remove_duplicated(seq):
                seen = set()
                seen_add = seen.add
                return [x for x in seq if not (x in seen or seen_add(x))]
        funccalls = remove_duplicated(funccalls)

        # remove functions we donot want to analyze
        for da in UNMODELED_SKIP_LIST:
            if da in funccalls:
                funccalls.remove(da)

        unhandled = []
        for f, cbs in fcbs.items():
            if f in funccalls:
                funccalls.remove(f)
                if cbs['ignored']:
                    self.info('ana_funccalls2', '{}{}->{}({})({})'.format('->' * (depth+1), caller, f, 'ignored', None), 0)
                    continue
                if caller in cbs:
                    ext = cbs[caller](self.config)
                    unhandled.extend(ext)
                    self.info('ana_funccalls2', '{}{}->{}({})({})'.format('->' * (depth+1), caller, f, 'handled', None), 0)
                else:
                    self.info('ana_funccalls2', '{}{}->{}({})({})'.format('->' * (depth+1), caller, f, 'unhandled', None), 0)
        funccalls.extend(unhandled)

        return funccalls

    def parse_globals2(self, caller, gs, depth=0):
        """
        Globals will not trigger analysis but serve for debugging.
        Global data/function pointer both will influence execution flow.
        Global data is interesting when
        1) it is defined by the value from nvram
        2) it is defined by the value from ioremap().
        Global data is interesting when
        1) it is defined conditionally
        2) it is defined according to CMDLINE
        """
        for g, ops in gs.items():
            pass
            # if 'store' in ops:
                # self.globals.append(g)
                # self.debug(firmware, '{} -> {}(global defined)'.format(caller, g), 1)
                # pass
            # if 'load' in ops and g not in self.globals:
                # self.warning(firmware, '{} -> {}(global used before defined)'.format(caller, g), 1)
                # pass

    def traverse_funccalls2(self, entry_point, caller=None, depth=0, fcbs={}):
        for ep in entry_point:
            path_to_ep, funccalls, gs, error_info = self.get_funccalls2(ep, caller=caller, depth=depth)

            if error_info is not None:
                self.info('get_funccalls2', '{}{}->{}({})({})'.format('->' * depth, caller, ep, error_info, path_to_ep), 0)
                continue

            if gs is not None:
                self.parse_globals2(ep, gs)
            if funccalls is not None:
                funccalls = self.parse_funcalls2(ep, funccalls, fcbs=fcbs, depth=depth)
                self.traverse_funccalls2(funccalls, caller=ep, depth=depth+1, fcbs=fcbs)

    def get_funccalls2(self, ep, caller='do_initcall', depth=0):
        # return path_to_entry_point, funccalls, gs, error_info
        path_to_entry_point = self.symbol2file(ep)
        if path_to_entry_point is None:
            path_to_entry_point = self.symbol2fileg(ep)
        if path_to_entry_point is None:
            return None, None, None, 'no address'

        d = path_to_entry_point.split('/')
        if path_to_entry_point.startswith('fs') or \
                path_to_entry_point.startswith('lib') or \
                path_to_entry_point.startswith('mm') or (len(d) > 2 and d[2] in ['fw']):
            return path_to_entry_point, None, None, 'built-in function'

        if path_to_entry_point.endswith('.S'):
            return path_to_entry_point, None, None, 'assembly file'

        if path_to_entry_point.endswith('.h'):
            path_to_entry_point = self.symbol2fileg(ep)
            if path_to_entry_point is None:
                return path_to_entry_point, None, None, 'inline in header'

        cmdline = self.get_cmdline(path_to_entry_point)
        path_to_pentry_point = self.preprocess(path_to_entry_point, cmdline=cmdline)
        if path_to_pentry_point is None:
            return None, None, None, 'error in preprocessing'

        funccalls = self.get_funccalls(path_to_pentry_point, ep, mode='sparse')
        gs = self.get_globals(path_to_pentry_point, ep, mode='sparse')
        self.info('get_funccalls2', '{}{}->{}({})({})'.format('->' * depth, caller, ep, None, path_to_entry_point), 0)

        return path_to_entry_point, funccalls, gs, None


    def get_funccalls(self, path, funcname, mode='sparse'):
        """
        This function takes a preprocessed file as input and return external function
        calls in a given function.
        """
        if self.sparse and mode == 'sparse':
            return self.__get_funccalls_by_sparse(path, funcname)
        return []

    def get_globals(self, path, funcname, mode='sparse'):
        """
        This function takes a preprocessed file as input and return global reading/writing
        states in a given function.
        """
        if self.sparse and mode == 'sparse':
            return self.__get_globals_by_sparse(path, funcname)
        return {}


