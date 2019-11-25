from unittest import TestCase

from analyses.device_tree import DeviceTree
from analyses.dot_config import DotConfig
from analyses.extraction import Extraction
from analyses.format import Format
from analyses.kernel import Kernel
from analyses.common.analysis import AnalysesManager
from analyses.openwrt import OpenWRTURL, OpenWRTRevision, OpenWRTToH
from analyses.srcode import SRCode
from analyses.strings import Strings


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
        # extraction, revision <- strings
        analyses_manager.register_analysis(Strings())
        # kernel <- revision
        analyses_manager.register_analysis(OpenWRTRevision())
        # revision, url <- toh
        analyses_manager.register_analysis(OpenWRTURL())
        analyses_manager.register_analysis(OpenWRTToH())
        # srcode <- .config
        analyses_manager.register_analysis(SRCode())
        analyses_manager.register_analysis(DotConfig())
        for analyses_tree_name, analyses_tree in analyses_manager.analyses_forest.items():
            res = analyses_manager.topological_traversal(analyses_tree)
            # ['format', 'extraction', 'dt', 'kernel', 'revision', 'strings', 'url', 'srcode', '.config', 'toh']
            self.assertEqual('format', res[0])
        self.assertEqual(0, len(analyses_manager.analyses_remaining))
