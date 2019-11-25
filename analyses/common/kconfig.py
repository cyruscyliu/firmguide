import os
import re


def find_conditional_configs(makefile):
    a = {}
    with open(makefile) as f:
        for line in f:
            config = re.findall(r'.*-\$\((CONFIG_[_A-Z0-9]*)\).*', line)
            if len(config) == 1:
                sources = re.compile(r'[_a-z0-9\-]+\.o').findall(line)
                if not len(sources):
                    continue
                a[config[0]] = sources
    if len(a):
        return a
    else:
        return None


def find_all_conditional_configs(linux_kernel_dir):
    for root, dirs, files in os.walk(linux_kernel_dir):
        for file_ in files:
            if file_ == 'Makefile':
                print(find_conditional_configs(os.path.join(root, file_)))


find_all_conditional_configs('../build/15007/source_code/linux-2.6.32')
