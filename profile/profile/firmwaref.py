from profile.simple import SimpleFirmware


def get_firmware_in_profile(profile, **kwargs):
    if profile == 'simple':
        return SimpleFirmware(**kwargs)
    else:
        raise NotImplementedError
