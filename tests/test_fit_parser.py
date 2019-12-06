from unittest import TestCase

from analyses.fit import fit_parser

example = """
FIT description: ARM OpenWrt FIT (Flattened Image Tree)
Created:         Sat Sep 12 01:13:52 2015
 Image 0 (kernel@1)
  Description:  ARM OpenWrt Linux-3.18.20
  Created:      Sat Sep 12 01:13:52 2015
  Type:         Kernel Image
  Compression:  uncompressed
  Data Size:    2988352 Bytes = 2918.31 kB = 2.85 MB
  Architecture: ARM
  OS:           Linux
  Load Address: 0x60008000
  Entry Point:  0x60008000
  Hash algo:    crc32
  Hash value:   bb7fe659
  Hash algo:    sha1
  Hash value:   8b1986ad81f17b94f355b1724a482496877f877a
 Image 1 (fdt@1)
  Description:  ARM OpenWrt kd20 device tree blob
  Created:      Sat Sep 12 01:13:52 2015
  Type:         Flat Device Tree
  Compression:  uncompressed
  Data Size:    8091 Bytes = 7.90 kB = 0.01 MB
  Architecture: ARM
  Hash algo:    crc32
  Hash value:   c2f4f5a9
  Hash algo:    sha1
  Hash value:   13de26cd9ac3e38c4073f010be71eac4f1915640
 Default Configuration: 'config@1'
 Configuration 0 (config@1)
  Description:  OpenWrt
  Kernel:       kernel@1
  FDT:          fdt@1
 """


class TestFitParser(TestCase):
    def test_fit_parser(self):
        fit = fit_parser(example.split('\n'))
        self.assertIn('kernel@1', fit['images'])
        self.assertIn('fdt@1', fit['images'])
        self.assertEqual('config@1', fit['configurations']['default configuration'])
        self.assertEqual('kernel@1', fit['configurations']['config@1']['kernel'])
        self.assertEqual('fdt@1', fit['configurations']['config@1']['fdt'])

