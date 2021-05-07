import platform
from spec_checker.modules.utilities import get_bit, get_size, reverse_binary, decimal_to_binary, decimal_to_hex
plt = platform.system()


class AntivirusRecord:
    """
    Holds information about the antivirus software installed in the client machine.

    :param
    display_name                    -- Branding information (Default: None)
    path_to_signed_product_exe      -- Path to AV product exe (Default: None)
    path_to_signed_reporting_exe    -- Path to AV signed reporting exe (Default: None)
    enabled                         -- String AV is enabled (Default: None)
    scanning                        -- String AV is currently scanning (Default: None)
    outdated                        -- String AV is currently outdated (Default: None)
    timestamp                       -- Time and date test was ran (Default: None)
    """
    def __init__(self, display_name=None, path_to_signed_product_exe=None, path_to_signed_reporting_exe=None,
                 enabled=None, scanning=None, outdated=None, timestamp=None):
        self.display_name = display_name
        self.path_to_signed_product_exe = path_to_signed_product_exe
        self.path_to_signed_reporting_exe = path_to_signed_reporting_exe
        self.enabled = enabled
        self.scanning = scanning
        self.outdated = outdated
        self.timestamp = timestamp

    def __repr__(self):
        return f"<AntivirusRecord display_name:{self.display_name}>"

    def __str__(self):
        return f"""
Antivirus Information:
Display Name: {self.display_name}
Path To Signed Product Exe: {self.path_to_signed_product_exe}
Path To Signed Reporting Exe: {self.path_to_signed_reporting_exe}
Enabled: {self.enabled}
Scanning: {self.scanning}
Outdated: {self.outdated}
Timestamp: {self.timestamp}"""


class AntivirusRecords:
    """Holds and records information about the antivirus program"""
    def __init__(self):
        self.list = []

    def __repr__(self):
        return f"<AntivirusRecords length: {len(self.list)}>"

    def __str__(self):
        if len(self.list) > 0:
            return f"""
First Antivirus Record:
Display Name: {self.list[0].display_name}
Path To Signed Product Exe: {self.list[0].path_to_signed_product_exe}
Path To Signed Reporting Exe: {self.list[0].path_to_signed_reporting_exe}
Enabled: {self.list[0].enabled}
Scanning: {self.list[0].scanning}
Outdated: {self.list[0].outdated}
Timestamp: {self.list[0].timestamp}"""

    def test(self):
        """Performs the antivirus test and records record to self

        :returns AntivirusRecord
        """
        if plt == "Windows":
            import wmi
            from win32com.client import GetObject

            obj_wmi = GetObject('winmgmts:\\\\.\\root\\SecurityCenter2').InstancesOf('AntiVirusProduct')
            self.list = []

            for obj in obj_wmi:
                display_name = ""
                path_to_signed_product_exe = ""
                path_to_signed_reporting_exe = ""
                enabled = ""
                scanning = ""
                outdated = ""
                timestamp = ""
                if obj.displayName is not None:
                    display_name = obj.displayName
                if obj.pathToSignedProductExe is not None:
                    path_to_signed_product_exe = obj.pathToSignedProductExe
                if obj.pathToSignedReportingExe is not None:
                    path_to_signed_reporting_exe = obj.pathToSignedReportingExe
                if obj.productState is not None:
                    ps_hex = decimal_to_hex(obj.productState)
                    ps_bin = decimal_to_binary(obj.productState)
                    ps_reverse = reverse_binary(obj.productState)

                    enabled_bit = get_bit(ps_reverse, 18)
                    scanning_bit = get_bit(ps_reverse, 12)
                    outdated_bit = get_bit(ps_reverse, 4)

                    enabled = str(enabled_bit)
                    scanning = str(scanning_bit)
                    outdated = str(outdated_bit)
                if obj.timestamp is not None:
                    timestamp = obj.timestamp
                self.list.append(AntivirusRecord(
                    display_name=display_name,
                    path_to_signed_product_exe=path_to_signed_product_exe,
                    path_to_signed_reporting_exe=path_to_signed_reporting_exe,
                    enabled=enabled,
                    scanning=scanning,
                    outdated=outdated,
                    timestamp=timestamp,
                ))
        else:
            self.list = []
            self.list.append(AntivirusRecord(
                display_name="Antivirus Test Not Available On MacOS",
                path_to_signed_product_exe="N/A",
                path_to_signed_reporting_exe="N/A",
                enabled="N/A",
                scanning="N/A",
                outdated="N/A",
                timestamp="N/A",
            ))
        return self
