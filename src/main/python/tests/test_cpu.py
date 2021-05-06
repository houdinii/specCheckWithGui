import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import main

app = QApplication(sys.argv)


class CpuTest(unittest.TestCase):
    """Tests the cpu scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.cpu.test()

    def test_physical_cores(self):
        """Tests that physical_cores is not 0"""
        self.assertNotEqual(self.results.physical_cores, 0, "physical_cores should not be 0")

    def test_total_cores(self):
        """Tests that total_cores is not 0"""
        self.assertNotEqual(self.results.total_cores, 0, "total_cores should not be 0")

    def test_min_frequency(self):
        """Tests that min_frequency is not None"""
        self.assertNotEqual(self.results.min_frequency, None, "min_frequency should not be None")

    def test_max_frequency(self):
        """Tests that max_frequency is not None"""
        self.assertNotEqual(self.results.max_frequency, None, "max_frequency should not be None")

    def test_current_frequency(self):
        """Tests that current_frequency is not None"""
        self.assertNotEqual(self.results.current_frequency, None, "current_frequency should not be None")

    def test_total_usage(self):
        """Tests that total_usage is not 0"""
        self.assertNotEqual(self.results.total_usage, None, "total_usage should not be None")


if __name__ == "__main__":
    unittest.main()
