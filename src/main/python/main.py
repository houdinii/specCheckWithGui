# This must come first or it crashes when it tries to multi thread
import asyncio

from spec_checker.modules.spec_record import SpecRecord
from spec_checker.modules.utilities import truncate

from spec_checker.modules.submit_to_google_forms import google_submit

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QStyle
from PyQt5.QtCore import QTimer, QObject, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QColor
from spec_checker.windows.MainWindow import Ui_MainWindow
from spec_checker.windows.About import Ui_AboutBox


import sys
import time

from spec_checker.modules.speedtest import speed_test


class AboutBox(QDialog, Ui_AboutBox):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


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
        self.updateStatus("Complete\n")

        self.progressBar.setValue(10)
        self.updateStatus("Starting Video Test......")
        self.specs.gpus.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(20)
        self.updateStatus("Starting CPU Test......")
        self.specs.cpu.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(30)
        self.updateStatus("Starting Hard Drive Test......")
        self.specs.harddrives.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(40)
        self.updateStatus("Starting Location Test......")
        self.specs.location.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(50)
        self.updateStatus("Starting Memory Test......")
        self.specs.memory.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(60)
        self.updateStatus("Starting Network Test......")
        self.specs.network.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(70)
        self.updateStatus("Starting General System Test......")
        self.specs.system.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(80)
        self.updateStatus("Starting Webcam Test (Light May Blink)......")
        self.specs.webcams.test()
        self.updateStatus("Complete\n")

        self.progressBar.setValue(90)
        self.updateStatus("Starting Speedtest......")
        loop = asyncio.new_event_loop()
        fut = loop.create_future()
        asyncio.set_event_loop(loop)
        speed_result = loop.run_until_complete(speed_test(fut))
        self.specs.speedtest.download_speed = speed_result['download_speed']
        self.specs.speedtest.upload_speed = speed_result['upload_speed']
        self.specs.speedtest.ping = speed_result['ping']
        self.updateStatus("Complete\n")

        self.progressBar.setValue(100)
        google_submit(self.specs)
        self.specs.write_to_file()
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
