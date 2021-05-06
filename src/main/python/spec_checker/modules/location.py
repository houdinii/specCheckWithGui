import requests
from json import JSONDecodeError


class LocationRecord:
    """Holds and records the location of the client device

    Keyword Arguments:
        ip          -- Current client device IP address (Default: None)
        city        -- Approximate city of the device (Default: None)
        region      -- Approximate region of device, typically state in the USA (Default: None)
        loc         -- Approximate gps location of device (Default: None)
        org         -- Registered owner of IP address, usually the ISP (Default: None)
        timezone    -- Timezone of client machine (Default: None)
    """
    def __init__(self, ip=None, city=None, region=None, loc=None, org=None, timezone=None):
        self.ip = ip
        self.city = city
        self.region = region
        self.loc = loc
        self.org = org
        self.timezone = timezone

    def __repr__(self):
        return f"<LocationRecord city:{self.city} region:{self.region}>"

    def __str__(self):
        return f"""
Location Information:
Ip: {self.ip}
City: {self.city}
Region: {self.region}
Loc: {self.loc}
Org Size: {self.org}
Timezone: {self.timezone}"""

    def test(self):
        """Performs the location test and records record to self

        Returns: <LocationRecord>
        """
        response = requests.get("https://ipinfo.io/")
        response_json = {}
        try:
            response_json = response.json()
        except JSONDecodeError as e:
            response_json["ip"] = "Error with remote website. This is not an error with the client."
            response_json["city"] = "Error with remote website. This is not an error with the client."
            response_json["region"] = "Error with remote website. This is not an error with the client."
            response_json["loc"] = "Error with remote website. This is not an error with the client."
            response_json["org"] = "Error with remote website. This is not an error with the client."
            response_json["timezone"] = "Error with remote website. This is not an error with the client."

        self.ip = str(response_json['ip'])
        self.city = str(response_json['city'])
        self.region = str(response_json['region'])
        self.loc = str(response_json['loc'])
        self.org = str(response_json['org'])
        self.timezone = str(response_json['timezone'])
        return self
