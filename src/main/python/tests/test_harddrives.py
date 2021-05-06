import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
from spec_checker.modules.harddrive import HardDriveRecord, HardDriveRecords
import main

app = QApplication(sys.argv)


class GpuTest(unittest.TestCase):
    """Tests the gpu scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.harddrives.test()

    def test_results_is_HardDriveRecords(self):
        """Tests that the results from harddrive.test() is a type <HardDriveRecords>"""
        self.assertEqual(type(self.results), type(HardDriveRecords()), "result of harddrive.test() should be of type <HardDriveRecords>")

    def test_list_items_are_type_HardDriveRecord(self):
        """Tests that the first item in the results from harddrive.test() is a type <HardDriveRecord>"""
        for i in range(len(self.results.list)):
            self.assertEqual(type(self.results.list[i]), type(HardDriveRecord()), "result of harddrive.test() should be of type <HardDriveRecord>")

    def test_device_is_not_None(self):
        """Test that device is not None"""
        self.assertNotEqual(self.results.list[0].device, None, "device should not be None")

    def test_mountpoint_is_not_None(self):
        """Test that mountpoint is not None"""
        self.assertNotEqual(self.results.list[0].mountpoint, None, "mountpoint should not be None")

    def test_filesystem_is_not_None(self):
        """Test that filesystem is not None"""
        self.assertNotEqual(self.results.list[0].filesystem, None, "filesystem should not be None")

    def test_usage_is_not_None(self):
        """Test that usage is not None"""
        self.assertNotEqual(self.results.list[0].usage, None, "usage should not be None")

    def test_total_size_is_not_None(self):
        """Test that total_size is not None"""
        self.assertNotEqual(self.results.list[0].total_size, None, "total_size should not be None")

    def test_used_is_not_None(self):
        """Test that used is not None"""
        self.assertNotEqual(self.results.list[0].used, None, "used should not be None")

    def test_free_is_not_None(self):
        """Test that free is not None"""
        self.assertNotEqual(self.results.list[0].free, None, "free should not be None")

    def test_percentage_is_not_None(self):
        """Test that percentage is not None"""
        self.assertNotEqual(self.results.list[0].percentage, None, "percentage should not be None")


if __name__ == "__main__":
    unittest.main()
