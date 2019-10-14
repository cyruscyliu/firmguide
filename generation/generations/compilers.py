import abc


class CompilerToQEMU(object):
    def __init__(self):
        self.license = ['/* \n * automatically generated, don\'t change\n */\n']

    @staticmethod
    def render_function(function):
        lines = []
        lines.extend(function['signature'])
        lines.append('\n')
        lines.append('{\n')
        if function['declaration']:
            lines.extend(function['declaration'])
        for line in function['body']:
            lines.append(line + '\n')
        lines.append('}\n')
        return lines

    @abc.abstractmethod
    def solve_makefile(self, firmware):
        pass

    @abc.abstractmethod
    def solve(self, firmware):
        pass

    @abc.abstractmethod
    def link(self, firmware):
        pass

    @abc.abstractmethod
    def install(self, firmware):
        pass

    @abc.abstractmethod
    def run(self, firmware):
        pass


class CompilerToQEMUMachine(CompilerToQEMU):
    def install(self, firmware):
        pass

    def run(self, firmware):
        pass

    def solve_makefile(self, firmware):
        pass

    def solve(self, firmware):
        self.solve_define_machine(firmware)
        self.solve_machine_class_init(firmware)

    def __init__(self):
        super().__init__()
        self.machine = {'fields': [], 'headers': []}
        self.machine_macro = {}
        self.machine_class_init = {'signature': [], 'declaration': [], 'body': []}
        self.machine_init = {'signature': [], 'declaration': [], 'body': []}

    def solve_machine_class_init(self, firmware):
        machine_desc = firmware.sget_machine_description()
        machine_name = firmware.sget_machine_name()
        architecture = firmware.sget_architecture()
        ram_size = firmware.iget_ram_size()
        cpu_model = firmware.sget_cpu_model()

        self.machine_class_init['signature'] = ['static void {}_machine_init(MachineClass *mc)'.format(machine_name)]
        self.machine_class_init['declaration'] = None
        self.machine_class_init['body'] = [
            '    /* mc->family = ; */',
            '    /* mc->name = "{}"; */'.format(machine_name),
            '    /* mc->alias = ; */',
            '    mc->desc = "{}";'.format(machine_desc),
            '    /* mc->deprecation_reason = ; */',
            '    mc->init = {}_init;'.format(machine_name),
            '    /* mc->reset = ; */',
            '    /* mc->hot_add_cpu = ; */',
            '    /* mc->kvm_type = ; */',
            '    /* mc->block_default_type = ; */',
            '    /* mc->units_per_default_bus = ; */',
            '    /* mc->max_cpus = ; */',
            '    /* mc->min_cpus = ; */',
            '    /* mc->default_cpus = ; */',
            '    /* mc->no_serial = 1; */',
            '    /* mc->no_paralled = 1; */',
            '    /* mc->no_floppy = 1; */',
            '    /* mc->no_cdrom = 1; */',
            '    /* mc->no_sdcard = 1; */',
            '    /* mc->pci_allow_0_address = 1; */',
            '    /* mc->legacy_fw_cfg_order = 1; */',
            '    /* mc->is_dault = ; */',
            '    /* mc->default_machine_opts = ; */',
            '    /* mc->default_boot_order = ; */',
            '    /* mc->default_display = ; */',
            '    /* mc->compat_props = ; */',
            '    /* mc->hw_version = ; */',
            '    mc->default_ram_size = {};'.format(ram_size),
            '    mc->default_cpu_type = {}_CPU_TYPE_NAME("{}");'.format(architecture.upper(), cpu_model),
            '    /* mc->default_kernel_irqchip_split = ; */',
            '    /* mc->option_rom_has_mr = ; */',
            '    /* mc->minimum_page_bits = ; */',
            '    /* mc->has_hotpluggable_cpus = ; */',
            '    mc->ignore_memory_transaction_failures = false;',
            '    /* mc->numa_mem_align_shift = ; */',
            '    /* mc->valid_cpu_types = ; */',
            '    /* mc->allowed_dynamic_sysbus_devices = ; */',
            '    /* mc->auto_enable_numa_with_memhp = ; */',
            '    /* mc->numa_auto_assign_ram = ; */',
            '    /* mc->ignore_boot_device_suffixes = ; */',
            '    /* mc->smbus_no_migration_support = ; */',
            '    /* mc->nvdimm_supported = ; */',
            '    /* mc->get_hotplug_handler = ; */',
            '    /* mc->cpu_index_to_instance_props = ; */',
            '    /* mc->CPuArchIdList = ; */',
            '    /* mc->get_default_cpu_node_id = ; */',
        ]

    def solve_define_machine(self, firmware):
        machine_name = firmware.sget_machine_name()
        self.machine_macro['define_machine'] = [
            'DEFINE_MACHINE(\"{}\", {}_machine_init)'.format(machine_name, machine_name)]

    def render_device(self, **context):
        context = {'device_state': 'XXXState', 'device_filed': 'xxx', 'device_header': 'xxx.h',
                   'device_type': 'TYPE_XXX',
                   'device_mmio_base': 0}
        self.machine['fields'].append('    {} {};'.format(context['device_state'], context['device_filed']))
        self.machine['headers'].append('#include "{}"'.format(context['device_header']))
        error = 'Error *err = NULL;'
        if error not in self.machine_init['declaration']:
            self.machine_init['declaration'].append(error)
        self.machine_init['body'].extend([
            'sysbus_init_child_obj(obj, "{0}", &s->{0}, sizeof(s->{0}), {1});'.format(
                context['device_filed'], context['device_type']),
            'object_property_set_bool(OBJECT(&s->{}), true, "realized", &err);'.format(context['device_filed']),
            'sysbus_mmio_map(SYS_BUS_DEVICE(&s->{}), 0, {});'.format(context['device_filed'],
                                                                     context['device_mmio_base']),
        ])

    def link(self, firmware):
        lines = []
        lines.extend(self.license)
        lines.append('\n')
        lines.extend(self.render_function(self.machine_class_init))
        lines.append('\n')
        lines.extend(self.machine_macro['define_machine'])
        return ''.join(lines)
