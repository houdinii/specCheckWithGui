import asyncio

import spec_checker.modules.fast_speedtest as fast
from spec_checker.modules.utilities import truncate
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from asyncqt import asyncSlot
import asyncio


async def speed_test(fut):
    dl_speed = await fast.run()
    dl_speed = truncate(float(dl_speed), 2)
    results = {
        'download_speed': dl_speed,
        'upload_speed': "Not Yet Implemented",
        'ping': "Not Yet Implemented"
    }
    fut.set_result(results)
    return results


class SpeedtestRecord:
    def __init__(self, download_speed=None, upload_speed=None, ping=None, complete=False):
        self.download_speed = download_speed
        self.upload_speed = upload_speed
        self.ping = ping

    def __repr__(self):
        return f"<SpeedtestRecord download_speed:{self.download_speed} upload_speed: {self.upload_speed} ping: {self.ping}>"

    def __str__(self):
        return f"""
Speedtest Information:
Download Speed: {self.download_speed}Mbps
Upload Speed: {self.upload_speed}Mpbs
Ping: {self.ping}"""

    def test(self):
        # The "long running task"
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
