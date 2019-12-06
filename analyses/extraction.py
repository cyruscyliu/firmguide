import os

from analyses.analysis import Analysis


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
            self.info(firmware, 'get kernel image {} at {}'.format(os.path.basename(kernel), kernel), 1)
            firmware.set_path_to_uimage(image_path)
            firmware.set_path_to_dtb(None)
        elif image_type == 'fit uImage':
            kernel = image_path.replace('uimage.fit', 'kernel')
            dtb = image_path.replace('uimage.fit', 'dtb')
            os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info(firmware, 'get kernel image {} at {}'.format(os.path.basename(kernel), kernel), 1)
            uimage = image_path.replace('uimage.fit', 'uimage')
            # mkimage -A arm -C none -O linux -T kernel -d path/to/zImage -a 0x8000 -e 0x8000
            #     path/to/uImage >/dev/null 2>&1
            os.system('mkimage -A {} -C none -O linux -T kernel -d {} '
                      '-a 0x8000 -e 0x8000 {} >/dev/null 2>&1'.format(firmware.get_architecture(), kernel, uimage))
            os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(image_path, dtb))
            firmware.set_path_to_uimage(uimage)
            firmware.set_path_to_dtb(dtb)
            self.info(
                firmware, 'get device tree image {} at {}'.format(os.path.basename(kernel), dtb), 1)
        elif image_type == 'trx kernel':
            kernel = image_path.replace('trx', 'kernel')
            os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info(firmware, 'get kernel image {} at {}'.format(os.path.basename(kernel), kernel), 1)
            uimage = image_path.replace('trx', 'uimage')
            os.system('mkimage -A {} -C none -O linux -T kernel -d {} '
                      '-a 0x8000 -e 0x8000 {} >/dev/null 2>&1'.format(firmware.get_architecture(), kernel, uimage))
            firmware.set_path_to_uimage(uimage)
            firmware.set_path_to_dtb(None)
        else:
            self.context['input'] = 'add support to this image type {}'.format(image_type)
            return False
        return True

    def __init__(self):
        super().__init__()
        self.name = 'extraction'
        self.description = 'extract kernel and dbt from the given firmware'
        self.context['hint'] = 'the image type is unsupported'
        self.required = ['format']
        self.critical = True
