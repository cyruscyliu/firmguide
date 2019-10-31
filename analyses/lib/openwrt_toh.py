from database.dbf import get_database


def find_openwrt_toh(revision, target, subtarget):
    openwrt = get_database('openwrt')
    results = openwrt.select('*', supportedcurrentrel=revision, target=target, subtarget=subtarget)
    print(results)
