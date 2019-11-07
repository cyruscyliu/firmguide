# Salamander

This is a project aiming to run and test any given firmware blob dynamically in a pure software way.

## dependency

```bash
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
```

## install
```bash
make # sudo make clean first if fails
```

## start 

#### for a single firmware blob

not supported yet

#### for tons of firmware blob

Prepare a file or a table with firmware information in it, say [firmware.text](./database/firmware.text).
The firmware.text is in CSV format(in fact, space not comma), and you can use any other formats your like. 
This file shows a least set of attributes you should put in your own file or table for your firmware:
uuid, path, arch, endian, and brand.

```text
uuid path arch endian brand
9692 firmware/278a494b4a543f4a48dbb56d7ce226a23a3fbcc3.bin arm l openwrt
```

Create a class for your file or table, say `DatabaseText`. The class must inherit `DatabaseInterface`, and you
have to realize two functions: `parse_pre` and `handle_post`. You are expect to parse your file or table in
`parse_pre` and save what you get in `handle_post`.

Don\'t forget to tell the database factory [dbf.py](./database/dbf.py) the name of your file or table.

```python
def get_database(dbtype, **kwargs):
    if dbtype == 'text':
        return DatabaseText(os.path.join('database', 'firmware.text'), **kwargs)
```

NOTE: COPY YOUR FIRMWARE TO RIGHT POSITION

Test all firmware.

```shell script
./salamander.py -dbt text -p dt -wd ./build
```

Test limited firmware.

```shell script
./salamander.py -dbt text -p dt -wd ./build -l 2
```

NOTE: To disable `save and restore`, please use `-r`.

Test one specific analysis in the database.

```shell script
./salamander.py -dbt text -p dt -wd ./build -u UUID
```

NOTE: `-l LIMIT` and `-r` still work.  

Visualize analyses.

```shell script
python tools/web/easy.py # then, open tools/web/statistics.html
```

For more help.
```shell script
./salamander.py --help
```

# Testing

empty

# Authors

empty

# License

empty

