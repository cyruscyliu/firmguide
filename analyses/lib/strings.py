import os


def get_strings(firmware):
    """
    We get strings from uncompressed binary.

    :param firmware:
    :return: [strings] or None
    """
    strings = []
    # get candidate files which contain useful strings
    candidates = get_candidates(firmware)
    if candidates is None:
        return None
    for candidate in candidates:
        info = os.popen('strings {} -n 2 | grep -E "^[a-zA-Z]+[a-zA-Z0-9_-]{{1,20}}"'.format(candidate))
        strings += info.readlines()
    return strings


def get_candidates(firmware):
    """
    We can find useful strings in uncompressed binary.

    :param firmware: the firmware.
    :return: [paths/to/candidates] or None
    """
    kernel = firmware.get_path_to_kernel()
    if kernel is None:
        return None
    working_dir = os.path.dirname(kernel)
    candidates = [kernel]
    for file_ in os.listdir(working_dir):
        if file_.endswith('7z') or file_.endswith('xz'):
            zimage = os.path.join(working_dir, file_[:-3])
            if os.path.exists(zimage):
                candidates.append(zimage)
    return candidates