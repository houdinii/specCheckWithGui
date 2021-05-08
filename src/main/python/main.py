# This must come first or it crashes when it tries to multi thread
import asyncio

from spec_checker.modules.spec_record import SpecRecord
from spec_checker.modules.utilities import truncate
from spec_checker.modules.submit_to_google_forms import google_submit
from spec_checker.windows.MainWindow import Ui_MainWindow
from spec_checker.windows.About import Ui_AboutBox

from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QStyle
from PyQt5.QtCore import QTimer, QObject, QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPalette, QColor

from os import path
import os
import sys
import time
import configparser
import pdoc
import logging
import pythoncom

from spec_checker.modules.speedtest import speed_test
pythoncom.CoInitialize()


class AboutBox(QDialog, Ui_AboutBox):
    """QT dialog box with version and author information"""
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


class MainTestWorker(QObject):
    finished = pyqtSignal(SpecRecord)
    progress = pyqtSignal(int, str, bool)  # for progress bar

    def __init__(self):
        super().__init__()
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

    def test(self):
        # The long running test
        self.progress.emit(0, "Sound Devices", True)
        if sys.platform.startswith('win32'):
            try:
                import pythoncom
                pythoncom.CoInitialize()
                import soundcard
                self.specs.sound.test()
            except RuntimeError as e:
                print("SOUND ERROR!")
        elif sys.platform.startswith('darwin'):
            pass

        self.progress.emit(10, "Graphics Card", False)
        self.specs.gpus.test()
        self.progress.emit(15, "CPU", False)
        self.specs.cpu.test()
        self.progress.emit(20, "Hard Drives", False)
        self.specs.harddrives.test()
        self.progress.emit(25, "Location", False)
        self.specs.location.test()
        self.progress.emit(30, "Memory", False)
        self.specs.memory.test()
        self.progress.emit(35, "Network", False)
        self.specs.network.test()
        self.progress.emit(36, "System In General", False)
        self.specs.system.test()
        self.progress.emit(40, "Antivirus", False)
        self.specs.antivirus.test()
        self.progress.emit(45, "Webcam", False)
        self.specs.webcams.test()
        self.progress.emit(50, "Internet Speed (This could take a few minutes!)", False)
        self.specs.speedtest.test()
        self.progress.emit(100, "", False)
        self.finished.emit(self.specs)


class MainWindow(QMainWindow, Ui_MainWindow):
    """QT main window"""
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Logging
        self.log = logging.getLogger("SpecChecker Main")
        self.log.setLevel("NOTSET")
        self.log.info("Starting Main Application")

        # Configuration
        self.config = configparser.ConfigParser()
        self.load_configuration()
        self.load_logging_configuration()

        # GUI Code
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.btnStart.pressed.connect(self.runAllTests)
        self.btnExit.pressed.connect(self.doExit)
        self.actionExit.triggered.connect(self.doExit)
        self.actionAbout.triggered.connect(self.showAbout)
        self.statusText = ""

        # Specifications Code
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

    def finished(self, spec_record):
        self.btnStart.setEnabled(True)
        self.btnStart.setText("Start")
        self.specs = spec_record
        # google_submit(self.specs)
        self.specs.write_to_file()
        # self.btnStart.setDisabled(False)

    def runAllTests(self):
        self.thread = QThread()
        self.worker = MainTestWorker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.test)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.reportProgress)
        self.thread.start()

        self.btnStart.setDisabled(True)
        self.btnStart.setText("Running Tests...")
        self.worker.finished.connect(self.finished)
        self.thread.finished.connect(
            lambda: self.updateStatus("\n\n All Tests Complete!")
        )

    def reportProgress(self, percentage, module_name=None, first_pass=True):
        if not first_pass:
            self.updateStatus("Complete\n")
        if module_name is not None and module_name != "":
            self.updateStatus(f"Scanning {module_name}..........")

        if 100 >= percentage >= 0 and isinstance(percentage, int):
            self.progressBar.setValue(percentage)

    def showAbout(self):
        """Show the about box"""
        dlg = AboutBox()
        dlg.exec_()

    def doExit(self):
        """Exit the program cleanly"""
        self.log.info("Closing Application")
        self.close()

    def updateStatus(self, text):
        """Update the status text in the main text area of the app"""
        self.statusText = self.statusText + text
        self.txtStatus.setPlainText(self.statusText)

    def clearStatus(self):
        """Clear the status text in the main text area of the app"""
        self.statusText = ""
        self.txtStatus.setPlainText("")

    def load_configuration(self, filename='config.ini'):
        """Check if a configuration file exists. If it does, load it
        If not, load the default"""
        if path.exists(filename):
            self.config.read(filename)
            self.log.info(f"Loaded Configuration: {filename}")
        else:
            self.load_default_configuration()
            self.log.info("Configuration File Does Not Exist. Loading Defaults.")

    def load_default_configuration(self):
        """Load built in default configuration"""
        default_config = """
        [general]
        # Comment out lines that are unnecessary with hash
        save to file = False
        debug = True
        # Debug Levels: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET (NOTSET turns off logging)
        debug level = INFO

        [email_submission]
        enabled = False
        fields json = fields.json
        # Not Yet Implemented
        
        [google_submission]
        enabled = False
        pre url = https://docs.google.com/forms/d/e/
        form id = ***REMOVED***
        post url = /formResponse
        full url = ${pre url}${form id}${post url}
        fields json = fields.json
        
        [cpu]
        enabled = True
         
        [gpu]
        enabled = True
         
        [harddrive]
        enabled = True
        
        [location]
        enabled = True
        # options: ipinfo, 
        provider = ipinfo
        
        [memory]
        enabled = True
        
        [network]
        enabled = True
        
        [sound]
        enabled = True
        
        [speedtest]
        enabled = True
        # options: fast, 
        provider = fast
        
        [system]
        enabled = True
        """
        self.config.read_string(default_config)
        self.log.info("Loaded Default Configuration")

    def load_logging_configuration(self):
        """todo Sets Application Wide Log Level From Configuration"""
        log_flag = bool(self.config.get('general', 'debug'))
        log_level = self.config.get('general', 'debug level')
        if log_flag is False:
            log_level = "NOTSET"


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
