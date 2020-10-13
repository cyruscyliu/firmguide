import os
import abc
import yaml
import shutil
import logging

from slcore.common import Common, setup_logging
from slcore.profile.firmware import Firmware
from slcore.srcodecontroller import get_srcodecontroller
from slcore.qemucontroller import get_qemucontroller
from slcore.compositor import unpack


class AnalysesManager(Common):
    def __init__(self, **kwargs):
        super().__init__()

        self.analyses_flat = {}  # name:analysis
        self.analyses_tree = {}
        self.last_analysis_status = True

        self.project = None
        self.firmware = None
        self.reset = False
        self.arguments = kwargs # don't delete this
        self.analysis_progress = {}

    def wrapup(self):
        self.firmware.save_profile()
        path = self.project.attrs['path']
        self.info('snapshot', 'profile at {}'.format(
            self.firmware.path_to_profile), 1)
        return True

    def print_analyses_chain(self):
        analyses_chain = self.topological_traversal()

        analyses_chain_p = []
        for analysis in analyses_chain:
            if self.get_analysis(analysis) is None:
                analyses_chain_p.append('{}(invalid)'.format(analysis))
            else:
                analyses_chain_p.append(analysis)

        line = len(analyses_chain_p) // 5
        rem = len(analyses_chain_p) % 5
        for i in range(0, line):
            if line == 1:
                self.info('chain', '->'.join(analyses_chain_p[:5]), 1)
            else:
                self.info('chain cont\'d', '->'.join(analyses_chain_p[5*i:5*(i+1)]), 1)
        if rem > 0:
            self.info('chain cont\'d', '->'.join(analyses_chain_p[5*line:]), 1)

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

    def topological_traversal(self):
        # mark all the vertices as not visited
        vertices = list(self.analyses_tree.keys())
        for value in self.analyses_tree.values():
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
                self.topological_sort(self.analyses_tree, i, visited, stack)

        # fix the order
        stack.reverse()
        return stack

    def get_analysis(self, name):
        try:
            return self.analyses_flat[name]
        except KeyError:
            return None

    def add_analysis_to_tree(self, analysis):
        self.analyses_tree[analysis.name] = analysis.required

    def register_analysis(self, analysis, required=True):
        assert isinstance(analysis, Analysis)
        self.analyses_flat[analysis.name] = analysis
        self.add_analysis_to_tree(analysis)

    def restore_analysis(self):
        # handle analysis
        analysis = os.path.join(self.project.attrs['path'], 'analysis')
        if not os.path.exists(analysis) or self.reset:
            with open(analysis, 'w') as f:
                f.close()

        with open(analysis, 'r') as f:
            analysis_progress = yaml.safe_load(f)
            if analysis_progress is None:
                self.analysis_progress = {}
            else:
                self.analysis_progress = analysis_progress

    def save_analysis(self):
        analysis = os.path.join(self.project.attrs['path'], 'analysis')
        with open(analysis, 'w') as f:
            yaml.safe_dump(self.analysis_progress, f)

    def finish(self, analysis):
        if self.analysis_progress is None:
            return
        if analysis.name not in self.analysis_progress:
            self.analysis_progress[analysis.name] = 1

    def finished(self, analysis):
        if self.analysis_progress is None:
            return False
        try:
            self.analysis_progress[analysis.name]
            return True
        except KeyError:
            return False

    def run(self):
        analyses_chain = self.topological_traversal()
        for analysis in analyses_chain:
            try:
                a = self.analyses_flat[analysis]
            except KeyError:
                continue  # there is no such analysis
            # save and restore

            if not self.reset and self.finished(a):
                self.info('done before', a.name, 0)
                continue

            try:
                res = a.run(**self.arguments)
                self.last_analysis_status = res
                if not res:
                    a.error()
                if not res and a.is_critical():
                    return False
            except NotImplementedError as e:
                self.warning('exception', e.args[0], 0)
                return False
            except SystemExit:
                self.finish(a)
                break
            self.finish(a)
        return True


class AnalysisInterface():
    @abc.abstractmethod
    def register(self, *args, **kwargs):
        """Register this analysis to analysis manager."""
        pass


class Analysis(Common, AnalysisInterface):
    def __init__(self, analysis_manager):
        super().__init__()

        self.name = None
        self.description = None
        self.required = []
        self.settings = []
        self.error_info = ''
        self.critical = False
        self.args = None
        self.type = 'inf'

        self.analysis_manager = analysis_manager
        if analysis_manager is not None:
            self.firmware = analysis_manager.firmware
        else:
            self.firmware = None

    def is_critical(self):
        return self.critical

    def has_required(self):
        return len(self.required)

    def add_required(self, analysis_name):
        pass

    @abc.abstractmethod
    def run(self, **kwargs):
        pass

    def info(self, message, status):
        super().info(self.name, message, status)

    def debug(self, message, status):
        super().debug(self.name, message, status)

    def warning(self, message, status):
        super().warning(self.name, message, status)

    def error(self):
        if self.error_info.find('\n') != -1:
            lines = self.error_info.split('\n')
            for line in lines:
                if len(line) > 0:
                    self.warning(line, 0)
        else:
            self.warning(self.error_info, 0)

    def register(self, *args, **kwargs):
        analysis_manager = AnalysesManager(*args, **kwargs)
        self.analysis_manager = analysis_manager
        self.firmware = analysis_manager.firmware

        analysis_manager.register_analysis(self)

        return analysis_manager

    def check_components_is_none(self):
        components = self.firmware.get_components()
        if components is None:
            self.error_info = 'components is missing'
            return True
        if not components.supported:
            self.error_info = 'firmware format is not supported'
            return True
        return False

    def check_components(self):
        if self.check_components_is_none():
            return False

        components = self.firmware.get_components()
        if not components.has_kernel():
            self.error_info = 'firmware have no kernel, maybe is a rootfs image'
            return False

        return True


class AnalysisGroup(AnalysisInterface):
    def __init__(self):
        super().__init__()
        self.name = None
        self.description = None
        self.members = []

    def register(self, *args, **kwargs):
        analysis_manager = AnalysesManager(*args, **kwargs)
        for member in self.members:
            analysis_manager.register_analysis(
                member['class'](analysis_manager))
        return analysis_manager
