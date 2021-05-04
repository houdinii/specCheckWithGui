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
