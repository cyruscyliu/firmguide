Table of Contents
=================

   * [Development](#development)
      * [Add analysis (group)](#add-analysis-group)
      * [APIs for analysis (group)](#apis-for-analysis-group)
         * [Analysis Manager](#analysis-manager)
         * [Frimware profile getter/setter](#frimware-profile-gettersetter)
         * [Components getter/setter](#components-gettersetter)
         * [Device tree parsers (dt_parsers)](#device-tree-parsers-dt_parsers)
         * [Database](#database)
         * [QEMU controller](#qemu-controller)
         * [Source controller](#source-controller)
      * [Add subcommand](#add-subcommand)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Development

## Add analysis (group)

An analysis focuses on a specific task, such as parsing a device tree blob,
which is the basic schedule unit in FirmGuide. Each analysis is a Python
class and all of them are put under `slcore/analysis`.
Several analyses work together as an analysis group that is more powerful
to accomplish a complex task. The group of analysis is defined in `slcore/aconfigs`.

Here is the template of an analysis.
```Python
# slcore/analyses/analysis_name.py
from slcore.amanager import Analysis

class AnalysisClassName(Analysis):
      def __init__(self, analysis_manager):
         super().__init__(analysis_manager)
         self.name = 'analysis_name'
         self.description = 'analysis description'
         self.required = []  # what other analysis that should be executed in advance

      def run(self):
         return True
```

Here is an example of the analysis group definition.

```yaml
# touch slcore/aconfigs/plugins/xxx.a.yaml
AnalysisGroupClassName:
   analyses: [AnalysisClassName1, AnalysisClassName2, AnalysisClassName3]
   description: 'analysis group description'
```

## APIs for analysis (group)

### Analysis Manager

```python
def run(self, **kwargs):
    # get details of the project
    self.analysis_manager.project.attrs['path']
    self.analysis_manager.project.attrs['base_dir']
    # log
    self.warning('message', 1)
    self.info('message', 1)
    self.debug('message', 1)
    # return False after setting an error information
    if False:
        self.error_info = 'error_info'
        return False
    return True
```

### Frimware profile getter/setter

```python
def run(self, **kwargs):
    self.analysis_manager.firmware.get_realdtb() # set_realdtb('path')
    self.analysis_manager.firmware.get_machine_name() # set_machine_name('plx-nas782x')
    self.analysis_manager.firmware.get_arch() # set_arch('arm')
    self.analysis_manager.firmware.get_endian() # set_endian('l')
    self.analysis_manager.firmware.get_components() # set_components(components)
    return True
```

### Components getter/setter

```python
def run(self, **kwargs):
    components = self.analysis_manager.firmware.get_components()

    components.get_path_to_raw() # set_path_to_raw('path')
    components.get_type() # set_type(LEGACY_UIMAGE)
    components.get_path_to_kernel() # set_path_to_kernel('path')
    components.get_path_to_dtb() #  et_path_to_dtb('path')
    components.get_path_to_uimage() # set_path_to_uimage('path')
    return True
```

### Device tree parsers (dt_parsers)

```python
from slcore.dt_parsers.common import load_dtb
from slcore.dt_parsers.compatible import find_compatible_in_fdt
from slcore.dt_parsers.cpu import find_flatten_cpu_in_fdt
from slcore.dt_parsers.serial import find_flatten_serial_in_fdt
from slcore.dt_parsers.intc import find_flatten_intc_in_fdt
from slcore.dt_parsers.timer import find_flatten_timer_in_fdt
from slcore.dt_parsers.flash import find_flatten_flash_in_fdt
from slcore.dt_parsers.misc import find_flatten_misc_in_fdt
from slcore.dt_parsers.memory import find_flatten_ram_in_fdt
from slcore.dt_parsers.mmio import find_flatten_mmio_in_fdt

def run(self, **kwargs):
    dtb = self.analysis_manager.firmware.get_realdtb()
    dts = load_dtb(dtb)
    
    find_compatible_in_fdt(dts)
    find_flatten_cpu_in_fdt(dts)
    find_flatten_serial_in_fdt(dts)
    find_flatten_intc_in_fdt(dts)
    find_flatten_timer_in_fdt(dts)
    find_flatten_flash_in_fdt(dts)
    find_flatten_misc_in_fdt(dts)
    find_flatten_ram_in_fdt(dts)
    find_flatten_mmio_in_fdt(dts)
    return True
```

### Database

Please check the implementation of [brick.py](../slcore/brick.py#L311).

### QEMU controller

Please check the implementation of [install.py](../slcore/analyses/install.py#L20).

### Source controller

Please check the implementation of [quicksrc.py](../slcore/analyses/quicksrca.py#L17)
and [ktraversal.py](../slcore/analyses/ktraversal.py#L164).

## Add subcommand

A subcommand focuses on a specific user interface,
such as uploading and booting a firmware image.
The subcommand is registered in `slcore/cmdconfigs`.

Here is an example of the subcommand registration.

```yaml
touch slcore/cmdconfigs/plugins/xxx.cmd.yaml
subcommand:
   help: "Subcommand help information"
   optional:
      opt1:
            short: o1
            # prop: val
   callback: lower_case_of_analysis_class_name_or_analysis_group_class_name
```

Note that the `prop` and `val` should follow the argument list in
[argparse.add_argument()](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument).

