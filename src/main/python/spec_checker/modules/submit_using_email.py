#  we'll need the spec record and an emailRecord class
import json

import requests

SPEC_FIELDS = [
    "sound_card_present",
    "default_sound_card",
    "mic_present",
    "default_mic",
    "gpu_name",
    "gpu_free_memory",
    "gpu_total_memory",
    "gpu_load",
    "physical_cores",
    "total_cores",
    "max_frequency",
    "current_frequency",
    "cpu_load",
    "device",
    "filesystem",
    "total_size",
    "used",
    "percent_used",
    "location_provider",
    "ip_address",
    "city",
    "state",
    "gps_location",
    "isp",
    "timezone",
    "wifi_connected",
    "interface_name",
    "address_family",
    "netmask",
    "network_ip_address",
    "system_type",
    "computer_name",
    "os_release",
    "os_version",
    "machine_type",
    "processor_family",
    "boot_time_timestamp",
    "boot_time_formatted",
    "source",
    "status",
    "speedtest_provider",
    "download_speed",
    "upload_speed",
    "ping",
]


class EmailRecord:
    """Holds and submits specifications to an email server

Keyword Arguments:
data            -- Data in string form that should be the body text of email (Default: None)
email_provider  -- Email provider to send emails (Default: formsubmit_io)
email_subject   -- Subject line of results email (Default: Specification Results)"""

    def __init__(self, data=None, provider="internal", subject="Specification Results", send_address=None, cc_addresses=None):
        self.sent = False
        self.provider = provider
        self.data = data
        self.subject = subject
        self.send_address = send_address

    def __repr__(self):
        return f"<EmailRecord email_sent:{self.sent} email_provider:{self.provider}>"

    def __str__(self):
        return f"""
Email Submission Information:
Email Sent: {self.email_sent}
Email Provider: {self.email_provider}"""

    def submit(self):
        """Submits SpecRecord to email provider
        Returns: <EmailRecord>
        """
        pass


class FormSubmitRecord(EmailRecord):
    def __init__(self, fields=None, email_provider="internal", send_address=None, subject=None,
                 template=None, autoresponse=None, cc_addresses=None, webhook=None, url=None):
        super().__init__()
        if fields is not None:
            self.fields = fields
            pass
        else:
            self.fields = SPEC_FIELDS
        if email_provider is not None:
            self.email_provider = email_provider
        if send_address is not None:
            self.send_address = send_address
        if subject is not None:
            self.subject = subject
        if template is not None:
            self.template = template
        if autoresponse is not None:
            self.autoresponse = autoresponse
        if cc_addresses is not None:
            self.cc_addresses = cc_addresses
        if webhook is not None:
            self.webhook = webhook
        if url is not None:
            self.url = url

    def submit(self, data=None):
        specs = data
        email_data = {
            "email_provider": f"{self.email_provider}",
            "send_address": f"{self.send_address}",
            "subject": f"{self.subject}",
            "template": f"{self.template}",
            "autoresponse": f"{self.autoresponse}",
            "cc_addresses": f"{self.cc_addresses}",
            "webhook": f"{self.webhook}",
            "specs_msg": {
                "sound_card_present": {
                    "name": "Sound Card Present",
                    "value": str(specs.sound.sound_card_present),
                },
                "default_sound_card": {
                    "name": "Default Sound Card",
                    "value": str(specs.sound.default_sound_card),
                },
                "mic_present": {
                    "name": "Mic Present",
                    "value": str(specs.sound.mic_present),
                },
                "default_mic": {
                    "name": "Default Mic",
                    "value": str(specs.sound.default_mic),
                },
                "gpu_name": {
                    "name": "GPU Name",
                    "value": str(specs.gpus.list[0].gpu_name),
                },
                "gpu_free_memory": {
                    "name": "GPU Free Memory",
                    "value": str(specs.gpus.list[0].gpu_free_memory),
                },
                "gpu_total_memory": {
                    "name": "GPU Total Memory",
                    "value": str(specs.gpus.list[0].gpu_total_memory),
                },
                "gpu_load": {
                    "name": "GPU Load",
                    "value": str(specs.gpus.list[0].gpu_load),
                },
                "physical_cores": {
                    "name": "CPU Physical Cores",
                    "value": str(specs.cpu.physical_cores),
                },
                "total_cores": {
                    "name": "CPU Total Cores",
                    "value": str(specs.cpu.total_cores),
                },
                "max_frequency": {
                    "name": "CPU Max Frequency",
                    "value": str(specs.cpu.max_frequency),
                },
                "current_frequency": {
                    "name": "CPU Current Frequency",
                    "value": str(specs.cpu.current_frequency),
                },
                "cpu_load": {
                    "name": "CPU Load",
                    "value": str(specs.cpu.total_usage),
                },
                "device": {
                    "name": "Hard Drive Device",
                    "value": str(specs.harddrives.list[0].device),
                },
                "filesystem": {
                    "name": "Hard Drive File System",
                    "value": str(specs.harddrives.list[0].filesystem),
                },
                "total_size": {
                    "name": "Hard Drive Total Size",
                    "value": str(specs.harddrives.list[0].total_size),
                },
                "used": {
                    "name": "Hard Drive Used",
                    "value": str(specs.harddrives.list[0].used),
                },
                "percent_used": {
                    "name": "Hard Drive Percent Used",
                    "value": str(specs.harddrives.list[0].percentage),
                },
                "location_provider": {
                    "name": "Location Provider",
                    "value": str("ip.info")
                },
                "ip_address": {
                    "name": "IP Address",
                    "value": str(specs.location.ip),
                },
                "city": {
                    "name": "City",
                    "value": str(specs.location.city),
                },
                "state": {
                    "name": "State",
                    "value": str(specs.location.region),
                },
                "gps_location": {
                    "name": "Approximate GPS Location",
                    "value": str(specs.location.loc),
                },
                "isp": {
                    "name": "ISP",
                    "value": str(specs.location.org),
                },
                "timezone": {
                    "name": "Timezone",
                    "value": str(specs.location.timezone),
                },
                "wifi_connected": {
                    "name": "Wifi Connected",
                    "value": str(specs.network.wifi_status),
                },
                "interface_name": {
                    "name": "Network Interface Name",
                    "value": str(specs.network.list[0].interface_name),
                },
                "address_family": {
                    "name": "Address Family",
                    "value": str(specs.network.list[0].address_family),
                },
                "netmask": {
                    "name": "Netmask",
                    "value": str(specs.network.list[0].netmask),
                },
                "network_ip_address": {
                    "name": "Network IP Address",
                    "value": str(specs.network.list[0].ip_address),
                },
                "system_type": {
                    "name": "System Type",
                    "value": str(specs.system.system_type),
                },
                "computer_name": {
                    "name": "Computer Name",
                    "value": str(specs.system.computer_name),
                },
                "os_release": {
                    "name": "OS Release",
                    "value": str(specs.system.os_release),
                },
                "os_version": {
                    "name": "OS Version",
                    "value": str(specs.system.os_version),
                },
                "machine_type": {
                    "name": "Machine Type",
                    "value": str(specs.system.machine_type),
                },
                "processor_family": {
                    "name": "Processor Family",
                    "value": str(specs.system.processor_family),
                },
                "boot_time_timestamp": {
                    "name": "Boot Time Timestamp",
                    "value": str(specs.system.boot_time_timestamp),
                },
                "boot_time_formatted": {
                    "name": "Boot Time Formatted",
                    "value": str(specs.system.boot_time_formatted),
                },
                "source": {
                    "name": "Webcam Source",
                    "value": str(specs.webcams.list[0].source),
                },
                "status": {
                    "name": "Webcam Status",
                    "value": str(specs.webcams.list[0].status),
                },
                "speedtest_provider": {
                    "name": "Speed Test Provider",
                    "value": str("fast.com")
                },
                "download_speed": {
                    "name": "Download Speed",
                    "value": str(specs.speedtest.download_speed),
                },
                "upload_speed": {
                    "name": "Upload Speed",
                    "value": str(specs.speedtest.upload_speed),
                },
                "ping": {
                    "name": "Ping",
                    "value": str(specs.speedtest.ping),
                },
                "share": {
                    "name": "Speedtest Results Image Link",
                    "value": str(specs.speedtest.share)
                }
            },
            "fields": f"{self.fields}"
        }
        url = f"{self.url}"
        print(json.dumps(email_data))
        request = requests.post(url, data=json.dumps(email_data))
        print(request)
        return request
