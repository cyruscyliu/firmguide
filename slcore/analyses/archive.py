import os

from slcore.amanager import Analysis
from slcore.database.dbf import get_database
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.common import load_dtb


class Archive(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'archive'
        self.description = 'Archive device tree.'
        self.required = []

    def run(self, **kwargs):
        """
        Must be called after ./firmware systhesize ...
        """
        return True
