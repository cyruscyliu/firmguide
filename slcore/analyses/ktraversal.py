import os
import pydot

from slcore.amanager import Analysis
from slcore.srcskiplist import UNMODELED_SKIP_LIST


generic_fcbs = {
    'plat_irq_dispatch': {'ignored': True},
    'of_irq_init': {'ignored': False},
    'irq_set_chip_and_handler_name': {'ignored': False},
    'irq_set_chained_handler_and_data': {'ignored': False},
    'irq_domain_add_legacy': {'ignored': False},
    '__irq_domain_add': {'ignored': False},
    'panic': {'ignored': True},
    'r4k_clockevent_init': {'ignored': True},
    'init_r4k_clocksource': {'ignored': True},
    'mips_cpu_irq_init': {'ignored': True},
    '__irq_set_handler': {'ignored': False},
    'irq_domain_add_simple': {'ignored': False},
    'of_clk_init': {'ignored': True},
    'set_handle_irq': {'ignored': False},
}

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
    
    def is_in_dirs_blacklist(self, root):
        for db in dirs_blacklist:
            if root.startswith(os.path.join(self.source_code, db)):
                return True
        return False
    
    def get_funccall_graph(self, path):
        with open.popen('{}/traverse {} 2>/dev/null'.format(
                self.project.attrs['sparse_dir'], path)) as o:
            output = o.readlines()
        output = ''.join(output)

        graphs = pydot.graph_from_dot_data(output)
        assert len(graphs) == 1, 'something wrong in graph'
        return graphs[0]
    
    def walk_kernel(self, caller, fcbs={}, depth=0):
        for edge in self.graph.get_edge(caller):
            dest = edge.get_destination()
            self.parse_funcall(caller, funccall, fcbs, depth+=1)
            self.walk_kernel(dest, fcbs=fcbs, depth+=1)

    def parse_funccall(self, caller, funccall, fcbs, depth):
        # ignore functions we donot want to analyze
        if funccall in UNMODELED_SKIP_LIST:
            return True

        if funccall not in fcbs:
            return False
        
        cbs = fcsb[funccall]
        if cbs['ignored']:
            # self.info('ana_funccalls2', '{}{}->{}({})({})'.format('->' * (depth+1), caller, f, 'ignored', None), 0)
            return True
        if caller in cbs:
            ext = cbs[caller](self.config)
            unhandled.extend(ext)
            self.info('ana_funccalls2', '{}{}->{}({})({})'.format('->' * (depth+1), caller, f, 'handled', None), 0)
        else:
            self.info('ana_funccalls2', '{}{}->{}({})({})'.format('->' * (depth+1), caller, f, 'unhandled', None), 0)
        return funccalls

    def run(self, **kwargs):
        target_dirs = kwargs.pop('dirs')

        # We simply preprocess the c file containing
        # the entry point if no other arguments assigned.
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False
        self.source_code = os.path.realpath(srcodec.get_path_to_source_code())

        # load all symbols
        failed_cases = 0
        for root, dirs, files in os.walk(source_code):
            for f in files:
                if self.is_in_dirs_blacklist(source_code, root):
                    continue
                if not f.endswith('.c') and not f.endswith('.S'):
                    continue
                relative = os.path.join(root, f)[len(source_code) + 1:]
                cmdline = srcodec.get_cmdline(relative)
                if cmdline is None:
                    continue
                fp = srcodec.preprocess(relative, cmdline=cmdline)
                if fp is None:
                    failed_cases += 1
                    continue
                graph = self.get_funccall_graph()
                for subgraph in graph.get_subgraph_list():
                    full_graph.add_subgraph(subgraph)

        # walk kernel
        self.walk_kernel('start_kernel', fcbs=generic_fcbs, depth=0)
        
        if failed_cases > 0:
            self.warning('{} failed cases'.format(failed_cases), 0)
        
        return True