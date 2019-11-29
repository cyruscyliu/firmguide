# Salamander

Salamander is a project aiming to run and test any given firmware blob dynamically in a pure software way.

## Install

```shell script
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.7
sudo -H python3.7 -m pip install --upgrade pip
sudo -H pip3.7 install -r requirements.txt
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
sudo apt-get install -y libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev
sudo apt-get install -y libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev
sudo apt-get install -y libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev
sudo apt-get install -y librbd-dev librdmacm-dev
sudo apt-get install -y libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev
sudo apt-get install -y valgrind xfslibs-dev
sudo apt-get install -y libnfs-dev libiscsi-dev
sudo apt-get install -y bison flex
sudo apt-get install -y libcapstone3 libcapstone-dev
sudo apt-get install -y u-boot-tools
sudo apt-get install -y gawk
sudo make clean && make
```

## Start 

```shell script
usage: salamander.py [-h] [-p {simple,dt,ipxact}] [-wd WORKING_DIRECTORY] [-r]
                     [-d] [-f FIRMWARE] [-i ID] [-a--architecture {arm,mips}]
                     [-e {b,l}] [-b {openwrt}] [-dbt {text,firmadyne}]
                     [-l LIMIT] [-u UUID [UUID ...]] [-t TRACE]
                     [-tf {ktracer,qemudebug}]

optional arguments:
  -h, --help            show this help message and exit
  -p {simple,dt,ipxact}, --profile {simple,dt,ipxact}
                        assign the device profile standard
  -wd WORKING_DIRECTORY, --working_directory WORKING_DIRECTORY
                        assign the working directory for getting metadata, by default /tmp or %TEMP%
  -r, --rerun           ingore save and restore and rerun all analysis
  -d, --debug           show verbose logs

single analysis:
  -f FIRMWARE, --firmware FIRMWARE
                        path to firmware
  -i ID, --id ID        assign a id to the firmware
  -a--architecture {arm,mips}
                        assign the architecture
  -e {b,l}, --endian {b,l}
                        assign the endian
  -b {openwrt}, --brand {openwrt}
                        assign the brand of this firmware

massive analyses:
  -dbt {text,firmadyne}, --database_type {text,firmadyne}
                        assign the firmware db type
  -l LIMIT, --limit LIMIT
                        limit the amount of firmware to test
  -u UUID [UUID ...], --uuid UUID [UUID ...]
                        assign a uuid to a firmware in the firmware db

diagnosis:
  -t TRACE, --trace TRACE
                        assign a trace file
  -tf {ktracer,qemudebug}, --trace_format {ktracer,qemudebug}
                        assign a trace file format
```

To test your firmware.
```shell script
./salamander.py -f path/to/firmware -i 1 -a arm -e l -b openwrt
```

To test plenty of firmware.

```shell script
./salamander.py -dbt text -p dt -wd ./build
./salamander.py -dbt text -p dt -wd ./build -l 2 # run first 2
./salamander.py -dbt text -p dt -wd ./build -u UUID # run UUID in the database
```

NOTE: To disable `save and restore`, please use `-r`.

## Visualization

```shell script
python dashboard/__init__.py
```

![dashboard](./dashboard/dashboard.png)


## License
