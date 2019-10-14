import yaml
import os


def load_machine(path):
    with open(path, encoding='utf-8') as f:
        machine = yaml.safe_load(f)
    return machine


def load_machines(dir_=None, file_=None):
    if dir_ is None and file_ is None:
        raise ValueError('No available machines!')

    machines = []
    if dir_ is not None:
        if not os.path.isdir(dir_):
            raise ValueError('Invalid directory.')
        files = os.listdir(dir_)
        files.remove(os.path.basename(__file__))
        files.remove('__pycache__')
        for machine in files:
            machines.append(load_machine(os.path.join(dir_, machine)))
        return machines

    if file_ is not None:
        if not os.path.isfile(file_):
            raise ValueError('Invalid file.')
        machines.append(load_machine(file_))
        return machines


if __name__ == '__main__':
    print(load_machines('..\\machines'))
