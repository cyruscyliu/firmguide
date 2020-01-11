import os
import binwalk

from analyses.analysis import Analysis


class Binwalk(Analysis):
    def run(self, firmware):
        """
        The patched binwalk must be available.
        """
        # remove duplicated extraction sub-dirs
        os.system('rm -rf {}/*.extracted'.format(firmware.target_dir))

        for module in binwalk.scan(firmware.working_path, signature=True, extract=True,
                                   quiet=True, block=firmware.size, directory=firmware.target_dir):
            count = 0
            uimage3 = False
            uimage3_offset = 0
            for result in module.results:
                # some uimages are compress type 3 which QEMU does not support
                if result.description.lower().startswith('uimage') and result.stub0 == 3:
                    uimage3 = True
                    uimage3_offset = result.offset
                if str(result.description).find('flattened image tree') != -1:
                    self.info(firmware, 'FIT uImage found, offset {}, {}'.format(
                        result.offset, result.description), 1)
                    image_type = 'fit uImage'
                    image_path = module.extractor.output[result.file.path].carved[result.offset]
                    firmware.set_format(image_type)
                    firmware.set_path_to_image(image_path)
                    count += 1
                    break
                elif str(result.description).find('uImage') != -1:
                    self.info(firmware, 'Legacy uImage found, offset {}, {}'.format(
                        result.offset, result.description), 1)
                    image_type = 'legacy uImage'
                    image_path = module.extractor.output[result.file.path].carved[result.offset]
                    firmware.set_format(image_type)
                    firmware.set_path_to_image(image_path)
                    count += 1
                    break
                elif str(result.description).find('TRX') != -1:
                    self.info(firmware, 'TRX image found, offset {}, {}'.format(
                        result.offset, result.description), 1)
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
                self.context['input'] += '0x%.8X    %s\n' % (
                    result.offset, result.description)
            if not count:
                return False

            if uimage3:
                # reconstruct the uimage
                image_path = firmware.get_path_to_image()
                uncompressed_kernel = os.path.join(os.path.dirname(image_path), '{:x}'.format(uimage3_offset + 0x40))
                os.system('mv {0} {0}.bak'.format(image_path))
                os.system('dd if={0}.bak of={0} bs=1 count=64 >/dev/null 2>&1'.format(image_path))
                os.system('dd if=/dev/zero of={} bs=1 seek=31 count=1 >/dev/null 2>&1'.format(image_path))
                os.system('dd if={} of={} bs=1 seek=64 >/dev/null 2>&1'.format(uncompressed_kernel, image_path))
                # find dtb
                for module in binwalk.scan(image_path, signature=True, extract=True,
                                           quiet=True, block=os.path.getsize(image_path),
                                           directory=firmware.target_dir):
                    for result in module.results:
                        if str(result.description.lower()).find('mips built-in fdt') != -1:
                            self.info(firmware, 'MIPS built-in fdt, offset {:x}, {}'.format(
                                result.offset, result.description), 1)
                            dtb = module.extractor.output[result.file.path].carved[result.offset]
                            firmware.set_path_to_dtb(dtb)
                            self.info(firmware, 'get device tree image {} at {}'.format(
                                os.path.basename(dtb), dtb), 1)
                            break

            return True

    def __init__(self, analysis_manager):
        super().__init__(analysis_manager)
        self.name = 'format'
        self.description = 'check the format of the given firmware by binwalk'
        self.context['hint'] = 'binwalk does not recognize this new format'
        self.critical = True
        self.required = []
        self.settings = ['format', 'path_to_image']
