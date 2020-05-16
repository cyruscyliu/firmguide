import os
import abc
import yaml
import shutil
import logging
import logging.config

from slcore.common import Common
from slcore.profile.firmware import Firmware
from slcore.srcodecontroller import get_srcodecontroller
from slcore.qemucontroller import get_qemucontroller
from slcore.compositor import unpack


class AnalysesManager(Common):
    def __init__(self, project, **kwargs):
        super().__init__()

        self.project = project
        self.srcodec = get_srcodecontroller(
            self.project.attrs['source'], self.project.attrs['cross_compile'],
            self.project.attrs['arch'], self.project.attrs['endian'],
            self.project.attrs['makeout']
        )
        self.qemuc = get_qemucontroller(self.project.attrs['qemu_dir'])
        self.firmware = Firmware()

        self.arguments = kwargs
        self.max_iteration = 1
        self.reset = kwargs.pop('reset')
        self.archive = kwargs.pop('archive')

        self.arguments['trace_format'] = 'qemudebug'
        self.arguments['path_to_trace'] = kwargs.pop(
            'trace', '{}/{}-{}-{}.trace'.format(
                self.project.attrs['path'], self.project.attrs['name'],
                self.project.attrs['arch'], self.project.attrs['endian']
            ))

        self.analyses_flat = {}  # name:analysis
        self.analyses_tree = {}
        self.last_analysis_status = True

    def setup_logging(self, default_level=logging.INFO):
        path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), 'logging.yaml')
        if os.path.exists(path):
            with open(path, "r") as f:
                config = yaml.safe_load(f)
            config['handlers']['file']['filename'] = \
                os.path.join(
                    self.project.attrs['path'],
                    '{}.log'.format(self.project.attrs['name']))
            config['root']['level'] = default_level
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)
        return True

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

        # there at least one image available
        images = self.project.attrs['images']
        assert len(images), 'please add an image first'
        if 'firmware' in self.arguments:
            components = self.firmware.get_components()
            if components is None and self.arguments['firmware'] is None:
                components = unpack(images[0], target_dir=path)
            elif components is None and self.arguments['firmware'] is not None:
                components = unpack(self.arguments['firmware'], target_dir=path)
            elif components is not None and self.arguments['firmware'] is None:
                pass
            else:
                if self.arguments['firmware'] != components.get_path_to_raw():
                    components = unpack(self.arguments['firmware'], target_dir=path)

            if not components.supported:
                return False

            working_path = os.path.join(path, components.get_raw_name())
            if not os.path.exists(working_path):
                shutil.copy(components.get_path_to_raw(), os.path.join(working_path))
            self.firmware.set_components(components)

        debug = self.arguments.pop('debug')
        if debug:
            self.setup_logging(default_level=logging.DEBUG)
        else:
            self.setup_logging()
        return True

    def wrapup(self):
        self.firmware.save_profile()
        self.snapshot()
        if self.archive and self.firmware.get_stage('user_mode'):
            return self.archive()
        return True

    def snapshot(self):
        path = self.project.attrs['path']
        self.info('snapshot', 'profile at {}'.format(self.firmware.path_to_profile), 1)
        self.info('snapshot', 'dtb at {}'.format(self.firmware.realdtb), 1)
        self.info('snapshot', 'dts at {}'.format(self.firmware.realdts), 1)
        self.info('snapshot', 'project at {}/project.yaml'.format(path), 1)
        self.info('snapshot', 'source at {}/qemu-4.0.0'.format(path), 1)
        return True

    def archive(self):
        """Should be called after firmware.snapshot()."""
        # move profile to examples/profiles/machine_name/profile.yaml
        target_profiles = os.path.join(
            self.project.attrs['base_dir'],
            'examples/profiles/{}'.format(self.firmware.get_machine_name()))
        os.makedirs(target_profiles, exist_ok=True)
        os.system('cp {} {}'.format(
            os.path.join(self.project.attrs['path'], 'profile.yaml'),
            os.path.join(target_profiles, 'profile.yaml')
        ))

        # move dtb to examples/profiles/machine_name/profile.dtb
        os.system('cp {} {}'.format(
            self.firmware.get_realdtb(),
            os.path.join(target_profiles, 'profile.dtb')
        ))

        # move qemu c files to examples/machines/machine_name/profile.yaml
        target_machines = os.path.join(
            self.project.attrs['base_dir'],
            'examples/machines/{}'.format(self.firmware.get_machine_name()))
        os.makedirs(target_machines, exist_ok=True)
        os.system('cp -r {}/* {}'.format(
            os.path.join(self.project.attrs['path'], 'qemu-4.0.0'),
            target_machines
        ))

        return True

    def print_analyses_chain(self):
        analyses_chain = self.topological_traversal(self.analyses_tree)
        if len(analyses_chain) > 5:
            self.info('chain', '->'.join(analyses_chain[:5]), 1)
            self.info('chain cont\'d', '->'.join(analyses_chain[5:]), 1)
        else:
            self.info('chain', '->'.join(analyses_chain), 1)

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
        analyses_chain = self.topological_traversal(self.analyses_tree)
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


class AnalysisGroup(AnalysisInterface):
    def __init__(self):
        super().__init__()

        self.name = None
        self.description = None
        self.members = []

    def register(self, project, **kwargs):
        analysis_manager = AnalysesManager(project, **kwargs)
        for member in self.members:
            analysis_manager.register_analysis(member['class'](analysis_manager))
        return analysis_manager
