import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
from spec_checker.modules.network import NetworkRecords, NetworkRecord
import main

app = QApplication(sys.argv)


class NetworkTest(unittest.TestCase):
    """Tests the network scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.network.test()

    def test_results_is_NetworkRecords(self):
        """Tests that the results from network.test() is a type <NetworkRecords>"""
        self.assertEqual(type(self.results), type(NetworkRecords()), "result of network.test() should be of type <NetworkRecords>")

    def test_list_items_are_type_NetworkRecord(self):
        """Tests that the first item in the results from network.test() is a type <NetworkRecord>"""
        for i in range(len(self.results.list)):
            self.assertEqual(type(self.results.list[i]), type(NetworkRecord()), "result of network.test() should be of type <NetworkRecord>")

    def test_interface_name_is_not_None(self):
        """Test that interface_name is not None"""
        self.assertNotEqual(self.results.list[0].interface_name, None, "interface_name should not be None")

    def test_address_family_is_not_None(self):
        """Test that address_family is not None"""
        self.assertNotEqual(self.results.list[0].address_family, None, "address_family should not be None")

    def test_netmask_is_not_None(self):
        """Test that netmask is not None"""
        self.assertNotEqual(self.results.list[0].netmask, None, "netmask should not be None")

    def test_ip_address_is_not_None(self):
        """Test that ip_address is not None"""
        self.assertNotEqual(self.results.list[0].ip_address, None, "ip_address should not be None")


if __name__ == "__main__":
    unittest.main()
