"""
Device tree solution.
"""
from profile.firmware import Firmware
import os
import fdt


class DTFirmware(Firmware):

    def get_soc_model(self, *args, **kwargs):
        root_node = self.profile.get_node('/')
        assert root_node is not None
        model = root_node.get_property('model').data[0]
        return model

    def set_soc_model(self, *args, **kwargs):
        soc = args[0]
        root_node = self.profile.get_node('/', create=True)
        root_node.append(fdt.PropStrings('model', soc))

    def get_toh(self, *args, **kwargs):
        if not len(args):
            return None
        toh = []
        brand_node = self.profile.get_node('/brand')
        assert brand_node is not None
        for property_ in args:
            value = brand_node.get_property(property_)
            if value is None:
                toh.append(value)
            else:
                toh.append(value.data[0])
        return toh

    def set_toh(self, *args, **kwargs):
        toh = args[0]
        assert isinstance(toh, dict)
        brand_node = self.profile.get_node('/brand', create=True)
        for k, v in toh.items():
            brand_node.append(fdt.PropStrings(k, v))

    def get_revision(self, *args, **kwargs):
        brand_node = self.profile.get_node('/brand')
        assert brand_node is not None
        revision = brand_node.get_property('revision').data[0]
        return revision

    def set_revision(self, *args, **kwargs):
        revision = args[0]
        brand_node = self.profile.get_node('/brand', create=True)
        brand_node.append(fdt.PropStrings('revision', revision))

    def get_dts(self, *args, **kwargs):
        return None

    def set_dts(self, *args, **kwargs):
        dt = args[0]
        self.profile.merge(dt)

    def set_profile(self, *args, **kwargs):
        if len(args):
            profile = args[0]
        else:
            profile = None
        first = kwargs.pop('first', False)
        working_dir = kwargs.pop('working_dir', None)

        if profile is not None:
            self.profile = profile
            return
        if working_dir is None:
            raise ValueError('please assign the working directory if no profile available')
        path_to_profile = os.path.join(working_dir, 'profile.dt')
        if first:
            with open(path_to_profile, 'w') as f:
                f.write('/dts-v1/;\n\n/ {\n};\n')
        with open(path_to_profile, 'r') as f:
            profile = f.read()
        self.profile = fdt.parse_dts(profile)

    def save_profile(self, *args, **kwargs):
        working_dir = kwargs.pop('working_dir', None)
        path_to_profile = os.path.join(working_dir, 'profile.dt')
        with open(path_to_profile, 'w') as f:
            f.write(self.profile.to_dts())

    def get_profile(self, *args, **kwargs):
        return self.profile

    def get_target(self, *args, **kwargs):
        brand_node = self.profile.get_node('/brand')
        assert brand_node is not None
        target = brand_node.get_property('target').data[0]
        return target

    def set_target(self, *args, **kwargs):
        target = args[0]
        brand_node = self.profile.get_node('/brand', create=True)
        brand_node.append(fdt.PropStrings('target', target))

    def get_subtarget(self, *args, **kwargs):
        brand_node = self.profile.get_node('/brand')
        assert brand_node is not None
        subtarget = brand_node.get_property('subtarget').data[0]
        return subtarget

    def set_subtarget(self, *args, **kwargs):
        subtarget = args[0]
        brand_node = self.profile.get_node('/brand', create=True)
        brand_node.append(fdt.PropStrings('subtarget', subtarget))

    def get_kernel_load_address(self, *args, **kwargs):
        kernel_node = self.profile.get_node('/kernel')
        assert kernel_node is not None
        kernel_load_address = kernel_node.get_property('kernel_load_address').data[0]
        return kernel_load_address

    def set_kernel_load_address(self, *args, **kwargs):
        kernel_load_address = args[0]
        kernel_node = self.profile.get_node('/kernel', create=True)
        kernel_node.append(fdt.PropStrings('kernel_load_address', kernel_load_address))

    def get_kernel_version(self, *args, **kwargs):
        kernel_node = self.profile.get_node('/kernel')
        assert kernel_node is not None
        kernel_version = kernel_node.get_property('kernel_version').data[0]
        return kernel_version

    def set_kernel_version(self, *args, **kwargs):
        kernel_version = args[0]
        kernel_node = self.profile.get_node('/kernel', create=True)
        kernel_node.append(fdt.PropStrings('kernel_version', kernel_version))

    def get_kernel_created_time(self, *args, **kwargs):
        kernel_node = self.profile.get_node('/kernel')
        assert kernel_node is not None
        kernel_created_time = kernel_node.get_property('kernel_created_time').data[0]
        return kernel_created_time

    def set_kernel_created_time(self, *args, **kwargs):
        kernel_created_time = args[0]
        kernel_node = self.profile.get_node('/kernel', create=True)
        kernel_node.append(fdt.PropStrings('kernel_created_time', kernel_created_time))

    def get_kernel_entry_point(self, *args, **kwargs):
        kernel_node = self.profile.get_node('/kernel')
        assert kernel_node is not None
        kernel_entry_point = kernel_node.get_property('kernel_entry_point').data[0]
        return kernel_entry_point

    def set_kernel_entry_point(self, *args, **kwargs):
        kernel_entry_point = args[0]
        kernel_node = self.profile.get_node('/kernel', create=True)
        kernel_node.append(fdt.PropStrings('kernel_entry_point', kernel_entry_point))

    def get_cpu_model(self, *args, **kwargs):
        cpus = self.profile.get_node('/cpus')
        assert cpus is not None
        for cpu in cpus.nodes:
            return cpu.get_property('compatible').data[0]

    def set_cpu_model(self, *args, **kwargs):
        cpu_model = args[0]
        cpu = self.profile.get_node('/cpus/cpu@0', create=True)
        cpu.append(fdt.PropBytes('reg', 0x0))
        cpu.append(fdt.PropStrings('compatible', cpu_model))
        cpu.append(fdt.PropStrings('device_type', 'cpu'))

    def get_ram(self, *args, **kwargs):
        ram = self.profile.get_node('/memory')
        assert ram is not None
        ram_base, ram_size = ram.get_property('reg').data
        return ram_base, ram_size / 1024  # to MiB

    def set_ram(self, *args, **kwargs):
        ram_base, ram_size = args
        unit = kwargs.pop('unit', 'MiB')
        ram = self.profile.get_node('/memory', create=True)
        factor = 1024
        ram.remove_property('reg')
        ram.append(fdt.PropWords('reg', int(ram_base) * factor, int(ram_size) * factor))

    def get_interrupt_controller(self, *args, **kwargs):
        pass

    def set_interrupt_controller(self, *args, **kwargs):
        pass

    def get_flash(self, *args, **kwargs):
        pass

    def set_flash(self, *args, **kwargs):
        pass

    def get_uart(self, *args, **kwargs):
        pass

    def __init__(self, *args, **kwargs):
        super(DTFirmware, self).__init__(*args, **kwargs)
