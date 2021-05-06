import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import main

app = QApplication(sys.argv)


class MemoryTest(unittest.TestCase):
    """Tests the memory scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.memory.test()

    def test_total(self):
        """Tests that total memory is not None"""
        self.assertNotEqual(self.results.total, None, "total should not be None")

    def test_available(self):
        """Tests that available memory is not None"""
        self.assertNotEqual(self.results.available, None, "available should not be None")

    def test_used(self):
        """Tests that used memory is not None"""
        self.assertNotEqual(self.results.used, None, "used should not be None")

    def test_percentage(self):
        """Tests that percentage memory is not None"""
        self.assertNotEqual(self.results.percentage, None, "percentage should not be None")


if __name__ == "__main__":
    unittest.main()
