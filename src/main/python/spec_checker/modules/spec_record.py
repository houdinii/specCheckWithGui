import os.path

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
from spec_checker.modules.antivirus import AntivirusRecords
from spec_checker.modules.submit_using_email import FormSubmitRecord
from PyQt5.QtWidgets import QFileDialog

import sys
from os.path import expanduser
import pythoncom
pythoncom.CoInitialize()


class SpecRecord:
    def __init__(self):
        # Sound only has one record with a list of cards
        self.sound = SoundRecord()
        # Will be a list of GpuRecords
        self.gpus = GpuRecords()
        self.cpu = CpuRecord()
        self.harddrives = HardDriveRecords()
        self.location = LocationRecord()
        self.memory = MemoryRecord()
        self.network = NetworkRecords()
        self.system = SystemRecord()
        self.webcams = WebcamRecords()
        self.speedtest = SpeedtestRecord()
        self.antivirus = AntivirusRecords()
        self.email = FormSubmitRecord()
        self.client_name = ""
        self.client_email_address = ""

    def __repr__(self):
        return "<SpecRecord>"

    def __str__(self):
        return f"""Spec Checker Results:
{self.sound}
{self.gpus}
{self.cpu}
{self.harddrives}
{self.location}
{self.memory}
{self.network}
{self.system}
{self.antivirus}
{self.webcams}
{self.speedtest}"""

    def write_to_file(self, filename="results.txt"):
        try:
            user_dir = os.path.join(expanduser("~"), filename)
            name = QFileDialog.getSaveFileName(
                parent=None,
                directory=user_dir,
                caption='Save Results',
                filter="Text Files (*.txt)",
                initialFilter="Text Files (*.txt)"
            )
            file = open(name[0], 'w', encoding='utf8')
            text = str(self)
            file.write(text)
            file.close()
        except Exception:
            pass
            # print("Error has occurred when trying to write file")
