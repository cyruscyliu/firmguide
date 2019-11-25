import os

from analyses.common.analysis import Analysis


class Extraction(Analysis):
    def run(self, firmware):
        image_type = firmware.get_format()
        image_path = firmware.get_path_to_image()
        if image_type not in ['fit uImage', 'legacy uImage', 'trx kernel']:
            self.context['input'] = 'add support to this image type {}'.format(image_type)
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
            self.context['input'] = 'add support to this image type {}'.format(image_type)
            return False
        return True

    def __init__(self):
        super().__init__()
        self.name = 'extraction'
        self.description = 'extract kernel and dbt from the given firmware'
        self.log_suffix = '[EXTRACTION]'
        self.context['hint'] = 'the image type is unsupported'
        self.required = ['format']
        self.critical = True
