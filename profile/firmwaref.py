from profile.simple import SimpleFirmware


def get_firmware(profile, **kwargs):
    if profile == 'simple':
        return SimpleFirmware(**kwargs)
    else:
        raise NotImplementedError
