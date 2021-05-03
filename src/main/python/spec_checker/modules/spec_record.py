from spec_checker.modules.network import NetworkRecords
from spec_checker.modules.sound import SoundRecord
from spec_checker.modules.gpu import GpuRecords
from spec_checker.modules.cpu import CpuRecord
from spec_checker.modules.harddrive import HardDriveRecords
from spec_checker.modules.location import LocationRecord
from spec_checker.modules.memory import MemoryRecord
from spec_checker.modules.system import SystemRecord
from spec_checker.modules.webcam import WebcamRecords

import sys


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
{self.webcams}"""

    def write_to_file(self, filename="results.txt"):
        try:
            sys.stdout = open(filename, "w", encoding='utf8')
            print(self)
            sys.stdout.close()
        except Exception:
            print("Error has occurred when trying to write file")
