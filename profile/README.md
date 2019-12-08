# Device Profile

### Device Tree

We refer to [this](https://www.devicetree.org) and
[device tree in yaml](https://lwn.net/Articles/730217).

### IP-XACT

We refer to this [user guid](https://www.accellera.org/images/downloads/standards/ip-xact/IP-XACT_User_Guide_2018-02-16.pdf).
The IP-XACT standard provides for a consistent, machine readable description of an individual IP 
or system of interconnected IPs. The fact that IP descriptions are written to adhere to specific 
set of syntax and semantic rules, as defined in the standard, means that design tools and scripts 
can leverage these "electronic databooks" for documentation generation, test generation,
system assembly, script generation for tools flows, or any other operation that typically requires 
knowledge about the key details defining IP components.

### Format

To simplify the code generation task, 
we define our device format using yaml syntax and Device Tree syntax as below.

#### YAML Syntax

Take [2b38a3.yaml](../tests/files/2b38a3.yaml), [ec5859.yaml](../tests/files/ec5859.yaml), 
and [9874f6.yaml](../tests/files/9874f6.yaml) as examples.

#### Device Tree Syntax
Take [2b38a3.dt](../tests/files/2b38a3.dt), [ec5859.dt](../tests/files/ec5859.dt), 
and [9874f6.dt](../tests/files/9874f6.dt) as examples.

### Converting

We support the converting between different formats of device profiles.

```shell script
./profile/convert.py -I simple -O dt tests/files/ec5859.yaml
./profile/convert.py -I simple -O dt tests/files/2b38a3.yaml
./profile/convert.py -I simple -O dt tests/files/9874f6.yaml
./profile/convert.py -I dt -O simple tests/files/2b38a3.dt -o 2b38a3.yaml # to avoid override
./profile/convert.py -I dt -O simple tests/files/2b38a3.dt -o 2b38a3.yaml # to avoid override
./profile/convert.py -I dt -O simple tests/files/9874f6.dt -o 9874f6.yaml # to avoid override
```
