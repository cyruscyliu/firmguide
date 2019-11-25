import binwalk

from analyses.common.analysis import Analysis


class Format(Analysis):
    def run(self, firmware):
        """
        The patched binwalk must be available.
        """
        for module in binwalk.scan(firmware.working_path, signature=True, extract=True,
                                   quiet=True, block=firmware.size, directory=firmware.working_dir):
            count = 0
            for result in module.results:
                if str(result.description).find('flattened image tree') != -1:
                    self.info('\033[32mFIT uImage found, offset {}, {}\033[0m'.format(
                        result.offset, result.description))
                    image_type = 'fit uImage'
                    image_path = module.extractor.output[result.file.path].carved[result.offset]
                    firmware.set_format(image_type)
                    firmware.set_path_to_image(image_path)
                    count += 1
                    break
                elif str(result.description).find('uImage') != -1:
                    self.info('\033[32mLegacy uImage found, offset {}, {}\033[0m'.format(
                        result.offset, result.description))
                    image_type = 'legacy uImage'
                    image_path = module.extractor.output[result.file.path].carved[result.offset]
                    firmware.set_format(image_type)
                    firmware.set_path_to_image(image_path)
                    count += 1
                    break
                elif str(result.description).find('TRX') != -1:
                    self.info('\033[32mTRX image found, offset {}, {}\033[0m'.format(
                        result.offset, result.description))
                    image_type = 'trx kernel'
                    # because *.trx will be overwrote by *.7z, we replace 7z with trx here
                    image_path = module.extractor.output[result.file.path].carved[result.offset].replace('7z', 'trx')
                    firmware.set_format(image_type)
                    firmware.set_path_to_image(image_path)
                    count += 1
                    break
                else:
                    image_type = 'unknown'
                    firmware.set_format(image_type)
                self.context['hint'] += '0x%.8X    %s\n' % (
                    result.offset, result.description)
            if not count:
                return False
            else:
                return True

    def __init__(self):
        super().__init__()
        self.name = 'format'
        self.description = 'check the format of the given firmware by binwalk'
        self.log_suffix = '[BINWALK]'
        self.context['hint'] = 'binwalk does not recognize this new format'
        self.critical = True
        self.required = []