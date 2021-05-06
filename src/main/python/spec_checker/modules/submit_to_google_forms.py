import requests

import spec_checker.modules.spec_record


def google_submit(spec_object=spec_checker.modules.spec_record.SpecRecord()):
    # with open('example.config.json5') as f:
    #     json_data = json5.load(f)
    data = fill_data(spec_object)
    url = str(data['pre_url']) + str(data['form_id']) + str(data['post_url'])
    post_data = {}
    for field in data['fields']:
        entry = data['fields'][field]['entry']
        name = data['fields'][field]['name']
        value = data['fields'][field]['value']
        post_data[entry] = str(value)
    r = requests.post(url=url, data=post_data)
    return r


def fill_data(specs=spec_checker.modules.spec_record.SpecRecord()):
    google_sheets = {
        "enabled": True,
        "pre_url": "https://docs.google.com/forms/d/e/",
        "form_id": "***REMOVED***",
        "post_url": "/formResponse",
        "fields": {
            "sound_card_present": {
                "name": "Sound Card Present",
                "entry": "entry.429961728",
                "enabled": True,
                "value": specs.sound.sound_card_present,
            },
            "default_sound_card": {
                "name": "Default Sound Card",
                "entry": "entry.230414178",
                "enabled": True,
                "value": specs.sound.default_sound_card,
            },
            "mic_present": {
                "name": "Mic Present",
                "entry": "entry.1918180951",
                "enabled": True,
                "value": specs.sound.mic_present,
            },
            "default_mic": {
                "name": "Default Mic",
                "entry": "entry.1649797265",
                "enabled": True,
                "value": specs.sound.default_mic,
            },
            "gpu_name": {
                "name": "GPU Name",
                "entry": "entry.1834660995",
                "enabled": True,
                "value": specs.gpus.list[0].gpu_name,
            },
            "gpu_free_memory": {
                "name": "GPU Free Memory",
                "entry": "entry.1557665733",
                "enabled": True,
                "value": specs.gpus.list[0].gpu_free_memory,
            },
            "gpu_total_memory": {
                "name": "GPU Total Memory",
                "entry": "entry.270378644",
                "enabled": True,
                "value": specs.gpus.list[0].gpu_total_memory,
            },
            "gpu_load": {
                "name": "GPU Load",
                "entry": "entry.467932031",
                "enabled": True,
                "value": specs.gpus.list[0].gpu_load,
            },
            "physical_cores": {
                "name": "CPU Physical Cores",
                "entry": "entry.153889402",
                "enabled": True,
                "value": specs.cpu.physical_cores,
            },
            "total_cores": {
                "name": "CPU Total Cores",
                "entry": "entry.2084526737",
                "enabled": True,
                "value": specs.cpu.total_cores,
            },
            "max_frequency": {
                "name": "CPU Max Frequency",
                "entry": "entry.1380246857",
                "enabled": True,
                "value": specs.cpu.max_frequency,
            },
            "current_frequency": {
                "name": "CPU Current Frequency",
                "entry": "entry.2023555002",
                "enabled": True,
                "value": specs.cpu.current_frequency,
            },
            "cpu_load": {
                "name": "CPU Load",
                "entry": "entry.1660444592",
                "enabled": True,
                "value": specs.cpu.total_usage,
            },
            "device": {
                "name": "Hard Drive Device",
                "entry": "entry.1467072790",
                "enabled": True,
                "value": specs.harddrives.list[0].device,
            },
            "filesystem": {
                "name": "Hard Drive File System",
                "entry": "entry.1536454890",
                "enabled": True,
                "value": specs.harddrives.list[0].filesystem,
            },
            "total_size": {
                "name": "Hard Drive Total Size",
                "entry": "entry.1199915875",
                "enabled": True,
                "value": specs.harddrives.list[0].total_size,
            },
            "used": {
                "name": "Hard Drive Used",
                "entry": "entry.43503379",
                "enabled": True,
                "value": specs.harddrives.list[0].used,
            },
            "percent_used": {
                "name": "Hard Drive Percent Used",
                "entry": "entry.1395473982",
                "enabled": True,
                "value": specs.harddrives.list[0].percentage,
            },
            "location_provider": {
                "name": "Location Provider",
                "entry": "entry.557364417",
                "enabled": True,
                "value": "ip.info"
            },
            "ip_address": {
                "name": "IP Address",
                "entry": "entry.1853485645",
                "enabled": True,
                "value": specs.location.ip,
            },
            "city": {
                "name": "City",
                "entry": "entry.619756930",
                "enabled": True,
                "value": specs.location.city,
            },
            "state": {
                "name": "State",
                "entry": "entry.327537330",
                "enabled": True,
                "value": specs.location.region,
            },
            "gps_location": {
                "name": "Approximate GPS Location",
                "entry": "entry.203968900",
                "enabled": True,
                "value": specs.location.loc,
            },
            "isp": {
                "name": "ISP",
                "entry": "entry.1275072",
                "enabled": True,
                "value": specs.location.org,
            },
            "timezone": {
                "name": "Timezone",
                "entry": "entry.249862697",
                "enabled": True,
                "value": specs.location.timezone,
            },
            "wifi_connected": {
                "name": "Wifi Connected",
                "entry": "entry.599324513",
                "enabled": True,
                "value": specs.network.wifi_status,
            },
            "interface_name": {
                "name": "Network Interface Name",
                "entry": "entry.292860716",
                "enabled": True,
                "value": specs.network.list[0].interface_name,
            },
            "address_family": {
                "name": "Address Family",
                "entry": "entry.2122513792",
                "enabled": True,
                "value": specs.network.list[0].address_family,
            },
            "netmask": {
                "name": "Netmask",
                "entry": "entry.1584727169",
                "enabled": True,
                "value": specs.network.list[0].netmask,
            },
            "network_ip_address": {
                "name": "Network IP Address",
                "entry": "entry.1760686138",
                "enabled": True,
                "value": specs.network.list[0].ip_address,
            },
            "system_type": {
                "name": "System Type",
                "entry": "entry.1285486647",
                "enabled": True,
                "value": specs.system.system_type,
            },
            "computer_name": {
                "name": "Computer Name",
                "entry": "entry.279575207",
                "enabled": True,
                "value": specs.system.computer_name,
            },
            "os_release": {
                "name": "OS Release",
                "entry": "entry.166883694",
                "enabled": True,
                "value": specs.system.os_release,
            },
            "os_version": {
                "name": "OS Version",
                "entry": "entry.873836820",
                "enabled": True,
                "value": specs.system.os_version,
            },
            "machine_type": {
                "name": "Machine Type",
                "entry": "entry.1441645089",
                "enabled": True,
                "value": specs.system.machine_type,
            },
            "processor_family": {
                "name": "Processor Family",
                "entry": "entry.1624773142",
                "enabled": True,
                "value": specs.system.processor_family,
            },
            "boot_time_timestamp": {
                "name": "Boot Time Timestamp",
                "entry": "entry.1220943210",
                "enabled": True,
                "value": specs.system.boot_time_timestamp,
            },
            "boot_time_formatted": {
                "name": "Boot Time Formatted",
                "entry": "entry.1324801338",
                "enabled": True,
                "value": specs.system.boot_time_formatted,
            },
            "source": {
                "name": "Webcam Source",
                "entry": "entry.501091558",
                "enabled": True,
                "value": specs.webcams.list[0].source,
            },
            "status": {
                "name": "Webcam Status",
                "entry": "entry.1761300635",
                "enabled": True,
                "value": specs.webcams.list[0].status,
            },
            "speedtest_provider": {
                "name": "Speed Test Provider",
                "entry": "entry.2127323182",
                "enabled": True,
                "value": "fast.com"
            },
            "download_speed": {
                "name": "Download Speed",
                "entry": "entry.1143050692",
                "enabled": True,
                "value": specs.speedtest.download_speed,
            },
            "upload_speed": {
                "name": "Upload Speed",
                "entry": "entry.338182180",
                "enabled": True,
                "value": specs.speedtest.upload_speed,
            },
            "ping": {
                "name": "Ping",
                "entry": "entry.259521278",
                "enabled": True,
                "value": specs.speedtest.ping,
            },
        }
    }
    return google_sheets
