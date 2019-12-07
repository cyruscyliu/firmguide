from profile.dt import DTFirmware
from profile.simple import SimpleFirmware
from profile.tinyft import TinyForTestFirmware


def get_firmware_in_profile(profile, **kwargs):
    if profile == 'dt':
        return DTFirmware(**kwargs)
    elif profile == 'simple':
        return SimpleFirmware(**kwargs)
    elif profile == 'tiny':
        return TinyForTestFirmware(**kwargs)
    else:
        raise NotImplementedError
