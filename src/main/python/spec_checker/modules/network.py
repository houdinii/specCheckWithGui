import sys
import psutil
if sys.platform.startswith('win32'):
    import pywifi


class NetworkRecord:
    def __init__(self, interface_name=None, address_family=None, netmask=None, ip_address=None):
        self.interface_name = interface_name
        self.address_family = address_family
        self.netmask = netmask
        self.ip_address = ip_address


class NetworkRecords:
    """
    A list of Network Records
    """
    def __init__(self, network_record_list=None, wifi_status=False):
        # Check if all list items are GpuRecord and if so, add them to self.
        if network_record_list and all(isinstance(x, NetworkRecord) for x in network_record_list):
            self.list = network_record_list
        else:
            self.list = []
        self.wifi_status = wifi_status

    def addRecord(self, network_record):
        if isinstance(network_record, NetworkRecord):
            self.list.append(network_record)

    def test(self):
        disk_io = psutil.disk_io_counters()
        partitions = psutil.disk_partitions()
        self.list = []

        if_addrs = psutil.net_if_addrs()

        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                if str(address.family) != 'AddressFamily.AF_LINK' and 'Loopback' not in str(interface_name):
                    network_object = NetworkRecord(
                        interface_name=str(interface_name),
                        address_family=str(address.family),
                        netmask=str(address.netmask),
                        ip_address=str(address.address)
                    )
                    self.addRecord(network_object)
        self.wifi_status = None
        if sys.platform.startswith('win32'):
            wifi = pywifi.PyWiFi()
            iface = wifi.interfaces()[0]
            self.wifi_status = self.get_wifi_status(iface)
        return self

    def get_wifi_status(self, iface):
        if iface.status() == pywifi.const.IFACE_CONNECTED:
            status = "Connected"
        elif iface.status() == pywifi.const.IFACE_DISCONNECTED:
            status = "Disconnected"
        elif iface.status() == pywifi.const.IFACE_INACTIVE:
            status = "Inactive"
        elif iface.status() == pywifi.const.IFACE_SCANNING:
            status = "Scanning"
        elif iface.status() == pywifi.const.IFACE_CONNECTING:
            status = "Connecting"
        else:
            status = "Error"
        return status
