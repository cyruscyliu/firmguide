import os

def parse(components):
    """
    once a firmware cannot be supported, we would display some hints
    for you to seek suitable source code
    """
    pass

def get_candidates(self, path):
    """
    We can find useful strings in uncompressed files related to a file.
    :param path: path to the file
    :return: [paths/to/candidates] or None
    """
    if path is None:
        return None

    working_dir = os.path.dirname(path)
    candidates = [path]
    for file_ in os.listdir(working_dir):
        if file_.endswith('7z') or file_.endswith('xz'):
            uncompressed = os.path.join(working_dir, file_[:-3])
            if os.path.exists(uncompressed):
                candidates.append(umcompressed)
    return candidates

def get_all_strings(self, candidates):
    """
    We get strings from uncompressed binary.
    :param candidates: return of get_candidates()
    :return: [strings] or None
    """
    strings = []
    if candidates is None:
        return None

    for candidate in candidates:
        info = os.popen('strings {} -n 2 | grep -E "^[a-zA-Z]+[a-zA-Z0-9_-]{{1,20}}"'.format(candidate))
        strings += info.readlines()
    return strings

