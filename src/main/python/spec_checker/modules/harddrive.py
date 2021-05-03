import psutil
from spec_checker.modules.utilities import get_size


class HardDriveRecord:
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


class HardDriveRecords:
    """
    A list of Hard Drive Records
    """
    def __init__(self, hard_drive_record_list=None):
        # Check if all list items are HardDriveRecord and if so, add them to self.
        if hard_drive_record_list and all(isinstance(x, HardDriveRecord) for x in hard_drive_record_list):
            self.list = hard_drive_record_list
        else:
            self.list = []

    def addRecord(self, hard_drive_record):
        if isinstance(hard_drive_record, HardDriveRecord):
            self.list.append(hard_drive_record)

    def test(self):
        disk_io = psutil.disk_io_counters()
        partitions = psutil.disk_partitions()
        self.hard_drive_record_list = []

        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                partition_usage = "Disk Not Ready"
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
