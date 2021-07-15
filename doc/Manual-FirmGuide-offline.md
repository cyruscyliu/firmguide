Table of Contents
=================

   * [Manual Analysis](#manual-analysis)
      * [QEMU hw implementation template](#qemu-hw-implementation-template)
         * [Interrupt Controller](#interrupt-controller)
            * [State transition](#state-transition)
            * [Parameters details](#parameters-details)
            * [Where to infer parameters](#where-to-infer-parameters)
         * [Timer](#timer)
            * [State transition](#state-transition-1)
            * [Parameters details](#parameters-details-1)
            * [Where to infer parameters](#where-to-infer-parameters-1)
         * [MMIO Region](#mmio-region)
            * [Parameters details](#parameters-details-2)
            * [Where to infer parameters](#where-to-infer-parameters-2)
      * [Tools](#tools)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc)

# Manual Analysis

## QEMU hw implementation template

### Interrupt Controller

#### State transition

We will first briefly introduce several concepts.

We have defined three states and they are illustrated one by one in the
following.

+ REST

The Interrupt Controller is idle.

+ NOISE

There exist some interrupt requests.

+ ALARM

The interrupt Controller should file the interrupt to a processor.

At the same time, we defined several internal properties to label what
has happend for each interrupt source.

+ pending

The property of an interrupt request indicates that there exist a
interrupt request pending.

+ masked

The property of an interrupt request indicates whether or not it is
allowed to file the interrupt to a processor.

Finally, we have defined two internal actions to respond Linux kernel.
The two actions are used with qemu_setup_irq together.
+ set_irqn_to_regs will set the pending register to a specific value.
+ clear_irqn_to_regs will clear the pending register to a specific
+ value.
Linux kernel will read the pending register, calculate the interrupt
request number, and call its interrupt servise routine.

| state_from | pending | masked | state_to |                   action                   |
|:----------:|:-------:|:------:|:--------:|:------------------------------------------:|
|    REST    |    0    |    0   |   REST   |                                            |
|    REST    |    0    |    1   |   REST   |                                            |
|    REST    |    1    |    0   |   ALARM  |  set_irqn_to_regs(irqn) qemu_setup_irq(1)  |
|    REST    |    1    |    1   |   NOISE  |                                            |
|    NOISE   |    0    |    0   |   REST   | clear_irqn_to_regs(irqn) qemu_setup_irq(0) |
|    NOISE   |    0    |    1   |   REST   | clear_irqn_to_regs(irqn) qemu_setup_irq(0) |
|    NOISE   |    1    |    0   |   ALARM  |  set_irqn_to_regs(irqn) qemu_setup_irq(1)  |
|    NOISE   |    1    |    1   |   NOISE  |                                            |
|    ALARM   |    0    |    0   |   REST   | clear_irqn_to_regs(irqn) qemu_setup_irq(0) |
|    ALARM   |    0    |    1   |   REST   | clear_irqn_to_regs(irqn) qemu_setup_irq(0) |
|    ALARM   |    1    |    0   |   ALARM  |                                            |
|    ALARM   |    1    |    1   |   NOISE  | clear_irqn_to_regs(irqn) qemu_setup_irq(0) |

Here, we summarize the time when the too properties are changed. By the
way, xxx_action below is infered from Interrupt Controller low-level
callbacks.

| property | set/clear | when |
|:---:|:---:|:---:|
|pending|set|other peripheral has an interrrupt request|
|pending|clear|other peripheral cancles its interrrupt request|
|pending|clear|mask_ack_action happens|
|pending|clear|ack_action happens|
|masked|set|the interrupt controller is reset|
|masked|set|mask_ack_action happens|
|masked|set|mask_action happens|
|masked|clear|masked is clear when|
|masked|clear|unmask_action happens|

#### Parameters details

|      parameter     |                            |                         |  type  | description |
|:------------------:|:--------------------------:|:-----------------------:|:------:|:-----------:|
|       license      |     internal parameter     | automatically generated | string |             |
|        name        |      dynamic parameter     | automatically generated | string |             |
|     endianness     |      dynamic parameter     | automatically generated | string |             |
|         reg        |      dynamic parameter     | automatically generated |  dict  |             |
|        size        |         item of reg        | automatically generated | string |             |
|  intc_irqn_to_regs |       fixed parameter      |    manually generated   |  list  |             |
|  intc_irqn_to_reg  |  item of intc_irqn_to_regs |    manually generated   |  dict  | When an interrupt is triggered, Linux kernel will check a pending register in an interrupt controller to calculate the current interrupt request number. Figure out the way of calculation and the name of the pending register. |
|        irqn        |  item of intc_irqn_to_reg  |    manullay generated   | string |             |
|      set_body      |  item of intc_irqn_to_reg  |    manullay generated   | string |             |
|     clear_body     |  item of intc_irqn_to_reg  |    manullay generated   | string |             |
| intc_get_registers |       fixed parameter      |    manually generated   |  list  |             |
|      register      | item of intc_get_registers |    manually generated   |  dict  | An interrupt controller has several internal registers. Figure out the offset of name and the operation on them according to the low-level driver callbacks. |
|       offset       |      item of register      |    manullay generated   | string |             |
|        rname       |      item of register      |    manullay generated   | string |             |
|      mask_ack      |      item of register      |    manullay generated   |  bool  |             |
|   mask_ack_action  |      item of register      |    manullay generated   | string |             |
|        mask        |      item of register      |    manullay generated   |  bool  |             |
|     mask_action    |      item of register      |    manullay generated   | string |             |
|         ack        |      item of register      |    manullay generated   |  bool  |             |
|     ack_action     |      item of register      |    manullay generated   | string |             |
|       unmask       |      item of register      |    manullay generated   |  bool  |             |
|    unmask_action   |      item of register      |    manullay generated   | string |             |
|      override      |      item of register      |    manullay generated   |  bool  | Whether or not to update the internal register when Linux kernel write new a value. |

#### Where to infer parameters

+ irq_domain_add_simple
+ irq_domain_add_legacy
+ irq_domain_add_linear
+ __irq_domain_add
+ __irq_set_handler
+ irq_set_chained_handler
+ irq_set_chip_and_handler_name
+ irq_set_chained_handler_and_data
+ set_handle_irq (ARM)
+ plat_irq_dispatch (MIPS)

### Timer

#### State transition

The state transition of Timer is quite simple. There are two timers in
the tempate. The first timer will file the interrupt periodically; the
second timer is freely running and will be acquired by Linux kernel to
maintain a precise time.

#### Parameters details
|    parameter     |                        |                         |  type  | description |
|:----------------:|:----------------------:|:-----------------------:|:------:|:-----------:|
|     license      |   internal parameter   | automatically generated | string |             |
|      name        |   dynamic parameter    | automatically generated | string |             |
|   endianness     |   dynamic parameter    | automatically generated | string |             |
|       reg        |   dynamic parameter    | automatically generated |  dict  |             |
|      size        |     item of reg        | automatically generated | string |             |
|   timer_n_irq    |     fixed parameter    |    manually generated   | string | The number of interrupts this timer can trigger. |
|  timer_counters  |     fixed parameter    |    manually generated   |  list  |             |
|      counter     | item of timer_counters |    manually generated   |  dict  | The counter register information. Figuir out its interrupt id and its address. |
|       addr       |     item of counter    |    manullay generated   | string |             |
|        id        |     item of counter    |    manullay generated   | string |             |
| timer_increasing |     fixed parameter    |    manually generated   |  bool  | Whether or not the counter register increases. |
| timer_decreasing |     fixed parameter    |    manually generated   |  bool  | Whether or not the counter register decreases. |
|    timer_freq    |     fixed paramter     |    manually generated   | string |             |
|    timer_bits    |     fixed paramter     |    manually generated   | string | The valid bits of the counter. |

#### Where to infer parameters

+ clocksource_register_hz
+ clocksource_mmio_init
+ clocksource_register
+ __clocksource_register_scale
+ sched_clock_register
+ clockevents_config_and_register
+ clockevents_register_device
+ clk_register
+ clk_hw_register
+ clk_get_sys
+ clkdev_add
+ register_current_timer_delay

### MMIO Region

#### Parameters details

| parameter  |                   |                         |  type  | description |
|:----------:|:-----------------:|:-----------------------:|:------:|:-----------:|
|    name    | dynamic parameter | automatically generated | string |             |
| endianness | dynamic parameter | automatically generated | string |             |
|     id     | dynamic parameter | automatically generated | string |             |
|    regs    | dynamic parameter | automatically generated |  list  |             |
|    reg     |    item of regs   |    manually generated   |  item  |             |
| registers  |  fixed parameter  |    manually generated   |  list  |             |
|  register  | item of registers |    manually generated   |  item  | Some internal registers of the peripheral have to be initialized with proper value. Figure out their offset and the expected value. |
|   offset   | item of registers |    manually generated   |  item  |             |
|   value    | item of registers |    manually generated   |  item  |             |

#### Where to infer parameters

+ setup_arch
+ do_initcall_level

## Tools

We provide several subcommands for manual analysis.

First, try `traversrc` to pricisely traverse kernel function from
`start_kernel` to `rest_init`. The traversal in implemented by `sparse`
in AST level.  We only care about functions, such that global/local
variables are ignored in the traversal. Because of simple
implementation, conditions are also ignored, such that each callee in
the caller will be visited.  After the traversal, we will save all
interesting functions as `.slicing`.  Each recored in `.slicing`
consists of the function name, in which file the function is, and its
line number.

However, manual efforts are needed during the traversal because of
indirect calls.  You can use `-dtb` to solve indirect calls that go to
intc/timer initialization functions.  For remaining indirect calls you
have to update them manually by adding a record in `x.fcbs` in your
working directory.

In the traversal, we will list all interesting functions by `[unknown]`,
For your convenience, `traversrc` will save all `unknown` functions in
`0.fcbs`.  If `mach_desc.init_time` is an indirect call, add a record
below after running `tranversrc` in `1.fcbs`.  At the same time, please
`-a` to check intermediate functions whether they are visited,
otherwise, you should add file(s)/dir(s) that contain those functions
and rerun `traversrc`.  At last, you will see all interesting functions
in `.slicing`.

```
mach_desc.init_time:
  skipped: False,
  extend: [ox820_timer_init]
```

Second, use `analysrc` to locate interesting functions. It will
preprocess the file that has interesting functions for your convenience.

Third, look at all information in the front of this documentation to
infer paramaters.

