import os
import pydot

from slcore.amanager import Analysis
from slcore.srcskiplist import UNMODELED_SKIP_LIST
from slcore.srcfcbs import generic_fcbs


dirs_blacklist = [
    'include', '.pc', 'samples', 'patches', 'user_headers', 'tools',
    'Documentation', 'usr', 'scripts', 'virt'
]


class TraverseKernel(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'ktraversal'
        self.description = 'Linux kernel source code traversal.'

        self.full_graph = pydot.Dot(graph_type='digraph')
        self.source_code = None
        self.unknown_list = []
        self.unhandled_list = []
    
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
            for edge in subgraph.get_edges():
                if edge.get_source().strip('"') == src:
                    yield edge
    
    def walk_kernel(self, caller, fcbs={}, depth=0):
        for edge in self.get_edge(caller):
            dest = edge.get_destination().strip('"')
            if not self.parse_funccall(caller, dest, fcbs, depth=depth + 1):
                self.walk_kernel(dest, fcbs=fcbs, depth=depth + 1)

    def parse_funccall(self, caller, funccall, fcbs, depth):
        if funccall in UNMODELED_SKIP_LIST:
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
            self.info('{}|-{}->{}[intermediate]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            return False

        if 'handler' not in cbs:
            self.info('{}|-{}->{}[unhandled]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            self.unhandled_list.append(funccall)
            return False

        extend = []
        status = cbs['handler'](self, caller, extend=extend)
        if not status:
            self.info('{}|-{}->{}[unhandled]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
            self.unhandled_list.append(funccall)
            return False

        self.info('{}|-{}->{}[handled]'.format(' ' * 2 * (depth - 1), caller, funccall), 1)
        if not len(extend) > 0:
            return True

        for new_caller in extend:
            self.info('{}|-{}->{}[indirected]'.format(' ' * 2 * (depth + 1 - 1), funccall, new_caller), 1)
            self.walk_kernel(new_caller, fcbs=fcbs, depth=depth+1)
        return True

    def run(self, **kwargs):
        target_dirs = kwargs.pop('dirs')
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

        # load all symbols
        failed_cases = 0
        for root, dirs, files in os.walk(self.source_code):
            for f in files:
                if not f.endswith('.c') and not f.endswith('.S'):
                    continue
                absolute = os.path.join(root, f)
                relative = absolute[len(self.source_code) + 1:]

                if target_files:
                    if not self.is_in_files_whitelist(absolute, target_files):
                        continue
                else:
                    if self.is_in_dirs_blacklist(absolute):
                        continue
                    if target_dirs is not None and \
                            not self.is_in_dirs_whitelist(absolute, target_dirs):
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
        if entrypoint is None:
            entrypoint = 'start_kernel'
        self.walk_kernel(entrypoint, fcbs=generic_fcbs, depth=0)
        
        if failed_cases > 0:
            self.warning('{} failed cases'.format(failed_cases), 0)

        if len(self.unknown_list) > 0:
            self.info('You may add the unknown functions below to the skip list', 1)
            self.info(str(self.unknown_list), 1)

        if len(self.unhandled_list) > 0:
            self.info('You may add handlers for the functions below', 1)
            self.info(str(self.unhandled_list), 1)
        
        return True
