from database.dbf import get_database


def find_openwrt_toh(revision, target, subtarget):
    """
    Return the record if there is one and only one toh record meeting given conditions.
    """
    openwrt = get_database('openwrt')
    results = openwrt.select('*', supportedcurrentrel=revision, target=target, subtarget=subtarget)
    if len(results) == 1:
        return results[0], openwrt.header_last_selected
    else:
        return None, None
