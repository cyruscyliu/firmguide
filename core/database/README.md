# Database

[db.py](./db.py) provide a simple interface for your database implementation. You are expected to realize
select, add, update and delete functions in your own database class. If you don't allowed users to
modify your data, you should raise NotImplementationError as a warning. Don't forget to add your database name
to [dbf.py](./dbf.py), and all database are expected obtained by the database factory.

###### example
```text
class DatabaseExample(Database):
    def select(self, *args, **kwargs):
        """
        # your usage in sql format
        """
        # your code

    def add(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def delete(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

    def update(self, *args, **kwargs):
        raise NotImplementedError('you are not expected to modify this table')

def get_database(dbtype, **kwargs):
    if dbtype == 'example':
        return DatabaseExample()
    else:
        raise NotImplementedError('the dbtype {} is not support yet'.format(dbtype))
```

### QEMU Devices

This is one of the key parts of Salamander. We have listed useful [devices](qemu.devices.yaml) in QEMU.


### OpenWRT

To support OpenWRT, we add [openwrt.csv](openwrt_toh.csv) and [openwrt.yaml](openwrt_rk.yaml) two databases.
+ [openwrt.csv](openwrt_toh.csv) is the table of hardware of OpenWRT
+ [openwrt.yaml](openwrt_rk.yaml) maintains the mapping between OpenWRT revision and kernel version
