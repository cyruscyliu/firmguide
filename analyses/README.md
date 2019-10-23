# Analysis

## Programming Model

In this module, you are expected to follow the programming model below
to reduce logs, and to support save and restore mechanism. Add and register a function, 
then the function will be called automatically. At the beginning, the model describes this task 
by `TASK_DESCRIPTION`,  and the `do_a` function must define a `LOG_SUFFIX` to label itself. Doing 
all above, we will get less logs and boost the performance. The model instruments every `do_a` function
by `finished` and `finish` to decide whether to execute it or not. The save and restore mechanism saves
lots of time and is friendly to debugging.
 
Each function you add and register should define its own preconditions which the firmware must be provide, 
and check these preconditions by itself. At the same time, each function should raise NotImplementationError
when the whole routine must stop because this firmware has not been supported yet.

```python
import logging
from manager import finished, finish

logger = logging.getLogger()
TASK_DESCRIPTION = 'do something'

__do_something = []

def do_a(firmware): # add a function, the one and only one parameter is firmware
    LOG_SUFFIX = 'do_a'
    logger.info('xxx {}'.format(LOG_SUFFIX))
    pass

def register_do_something(func):
    __do_something.append(func)
    
register_do_something(do_a) # register the function

def do_something(firmware): # called by top routine
    logger.info(TASK_DESCRIPTION)
    for func in __do_something:
        if finished(firmware, 'do_something', func.__name__):
            continue
        func(firmware) # call it automatically
        finish(firmware, 'do_something', func.__name__)
```

## Preconditions and Exception

### extract kernel and dtb [extraction.py](.|extraction.py)

|                | preconditions | settings | exception |
|:--------------:|:---:|:---:|:---:|
|   by binwalk   | firmware.working_dir is not None | firmware.format | Y |
|                | firmware.working_path is not None | firmware.path_to_image| |
|                | firmware.size is not None | | |
||||
| by uboot tools | firmware.format is 'fit uImage' or 'legacy uImage' | firmware.path_to_kernel | |
|                | firmware.path_to_image is not None | firmware.path_to_dtb | |
||||
|  by lzma tools | firmware.format is 'trx kernel' | firmware.path_to_kernel | |
|                | firmware.path_to_image is not None | firmware.path_to_dtb | |
    
### get metadata [metadata.py](.|metadata.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      by file      | firmware.format is 'legacy uImage' | firmware.kernel_version | |
|                   | firmware.path_to_image is not None | firmware.kernel_created_time | |
|                   |                                    | firmware.kernel_load_address | |
|                   |                                    | firmware.kernel_entry_point | |
||||
|    by dumpimage   | firmware.format is 'fit uImage' | firmware.kernel_created_time | |
|                   | firmware.path_to_image is not None | firmware.kernel_load_address | |
|                   |                                    | firmware.kernel_entry_point | |
||||
| by kernel version | firmware.kernel_version | firmware.revision | |
||||
|   by device tree  | firmware.path_to_dtb is not None | firmware.dts | |
|                   | firmware.revision is not None | firmware.toh | |
||||
|     by strings    | firmware.revision is not None | firmware.target | |
|                   |                               | firmware.subtarget | |
||||
|       by url      | firmware.brand is 'openwrt' | firmware.homepage | |
|                   |                             | firmware.target | |
|                   |                             | firmware.subtarget | |
    
### get source code [srcode.py](./srcode.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|                   | firmware.brand is not None | firmware.path_to_source_code | Y |
|                   | firmware.revision is not None | | |
|                   | firmware.kernel_version is not None | | |
|                   | firmware.target is not None | | |
|                   | firmware.subtarget is not None | | |
|                   | firmware.working_dir is not None | | |

### get cpu info [cpu.py](./cpu.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      global       | firmware.cpu_model is None | | | 
||||
|      by toh       | firmware.toh is not None | firmware.cpu_model | |
|                   |                          | firmware.soc_model | |

### get ram info [ram.py](./ram.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      global       | firmware.ram is None | | | 
||||
|      by toh       | firmware.toh is not None | firmware.ram | |
||||
|    by default     | firmware.ram_size is not 0 | firmware.ram | |

### get flash info [flash.py](./flash.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      global       | firmware.flash_model is None | | |
||||
|      by toh       | firmware.toh is not None | firmware.flash_type | |

### get uart info [uart.py](./uart.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      global       | firmware.uart_model is None | | |
||||
|    by strings     | | firmware.uart_model | |

### get ic info [ic.py](./ic.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      global       | firmware.ic_model is None | | |
||||
|    by strings     | | firmware.uart_model | |

### get timer info [timer.py](./timer.py)

|                   | preconditions | settings | exception |
|:-----------------:|:---:|:---:|:---:|
|      global       | firmware.timer_model is None | | |

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
