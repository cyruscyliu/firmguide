import os
import pydot
import yaml

from slcore.amanager import Analysis
from slcore.analyses.ktraversalaux import funccalls_blacklist, \
        dirs_blacklist, files_whitelist
from slcore.analyses.ktraversalfcbs import generic_fcbs, \
        generic_slicing_handler, generic_indirect_call_handler


class TraverseKernel(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'ktraversal'
        self.description = 'Linux kernel source code traversal.'
        self.required = ['bfilter']

        self.full_graph = pydot.Dot(graph_type='digraph')
        self.source_code = None
        self.unknown_list = []
        self.unhandled_list = []
        self.pos = {'file': None, 'fun': None, 'line': None}
        self.slicing = {}
        self.last_user_fcbs = 0
        self.user_fcbs = {}
    
    def is_in_dirs_blacklist(self, root):
        for db in dirs_blacklist:
            if root.startswith(os.path.join(self.source_code, db)):
                return True
        return False

    def is_in_dirs_whitelist(self, root, dirs):
        for dw in dirs:
            if root.startswith(os.path.join(self.source_code, dw)):
                return True
        return False

    def is_in_files_whitelist(self, path, files):
        for fw in files:
            if path.endswith(fw):
                return True
        return False
    
    def get_funccall_graph(self, path):
        with os.popen('{}/traverse {} 2>/dev/null'.format(
                self.analysis_manager.project.attrs['sparse_dir'],
                os.path.join(self.source_code, path))) as o:
            output = o.readlines()
        output = ''.join(output)

        graphs = pydot.graph_from_dot_data(output)
        assert len(graphs) == 1, 'something wrong in graph'
        return graphs[0]

    def get_edge(self, src):
        for subgraph in self.full_graph.get_subgraphs():
            self.pos['file'] = subgraph.get_attributes()['file']
            self.pos['fun'] = subgraph.get_attributes()['fun']
            for edge in subgraph.get_edges():
                if edge.get_source().strip('"') == src:
                    # TODO
                    # self.pos['line'] = edge.get_attributes()['line']
                    self.pos['label'] = edge.get_attributes()['label']
                    yield edge
    
    def walk_kernel(self, caller, fcbs={}, depth=0):
        for edge in self.get_edge(caller):
            dest = edge.get_destination().strip('"')
            if not self.parse_funccall(caller, dest, fcbs, depth=depth + 1):
                self.walk_kernel(dest, fcbs=fcbs, depth=depth + 1)

    def parse_funccall(self, caller, funccall, fcbs, depth):
        if funccall in funccalls_blacklist:
            if self.show_skipped_functions:
                self.info('{}|-{}->{}[skip]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            return True

        if funccall not in fcbs:
            self.unknown_list.append(funccall)
            self.info('{}|-{}->{}[unknown]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            return False
        
        cbs = generic_fcbs[funccall]
        if 'ignored' in cbs and cbs['ignored']:
            self.info('{}|-{}->{}[ignored]'.format(' ' * 2 *  (depth - 1), caller, funccall), 1)
            return True
        if 'intermediate' in cbs and cbs['intermediate']:
            self.info('{}|-{}->{}'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            return False

        if 'handler' not in cbs:
            self.info('{}|-{}->{}[unhandled]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            self.unhandled_list.append(funccall)
            return False

        extend = []
        status = cbs['handler'](self, funccall, caller, extend=extend, pos=self.pos)
        if not status:
            self.info('{}|-{}->{}[unhandled]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            self.unhandled_list.append(funccall)
            return False

        if not len(extend) > 0:
            self.info('{}|-{}->{}[sliced]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            return True
        self.info('{}|-{}->{}[indirect call]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)

        for new_caller in extend:
            if new_caller in funccalls_blacklist:
                if self.show_skipped_functions:
                    self.info('{}|-{}->{}[skip]'.format(' ' * 2 * (depth - 1), funccall, new_caller), 1)
                continue
            if new_caller not in fcbs:
                self.unknown_list.append(new_caller)
            self.info('{}|-{}->{}[intermediate]'.format(' ' * 2 * (depth + 1 - 1), funccall, new_caller), 1)
            self.walk_kernel(new_caller, fcbs=fcbs, depth=depth+1)
        return True
    
    def dump_slicing(self):
        target = os.path.join(self.analysis_manager.project.attrs['path'], '.slicing')
        with open(target, 'w') as f:
            yaml.safe_dump(self.slicing, f)
        self.info('slicing info saved as {}'.format(target), 1)

    def run(self, **kwargs):
        target_dirs = kwargs.pop('dirs')  # dirs_whitelist
        entrypoint = kwargs.pop('entry_point')
        target_files = kwargs.pop('file')
        self.show_skipped_functions = kwargs.pop('all')

        # We simply preprocess the c file containing
        # the entry point if no other arguments assigned.
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False
        self.source_code = os.path.realpath(srcodec.get_path_to_source_code())
        if srcodec.path_to_cross_compile is None:
            self.error_info = 'please set the cross compile prefix'
            return False

        board = self.analysis_manager.firmware.get_board() # decided in bfilter
        arch = self.analysis_manager.firmware.get_arch() # decided in bfilter
        a_a_b = 'arch/{}/{}'.format(arch, board)
        self.info('-d {} automatically by bfilter'.format(board), 1)
        if target_dirs is None:
            target_dirs = [a_a_b]
        else:
            target_dirs.append(a_a_b)

        self.load_user_fcbs()
        self.update_generic_fcbs()

        # load all symbols
        failed_cases = 0
        for root, dirs, files in os.walk(self.source_code):
            for f in files:
                if not f.endswith('.c') and not f.endswith('.S'):
                    continue
                absolute = os.path.join(root, f)

                relative = absolute[len(self.source_code) + 1:]

                allowed = True
                if self.is_in_dirs_blacklist(absolute):
                    allowed = False
                if not self.is_in_files_whitelist(absolute, files_whitelist):
                    allowed = False
                if target_files is not None and \
                        self.is_in_files_whitelist(absolute, target_files):
                    allowed = True
                if target_dirs is not None and \
                        self.is_in_dirs_whitelist(absolute, target_dirs):
                    allowed = True

                if not allowed:
                    self.debug('relative {} is not allowed'.format(relative), 0)
                    continue

                cmdline = srcodec.get_cmdline(relative)
                if cmdline is None:
                    continue
                fp = srcodec.preprocess(relative, cmdline=cmdline)
                if fp is None:
                    failed_cases += 1
                    continue
                graph = self.get_funccall_graph(fp)
                for subgraph in graph.get_subgraph_list():
                    self.full_graph.add_subgraph(subgraph)
                self.info('[done] {}'.format(relative), 1)

        # walk kernel
        # load all customized configs
        if entrypoint is None:
            entrypoint = 'start_kernel'
        self.walk_kernel(entrypoint, fcbs=generic_fcbs, depth=0)
        
        if failed_cases > 0:
            self.warning('{} failed cases'.format(failed_cases), 0)

        if len(self.unknown_list) > 0:
            self.info('update unknown functions in {}.fcbs'.format(self.last_user_fcbs), 1)
            user_fcbs = {}
            for unknown_func in list(set(self.unknown_list)):
                user_fcbs[unknown_func] = {
                    'skipped': False,
                    'extend': [],
                }
            yaml.safe_dump(user_fcbs, open('{}.fcbs'.format(self.last_user_fcbs), 'w'))
        if len(self.unhandled_list) > 0:
            self.info('You may add handlers for the functions below', 1)
            self.info(str(list(set(self.unhandled_list))), 1)

        self.info('Please -a to check intermediate functions whether they are visited', 1)
        self.info('Otherwise, you should add file(s)/dir(s) that contain those functions', 1)

        self.dump_slicing()
        return True
    
    def load_user_fcbs(self):
        for i in range(0, 100):
            if not os.path.exists('{}.fcbs'.format(i)):
                continue
            user_fcbs_i = yaml.safe_load(open('{}.fcbs'.format(i)))
            for k, v in user_fcbs_i.items():
                if 'skipped' in v and v['skipped']:
                    self.user_fcbs[k] = {'ignored': True}
                    continue
                if 'extend' in v and len(v['extend']) != 0:
                    self.user_fcbs[k] = {'handler': generic_indirect_call_handler, 'extend': v['extend']}
                    continue
                self.user_fcbs[k] = {'handler': generic_slicing_handler}
            self.info('load {}.fcbs'.format(i), 1)
            self.last_user_fcbs = i + 1

    def update_generic_fcbs(self):
        for k, v in self.user_fcbs.items():
            generic_fcbs[k] = v
