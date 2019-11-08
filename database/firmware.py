import abc
import os

from profile.pff import get_firmware_in_profile


class DatabaseInterface(object):
    def __init__(self, *args, **kwargs):
        self.dbtype = None
        self.path = os.path.join(os.getcwd(), args[0])
        self.profile = kwargs.pop('profile')
        self.records = []
        self.count = 1
        self.header = None
        self.items = None  # for current line

    @abc.abstractmethod
    def parse_pre(self, line, **kwargs):
        pass

    @abc.abstractmethod
    def handle_post(self, firmware, **kwargs):
        pass

    def load(self, *args, **kwargs):
        with open(self.path) as f:
            for line in f:
                context = self.parse_pre(line.strip())
                # uuid, name, path, size
                if context is None:
                    continue
                firmware = get_firmware_in_profile(self.profile, **context)
                firmware.id = self.count
                self.handle_post(firmware)
                yield firmware
                self.count += 1

    def get_count(self, *args, **kwargs):
        return self.count

    def get_firmware(self, *args, **kwargs):
        for firmware in self.load(*args, **kwargs):
            yield firmware


class DatabaseFirmadyne(DatabaseInterface):

    def parse_pre(self, line, **kwargs):
        items = line.split(',')
        if self.header is None:
            self.header = items
            return
        kernel_extracted = items[self.header.index('kernel_extracted')]
        if kernel_extracted != 't':
            return
        uuid = items[self.header.index('id')]
        name = os.path.basename(items[self.header.index('filename')])
        path = items[self.header.index('filename')].replace('openwrt', 'firmware')
        size = os.path.getsize(path)
        brand = items[self.header.index('brand')]
        if not len(items[self.header.index('arch')]):
            arch = None
            endian = None
        else:
            arch = items[self.header.index('arch')][:-2]
            endian = items[self.header.index('arch')][-1:]
        # kernel_version: hard to use
        # kernel_version = items[self.header.index('kernel_version')]
        # if kernel_version:
        #     kernel_version = re.search(r'Linux kernel version (\d+\.\d+\.\d+)', kernel_version)
        # if kernel_version:
        #     kernel_version = kernel_version.groups()[0]
        description = items[self.header.index('description')]
        url = items[self.header.index('url')]
        self.items = {
            'uuid': uuid, 'name': name, 'path': path, 'size': size,
            'brand': brand, 'arch': arch, 'endian': endian,
            'description': description, 'url': url
        }
        return self.items

    def handle_post(self, firmware, **kwargs):
        firmware.preset_cache = [
            (firmware.set_brand, self.items['brand']),
            (firmware.set_description, self.items['description']),
            (firmware.set_url, self.items['url']),
            (firmware.set_architecture, self.items['arch']),
            (firmware.set_endian, self.items['endian'])
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbtype = 'firmadyne'


class DatabaseText(DatabaseInterface):
    def handle_post(self, firmware, **kwargs):
        firmware.preset_cache = [
            (firmware.set_brand, self.items['brand']),
            (firmware.set_architecture, self.items['arch']),
            (firmware.set_endian, self.items['endian'])
        ]

    def parse_pre(self, line, **kwargs):
        items = line.split()
        if self.header is None:
            self.header = items
            return
        uuid = items[self.header.index('uuid')]
        name = os.path.basename(items[self.header.index('path')])
        path = items[self.header.index('path')]
        size = os.path.getsize(path)
        brand = items[self.header.index('brand')]
        arch = items[self.header.index('arch')]
        endian = items[self.header.index('endian')]
        self.items = {
            'uuid': uuid, 'name': name, 'path': path, 'size': size,
            'brand': brand, 'arch': arch, 'endian': endian
        }
        return self.items

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dbtype = 'text'