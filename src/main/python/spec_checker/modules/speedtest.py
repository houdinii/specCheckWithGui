import asyncio

# import spec_checker.modules.fast_speedtest as fast
from spec_checker.modules.speedtest_net import Speedtest
from spec_checker.modules.utilities import truncate
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from asyncqt import asyncSlot
import asyncio
import pythoncom
pythoncom.CoInitialize()


async def speed_test(fut):
    servers = []
    threads = None
    s = Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads, pre_allocate=False)
    s.results.share()
    results_dict = s.results.dict()
    if "download" in results_dict:
        download = round(results_dict['download'] / 1000000, 2)
    else:
        download = 0.00
    if "upload" in results_dict:
        upload = round(results_dict['upload'] / 1000000, 2)
    else:
        upload = 0.00
    if "timestamp" in results_dict:
        timestamp_raw = results_dict['timestamp'].split("T")
        date = timestamp_raw[0]
        time = timestamp_raw[1]
    else:
        date = ""
        time = ""
    if "ping" in results_dict:
        ping = results_dict['ping']
    else:
        ping = ""
    if "ping" in results_dict:
        ping = results_dict['ping']
    else:
        ping = ""
    client = None
    if "client" in results_dict:
        client = results_dict['client']
        if "isp" in client:
            isp = client['isp']
        else:
            isp = ""
        if "ip" in client:
            ip = client['ip']
        else:
            ip = ""
    else:
        isp = ""
        ip = ""
    if "share" in results_dict:
        share = results_dict['share']
    else:
        share = ""

    results = {
        'download_speed': download,
        'upload_speed': upload,
        'date': date,
        'time': time,
        'ping': ping,
        'client': client,
        'isp': isp,
        'ip': ip,
        'share': share,
    }

    fut.set_result(results)
    return results


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

    def test(self):
        loop = asyncio.new_event_loop()
        fut = loop.create_future()
        asyncio.set_event_loop(loop)
        speed_result = loop.run_until_complete(speed_test(fut))
        self.download_speed = speed_result['download_speed']
        self.upload_speed = speed_result['upload_speed']
        self.ping = speed_result['ping']
        self.date = speed_result['date']
        self.time = speed_result['time']
        self.client = speed_result['client']
        self.isp = speed_result['isp']
        self.ip = speed_result['ip']
        self.share = speed_result['share']
        return self
