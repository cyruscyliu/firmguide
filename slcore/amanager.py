import os
import abc
import shutil
import logging

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
        self.firmware = None

        self.arguments = kwargs
        self.max_iteration = 1
        self.reset = kwargs.pop('reset')
        self.archive = kwargs.pop('archive')

        self.analyses_flat = {}  # name:analysis
        self.analyses_forest = {}  # analysis blocks
        self.analyses_remaining = {}  # name:analysis
        self.last_analysis_status = True

    def setup_logging(self, default_level=logging.INFO)
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
        self.firmware = Firmware()

        # set target dir
        path = self.project.attrs['path']

        # load profile from path_to_profile
        path_to_profile = os.path.join(path, 'profile.yaml')
        if not os.path.exists(path_to_profile):
            self.firmware.set_profile(target_dir=path, first=True)
        else:
            self.firmware.set_profile(path_to_profile=path_to_profile)
            # change save-to-path to avoid modifing our well-defined profile
            self.firmware.path_to_profile = \
                os.path.join(path, 'profile.yaml')

        # triple friends
        self.firmware.set_arch(self.project.attrs['arch'])
        self.firmware.set_endian(self.project.attrs['endian'])
        self.firmware.set_brand(self.project.attrs['brand'])

        # there at least one image available
        images = self.project.attrs['images']
        if 'firmware' in self.arguments:
            components = self.firmware.get_components()
            if components is not None and \
                        self.arguments['firmware'] != components.get_path_to_raw():
                components = unpack(
                    self.arguments['firmware'], target_dir=path)
            else:
                components = unpack(self.arguments['firmware'], target_dir=path)
        else:
            components = unpack(images[0], target_dir=path)

        working_path = os.path.join(path, components.get_raw_name())
        if not os.path.exists(working_path):
            shutil.copy(components.get_path_to_raw(), os.path.join(working_path))
        self.firmware.set_components(components)

        debug = self.kwargs.pop('debug')
        if debug:
            self.setup_logging(default_level=logging.DEBUG)
        else:
            self.setup_logging()
        return True

    def wrapup(self):
        self.firmware.snapshot()
        if self.archive and self.firmware.get_stage('user_mode'):
            return self.archive()
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

    def get_analysis(self, name):
        try:
            return self.analyses_flat[name]
        except KeyError:
            return None

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
        self.last_analysis_status = analysis.run(firmware)

    def run_remaining_analyses(self):
        for analysis in self.analyses_remaining:
            self.last_analysis_status = analysis.run(self.firmware)

    def finish(self, firmware, analysis):
        if firmware.analysis_progress is None:
            return
        if analysis.type == 'diag':
            return
        if analysis.name not in firmware.analysis_progress:
            firmware.analysis_progress[analysis.name] = 1

    def finished(self, firmware, analysis):
        if firmware.analysis_progress is None:
            return False
        try:
            firmware.analysis_progress[analysis.name]
            return True
        except KeyError:
            return False

    def run(self, target_analyses_tree=None):
        for analyses_tree_name, analyses_tree in self.analyses_forest.items():
            if target_analyses_tree is not None and analyses_tree_name != target_analyses_tree:
                continue
            analyses_chain = self.topological_traversal(analyses_tree)
            for analysis in analyses_chain:
                try:
                    a = self.analyses_flat[analysis]
                except KeyError:
                    # meaning that there is no such analysis at all
                    continue
                # save and restore
                if not self.firmware.rerun and self.finished(self.firmware, a):
                    self.info('done before', a.name, 0)
                    continue
                try:
                    res = a.run(self.firmware)
                    self.last_analysis_status = res
                    if not res:
                        a.error(self.firmware)
                    if not res and a.is_critical():
                        return False
                except NotImplementedError as e:
                    self.warning('exception', e.args[0], 0)
                    return False

                self.finish(self.firmware, a)
        return True


class AnalysisInterface():
    def __init__(self):
        self.analysis_manager = None
        self.analysis_tree = None

    @abc.abstractmethod
    def register(self, firmware):
        """Register this analysis to analysis manager."""
        pass

    @abc.abstractmethod
    def schedule(self):
        """Schedule this analysis."""
        pass


class Analysis(Common, AnalysisInterface):
    def __init__(self, analysis_manager):
        super().__init__()

        self.analysis_manager = analysis_manager
        self.firmware = None
        self.name = None
        self.description = None
        self.required = []
        self.settings = []
        self.context = {'hint': '', 'input': ''}
        self.critical = False
        self.args = None
        self.type = 'inf'

    def is_critical(self):
        return self.critical

    def has_required(self):
        return len(self.required)

    def add_required(self, analysis_name):
        pass

    @abc.abstractmethod
    def run(self, firmware, **kwargs):
        pass

    def info(self, firmware, message, status):
        super().info(self.name, message, status)

    def debug(self, firmware, message, status):
        super().debug(self.name, message, status)

    def warning(self, firmware, message, status):
        super().warning(self.name, message, status)

    def error(self, firmware):
        if self.context['input'].find('\n') != -1:
            self.warning(self.name, self.context['hint'], 0)
            lines = self.context['input'].split('\n')
            for line in lines:
                if len(line):
                    self.warning(self.name, line, 0)
        else:
            self.warning(self.name, ', '.join([self.context['hint'], self.context['input']]), 0)

    def register(self, firmware):
        self.firmware = firmware
        pass

    def schedule(self):
        self.run(self.firmware)


class AnalysisGroup(AnalysisInterface):
    def __init__(self):
        super().__init__()

        self.name = None
        self.description = None
        self.members = []
        self.required = []

    def register(self, firmware):
        analysis_manager = AnalysesManager(firmware)
        at = analysis_manager.new_analyses_tree()

        for member in self.members():
            analysis_manager.register_analysis(
                member['class'](analysis_manager),
                analyses_tree=at)

        self.analysis_manager = analysis_manager
        self.analysis_tree = at

    def schedule(self):
        status = self.analysis_manager.run(
            target_analyses_tree=self.analyses_tree)
        # try:
        #     status = self.analysis_manager.run(
        #         target_analyses_tree=self.analyses_tree)
        # except SystemExit:
        #     pass

        # if not firmware.get_stage('user_mode') and firmware.debug:
        #     firmware.qemuc.debug(firmware.running_command, firmware.srcodec.get_path_to_vmlinux())

        return status
