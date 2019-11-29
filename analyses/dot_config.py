import os

from analyses.asm.gnu import parser_proc_info_init
from analyses.common.analysis import Analysis
from analyses.common.makefile import obj_definition_filter


class DotConfig(Analysis):
    def run(self, firmware):
        architecture = firmware.get_architecture()
        if architecture != 'arm':
            self.context['input'] = 'only support arm now'
            return False
        path_to_source_code = firmware.get_path_to_source_code()
        if path_to_source_code is None:
            self.context['input'] = 'no source code available'
            return False
        path_to_mm = os.path.join(path_to_source_code, 'arch/{}/mm'.format(architecture))
        path_to_mm_makefile = os.path.join(path_to_mm, 'Makefile')
        path_to_dot_config = os.path.join(path_to_source_code, '.config')
        configs = []
        with open(path_to_dot_config) as f:
            for line in f:
                if line.startswith('#'):  # comment
                    continue
                if line.find('=') == -1:  # is not set
                    continue
                if line.find('CPU') == -1:  # not related to this task
                    continue
                config = line.strip().split('=')
                configs.append(config[0])
        stmts = obj_definition_filter(path_to_mm_makefile, configs)
        targets = []
        for stmt in stmts:
            targets.append(stmt.value[:-2])
        for file_ in os.listdir(path_to_mm):
            if file_.find('.') == -1:
                continue
            name, extent = file_.split('.')
            if name in targets:
                cpus = parser_proc_info_init(os.path.join(path_to_mm, file_))
                if cpus is None:
                    continue
                for cpu, properties in cpus.items():
                    self.info(firmware, '\033[32mget cpu model: {} \033[0m'.format(properties), 1)
                    path_to_cpu = firmware.find_cpu_nodes(new=True)
                    for k, v in properties.items():
                        firmware.set_node_property(path_to_cpu, k, v)

    def __init__(self):
        super().__init__()
        self.name = '.config'
        self.description = 'extract information from .config'
        self.required = ['srcode']
        self.context['hint'] = 'no .config available'
        self.critical = False
