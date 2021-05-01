from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5.QtCore import QMutex, QTimer, QObject, QThread, pyqtSignal
from spec_checker.windows.MainWindow import Ui_MainWindow
from spec_checker.windows.About import Ui_AboutBox
from spec_checker.modules.speedtest.test_speed import check_speed

import sys
import json

speedtest_results = {}
mutex = QMutex()


class SpeedtestWorker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    updateResults = pyqtSignal()

    def run(self):
        """Long-running task."""
        speed_results = check_speed()
        global speedtest_results
        mutex.lock()
        if speed_results:
            speedtest_results = speed_results
            print(speedtest_results)
        else:
            speedtest_results = {
                'download': 0,
                'upload': 0,
                'date': 0,
                'time': 0,
                'ping': 0,
                'client': {},
                'isp': "0",
                'ip': "0",
                'share': "0",
            }
        self.updateResults.emit()
        mutex.unlock()
        self.finished.emit()


class AboutBox(QDialog, Ui_AboutBox):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.btnStart.pressed.connect(self.runSpeedtest)
        self.btnExit.pressed.connect(self.doExit)
        self.actionExit.triggered.connect(self.doExit)
        self.actionAbout.triggered.connect(self.showAbout)
        self.statusText = ""

    def showAbout(self):
        dlg = AboutBox()
        dlg.exec_()

    def doExit(self):
        self.close()

    def runSpeedtest(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = SpeedtestWorker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.updateResults.connect(self.updateSpeedResults)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.updateStatus("Starting Speedtest.....")
        self.thread.start()

        # Final resets
        self.btnStart.setEnabled(False)
        self.thread.finished.connect(lambda: self.btnStart.setEnabled(True))
        self.thread.finished.connect(lambda: self.updateStatus("Complete\n"))
        self.thread.finished.connect(lambda: self.progressBar.setValue(100))

    def updateSpeedResults(self):
        global speedtest_results
        self.updateStatus(json.dumps(speedtest_results))

    def updateStatus(self, text):
        self.statusText = self.statusText + text
        self.txtStatus.setPlainText(self.statusText)


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
