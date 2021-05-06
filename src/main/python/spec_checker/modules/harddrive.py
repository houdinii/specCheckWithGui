import psutil
from spec_checker.modules.utilities import get_size


class HardDriveRecord:
    """
    Holds information about the hard drives installed in the client machine.

    Keyword Arguments:
        device      -- Device description (Default: None)
        mountpoint  -- Device mountpoint (Default: None)
        filesystem  -- Device filesystem (Default: None)
        usage       -- Device usage raw information (Default: None)
        total_size  -- Total size of the device (Default: None)
        used        -- Amount of space used on the device (Default: None)
        free        -- Free space available on the device (Default: None)
        percentage  -- Percent used on the device (Default: None) fixme: Check if it should be free?
    """
    def __init__(self, device=None, mountpoint=None, filesystem=None, usage=None,
                 total_size=None, used=None, free=None, percentage=None):
        self.device = device
        self.mountpoint = mountpoint
        self.filesystem = filesystem
        self.usage = usage
        self.total_size = total_size
        self.used = used
        self.free = free
        self.percentage = percentage

    def __repr__(self):
        return f"<HardDriveRecord device:{self.device} mountpoint:{self.mountpoint}>"

    def __str__(self):
        return f"""
Hard Drive Information:
Device: {self.device}
Mountpoint: {self.mountpoint}
Filesystem: {self.filesystem}
Usage: {self.usage}
Total Size: {self.total_size}
Used: {self.used}
Free: {self.free}
Percentage: {self.percentage}"""


class HardDriveRecords:
    """
    Holds and records a list of <HardDriveRecord> based on the specs of the current machine

    Returns: A <HardDriveRecords> object containing zero or more <HardDriveRecord> objects.
    """
    def __init__(self, hard_drive_record_list=None):
        # Check if all list items are HardDriveRecord and if so, add them to self.
        if hard_drive_record_list and all(isinstance(x, HardDriveRecord) for x in hard_drive_record_list):
            self.list = hard_drive_record_list
        else:
            self.list = []

    def __repr__(self):
        return f"<HardDriveRecords total_records:{len(self.list)}>"

    def __str__(self):
        if len(self.list) > 0:
            return f"""
First Hard Drive Record:
Device: {self.list[0].device}
Mountpoint: {self.list[0].mountpoint}
Filesystem: {self.list[0].filesystem}
Usage: {self.list[0].usage}
Total Size: {self.list[0].total_size}
Used: {self.list[0].used}
Free: {self.list[0].free}
Percentage: {self.list[0].percentage}"""
        else:
            return "No Hard Drives Found!"

    def addRecord(self, hard_drive_record):
        """Adds a <HardDriveRecord> to <HardDriveRecords> list"""
        if isinstance(hard_drive_record, HardDriveRecord):
            self.list.append(hard_drive_record)

    def test(self):
        """
        Performs the HardDrive test and records record to self

        Returns: <HardDriveRecord>
        """
        disk_io = psutil.disk_io_counters()
        partitions = psutil.disk_partitions()
        self.list = []

        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                partition_usage = "Disk Not Ready"
                continue
            except OSError:
                partition_usage = "Disk not ready"
                continue

            device_object = HardDriveRecord(
                device=partition.device,
                mountpoint=partition.mountpoint,
                filesystem=partition.fstype,
                usage=partition_usage,
                total_size=get_size(partition_usage.total),
                used=get_size(partition_usage.used),
                free=get_size(partition_usage.free),
                percentage=f"{partition_usage.percent}%"
            )
            self.addRecord(device_object)
        return self
