"""
source code controller
"""
from settings import *
from logger import logger_info
from pycparser import c_parser, c_ast, parse_file

import os
import qmp
import subprocess

BACKUP, PATCH, COMPILE, LINK = 0, 1, 2, 3

class SRCodeController(object):
    def __init__(self, srcode, arch, prefix, cpu=4):
        self.srcode = srcode
        self.arch = arch
        self.prefix = prefix

        self.makeout = None
        self.cpu = cpu
        self.fake_defs =  [
            os.path.join(BASE_DIR, 'slcore/fake_typedefs.h'),
            os.path.join(BASE_DIR, 'slcore/fake_gnuext.h'),
        ]

    def fix_gnu_extensions(self, preprocessed_file):
        path = os.path.join(self.srcode, preprocessed_file)

        with open(path) as f:
            content = f.readlines()
        prepared_content = []
        for line in content:
            if line.startswith('#'):
                prepared_content.append(line)
                continue
            # syntax case ...
            # case '0' ... '7':
            line = line.replace('case \'0\' ... \'7\':', 'case \'0\':')
            # builtin keywords
            line = line.replace('__inline__', '')
            line = line.replace('volatile', '')
            line = line.replace('asm', '')
            import re
            # syntax {} implicit function
            # line = re.sub('do \{.*\} while \(0\)', '', line)
            line = line.replace('({', '{').replace('})', '}')
            line = line.replace('= ({', '= 0; ({')
            # res = { int __res; if (0 == 0)  ; else  ; __res;  }
            line = re.sub('res = \{ int __res; if \(\d == 0\)  ; else  ; __res; \}', 'res = 0', line)
            # res = { int __res;  ; __res; }
            line = re.sub('res = \{ int __res;  ; __res; \}', 'res = 0', line)
            # *remainder = { };
            line = re.sub('\*remainder = \{.*\}', '', line)
            # struct idr_layer *hint = { };
            line = re.sub('struct idr_layer \*hint = \{.*\};', 'struct idr_layer *hint = 0;', line)
            line = line.replace('= { int', '= 0; {')
            line = re.sub('\{ void.*\}', '0', line)
            # ((pte).pte) |= {BUG(); 1; };
            line = line.replace('{BUG(); 1; }', '0')
            # { int __res; if (0 == 0)  ; else  ; __res; }
            line = line.replace('{ int __res; if (0 == 0)  ; else  ; __res; }', '0')
            line = line.replace('0 ...', '')
            # (current_thread_info()->task)->thread.fpu.fcr31 =
            line = line.replace(
                '(current_thread_info()->task)->thread.fpu.fcr31 =',
                '(current_thread_info()->task)->thread.fpu.fcr31 = 0')
            # timer->node.expires = { (ktime_t){ .tv64 = (timer->node.expires).tv64 + (ns) }; };
            line = line.replace(
                'timer->node.expires = { (ktime_t){ .tv64 = (timer->node.expires).tv64 + (ns) }; };',
                'timer->node.expires = (ktime_t){ .tv64 = (timer->node.expires).tv64 + (ns) };')
            # timer->_softexpires = { (ktime_t){ .tv64 = (timer->_softexpires).tv64 + (ns) }; };
            line = line.replace(
                'timer->_softexpires = { (ktime_t){ .tv64 = (timer->_softexpires).tv64 + (ns) }; };',
                'timer->_softexpires = (ktime_t){ .tv64 = (timer->_softexpires).tv64 + (ns) }; ')
            line = re.sub('= { unsigned.*?\}', '0', line)
            # {unsigned long __ms=(100); while (__ms--) __udelay(1000);}
            line = line.replace('{unsigned long __ms=(100); while (__ms--) __udelay(1000);}', '0')
            # struct platform_device_info pdevinfo = {
            line = line.replace(
                'struct platform_device_info pdevinfo = 0; {',
                'struct platform_device_info pdevinfo = {')
            line = line.replace(' return {', ' return 0; {')
            line = re.sub('\(\{.*?\}\)', '(0)', line)
            line = re.sub('; \{.*\}', '', line)
            line = re.sub('\? \{.*\}', '? 0', line)
            line = re.sub('^\s*\{.*\};', ';', line)
            line = re.sub('& \{.*?\}', '& 0', line)
            # ((32) & 31))) } };
            line = line.replace('((32) & 31))) } };', '((32) & 31))) } });')
            # { __label__ __here; __here: (unsigned long)&&__here;  }
            line = line.replace('{ __label__ __here; __here: (unsigned long)&&__here; }', '0')
            # ((unsigned long){ void *_________p1 = (void *)(*( void *)&((h->first))); do { } while (0); ; do { } while(0); ((void *)(_________p1)); } & ~0UL);
            line = line.replace(
                '((unsigned long){ void *_________p1 = (void *)(*( void *)&((h->first))); do { } while (0); ; do { } while(0); ((void *)(_________p1)); } & ~0UL)', '0')
            # ( { void quot = (val) / (100); void rem = (val) % (100); (quot * (sysctl_vfs_cache_pressure)) + ((rem * (sysctl_vfs_cache_pressure)) / (100)); } )
            line = line.replace(
                '( { void quot = (val) / (100); void rem = (val) % (100); (quot * (sysctl_vfs_cache_pressure)) + ((rem * (sysctl_vfs_cache_pressure)) / (100)); } )',
                '0')
            # ? 1 : { do { do { } while (0); arch_local_irq_enable(); } while (0); 0; };
            line = line.replace(
                '? 1 : { do { do { } while (0); arch_local_irq_enable(); } while (0); 0; };',
                '? 1 : 0;')
            # (struct semaphore) { .lock = (raw_spinlock_t) { .raw_lock = 0;
            line = line.replace(
                '(struct semaphore) { .lock = (raw_spinlock_t) { .raw_lock = 0;',
                '(struct semaphore) { .lock = (raw_spinlock_t) { .raw_lock = 0}};'
            )
            # return 0; } } __cu_len; } ? -14 : 0;
            line = line.replace(
                'return 0; } } __cu_len; } ? -14 : 0;',
                'return 0;'
            )
            # projid_eq(projid, (kprojid_t){ -1 };
            line = line.replace(
                'projid_eq(projid, (kprojid_t){ -1 };',
                'projid_eq(projid, (kprojid_t){ -1 });'
            )
            # return !uid_eq(uid, (kuid_t){ -1 };
            line = line.replace('(uid, (kuid_t){ -1 }', '(uid, (kuid_t){ -1 })')
            # return !gid_eq(gid, (kgid_t){ -1 };
            line = line.replace('(gid, (kgid_t){ -1 }', '(kid, (kgid_t){ -1 })')
            # do { *(&rs->lock) = (raw_spinlock_t) { .raw_lock = 0; } while (0);
            line = line.replace(
                'do { *(&rs->lock) = (raw_spinlock_t) { .raw_lock = 0; } while (0);',
                'do { *(&rs->lock) = 0; } while (0);')
            # ((((mm_segment_t) { 0UL })).seg))
            line = line.replace('((((mm_segment_t) { 0UL })).seg)', '0)')
            # syntax typeof() * implicit pointer type
            # (*(volatile typeof(s->sequence) *)&(s->sequence))
            line = line.replace('volatile typeof', 'typeof')
            line = line.replace(' *)&(', ')&(')
            line = line.replace(') *)(', '))(')
            # unsigned long __dummy; typeof(flags) __dummy2;
            line = re.sub(
                'unsigned long __dummy; typeof\(.*?\) __dummy2',
                'unsigned long __dummy; void* __dummy2', line)
            # ((typeof(*(&head->first))) __xchg()
            line = re.sub('\(typeof\(.*?\)\) __xchg', '__xchg', line)
            line = re.sub('typeof\(.*?\) __ptr', '__ptr', line)
            line = re.sub('typeof\(.*?\) __old', '__old', line)
            line = re.sub('typeof\(.*?\) __new', '__new', line)
            line = re.sub('typeof\(.*?\) __res', '__res', line)
            line = re.sub('typeof\(.*?\) __ret', '__ret', line)
            prepared_content.append(line)

        with open(path, 'w') as f:
            f.writelines(prepared_content)

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
        # items.insert(-4, '-U__GNUC__')
        for fake_def in self.fake_defs:
            items.insert(-4, '-include{}'.format(fake_def))
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

    def __traverse(self, body, funccalls):
        if isinstance(body, c_ast.Compound):
            for block in body.block_items:
                self.__traverse(block, funccalls)
        elif isinstance(body, c_ast.FuncCall):
            funccalls.append(body.name.name)
            self.__traverse(body.args, funccalls)
        elif isinstance(body, c_ast.If):
            self.__traverse(body.cond, funccalls)
            self.__traverse(body.iftrue, funccalls)
            self.__traverse(body.iffalse, funccalls)
        elif isinstance(body, c_ast.DoWhile) or \
                isinstance(body, c_ast.While):
            self.__traverse(body.stmt, funccalls)
        elif isinstance(body, c_ast.Case):
            for stmt in body.stmts:
                self.__traverse(stmt, funccalls)
        elif isinstance(body, c_ast.Decl):
            self.__traverse(body.init, funccalls)
        elif isinstance(body, c_ast.Switch):
            self.__traverse(body.stmt, funccalls)
        elif isinstance(body, c_ast.Assignment):
            self.__traverse(body.lvalue, funccalls)
            self.__traverse(body.rvalue, funccalls)
        elif isinstance(body, c_ast.BinaryOp):
            self.__traverse(body.left, funccalls)
            self.__traverse(body.right, funccalls)
        elif isinstance(body, c_ast.Default):
            for stmt in body.stmts:
                self.__traverse(stmt, funccalls)
        elif isinstance(body, c_ast.ExprList):
            for expr in body.exprs:
                self.__traverse(expr, funccalls)
        elif isinstance(body, c_ast.UnaryOp):
            self.__traverse(body.expr, funccalls)
        elif isinstance(body, c_ast.Break):
            return
        elif isinstance(body, c_ast.Cast):
            return
        elif isinstance(body, c_ast.EmptyStatement):
            return
        elif isinstance(body, c_ast.ID):
            return
        elif isinstance(body, c_ast.Constant):
            return
        elif isinstance(body, c_ast.StructRef):
            return
        elif isinstance(body, c_ast.Return):
            return
        elif body is None:
            return
        else:
            print(body)

    def traverse_func(self, path, funcname):
        path = os.path.join(self.srcode, path)
        ast = parse_file(path)

        funccalls = []
        for node in ast.ext:
            if not isinstance(node, c_ast.FuncDef):
                continue
            if node.decl.name != funcname:
                continue
            body = node.body
            self.__traverse(body, funccalls)

        return funccalls

