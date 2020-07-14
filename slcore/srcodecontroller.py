"""
source code controller
+ symbol2file, symbol2fileg
+ cmdline/preprocess/compile/link one file
+ cfg/cg/gloabls
"""
from slcore.common import Common

import os

BACKUP, PATCH, COMPILE, LINK = 0, 1, 2, 3

SOURCE_CODE_ATTRIBUTES = [
    'path_to_source_code', 'path_to_cross_compile',
    'path_to_makeout', 'arch', 'endian', 'path_to_vmlinux',
    'system_map', 'path_to_dot_config'
]


def load_system_map(path, bits=32):
    """Parse system map, get the address/size, the type, and the symbol in the lines.

    Example: ffffffff803687e8 00000008 T arch_init_irq

    Args:
        path(str): path: The path to the System.map.
        bit(int) : How many bits of an address, default is 32.

    Returns:
        dict: The dict with symbols as keys, like {__start: {'addr': 0x00000000, 'type': T}}
    """
    system_map = {}

    if bits == 32:
        mask = 0xffffffff
    else:
        mask = 0xffffffffffffffff >> (64 - bits)

    os.system('nm -S {0}/vmlinux > /tmp/system.map.nms'.format(path))

    with open('/tmp/system.map.nms') as f:
        for line in f:
            items = line.strip().split()
            if len(items) == 3:
                addr, t, sym = items
                size = '0'
            elif len(items) == 4:
                addr, size, t, sym = items
            else:
                continue
            system_map[sym] = {
                'addr': int(addr, 16) & mask,
                'size': int(size, 16),
                'type': t}
    return system_map


def addr2file(path, address):
    """Find the file according to the address.

    A wrapper of addr2line.

    Args:
        path(str)   : The path to the binary.
        address(str): The address you want to watch.

    Returns:
        str: The path w.s.t the address.
    """
    # /abs/path/to/x.c:69
    with os.popen('addr2line -e {} {}'.format(path, hex(address))) as o:
        output = o.readlines()
    if not len(output):
        return None
    assert len(output) == 1

    if output[0].startswith('??'):
        return None

    f, _ = output[0].split(':')
    f = os.path.realpath(f)

    return f


class SRCodeController(Common):
    def __init__(self):
        super().__init__()
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
            return f

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
            realsource = os.path.realpath(self.path_to_source_code)
            if f[:6] != realsource[:6]:
                self.warning('addr2file', 'maybe you should use sudo?', 0)
            return f[len(realsource) + 1:]
        else:
            return f

    def address2symbol(self, address):
        if self.system_map is None:
            self.system_map = load_system_map(self.path_to_source_code)

        for k, v in self.system_map.items():
            symbols = []
            if v['addr'] <= address <= v['addr'] + v['size']:
                symbols.append(k)
            if len(symbols):
                return ','.join(symbols)
        return None

    def symbol2file(self, symbol, relative=True):
        if self.system_map is None:
            self.system_map = load_system_map(self.path_to_source_code)

        if symbol in self.system_map:
            address = self.system_map[symbol]['addr']
        else:
            return None

        f = addr2file(self.path_to_vmlinux, address)

        if f is None:
            return None
        if relative:
            realsource = os.path.realpath(self.path_to_source_code)
            if f[:6] != realsource[:6]:
                self.warning('addr2file', 'maybe you should use sudo?', 0)
            return f[len(realsource) + 1:]
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
        
        command = None
        if cmdline is not None:
            command = cmdline
        else:
            if self.path_to_makeout is not None:
                target = path
                with open(self.path_to_makeout) as f:
                    for line in f:
                        if not self.__has_gcc(line):
                            continue
                        if line.strip().endswith(target):
                            command = line
                            break
        if command is None:
            return None

        command = self.__correct_gcc(command)
        command = self.__adjuct_to_preprocess(command)
        status = self.run(command)
        if status == 0:
            return path.replace('.c', '.i')
        else:
            return None

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

def get_srcodecontroller(source, cross_compile, arch, endian, makeout=None):
    srcodec = SRCodeController()

    srcodec.set_path_to_source_code(source)
    if source is not None:
        srcodec.set_path_to_vmlinux(os.path.join(source, 'vmlinux'))
        srcodec.set_path_to_dot_config(os.path.join(source, '.config'))
        srcodec.supported = True
    else:
        srcodec.supported = False
    srcodec.set_path_to_cross_compile(cross_compile)
    srcodec.set_arch(arch)
    srcodec.set_endian(endian)
    srcodec.set_path_to_makeout(makeout)
    return srcodec