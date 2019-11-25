# Analysis

## Analysis Dependency and Exception

|file|analysis|settings|dependent on|exception|
|:---:|:---:|:---:|:---:|:---:|
|[format.py](./format.py)|format|format, path_to_image|-|you must tell binwalk to handle this new format|
|[extraction.py](./extraction.py)|extraction|path_to_kernel, path_to_dbt|format|you must add a tool to handle this new format|
|[kernel.py](./kernel.py)|kernel|kernel_version, kernel_created_time, kernel_load_address, kernel_entry_point|extraction|-|
|[device_tree.py](./device_tree)|dt|dtc|extraction|-|
|[openwrt.py](./openwrt.py)|url|homepage, target, subtarget, revision|-|update download url for this firmware|
|[openwrt.py](./openwrt.py)|revision|revision|kernel|no kernel version available or no handler for this kernel version|
|[openwrt.py](./openwrt.py)|toh|url|toh, cpu, ram, flash|-|
|[dot_config.py](./dot_config.py)|.config|cpu|srcode|-|

### get source code [srcode.py](./srcode.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|                   | firmware.brand is not None | firmware.path_to_source_code | Y |
|                   | firmware.revision is not None | | |
|                   | firmware.kernel_version is not None | | |
|                   | firmware.target is not None | | |
|                   | firmware.subtarget is not None | | |
|                   | firmware.working_dir is not None | | |


## source code

To manage source code, we provide several interfaces to fetch and cache them.

`find_url_for_kernel` accepts a kernel version string, say `2.6.30` and returns
its download link, `https://mirrors.edge.kernel.org/pub/linux/kernel/v2.6/linux-2.6.32.tar.gz`.
By default, the compression format is `tar.gz`.

'find_url_for_openwrt' accepts an openwrt reversion string, say `15.05` and returns
its source code download link, `https://github.com/openwrt/chaos_calmer/archive/v15.05.tar.gz`.


It is recommended to call `cache_package` which accepts a download link and cache
target directory. The function will check the cache target directory first, if the
package has not been cached, then this function will download the package. Finally, this
function will return the real path of the package.

```python
url = find_url_for_openwrt('15.05')
path_to_openwrt = cache_package(url, 'cache/openwrt')
```

Tools for source code analysis.
+ [pymake](https://github.com/mozilla/pymake), an implementation of the make tool
which are mostly compatible with makefiles written for GNU make, Mozilla.
+ [dr_checker](https://github.com/ucsb-seclab/dr_checker), a soundy vulnerability 
detection tool for Linux kernel drivers, ucsb.
