import asyncio

# import spec_checker.modules.fast_speedtest as fast
from spec_checker.modules.speedtest_net import Speedtest
from spec_checker.modules.utilities import truncate
# from main import speed_stage
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer
from asyncqt import asyncSlot
import asyncio
import pythoncom
pythoncom.CoInitialize()

speed_stage = 0





class SpeedtestRecord:
    def __init__(self, download_speed=None, upload_speed=None, ping=None, date=None, time=None, client=None,
                 isp=None, ip=None, share=None, complete=False):
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.ping = ping
        self.date = date
        self.time = time
        self.client = client
        self.isp = isp
        self.ip = ip
        self.share = share

    def __repr__(self):
        return f"<SpeedtestRecord download_speed:{self.download_speed} upload_speed: {self.upload_speed} ping: {self.ping}ms>"

    def __str__(self):
        return f"""
Speedtest Information:
Download Speed: {self.download_speed}Mbps
Upload Speed: {self.upload_speed}Mpbs
Ping: {self.ping}ms
Date: {self.date}
Time: {self.time}
ISP: {self.isp}
IP Address: {self.ip}
Share Link: {self.share}"""
    
    # def test(self):
    #     global speed_stage
    #     # Speedtest must be done this way outside of the module.
    #     servers = []
    #     threads = None
    #     s = Speedtest()
    #     s.get_servers(servers)
    #     s.get_best_server()
    #     change_speed_stage(1)
    #
    #     s.download(threads=threads)
    #     change_speed_stage(2)
    #
    #     s.upload(threads=threads, pre_allocate=False)
    #     change_speed_stage(3)
    #
    #     s.results.share()
    #     results_dict = s.results.dict()
    #     change_speed_stage(4)
    #
    #     # region Fill Results Object
    #     if not results_dict:
    #         self.download_speed = 0.00
    #         self.upload_speed = 0.00
    #         self.date = ""
    #         self.time = ""
    #         self.ping = ""
    #         self.isp = ""
    #         self.ip = ""
    #         self.share = ""
    #     if "download" in results_dict:
    #         self.download_speed = round(results_dict['download'] / 1000000, 2)
    #     if "upload" in results_dict:
    #         self.upload_speed = round(results_dict['upload'] / 1000000, 2)
    #     if "timestamp" in results_dict:
    #         timestamp_raw = results_dict['timestamp'].split("T")
    #         self.date = timestamp_raw[0]
    #         self.time = timestamp_raw[1]
    #     if "ping" in results_dict:
    #         self.ping = results_dict['ping']
    #     if "client" in results_dict:
    #         self.client = results_dict['client']
    #         if "isp" in self.client:
    #             self.isp = self.client['isp']
    #         if "ip" in self.client:
    #             self.ip = self.client['ip']
    #     if "share" in results_dict:
    #         self.share = results_dict['share']
    #
    #     # endregion
    #     change_speed_stage(5)
    #
