import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
from spec_checker.modules.webcam import WebcamRecord, WebcamRecords
import main

app = QApplication(sys.argv)


class WebcamTest(unittest.TestCase):
    """Tests the webcam scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.webcams.test()

    def test_results_is_WebcamRecords(self):
        """Tests that the results from webcams.test() is a type <WebcamRecords>"""
        self.assertEqual(type(self.results), type(WebcamRecords()), "result of webcams.test() should be of type <WebcamRecords>")

    def test_list_items_are_type_WebcamRecord(self):
        """Tests that the first item in the results from webcams.test() is a type <WebcamRecord>"""
        for i in range(len(self.results.list)):
            self.assertEqual(type(self.results.list[i]), type(WebcamRecord()), "result of webcams.test() should be of type <WebcamRecord>")

    def test_source_is_not_None(self):
        """Tests that webcam source is not None"""
        self.assertNotEqual(self.results.list[0].source, None, "source should not be None")

    def test_status_is_not_None(self):
        """Tests that webcam status is not None"""
        self.assertNotEqual(self.results.list[0].status, None, "status should not be None")


if __name__ == "__main__":
    unittest.main()
