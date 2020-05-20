import os


def parse_openwrt_url(url):
    homepage = os.path.dirname(url)

    items = homepage.split('/')
    revision = items[4]
    target = items[5]
    subtarget = None
    if len(items) >= 7:
        subtarget = items[6]

    if target in ['targets']:
        target = subtarget

    return revision, target, subtarget
