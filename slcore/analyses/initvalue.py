from slcore.analyses.analysis import Analysis


class ExecutionFlow(Analysis):
    def run(self, firmware):
        if firmware.uuid == 'ath79':
            # prom_putchar -> prom_putchar_init: r/w, switch/case, no panic
            firmware.insert_bamboo_devices(0x18060090, 0x4, value=0x00b0)

        if firmware.uuid == 'ar71xx_generic':
            ## =========== from stinc.py =============
            firmware.insert_bamboo_devices(0x18060010, 0x4, value=0x10000000)
            firmware.insert_bamboo_devices(0x18060014, 0x4, value=0x10000000)
            ## =======================================
            ## =========== from stimer.py ==============
            firmware.insert_bamboo_devices(0x18050000, 0x4, value=0x10)
            ## =========================================

        firmware.update_bamboo_devices()
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'excflow'
        self.description = 'source code info analysis (sparse)'
        self.required = ['preprocdt']
        self.context['hint'] = ''
        self.critical = False
        #
        self.globals = []

