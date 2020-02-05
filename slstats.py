#!/usr/bin/python

from slcore.profile.stats import statistics
from slcore.profile.firmwaref import get_firmware

def run():
    firmware = get_firmware('simple')
    statistics(firmware)

if __name__ == '__main__':
    run()
