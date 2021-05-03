import spec_checker.modules.speedtest.speedtest as speedtest


def check_speed():
    download = ""
    upload = ""
    date = ""
    time = ""
    ping = ""
    client = ""
    isp = ""
    ip = ""
    share = ""

    servers = []
    threads = None
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads, pre_allocate=False)
    s.results.share()

    results_dict = s.results.dict()
    if "download" in results_dict:
        download = round(results_dict['download'] / 1000000, 2)
    else:
        download = 0.00
    if "upload" in results_dict:
        upload = round(results_dict['upload'] / 1000000, 2)
    else:
        upload = 0.00
    if "timestamp" in results_dict:
        timestamp_raw = results_dict['timestamp'].split("T")
        date = timestamp_raw[0]
        time = timestamp_raw[1]
    else:
        date = ""
        time = ""
    if "ping" in results_dict:
        ping = results_dict['ping']
    else:
        ping = ""
    if "ping" in results_dict:
        ping = results_dict['ping']
    else:
        ping = ""
    if "client" in results_dict:
        client = results_dict['client']
        if "isp" in client:
            isp = client['isp']
        else:
            isp = ""
        if "ip" in client:
            ip = client['ip']
        else:
            ip = ""
    else:
        isp = ""
        ip = ""
    if "share" in results_dict:
        share = results_dict['share']
    else:
        share = ""

    return {
        'download': download,
        'upload': upload,
        'date': date,
        'time': time,
        'ping': ping,
        'client': client,
        'isp': isp,
        'ip': ip,
        'share': share,
    }


def get_speed():
    return check_speed()


def print_speed():
    speed = get_speed()
    print("="*20 + " Internet Speed Information " + "="*20)
    print("Timestamp: " + str(speed['date']) + "  " + str(speed['time']))
    print("IP Address: " + str(speed['ip']))
    print("Download Speed: " + str(speed['download']) + "Mbps")
    print("Upload Speed: " + str(speed['upload']) + "Mbps")
    print("Ping: " + str(speed['ping']) + "ms")
    print("ISP: " + str(speed['isp']))
    print("Share Link: " + str(speed['share']))
    print(" ")


if __name__ == '__main__':
    print_speed()
