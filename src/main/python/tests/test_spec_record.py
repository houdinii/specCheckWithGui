import unittest
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5 import Qt
from PyQt5.QtCore import QSize
from unittest import TestCase
from spec_checker.modules.spec_record import SpecRecord
from spec_checker.modules.network import NetworkRecords
from spec_checker.modules.sound import SoundRecord
from spec_checker.modules.gpu import GpuRecords
from spec_checker.modules.cpu import CpuRecord
from spec_checker.modules.harddrive import HardDriveRecords
from spec_checker.modules.location import LocationRecord
from spec_checker.modules.memory import MemoryRecord
from spec_checker.modules.system import SystemRecord
from spec_checker.modules.webcam import WebcamRecords
from spec_checker.modules.speedtest import SpeedtestRecord
import main

app = QApplication(sys.argv)


class GpuTest(unittest.TestCase):
    """Tests the gpu scanner"""
    def setUp(self):
        """Create The Gui"""
        self.form = main.MainWindow()
        self.form.log.setLevel("NOTSET")
        self.results = self.form.specs

    def test_sound_is_SoundRecord(self):
        """Tests that sound is of type <SoundRecord>"""
        self.assertEqual(type(self.results.sound), type(SoundRecord()), "sound should be of type<SoundRecord>")

    def test_gpus_is_GpuRecords(self):
        """Tests that gpus is of type <GpuRecords>"""
        self.assertEqual(type(self.results.gpus), type(GpuRecords()), "gpus should be of type<GpuRecords>")

    def test_cpu_is_CpuRecord(self):
        """Tests that cpu is of type <CpuRecord>"""
        self.assertEqual(type(self.results.cpu), type(CpuRecord()), "cpu should be of type<CpuRecord>")

    def test_harddrives_is_HardDriveRecords(self):
        """Tests that harddrives is of type <HardDriveRecords>"""
        self.assertEqual(type(self.results.harddrives), type(HardDriveRecords()), "harddrives should be of type<HardDriveRecords>")

    def test_location_is_LocationRecord(self):
        """Tests that location is of type <LocationRecord>"""
        self.assertEqual(type(self.results.location), type(LocationRecord()), "location should be of type<LocationRecord>")

    def test_memory_is_MemoryRecord(self):
        """Tests that memory is of type <MemoryRecord>"""
        self.assertEqual(type(self.results.memory), type(MemoryRecord()), "memory should be of type<MemoryRecord>")

    def test_network_is_NetworkRecords(self):
        """Tests that network is of type <NetworkRecords>"""
        self.assertEqual(type(self.results.network), type(NetworkRecords()), "network should be of type<NetworkRecords>")

    def test_system_is_SystemRecord(self):
        """Tests that system is of type <SystemRecord>"""
        self.assertEqual(type(self.results.system), type(SystemRecord()), "system should be of type<SystemRecord>")

    def test_webcams_is_WebcamRecords(self):
        """Tests that webcams is of type <WebcamRecords>"""
        self.assertEqual(type(self.results.webcams), type(WebcamRecords()), "webcams should be of type<WebcamRecords>")

    def test_speedtest_is_SpeedtestRecord(self):
        """Tests that speedtest is of type <SpeedtestRecord>"""
        self.assertEqual(type(self.results.speedtest), type(SpeedtestRecord()), "speedtest should be of type<SpeedtestRecord>")


if __name__ == "__main__":
    unittest.main()
