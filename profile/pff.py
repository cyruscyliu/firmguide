from profile.dt import DTFirmware
from profile.ipxact import IPXACTFirmware
from profile.simple import SimpleFirmware
from profile.tinyft import TinyForTestFirmware


def get_firmware_in_profile(profile, **kwargs):
    if profile == 'simple':
        return SimpleFirmware(**kwargs)
    elif profile == 'dt':
        return DTFirmware(**kwargs)
    elif profile == 'ipxact':
        return IPXACTFirmware(**kwargs)
    elif profile == 'tiny':
        return TinyForTestFirmware(**kwargs)
    else:
        raise NotImplementedError
