import platform
import psutil
from spec_checker.modules.utilities import get_size


class MemoryRecord:
    """Holds and records the location of the client device

    Keyword Arguments:
        total       -- Total memory installed on client device (Default: None)
        available   -- Available memory installed on client device (Default: None)
        used        -- Used memory installed on client device (Default: None)
        percentage  -- Used memory installed on client device as a percentage (Default: None) fixme: Might be free memory
    """
    def __init__(self, total=None, available=None, used=None, percentage=None):
        self.total = total
        self.available = available
        self.used = used
        self.percentage = percentage

    def __repr__(self):
        return f"<MemoryRecord total:{self.city} used: {self.used} available: {self.available} percentage:{self.region}>"

    def __str__(self):
        return f"""
Location Information:
Total: {self.total}
Available: {self.available}
Used: {self.used}
Percentage: {self.percentage}"""

    def test(self):
        """Performs the memory test and records record to self

        Returns: <MemoryRecord>
        """
        uname = platform.uname()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()

        self.total = f"{get_size(svmem.total)}"
        self.available = f"{get_size(svmem.available)}"
        self.used = f"{get_size(svmem.used)}"
        self.percentage = f"{svmem.percent}%"
        return self
