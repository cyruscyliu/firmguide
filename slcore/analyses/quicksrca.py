from slcore.amanager import Analysis


class QuickSrcA(Analysis):
    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)

        self.name = 'quicksrca'
        self.description = 'Quick source code analysis.'

    def run(self, **kwargs):
        ep = kwargs.pop('entry_point')
        caller = kwargs.pop('caller')
        f = kwargs.pop('file')

        # We simply preprocess the c file containing
        # the entry point if no other arguments assigned.
        srcodec = self.analysis_manager.srcodec
        if not srcodec.supported:
            self.error_info = 'please set the source code'
            return False

        if ep:
            path_to_entry_point = srcodec.symbol2file(ep)
            if path_to_entry_point is None:
                path_to_entry_point = srcodec.symbol2fileg(ep)
                if path_to_entry_point is None:
                    self.info('cannot find {}'.format(ep), 0)
                    return False
            self.info('find {} in {}'.format(ep, path_to_entry_point), 1)
            cmdline = srcodec.get_cmdline(path_to_entry_point)
            path_to_pentry_point = \
                srcodec.preprocess(path_to_entry_point, cmdline=cmdline)
            self.info('preprocess and save as {}/{}'.format(
                srcodec.get_path_to_source_code(), path_to_pentry_point), 1)
            return True

        if f:
            cmdline = srcodec.get_cmdline(f)
            fp = srcodec.preprocess(f, cmdline=cmdline)
            self.info('preprocess and save as {}/{}'.format(
                srcodec.get_path_to_source_code(), fp), 1)
            return True

        self.error_info = 'nothing expected'
        return False