from unittest import TestCase

from slcore.database.dbf import get_database


class TestCompositor(TestCase):
    def test_support_db(self):
        support = get_database('support')

        a = support.select('profile', arch='arm', machine_id='0x661')
        self.assertEqual('/root/esv/examples/arm/mach-orion5x/profile.yaml', a)

        b = support.select('profile', arch='arm', compatible='plxtech,nas7820')
        self.assertEqual('/root/esv/examples/arm/mach-oxnas/profile.yaml', b)

        c = support.select('board', arch='arm', board='mach-orion5x')
        self.assertTrue(c)

        d = support.select('board', arch='arm', brand='openwrt', target='orion')
        self.assertIsNotNone(d)

