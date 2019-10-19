import os

from unittest import TestCase
from pyquery import PyQuery as pq


class TestPyquery(TestCase):
    def test_find_image_builder_in_openwrt_homepage(self):
        url = 'https://archive.openwrt.org/chaos_calmer/15.05/ar71xx/generic/'
        html = pq(url=url)
        a = html('a')
        image_builder = None
        for item in a.items():
            href = item.attr('href')
            if href.find('ImageBuilder') != -1:
                image_builder = os.path.join(url, href)
                break
        self.assertEqual(
            image_builder,
            'https://archive.openwrt.org/chaos_calmer/15.05/ar71xx/generic/'
            'OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64.tar.bz2')
