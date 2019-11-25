import abc
import logging


class Analysis(object):
    def __init__(self):
        self.name = None
        self.description = None
        self.log_suffix = None
        self.logger = logging.getLogger()
        self.required = []
        self.context = {'hint': '', 'input': ''}

    def has_required(self):
        return len(self.required)

    def add_required(self, analysis_name):
        pass

    @abc.abstractmethod
    def run(self, firmware):
        pass

    def info(self, message):
        self.logger.info('{} {}'.format(message, self.log_suffix))


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

    @staticmethod
    def find_analyses_tree_root(analyses_tree):
        keys = analyses_tree.keys()
        values = analyses_tree.values()
        values_flat = []
        for value in values:
            values_flat.extend(value)
        root = None
        for key in keys:
            if key not in values_flat:
                root = key
                break
        return root

    def traverse_analyses_tree(self, analyses_tree, root):
        analyses_chain = []
        if root:
            try:
                for leaf in analyses_tree[root]:
                    analyses_chain += self.traverse_analyses_tree(analyses_tree, leaf)
            except KeyError:
                analyses_chain += self.traverse_analyses_tree(analyses_tree, None)
            analyses_chain.append(root)
        return analyses_chain

    def remove_analyses_from_remaining_analyses(self, name):
        self.analyses_remaining.pop(name)

    def register_analysis(self, analysis):
        assert isinstance(analysis, Analysis) or isinstance(analysis, AnalysisGroup)
        self.analyses_flat[analysis.name] = analysis

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

    def run(self):
        for analyses_tree_name, analyses_tree in self.analyses_forest.items():
            root = AnalysesManager.find_analyses_tree_root(analyses_tree)
            analyses_chain = self.traverse_analyses_tree(analyses_tree, root)
            for analysis in analyses_chain:
                analysis.run()
        for analysis in self.analyses_remaining:
            analysis.run()
