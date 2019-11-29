import abc

from supervisor.logging_setup import logger_info, logger_warning
from supervisor.save_and_restore import finished, finish


class Analysis(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.required = []
        self.context = {'hint': '', 'input': ''}
        self.critical = False
        self.args = None

    def is_critical(self):
        return self.critical

    def has_required(self):
        return len(self.required)

    def add_required(self, analysis_name):
        pass

    @abc.abstractmethod
    def run(self, firmware):
        pass

    def info(self, firmware, message, status):
        logger_info(firmware.uuid, 'analysis', self.name, message, status)

    def error(self, firmware):
        if self.context['input'].find('\n') != -1:
            logger_warning(firmware.uuid, 'analysis', self.name, self.context['hint'], 0)
            lines = self.context['input'].split('\n')
            for line in lines:
                if len(line):
                    logger_warning(firmware.uuid, 'analysis', self.name, line, 0)
        else:
            logger_warning(
                firmware.uuid, 'analysis', self.name, ', '.join([self.context['hint'], self.context['input']]), 0)


class AnalysisGroup(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.members = []
        self.required = []

    @abc.abstractmethod
    def run(self, firmware):
        pass


class AnalysesManager(object):
    def __init__(self):
        self.analyses_flat = {}  # name:analysis
        self.analyses_forest = {}
        self.analyses_remaining = {}  # name:analysis
        self.last_analysis_status = True

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
        analyses_tree = 'analyses_tree_{}'.format(len(self.analyses_forest))
        self.analyses_forest[analyses_tree] = {}
        return self.analyses_forest[analyses_tree]

    def add_analysis_to_tree(self, analyses_tree, analysis):
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

    def register_analysis(self, analysis, no_chained=False):
        assert isinstance(analysis, Analysis) or isinstance(analysis, AnalysisGroup)
        self.analyses_flat[analysis.name] = analysis

        if no_chained:
            return

        if not analysis.has_required():
            self.analyses_remaining[analysis.name] = analysis
            return True

        new_analyses_tree_flag = True
        for analyses_tree_name, analyses_tree in self.analyses_forest.items():
            if AnalysesManager.find_analysis_in_tree(analyses_tree, analysis):
                self.add_analysis_to_tree(analyses_tree, analysis)
                new_analyses_tree_flag = False
        if new_analyses_tree_flag:
            analyses_tree = self.new_analyses_tree()
            self.add_analysis_to_tree(analyses_tree, analysis)

    def run_analysis(self, firmware, name):
        analysis = self.analyses_flat[name]
        self.last_analysis_status = self.analyses_flat[name].run(firmware)

    def run(self, firmware):
        for analyses_tree_name, analyses_tree in self.analyses_forest.items():
            analyses_chain = self.topological_traversal(analyses_tree)
            for analysis in analyses_chain:
                a = self.analyses_flat[analysis]
                # save and restore
                if finished(firmware, a):
                    logger_info(firmware.uuid, 'analysis', 'done before', a.name, 0)
                    continue
                res = a.run(firmware)
                self.last_analysis_status = res
                if not res:
                    a.error(firmware)
                if not res and a.is_critical():
                    raise NotImplementedError(firmware, a)
                finish(firmware, a)
        for analysis in self.analyses_remaining:
            self.last_analysis_status = analysis.run(firmware)
