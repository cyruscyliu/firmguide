import os


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

