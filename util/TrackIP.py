import requests
import json

class TrackIP:
    '''
        Helper class to Track location using https://ip-api.com/docs API

        @input IP: Only accepts ipv4
        Example:
        test = TrackIP(ip)
        result = test.getInfo()
        This will give json retrieved from the API call if api call was successful.

        Other Functions:
        getCountry(), getRegion(), getCity(), getZip(), getTimeZone()
    '''

    def __init__(self, ip):
        if ip and self.isValidIP(ip):
            self.ip = ip
            self.info = self.getInfo()
        else:
            raise Exception("IP Address is invalid")
    
    def isValidIP(self, ip):
        if not isinstance(ip, str):
            return False
        try:
            x = list(map(int, ip.split(".")))
        except:
            return False

        if len(x) != 4:
            return False

        return all(i >= 0 and i <= 255 for i in x)
        
    
    def getInfo(self):
        if self.ip and self.ip != '127.0.0.1':
            response = requests.get("http://ip-api.com/json/"+self.ip)
            info = json.loads(response.text)

            if info['status'] == 'success':
                return info
            return None
        elif self.ip == '127.0.0.1':
            return None
        else:
            raise Exception("Invalid IP address")

    def getCity(self):
        return self.info['city']

    def getCountry(self):
        return self.info['country']
    
    def getCountryCode(self):
        return lower(self.info['countryCode'])

    def getRegion(self):
        return self.info['regionName']

    def getZip(self):
        return self.info['zip']

    def getTimeZone(self):
        return self.info['timezone']
