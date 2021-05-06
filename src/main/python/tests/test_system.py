import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import main

app = QApplication(sys.argv)


class SystemTest(unittest.TestCase):
    """Tests the system scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.system.test()

    def test_system_type(self):
        """Test that system_type is not None"""
        self.assertNotEqual(self.results.system_type, None, "system_type is not None")

    def test_computer_name(self):
        """Test that computer_name is not None"""
        self.assertNotEqual(self.results.computer_name, None, "computer_name is not None")

    def test_os_release(self):
        """Test that os_release is not None"""
        self.assertNotEqual(self.results.os_release, None, "os_release is not None")

    def test_os_version(self):
        """Test that os_version is not None"""
        self.assertNotEqual(self.results.os_version, None, "os_version is not None")

    def test_machine_type(self):
        """Test that machine_type is not None"""
        self.assertNotEqual(self.results.machine_type, None, "machine_type is not None")

    def test_processor_family(self):
        """Test that processor_family is not None"""
        self.assertNotEqual(self.results.processor_family, None, "processor_family is not None")

    def test_boot_time_timestamp(self):
        """Test that boot_time_timestamp is not None"""
        self.assertNotEqual(self.results.boot_time_timestamp, None, "boot_time_timestamp is not None")

    def test_boot_time_formatted(self):
        """Test that boot_time_formatted is not None"""
        self.assertNotEqual(self.results.boot_time_formatted, None, "boot_time_formatted is not None")



if __name__ == "__main__":
    unittest.main()
