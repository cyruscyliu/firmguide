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
    def __init__(self, project, **kwargs):
        super().__init__()

        self.project = project
        self.srcodec = None

        qemu_dir = self.project.attrs['qemu_dir']
        qemu_ver = os.path.basename(qemu_dir.split('-')[1])
        self.qemuc = get_qemucontroller(qemu_dir, version=qemu_ver)

        self.firmware = Firmware()

        self.arguments = kwargs
        self.max_iteration = 1
        self.reset = kwargs.pop('reset')

        self.arguments['trace_format'] = 'qemudebug'
        default_path_to_trace = '{}/{}-{}-{}.trace'.format(
                self.project.attrs['path'], self.project.attrs['name'],
                self.project.attrs['arch'], self.project.attrs['endian'])
        path_to_trace = kwargs.pop('trace', default_path_to_trace)
        if path_to_trace is None:
            path_to_trace = default_path_to_trace
        self.arguments['path_to_trace'] = path_to_trace

        self.analyses_flat = {}  # name:analysis
        self.analyses_tree = {}
        self.last_analysis_status = True

    def warmup(self):
        # set target dir
        path = self.project.attrs['path']

        # load profile from path_to_profile
        path_to_profile = os.path.join(path, 'profile.yaml')
        if not os.path.exists(path_to_profile):
            self.firmware.create_empty_profile(path)
        else:
            self.firmware.load_from_profile(path_to_profile)
            # change save-to-path to avoid modifing our well-defined profile
            self.firmware.path_to_profile = \
                os.path.join(path, 'profile.yaml')

        # triple friends
        self.firmware.set_arch(self.project.attrs['arch'])
        self.firmware.set_endian(self.project.attrs['endian'])
        self.firmware.set_brand(self.project.attrs['brand'])

        # setup logger as early as possible
        debug = self.arguments.pop('debug')
        if debug:
            setup_logging(
                self.project.attrs['path'],
                self.project.attrs['name'],
                default_level=logging.DEBUG)
        else:
            setup_logging(
                self.project.attrs['path'],
                self.project.attrs['name'])

        if 'firmware' in self.arguments:
            images = self.project.attrs['images']
            components = self.firmware.get_components()
            if self.arguments['firmware'] is not None:
                if components is None or (not components.supported):
                    components = unpack(self.arguments['firmware'], target_dir=path)
                elif self.arguments['firmware'] != components.get_path_to_raw():
                    components = unpack(self.arguments['firmware'], target_dir=path)
                else:
                    components = components
            else:
                if components is None or (not components.supported):
                    if images is not None and len(images) > 0:
                        components = unpack(images[0], target_dir=path)
                    else:
                        components = unpack(None)
                else:
                    components = components

            assert components is not None, 'the components must not be none'
            if components.supported:
                working_path = os.path.join(path, components.get_raw_name())
                if not os.path.exists(working_path):
                    shutil.copy(components.get_path_to_raw(),
                                os.path.join(working_path))
            self.firmware.set_components(components)

        if 'dtb' in self.arguments:
            dtbs = self.project.attrs['dtbs']
            realdtb = self.firmware.get_realdtb()
            components = self.firmware.get_components()
            if self.arguments['dtb'] is not None:
                realdtb = self.arguments['dtb']
            else:
                if components is None or (not components.supported):
                    if dtbs is not None and len(dtbs) > 0:
                        realdtb = dtbs[0]
                    else:
                        realdtb = None
                else:
                    realdtb = self.firmware.get_components().get_path_to_dtb()
            self.firmware.set_realdtb(realdtb)

        if 'source' in self.arguments:
            source = self.arguments['source'] or self.project.attrs['source']
            self.srcodec = get_srcodecontroller(
                source, self.project.attrs['cross_compile'],
                self.project.attrs['arch'], self.project.attrs['endian'],
                self.project.attrs['makeout']
            )

        return True

    def wrapup(self):
        self.firmware.save_profile()
        self.snapshot()
        return True

    def snapshot(self):
        path = self.project.attrs['path']
        self.info('snapshot', 'profile at {}'.format(
            self.firmware.path_to_profile), 1)
        self.info('snapshot', 'project at {}/project.yaml'.format(path), 1)
        self.info('snapshot', 'source at {}/qemu-4.0.0'.format(path), 1)
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
                self.firmware.analysis_progress = {}
            else:
                self.firmware.analysis_progress = analysis_progress

    def save_analysis(self):
        analysis = os.path.join(self.project.attrs['path'], 'analysis')
        with open(analysis, 'w') as f:
            yaml.safe_dump(self.firmware.analysis_progress, f)

    def finish(self, analysis):
        if self.firmware.analysis_progress is None:
            return
        if analysis.type == 'diag':
            return
        if analysis.name not in self.firmware.analysis_progress:
            self.firmware.analysis_progress[analysis.name] = 1

    def finished(self, analysis):
        if self.firmware.analysis_progress is None:
            return False
        try:
            self.firmware.analysis_progress[analysis.name]
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
    def register(self, project):
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

    def register(self, project, **kwargs):
        analysis_manager = AnalysesManager(project, **kwargs)
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

    def register(self, project, **kwargs):
        analysis_manager = AnalysesManager(project, **kwargs)
        for member in self.members:
            analysis_manager.register_analysis(
                member['class'](analysis_manager))
        return analysis_manager
