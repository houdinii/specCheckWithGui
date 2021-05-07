import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
from spec_checker.modules.antivirus import AntivirusRecord, AntivirusRecords
import main

app = QApplication(sys.argv)


class AntivirusTest(unittest.TestCase):
    """Tests the antivirus scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.antivirus.test()

    def test_results_is_AntivirusRecords(self):
        """Tests that the results from antivirus.test() is a type <AntivirusRecords>"""
        self.assertEqual(type(self.results), type(AntivirusRecords()), "result of antivirus.test() should be of type <AntivirusRecords>")

    def test_list_items_are_type_AntivirusRecord(self):
        """Tests that the first item in the results from antivirus.test() is a type <AntivirusRecord>"""
        for i in range(len(self.results.list)):
            self.assertEqual(type(self.results.list[i]), type(AntivirusRecord()), "result of antivirus.test() should be of type <AntivirusRecord>")

    def test_display_name(self):
        """Test that display_name is not None"""
        self.assertNotEqual(self.results.list[0].display_name, None, "display_name should not be None")

    def test_path_to_signed_product_exe(self):
        """Test that path_to_signed_product_exe is not None"""
        self.assertNotEqual(self.results.list[0].path_to_signed_product_exe, None, "path_to_signed_product_exe should not be None")

    def test_path_to_signed_reporting_exe(self):
        """Test that path_to_signed_reporting_exe is not None"""
        self.assertNotEqual(self.results.list[0].path_to_signed_reporting_exe, None, "path_to_signed_reporting_exe should not be None")

    def test_enabled(self):
        """Test that enabled is not None"""
        self.assertNotEqual(self.results.list[0].enabled, None, "enabled should not be None")

    def test_scanning(self):
        """Test that scanning is not None"""
        self.assertNotEqual(self.results.list[0].scanning, None, "scanning should not be None")

    def test_outdated(self):
        """Test that outdated is not None"""
        self.assertNotEqual(self.results.list[0].outdated, None, "outdated should not be None")

    def test_timestamp(self):
        """Test that timestamp is not None"""
        self.assertNotEqual(self.results.list[0].timestamp, None, "timestamp should not be None")


if __name__ == "__main__":
    unittest.main()
