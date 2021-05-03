import psutil


class CpuRecord:
    def __init__(self, physical_cores=0, total_cores=0, min_frequency=None,
                 max_frequency=None, current_frequency=None, total_usage=None):
        self.physical_cores = physical_cores
        self.total_cores = total_cores
        self.min_frequency = min_frequency
        self.max_frequency = max_frequency
        self.current_frequency = current_frequency
        self.total_usage = total_usage

    def __repr__(self):
        return f"<CpuRecord physical_cores:{self.physical_cores} total_cores:{self.total_cores}>"

    def __str__(self):
        return f"""
CPU Information:
Physical Cores: {self.physical_cores}
Total Cores: {self.total_cores}
Minimum Frequency: {self.min_frequency}
Maximum Frequency: {self.max_frequency}
Current Frequency: {self.current_frequency}
Total Usage Percent: {self.total_usage}"""

    def test(self):
        self.physical_cores = psutil.cpu_count(logical=False)
        self.total_cores = psutil.cpu_count(logical=True)
        self.min_frequency = f"{psutil.cpu_freq().min:.2f}Mhz"
        self.max_frequency = f"{psutil.cpu_freq().max:.2f}Mhz"
        self.current_frequency = f"{psutil.cpu_freq().current:.2f}Mhz"
        self.total_usage = f"{psutil.cpu_percent()}%"
        return self
