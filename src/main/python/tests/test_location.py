import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import main

app = QApplication(sys.argv)


class LocationTest(unittest.TestCase):
    """Tests the location scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs.location.test()

    def test_ip(self):
        """Tests that ip is not None"""
        self.assertNotEqual(self.results.ip, None, "ip should not be None")

    def test_city(self):
        """Tests that city is not None"""
        self.assertNotEqual(self.results.city, None, "city should not be None")

    def test_region(self):
        """Tests that region is not None"""
        self.assertNotEqual(self.results.region, None, "region should not be None")

    def test_loc(self):
        """Tests that loc is not None"""
        self.assertNotEqual(self.results.loc, None, "loc should not be None")

    def test_org(self):
        """Tests that org is not None"""
        self.assertNotEqual(self.results.org, None, "org should not be None")

    def test_timezone(self):
        """Tests that timezone is not None"""
        self.assertNotEqual(self.results.timezone, None, "timezone should not be None")

    def test_ip_is_not_remote_error(self):
        """Tests that ip is not returning a remote error"""
        self.assertNotEqual(self.results.ip,
                            "Error with remote website. This is not an error with the client.",
                            "ip should not return remote error message")

    def test_city_is_not_remote_error(self):
        """Tests that city is not returning a remote error"""
        self.assertNotEqual(self.results.city,
                            "Error with remote website. This is not an error with the client.",
                            "city should not return remote error message")

    def test_region_is_not_remote_error(self):
        """Tests that region is not returning a remote error"""
        self.assertNotEqual(self.results.region,
                            "Error with remote website. This is not an error with the client.",
                            "region should not return remote error message")

    def test_loc_is_not_remote_error(self):
        """Tests that loc is not returning a remote error"""
        self.assertNotEqual(self.results.loc,
                            "Error with remote website. This is not an error with the client.",
                            "loc should not return remote error message")

    def test_org_is_not_remote_error(self):
        """Tests that org is not returning a remote error"""
        self.assertNotEqual(self.results.org,
                            "Error with remote website. This is not an error with the client.",
                            "org should not return remote error message")

    def test_timezone_is_not_remote_error(self):
        """Tests that timezone is not returning a remote error"""
        self.assertNotEqual(self.results.timezone,
                            "Error with remote website. This is not an error with the client.",
                            "timezone should not return remote error message")


if __name__ == "__main__":
    unittest.main()
