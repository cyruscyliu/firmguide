import os

from analyses.common.analysis import Analysis


class Extraction(Analysis):
    def run(self, firmware):
        image_type = firmware.get_format()
        image_path = firmware.get_path_to_image()
        if image_type not in ['fit uImage', 'legacy uImage', 'trx kernel']:
            return False
        if image_type == 'legacy uImage':
            kernel = image_path.replace('uimage', 'kernel')
            os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info('\033[32mget kernel image {} at {}\033[0m'.format(os.path.basename(kernel), kernel))
            firmware.set_path_to_dtb(None)
        elif image_type == 'fit uImage':
            kernel = image_path.replace('uimage.fit', 'kernel')
            dtb = image_path.replace('uimage.fit', 'dtb')
            os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info('\033[32mget kernel image {} at {}\033[0m'.format(os.path.basename(kernel), kernel))
            os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(image_path, dtb))
            firmware.set_path_to_dtb(dtb)
            self.info('\033[32mget device tree image {} at {}\033[0m'.format(os.path.basename(kernel), dtb))
        elif image_type == 'trx kernel':
            kernel = image_path.replace('trx', 'kernel')
            os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info('\033[32mget kernel image {} at {}\033[0m'.format(os.path.basename(kernel), kernel))
            firmware.set_path_to_dtb(None)
        else:
            return False
        return True

    def __init__(self):
        super().__init__()
        # basic
        self.description = 'extract kernel and dbt from the given firmware'
        self.name = 'extraction'
        # logging
        self.log_suffix = '[EXTRACTION]'
        # exception
        self.context['hint'] = 'you must add a tool to handle this new format'
        # requirement
        self.required = ['format']
