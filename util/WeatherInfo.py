import requests
import json
import os

class WeatherInfo:
    
    def __init__(self, city=None, country=None, zip=None, units='metric'):

        # First check API key is set in .env file
        self.checkAPIKey()

        self.city = city
        if country:
            self.country = country.title()
            self.countryCode = self.retrieveCountryCode()

        self.zip = zip
        self.units = units
    
    def checkAPIKey(self):
        if os.getenv('API_KEY'):
            return True
        else:
            raise "API key not found in .env file"

    def retrieveCountryCode(self):
        if not self.country:
            return None
        file = open("data\country_code.json", 'r')
        codes = json.load(file)

        for i in codes:
            if i['Name'] == self.country:
                file.close()
                return i['Code']

        file.close()
        return None

    def getWeatherByCity(self):
        '''
            Returns weather data in JSON format
        '''
        if self.city:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&units={self.units}&appid={os.getenv('API_KEY')}")
            if response.status_code == 200:
                info = json.loads(response.text)
                return info
            else:
                raise Exception("Could not retrieve the weather info")
        else:
            raise Exception("Please provide city name to get weather info")
    
    def getWeatherByZip(self):
        if self.zip and self.countryCode:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?zip={self.zip},{self.countryCode}&units={self.units}&appid={os.getenv('API_KEY')}")
            if response.status_code == 200:
                info = json.loads(response.text)
                return info
            else:
                raise Exception("Could not retrieve the weather info")
        else:
            raise Exception("Please provide Zip code and Country")            