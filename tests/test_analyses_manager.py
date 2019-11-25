from unittest import TestCase

from analyses.extraction import Extraction
from analyses.format import Format
from analyses.kernel import Kernel
from analyses.common.analysis import AnalysesManager
from analyses.openwrt import OpenWRTURL


class TestAnalysesManager(TestCase):
    def test_traverse_analyses_tree(self):
        analyses_manager = AnalysesManager()
        analyses_manager.register_analysis(Format())
        analyses_manager.register_analysis(Extraction())
        self.assertDictEqual({'analyses_tree_0': {'extraction': ['format']}}, analyses_manager.analyses_forest)
        self.assertDictEqual({}, analyses_manager.analyses_remaining)
        analyses_manager.register_analysis(Kernel())
        analyses_manager.register_analysis(OpenWRTURL())
        for analyses_tree_name, analyses_tree in analyses_manager.analyses_forest.items():
            root = AnalysesManager.find_analyses_tree_root(analyses_tree)
            res = analyses_manager.traverse_analyses_tree(analyses_tree, root)
            print(res)
        print(analyses_manager.analyses_remaining)

