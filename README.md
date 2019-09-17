# Embedded System Virtualization 

## dependency

```bash
sudo -H pip3.7 install -r requirements.txt
sudo apt-get install -y git libglib2.0-dev libfdt-dev libpixman-1-dev zlib1g-dev
sudo apt-get install -y git-email
sudo apt-get install -y libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev
sudo apt-get install -y libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev
sudo apt-get install -y libibverbs-dev libjpeg8-dev libncurses5-dev libnuma-dev
sudo apt-get install -y librbd-dev librdmacm-dev
sudo apt-get install -y libsasl2-dev libsdl1.2-dev libseccomp-dev libsnappy-dev libssh2-1-dev
sudo apt-get install -y valgrind xfslibs-dev
sudo apt-get install -y libnfs-dev libiscsi-dev
sudo apt-get install -y bison flex
sudo apt-get install -y libcapstone3 libcapstone-dev
```

## install
```bash
make
```

## start
```bash
python3.7 main.py -dbt text -s1
```

