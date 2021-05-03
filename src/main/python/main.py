# This must come first or it crashes when it tries to multi thread
# from spec_checker.modules.network import NetworkRecord, NetworkRecords
# from spec_checker.modules.location import LocationRecord
# from spec_checker.modules.harddrive import HardDriveRecords
# from spec_checker.modules.gpu import GpuRecord, GpuRecords
# from spec_checker.modules.sound import SoundRecord
# from spec_checker.modules.cpu import CpuRecord
# from spec_checker.modules.memory import MemoryRecord
# from spec_checker.modules.system import SystemRecord
# from spec_checker.modules.webcam import WebcamRecord, WebcamRecords
from spec_checker.modules.spec_record import SpecRecord

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QStyle
from PyQt5.QtCore import QTimer, QObject, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QColor
from spec_checker.windows.MainWindow import Ui_MainWindow
from spec_checker.windows.About import Ui_AboutBox

# from spec_checker.modules.utilities import get_size
# import GPUtil
# import psutil
# import requests
# import platform
# import cv2
# from datetime import datetime
import sys


class AboutBox(QDialog, Ui_AboutBox):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


# noinspection PyMethodMayBeStatic
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.btnStart.pressed.connect(self.runAllTests)
        self.btnExit.pressed.connect(self.doExit)
        self.actionExit.triggered.connect(self.doExit)
        self.actionAbout.triggered.connect(self.showAbout)
        self.statusText = ""
        self.specs = SpecRecord()

        self.audioInfo = {}
        self.list_gpus = []
        self.cpuInfo = {}
        self.networkInfo = {}
        self.hard_drive_list = []
        self.locationInfo = {}
        self.memoryInfo = {}
        self.systemInfo = {}
        self.webcamList = []

    def showAbout(self):
        dlg = AboutBox()
        dlg.exec_()

    def doExit(self):
        self.close()

    def updateStatus(self, text):
        self.statusText = self.statusText + text
        self.txtStatus.setPlainText(self.statusText)

    def clearStatus(self):
        self.statusText = ""
        self.txtStatus.setPlainText("")

    def runAllTests(self):
        self.btnStart.setDisabled(True)
        self.clearStatus()
        # With config files, hook goes here!
        self.progressBar.setValue(0)
        self.updateStatus("Starting Audio Test......")
        if sys.platform.startswith('win32'):
            self.specs.sound.test()
        # print(f"default_sound_card: {self.specs.sound.default_sound_card}")
        # print(f"sound_card_present: {self.specs.sound.sound_card_present}")
        # print(f"default_mic: {self.specs.sound.default_mic}")
        # print(f"mic_present: {self.specs.sound.mic_present}")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(11)
        self.updateStatus("Starting Video Test......")
        self.specs.gpus.test()
        # print(self.specs.gpus.list[0].gpu_name)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(22)
        self.updateStatus("Starting CPU Test......")
        self.specs.cpu.test()
        # print(self.specs.cpu.total_cores)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(33)
        self.updateStatus("Starting Hard Drive Test......")
        self.specs.harddrives.test()
        # print(self.specs.harddrives.list[0].usage)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(44)
        self.updateStatus("Starting Location Test......")
        self.specs.location.test()
        # print(self.specs.location.region)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(55)
        self.updateStatus("Starting Memory Test......")
        self.specs.memory.test()
        # print(self.specs.memory.available)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(66)
        self.updateStatus("Starting Network Test......")
        self.specs.network.test()
        print(self.specs.network.list[0].ip_address)
        print(self.specs.network.wifi_status)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(77)
        self.updateStatus("Starting General System Test......")
        self.specs.system.test()
        # print(self.specs.system.computer_name)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(88)
        self.updateStatus("Starting Webcam Test (Light May Blink)......")
        self.specs.webcams.test()
        # print(self.specs.webcams.list)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(100)
        self.updateStatus("All Tests Complete!\n")
        self.btnStart.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    appctxt = ApplicationContext()  # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
