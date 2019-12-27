from analyses.analysis import Analysis, AnalysisGroup
from supervisor.logging_setup import logger_info, logger_warning
from supervisor.save_and_restore import finished, finish

from analyses.diag_check import Checking
from analyses.diag_dead_loop import DeadLoop
from analyses.diag_trace import DoTracing
from analyses.diag_init_value import InitValue

from analyses.inf_device_tree import DeviceTree
from analyses.inf_dot_config import DotConfig
from analyses.inf_extraction import Extraction
from analyses.inf_format import Format
from analyses.inf_kernel import Kernel
from analyses.inf_openwrt import OpenWRTRevision, OpenWRTURL, OpenWRTToH
from analyses.inf_srcode import SRCode
from analyses.inf_strings import Strings
from analyses.inf_ram import AbeliaRAM


class AnalysesManager(object):
    def __init__(self, firmware):
        self.firmware = firmware
        self.analyses_flat = {}  # name:analysis
        self.analyses_forest = {}  # analysis blocks
        self.analyses_remaining = {}  # name:analysis
        self.last_analysis_status = True

        self.static_analysis = None
        self.dynamic_analysis = None

    @staticmethod
    def find_analysis_in_tree(analyses_tree, analysis):
        to_add = [analysis.name]
        to_add.extend(analysis.required)
        for key in analyses_tree.keys():
            if key in to_add:
                return True
        for value in analyses_tree.values():
            if value in to_add:
                return True
        return False

    def new_analyses_tree(self):
        """
        :return: the name of an anlyses tree
        """
        analyses_tree = 'analyses_tree_{}'.format(len(self.analyses_forest))
        self.analyses_forest[analyses_tree] = {}
        return analyses_tree

    def add_analysis_to_tree(self, analyses_tree_name, analysis):
        analyses_tree = self.analyses_forest[analyses_tree_name]
        analyses_tree[analysis.name] = analysis.required
        for requirement in analysis.required:
            if requirement in self.analyses_remaining:
                self.remove_analyses_from_remaining_analyses(requirement)

    def topological_sort(self, graph, v, visited, stack):
        # mark the current node as visited
        visited[v] = True

        # recur for all the vertices adjacent to this vertex
        try:
            for i in graph[v]:
                if not visited[i]:
                    self.topological_sort(graph, i, visited, stack)
        except KeyError:
            pass

        # push current vertex to stack which stores result
        stack.insert(0, v)
        # the function to do Topological Sort. It uses recursive

    def topological_traversal(self, analyses_tree):
        # mark all the vertices as not visited
        vertices = list(analyses_tree.keys())
        for value in analyses_tree.values():
            vertices.extend(list(value))
        vertices = list(set(vertices))

        visited = {}
        for vertex in vertices:
            visited[vertex] = False

        stack = []

        # call the recursive helper function to store topological
        # sort starting from all vertices one by one
        for i in vertices:
            if not visited[i]:
                self.topological_sort(analyses_tree, i, visited, stack)

        # fix the order
        stack.reverse()
        return stack

    def remove_analyses_from_remaining_analyses(self, name):
        self.analyses_remaining.pop(name)

    def register_analysis(self, analysis, analyses_tree=None, required=True):
        """
        An analysis must belong to an analysis tree(block) or be required to run.
        The required option is ignored if an analysis is in an analysis tree(block).
        """
        assert isinstance(analysis, Analysis) or isinstance(analysis, AnalysisGroup)
        self.analyses_flat[analysis.name] = analysis

        # not in analysis tree(block) but must be run
        if analyses_tree is None and required:
            self.analyses_remaining[analysis.name] = analysis
            return True

        # in analysis tree(block)
        self.add_analysis_to_tree(analyses_tree, analysis)

    def run_analysis(self, firmware, name):
        analysis = self.analyses_flat[name]
        self.last_analysis_status = self.analyses_flat[name].run(firmware)

    def run_remaining_analyses(self):
        for analysis in self.analyses_remaining:
            self.last_analysis_status = analysis.run(self.firmware)

    def run(self, target_analyses_tree=None):
        for analyses_tree_name, analyses_tree in self.analyses_forest.items():
            if target_analyses_tree is not None and analyses_tree_name != target_analyses_tree:
                continue
            analyses_chain = self.topological_traversal(analyses_tree)
            for analysis in analyses_chain:
                try:
                    a = self.analyses_flat[analysis]
                except KeyError:
                    # meaning that there is no analysis at all
                    continue
                # save and restore
                if finished(self.firmware, a):
                    logger_info(self.firmware.get_uuid(), 'analysis', 'done before', a.name, 0)
                    continue
                res = a.run(self.firmware)
                self.last_analysis_status = res
                if not res:
                    a.error(self.firmware)
                if not res and a.is_critical():
                    logger_warning(self.firmware.get_uuid(),
                                   'analysis', 'exception', 'can not support it, fix and rerun', 0)
                    exit(-1)
                finish(self.firmware, a)

    def run_static_analysis(self):
        self.run(target_analyses_tree=self.static_analysis)

    def run_dynamic_analyses(self):
        self.run(target_analyses_tree=self.dynamic_analysis)

    def register_static_analysis(self):
        static_analysis = self.new_analyses_tree()
        self.static_analysis = static_analysis

        # format <- extraction
        self.register_analysis(Format(), analyses_tree=static_analysis)
        self.register_analysis(Extraction(), analyses_tree=static_analysis)
        # extraction <- kernel
        self.register_analysis(Kernel(), analyses_tree=static_analysis)
        # extraction <- dt
        self.register_analysis(DeviceTree(), analyses_tree=static_analysis)
        # extraction, revision <- strings
        self.register_analysis(Strings(), analyses_tree=static_analysis)
        # kernel <- revision
        self.register_analysis(OpenWRTRevision(), analyses_tree=static_analysis)
        # revision, url <- toh
        self.register_analysis(OpenWRTURL(), analyses_tree=static_analysis)
        self.register_analysis(OpenWRTToH(), analyses_tree=static_analysis)
        # toh <- ram by default
        self.register_analysis(AbeliaRAM(), analyses_tree=static_analysis)
        # srcode <- .config
        self.register_analysis(SRCode(), analyses_tree=static_analysis)
        self.register_analysis(DotConfig(), analyses_tree=static_analysis)

    def register_dynamic_analysis(self, tracing=True, check_only=False):
        dynamic_analysis = self.new_analyses_tree()
        self.dynamic_analysis = dynamic_analysis

        if tracing:
            self.register_analysis(DoTracing(), analyses_tree=dynamic_analysis)
        self.register_analysis(Checking(), analyses_tree=dynamic_analysis)
        if not check_only:
            self.register_analysis(DeadLoop(), analyses_tree=dynamic_analysis)
            self.register_analysis(InitValue(), analyses_tree=dynamic_analysis)
