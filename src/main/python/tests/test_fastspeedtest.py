import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
import asyncio
import main
from spec_checker.modules.speedtest import speed_test

app = QApplication(sys.argv)


class FastSpeedtestTest(unittest.TestCase):
    """Tests the speedtest scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.config.set("speedtest", "provider", "fast")
        self.form.log.setLevel("NOTSET")

        loop = asyncio.new_event_loop()
        fut = loop.create_future()
        asyncio.set_event_loop(loop)
        speed_result = loop.run_until_complete(speed_test(fut))
        self.form.specs.speedtest.download_speed = speed_result['download_speed']
        self.form.specs.speedtest.upload_speed = speed_result['upload_speed']
        self.form.specs.speedtest.ping = speed_result['ping']

    def test_download_results_not_empty(self):
        """Ensures the speed test download results are not empty"""
        self.assertIsNotNone(self.form.specs.speedtest.download_speed, "physical_cores should not be 0")

    def test_upload_results_not_implemented(self):
        """Ensures the speed test upload results are not implemented"""
        self.assertEqual(self.form.specs.speedtest.upload_speed, "Not Yet Implemented", "upload speed shouldn't be implemented")

    def test_ping_results_not_implemented(self):
        """Ensures the speed test ping results are not implemented"""
        self.assertEqual(self.form.specs.speedtest.ping, "Not Yet Implemented", "ping shouldn't be implemented")


if __name__ == "__main__":
    unittest.main()
