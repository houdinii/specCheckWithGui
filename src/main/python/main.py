import pywifi
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QDialog, QDialogButtonBox, QVBoxLayout, QLabel
from PyQt5.QtCore import QMutex, QTimer, QObject, QThread, pyqtSignal
from spec_checker.windows.MainWindow import Ui_MainWindow
from spec_checker.windows.About import Ui_AboutBox
# from spec_checker.modules.speedtest.test_speed import check_speed
import soundcard
import GPUtil
import psutil
import requests
import platform
import cv2
from datetime import datetime
# import spec_checker.modules.audio.audio as audio

# import multiprocessing
import sys
import json

# speedtest_results = {}
# mutex = QMutex()

# region speedtest
# class SpeedtestWorker(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(int)
#     updateResults = pyqtSignal()
#
#     def run(self):
#         """Long-running task."""
#         speed_results = check_speed()
#         global speedtest_results
#         mutex.lock()
#         if speed_results:
#             speedtest_results = speed_results
#             # print(speedtest_results)
#         else:
#             speedtest_results = {
#                 'download': 0,
#                 'upload': 0,
#                 'date': 0,
#                 'time': 0,
#                 'ping': 0,
#                 'client': {},
#                 'isp': "0",
#                 'ip': "0",
#                 'share': "0",
#             }
#         self.updateResults.emit()
#         mutex.unlock()
#         self.finished.emit()
# endregion


def get_size(num_bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if num_bytes < factor:
            return f"{num_bytes:.2f}{unit}{suffix}"
        num_bytes /= factor


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
        self.audioInfo = {}
        self.list_gpus = []
        self.cpuInfo = {}
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

    # def runSpeedtest(self):
    #     # Step 2: Create a QThread object
    #     self.thread = QThread()
    #     # Step 3: Create a worker object
    #     self.worker = SpeedtestWorker()
    #     # Step 4: Move worker to the thread
    #     self.worker.moveToThread(self.thread)
    #     # Step 5: Connect signals and slots
    #     self.thread.started.connect(self.worker.run)
    #     self.worker.updateResults.connect(self.updateSpeedResults)
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.thread.finished.connect(self.thread.deleteLater)
    #     # self.worker.progress.connect(self.reportProgress)
    #     # Step 6: Start the thread
    #     self.updateStatus("Starting Speedtest.....")
    #     self.thread.start()
    #
    #     # Final resets
    #     self.btnStart.setEnabled(False)
    #     self.thread.finished.connect(lambda: self.btnStart.setEnabled(True))
    #     self.thread.finished.connect(lambda: self.updateStatus("Complete\n"))
    #     self.thread.finished.connect(lambda: self.progressBar.setValue(90))

    # def updateSpeedResults(self):
    #     global speedtest_results
    #     self.updateStatus(".")

    def updateStatus(self, text):
        self.statusText = self.statusText + text
        self.txtStatus.setPlainText(self.statusText)

    def clearStatus(self):
        self.statusText = ""
        self.txtStatus.setPlainText("")

    def runAllTests(self):
        self.clearStatus()
        # With config files, hook goes here!
        # self.runSpeedtest()
        self.progressBar.setValue(0)
        self.updateStatus("Starting Audio Test......")
        raw_audio_info = self.audio_test()
        print(self.audioInfo)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(11)
        self.updateStatus("Starting Video Test......")
        raw_video_info = self.video_test()
        print(self.list_gpus)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(22)
        self.updateStatus("Starting CPU Test......")
        raw_cpu_info = self.cpu_test()
        print(self.cpuInfo)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(33)
        self.updateStatus("Starting Hard Drive Test......")
        raw_hd_info = self.hard_drive_test()
        print(self.hard_drive_list)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(44)
        self.updateStatus("Starting Location Test......")
        raw_location_info = self.location_test()
        print(self.locationInfo)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(55)
        self.updateStatus("Starting Memory Test......")
        raw_memory_info = self.memory_test()
        print(self.memoryInfo)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(66)
        self.updateStatus("Starting Network Test......")
        raw_network_info = self.network_test()
        print(self.networkInfo)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(77)
        self.updateStatus("Starting General System Test......")
        raw_system_info = self.system_test()
        print(self.systemInfo)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(88)
        self.updateStatus("Starting Webcam Test (Light May Blink)......")
        raw_webcam_list = self.webcam_test()
        print(self.webcamList)
        self.updateStatus("Complete\n")
        self.progressBar.setValue(100)
        self.updateStatus("All Tests Complete")

    def audio_test(self):
        sound_cards = soundcard.all_speakers()
        mics = soundcard.all_microphones()

        if len(sound_cards) > 0:
            sound_card_present = True
            default_sound_card = soundcard.default_speaker()
        else:
            sound_card_present = False
            default_sound_card = "No default sound card found. May not be enabled or plugged in."

        if len(mics) > 0:
            mic_present = True
            default_mic = soundcard.default_microphone()
        else:
            mic_present = False
            default_mic = "No default mic found. May not be enabled or plugged in."

        self.audioInfo = {
            'sound_cards': sound_cards,
            'sound_card_present': sound_card_present,
            'default_sound_card': default_sound_card,
            'mics': mics,
            'mic_present': mic_present,
            'default_mic': default_mic
        }

        return self.audioInfo

    def video_test(self):
        gpus = GPUtil.getGPUs()
        self.list_gpus = []
        for gpu in gpus:
            video_object = {
                'gpu_id': gpu.id,
                'gpu_name': f"{gpu.name}",
                'gpu_load': f"{gpu.load * 100}%",
                'gpu_free_memory': f"{gpu.memoryFree}MB",
                'gpu_used_memory': f"{gpu.memoryUsed}MB",
                'gpu_total_memory': f"{gpu.memoryTotal}MB",
                'gpu_temperature': f"{gpu.temperature} °C",
            }

            self.list_gpus.append(video_object)
        return self.list_gpus

    def cpu_test(self):
        self.cpuInfo = {
            'physical_cores': psutil.cpu_count(logical=False),
            'total_cores': psutil.cpu_count(logical=True),
            'min_frequency': f"{psutil.cpu_freq().min:.2f}Mhz",
            'max_frequency': f"{psutil.cpu_freq().max:.2f}Mhz",
            'current_frequency': f"{psutil.cpu_freq().current:.2f}Mhz",
            'total_usage': f"{psutil.cpu_percent()}%"
        }
        return self.cpuInfo

    def hard_drive_test(self):
        disk_io = psutil.disk_io_counters()
        partitions = psutil.disk_partitions()
        self.hard_drive_list = []

        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                partition_usage = "Disk Not Ready"
                continue

            device_object = {
                'device': partition.device,
                'mountpoint': partition.mountpoint,
                'filesystem': partition.fstype,
                'usage': partition_usage,
                'total_size': get_size(partition_usage.total),
                'used': get_size(partition_usage.used),
                'free': get_size(partition_usage.free),
                'percentage': f"{partition_usage.percent}%"
            }
            self.hard_drive_list.append(device_object)
        return self.hard_drive_list

    def location_test(self):
        response = requests.get("https://ipinfo.io/")
        response_json = {}
        try:
            response_json = response.json()
        except JSONDecodeError as e:
            print("%sError%s" % (Fore.RED, Fore.RESET), e)
            response_json["ip"] = "Error with remote website. This is not an error with the client."
            response_json["city"] = "Error with remote website. This is not an error with the client."
            response_json["region"] = "Error with remote website. This is not an error with the client."
            response_json["loc"] = "Error with remote website. This is not an error with the client."
            response_json["org"] = "Error with remote website. This is not an error with the client."
            response_json["timezone"] = "Error with remote website. This is not an error with the client."

        self.locationInfo = {
            'ip': str(response_json['ip']),
            'city': str(response_json['city']),
            'region': str(response_json['region']),
            'loc': str(response_json['loc']),
            'org': str(response_json['org']),
            'timezone': str(response_json['timezone']),
        }
        return self.locationInfo

    def memory_test(self):
        uname = platform.uname()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        self.memoryInfo = {
            'total': f"{get_size(svmem.total)}",
            'available': f"{get_size(svmem.available)}",
            'used': f"{get_size(svmem.used)}",
            'percentage': f"{svmem.percent}%",
        }
        return self.memoryInfo

    def network_test(self):
        disk_io = psutil.disk_io_counters()
        partitions = psutil.disk_partitions()
        network_list = []

        if_addrs = psutil.net_if_addrs()

        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                if str(address.family) != 'AddressFamily.AF_LINK' and 'Loopback' not in str(interface_name):
                    network_object = {
                        'interface_name': str(interface_name),
                        'address_family': str(address.family),
                        'netmask': str(address.netmask),
                        'ip_address': str(address.address)
                    }
                    network_list.append(network_object)

        wifi = pywifi.PyWiFi()
        iface = wifi.interfaces()[0]
        wifi_status = self.get_wifi_status(iface)
        self.networkInfo = {
            'network_list': network_list,
            'wifi_status': wifi_status
        }
        return self.networkInfo

    def get_wifi_status(self, iface):
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            status = "Connected"
        elif iface.status() == pywifi.const.IFACE_DISCONNECTED:
            status = "Disconnected"
        elif iface.status() == pywifi.const.IFACE_INACTIVE:
            status = "Inactive"
        elif iface.status() == pywifi.const.IFACE_SCANNING:
            status = "Scanning"
        elif iface.status() == pywifi.const.IFACE_CONNECTING:
            status = "Connecting"
        else:
            status = "Error"
        return status

    def system_test(self):
        uname = platform.uname()
        boot_time = datetime.fromtimestamp(psutil.boot_time())

        formatted_b_time = f"{boot_time.month}/{boot_time.day}/{boot_time.year} {boot_time.hour}:{boot_time.minute}:{boot_time.second}"
        self.systemInfo = {
            'system_type': uname.system,
            'computer_name': uname.node,
            'os_release': uname.release,
            'os_version': uname.version,
            'machine_type': uname.machine,
            'processor_family': uname.processor,
            'boot_time_timestamp': boot_time,
            'boot_time_formatted': formatted_b_time
        }
        return self.systemInfo

    def webcam_test(self):
        webcam_list = []
        count = 0

        while True:
            cap = cv2.VideoCapture(count)
            if cap is None or not cap.isOpened():
                if count > 10:
                    break
            else:
                webcam_list.append({
                    "source": count + 1,
                    "status": True
                })
            count += 1

        if len(webcam_list) == 0:
            webcam_list.append({
                "source": 0,
                "status": False
            })

        self.webcamList = webcam_list
        return self.webcamList


if __name__ == '__main__':
    # multiprocessing.freeze_support()
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
