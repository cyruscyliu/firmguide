import os
import yaml

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
        profile = kwargs.pop('profile')
        if profile is None:
            profile = '.profile'

        machine_name = yaml.safe_load(open(profile))['basics']['machine_name']

        # Copy profile to database
        base_dir = self.analysis_manager.project.attrs['base_dir']
        target = os.path.join(
            base_dir, 'slcore/database/by_compatible',
            machine_name + '.yaml')
        os.system('cp {} {}'.format(profile, target))
        self.info('archive {}'.format(target), 1)

        # TODO
        # Update record in some summary file
        return True
