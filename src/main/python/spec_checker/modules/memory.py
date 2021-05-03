import platform
import psutil
from spec_checker.modules.utilities import get_size


class MemoryRecord:
    def __init__(self, total=None, available=None, used=None, percentage=None):
        self.total = total
        self.available = available
        self.used = used
        self.percentage = percentage

    def test(self):
        uname = platform.uname()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        self.total = f"{get_size(svmem.total)}"
        self.available = f"{get_size(svmem.available)}"
        self.used = f"{get_size(svmem.used)}"
        self.percentage = f"{svmem.percent}%"
        return self

    def __repr__(self):
        return f"<MemoryRecord total:{self.city} used: {self.used} available: {self.available} percentage:{self.region}>"

    def __str__(self):
        return f"""
Location Information:
Total: {self.total}
Available: {self.available}
Used: {self.used}
Percentage: {self.percentage}"""
