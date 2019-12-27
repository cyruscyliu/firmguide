import os

from analyses.analysis import Analysis
from analyses.inf_makefile import obj_definition_filter


def parse_kconfig(data):
    """
    https://raw.githubusercontent.com/Gallopsled/pwntools/ \
        292b81af179e25e7810e068b3c06a567256afd1d/pwnlib/elf/config.py
    """
    config = {}

    NOT_SET = ' is not set'
    if not data:
        return

    for line in data.splitlines():
        # Not set? Then set to None.
        if NOT_SET in line:
            line = line.split(NOT_SET, 1)[0]
            name = line.strip('# ')
            config[name] = None
        # Set to a value? Extract it
        if '=' in line:
            k, v = line.split('=', 1)
            # Boolean conversions
            if v == 'y':
                v = True
            elif v == 'n':
                v = False
            else:
                # Integer conversions
                try:
                    v = int(v, 0)
                except ValueError:
                    pass
            config[k] = v

    return config


def parse_proc_info_init(firmware, path_to_mm, filename):
    # path_to_make_out = firmware.get_path_to_makeout()
    #
    # command = None
    # with open(path_to_make_out) as f:
    #     for line in f:
    #         if line.find('gcc') != -1 and line.find('-c') != -1 and line.find(filename) != -1:
    #             command = line.strip()
    #             break
    # path_to_source_code = firmware.get_path_to_source_code()
    # command = command.replace('-c', '-E').replace('.o', '.i')
    # cwd = os.getcwd()
    # os.chdir(path_to_source_code)
    # os.system(command)
    # os.chdir(cwd)
    # path_to_assembly_file = os.path.join(path_to_source_code, path_to_mm, filename + '.i')
    # call asm2xml
    return None


class DotConfig(Analysis):
    def run(self, firmware):
        # https://lwn.net/Articles/426006/
        # https://github.com/ulfalizer/Kconfiglib
        architecture = firmware.get_architecture()
        if architecture != 'arm':
            self.context['input'] = 'only support arm now'
            return False
        path_to_source_code = firmware.get_path_to_source_code()
        path_to_dot_config = firmware.get_path_to_dot_config()
        if path_to_source_code is None:
            self.context['input'] = 'no source code available'
            return False
        path_to_mm = os.path.join(path_to_source_code, 'arch/{}/mm'.format(architecture))
        path_to_mm_makefile = os.path.join(path_to_mm, 'Makefile')
        with open(path_to_dot_config) as f:
            configs = parse_kconfig('\n'.join(f.readlines()))
        stmts = obj_definition_filter(path_to_mm_makefile, configs)
        targets = []
        for stmt in stmts:
            targets.append(stmt.value[:-2])
        for file_ in os.listdir(path_to_mm):
            if file_.endswith('.cmd'):
                continue
            if file_.find('.') == -1:
                continue
            name, extent = file_.split('.')
            if name in targets:
                cpus = parse_proc_info_init(firmware, path_to_mm, name)  # os.path.join(path_to_mm, file_))
                if cpus is None:
                    continue
                for cpu, properties in cpus.items():
                    self.info(firmware, 'get cpu model: {}'.format(properties), 1)
                    path_to_cpu = firmware.find_cpu_nodes(new=True)
                    for k, v in properties.items():
                        firmware.set_node_property(path_to_cpu, k, v)
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = '.config'
        self.description = 'extract information from .config'
        self.required = ['srcode']
        self.context['hint'] = 'no .config available'
        self.critical = False
