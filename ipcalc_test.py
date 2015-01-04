import unittest
from ipcalc_filter import FilterModule


class TestIPv4_network(unittest.TestCase):

    def setUp(self):
        self.network = FilterModule().filters()['ipcalc']("192.168.8.0/22")

    def test_version(self):
        self.assertEqual(self.network['version'], 4)

    def test_network(self):
        self.assertEqual(self.network['network'], "192.168.8.0")

    def test_netmask(self):
        self.assertEqual(self.network['netmask'], "255.255.252.0")

    def test_subnet(self):
        self.assertEqual(self.network['subnet'], 22)

    def test_size(self):
        self.assertEqual(self.network['size'], 2**10)

    def test_host_min(self):
        self.assertEqual(self.network['host_min'], "192.168.8.1")

    def test_host_max(self):
        self.assertEqual(self.network['host_max'], "192.168.11.254")

    def test_broadcast(self):
        self.assertEqual(self.network['broadcast'], "192.168.11.255")


class TestIPv6_network(unittest.TestCase):

    def setUp(self):
        self.network = FilterModule().filters()['ipcalc']("fe80::/64")

    def test_version(self):
        self.assertEqual(self.network['version'], 6)

    def test_network(self):
        self.assertEqual(self.network['network'], "fe80::")

    def test_netmask(self):
        self.assertEqual(self.network['netmask'], "ffff:ffff:ffff:ffff:0000:0000:0000:0000")

    def test_subnet(self):
        self.assertEqual(self.network['subnet'], 64)

    def test_size(self):
        self.assertEqual(self.network['size'], 2**64)

    def test_host_min(self):
        self.assertEqual(self.network['host_min'], "fe80::1")

    def test_host_max(self):
        self.assertEqual(self.network['host_max'], "fe80::ffff:ffff:ffff:fffe")

    def test_broadcast(self):
        self.assertFalse(self.network.has_key('broadcast'))


class TestIPv4_add(unittest.TestCase):

    def setUp(self):
        self.method = FilterModule().filters()['ipadd']

    def test_add(self):
        self.assertEqual(self.method("192.168.0.3",4), "192.168.0.7")

    def test_add_negative(self):
        self.assertEqual(self.method("192.168.1.3",-6), "192.168.0.253")


class TestIPv6_add(unittest.TestCase):

    def setUp(self):
        self.method = FilterModule().filters()['ipadd']

    def test_add1(self):
        self.assertEqual(self.method("fe80::","::dead:beef"), "fe80::dead:beef")

    def test_add2(self):
        self.assertEqual(self.method("fe80::1",2), "fe80::3")


if __name__ == '__main__':
    unittest.main()
