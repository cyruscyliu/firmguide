import os

from analyses.analysis import Analysis


def replace_extension(path, src, dst):
    filename, file_extension = os.path.splitext(path)
    file_extension = file_extension.replace(src, dst)
    return filename + file_extension


class Extraction(Analysis):
    def run(self, firmware):
        image_type = firmware.get_format()
        image_path = firmware.get_path_to_image()
        if image_type not in ['fit uImage', 'legacy uImage', 'trx kernel']:
            self.context['input'] = 'add support to this image type {}'.format(image_type)
            return False
        if image_type == 'legacy uImage':
            kernel = replace_extension(image_path, 'uimage', 'kernel')
            os.system('dd if={} of={} bs=1 skip=64 >/dev/null 2>&1'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info(firmware, 'get kernel image {} at {}'.format(os.path.basename(kernel), kernel), 1)
            firmware.set_path_to_uimage(image_path)
        elif image_type == 'fit uImage':
            kernel = replace_extension(image_path, 'fit', 'kernel')
            dtb = image_path.replace('uimage.fit', 'dtb')
            os.system('dumpimage -T flat_dt -i {} -p 0 {} >/dev/null 2>&1'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info(firmware, 'get kernel image {} at {}'.format(os.path.basename(kernel), kernel), 1)
            uimage = replace_extension(image_path, 'fit', 'uimage')
            # mkimage -A arm -C none -O linux -T kernel -d path/to/zImage -a 0x8000 -e 0x8000
            #     path/to/uImage >/dev/null 2>&1
            if firmware.get_architecture() == 'arm':
                os.system('mkimage -A arm -C none -O linux -T kernel -d {} '
                          '-a 0x8000 -e 0x8000 {} >/dev/null 2>&1'.format(kernel, uimage))
                firmware.set_path_to_uimage(uimage)
            os.system('dumpimage -T flat_dt -i {} -p 1 {} >/dev/null 2>&1'.format(image_path, dtb))
            firmware.set_path_to_dtb(dtb)
            self.info(firmware, 'get device tree image {} at {}'.format(os.path.basename(kernel), dtb), 1)
        elif image_type == 'trx kernel':
            kernel = replace_extension(image_path, 'trx', 'kernel')
            os.system('lzma -d < {} > {} 2>/dev/null'.format(image_path, kernel))
            firmware.set_path_to_kernel(kernel)
            self.info(firmware, 'get kernel image {} at {}'.format(os.path.basename(kernel), kernel), 1)
            uimage = replace_extension(image_path, 'trx', 'uimage')
            if firmware.get_architecture() == 'arm':
                os.system('mkimage -A arm -C none -O linux -T kernel -d {} '
                          '-a 0x8000 -e 0x8000 {} >/dev/null 2>&1'.format(kernel, uimage))
            firmware.set_path_to_uimage(uimage)
        else:
            self.context['input'] = 'add support to this image type {}'.format(image_type)
            return False
        return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'extraction'
        self.description = 'extract kernel and dbt from the given firmware'
        self.context['hint'] = 'the image type is unsupported'
        self.required = ['format']
        self.critical = True
        self.settings = ['path_to_kernel', 'path_to_dbt']
