# This must come first or it crashes when it tries to multi thread
from spec_checker.modules.spec_record import SpecRecord

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QStyle
from PyQt5.QtCore import QTimer, QObject, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QColor
from spec_checker.windows.MainWindow import Ui_MainWindow
from spec_checker.windows.About import Ui_AboutBox

import sys


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
        # print(self.specs.sound)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(11)
        self.updateStatus("Starting Video Test......")
        self.specs.gpus.test()
        # print(self.specs.gpus)
        # print(self.specs.gpus.list[0])
        self.updateStatus("Complete\n")
        # print("")
        self.progressBar.setValue(22)
        self.updateStatus("Starting CPU Test......")
        self.specs.cpu.test()
        # print(self.specs.cpu)
        # print("")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(33)
        self.updateStatus("Starting Hard Drive Test......")
        self.specs.harddrives.test()
        # print(self.specs.harddrives)
        # print(self.specs.harddrives.list[0])
        # print("")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(44)
        self.updateStatus("Starting Location Test......")
        self.specs.location.test()
        # print(self.specs.location)
        # print("")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(55)
        self.updateStatus("Starting Memory Test......")
        self.specs.memory.test()
        # print(self.specs.memory)
        # print("")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(66)
        self.updateStatus("Starting Network Test......")
        self.specs.network.test()
        # print(self.specs.network.list[0])
        # print(self.specs.network)
        # print(self.specs.network.wifi_status)
        # print("")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(77)
        self.updateStatus("Starting General System Test......")
        self.specs.system.test()
        # print(self.specs.system)
        # print("")
        self.updateStatus("Complete\n")
        self.progressBar.setValue(88)
        self.updateStatus("Starting Webcam Test (Light May Blink)......")
        self.specs.webcams.test()
        # print(self.specs.webcams)
        # print(self.specs.webcams.list[0])
        # print("")
        print(self.specs)
        self.specs.write_to_file()
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
