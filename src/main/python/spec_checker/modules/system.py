import platform
from datetime import datetime
import psutil


class SystemRecord:
    def __init__(self, system_type=None, computer_name=None, os_release=None, os_version=None, machine_type=None,
                 processor_family=None, boot_time_timestamp=None, boot_time_formatted=None):
        self.system_type = system_type
        self.computer_name = computer_name
        self.os_release = os_release
        self.os_version = os_version
        self.machine_type = machine_type
        self.processor_family = processor_family
        self.boot_time_timestamp = boot_time_timestamp
        self.boot_time_formatted = boot_time_formatted

    def test(self):
        uname = platform.uname()
        boot_time = datetime.fromtimestamp(psutil.boot_time())

        formatted_b_time = f"{boot_time.month}/{boot_time.day}/{boot_time.year}"\
                           + f"{boot_time.hour}:{boot_time.minute}:{boot_time.second}"

        self.system_type = uname.system
        self.computer_name = uname.node
        self.os_release = uname.release
        self.os_version = uname.version
        self.machine_type = uname.machine
        self.processor_family = uname.processor
        self.boot_time_timestamp = boot_time
        self.boot_time_formatted = formatted_b_time
        return self

    def __repr__(self):
        return f"<SystemRecord system_type:{self.system_type} computer_name:{self.computer_name} os_release:{self.os_release}>"

    def __str__(self):
        return f"""
System Information:
System Type: {self.system_type}
Computer Name: {self.computer_name}
OS Release: {self.os_release}
OS Version: {self.os_version}
Machine Type: {self.machine_type}
Processor Family: {self.processor_family}
Boot Time Timestamp: {self.boot_time_timestamp}
Boot Time Formatted: {self.boot_time_formatted}"""
