from unittest import TestCase

from analyses.device_tree import DeviceTree
from analyses.dot_config import DotConfig
from analyses.extraction import Extraction
from analyses.format import Format
from analyses.kernel import Kernel
from analyses.common.analysis import AnalysesManager
from analyses.openwrt import OpenWRTURL, OpenWRTRevision, OpenWRTToH
from analyses.srcode import SRCode


class TestAnalysesManager(TestCase):
    def test_traverse_analyses_tree(self):
        analyses_manager = AnalysesManager()
        # format <- extraction
        analyses_manager.register_analysis(Format())
        analyses_manager.register_analysis(Extraction())
        self.assertDictEqual({'analyses_tree_0': {'extraction': ['format']}}, analyses_manager.analyses_forest)
        self.assertDictEqual({}, analyses_manager.analyses_remaining)
        # extraction <- kernel
        analyses_manager.register_analysis(Kernel())
        # extraction <- dt
        analyses_manager.register_analysis(DeviceTree())
        # kernel <- revision
        analyses_manager.register_analysis(OpenWRTRevision())
        # revision, url <- toh
        analyses_manager.register_analysis(OpenWRTURL())
        analyses_manager.register_analysis(OpenWRTToH())
        # srcode <- .config
        analyses_manager.register_analysis(SRCode())
        analyses_manager.register_analysis(DotConfig())
        print(analyses_manager.analyses_forest)
        for analyses_tree_name, analyses_tree in analyses_manager.analyses_forest.items():
            root = AnalysesManager.find_analyses_tree_root(analyses_tree)
            res = analyses_manager.traverse_analyses_tree(analyses_tree, root)
            print(res)
        print(analyses_manager.analyses_remaining)
