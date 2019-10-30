import os


def parser_proc_info_init(path_to_assembly_file):
    """
    Only for ARM32.
    """
    lines = []
    # pre-processor
    partial_line = ''
    partial_line_flag = False
    with open(path_to_assembly_file) as f:
        for line in f:
            if not len(line.strip()):  # empty
                continue
            line = line.strip()
            if line.startswith('#'):  # conditional compilation
                continue
            if line.startswith('/') or line.startswith('*'):
                continue
            if not partial_line_flag and line.endswith('\\'):
                partial_line = line[:-1]
                partial_line_flag = True
                continue
            if partial_line_flag and line.endswith('\\'):
                partial_line += line[:-1]
                continue
            if partial_line and not line.endswith('\\'):
                partial_line += line
                partial_line_flag = False
                line = partial_line
                partial_line = ''
            if not partial_line_flag:
                lines.append(line)
    # get labels
    labels = {}
    i = 0
    while i + 1 < len(lines):
        line = lines[i]
        a, _, b = line.partition(':')
        label = a
        if line.find('.asciz') != -1:
            a, _, line_string = line.partition(':')
            line_string = line_string.strip()
        else:
            line_string = lines[i + 1]
        if line_string.startswith('.asciz'):
            _, _, string = line_string.partition('"')
            labels[label] = string[:-1]
            i += 2
        elif line_string.startswith('.ascii'):
            labels[label] = line_string.split()[1]
            i += 2
        else:
            i += 1
    if not len(labels):
        return None

    # get cpus
    cpus = {}
    section_flag = False
    i = 0
    while i + 13 < len(lines):
        line = lines[i]
        if line.find('.proc.info.init') != -1:
            section_flag = True
            i += 1
            continue
        if not section_flag:
            i += 1
            continue
        a, _, b = line.partition(':')
        label = a
        if not len(_):
            i += 1
            continue
        for j in range(0, 10):
            if lines[i + j].startswith('b'):
                break

        cpu_id = lines[i + 1].split()[1]
        cpu_mask = lines[i + 2].split()[1]
        cpu_arch_name = labels[lines[i + j + 1].split()[1]]
        cpu_elf_name = labels[lines[i + j + 2].split()[1]]
        cpu_name = labels[lines[i + j + 4].split()[1]]
        i += 13
        cpus[label] = {'cpu_id': cpu_id, 'cpu_mask': cpu_mask, 'cpu_arch_name': cpu_arch_name,
                       'cpu_elf_name': cpu_elf_name, 'cpu_name': cpu_name}
        section_flag = False
    return cpus
