import requests
import json
import os
import logging
from util.Helper import Country
from DataClass.WeatherSearchResult import Weather

class WeatherInfo:
    
    def __init__(self, city=None, country=None, zip=None, units='metric'):

        # First check API key is set in .env file
        self.checkAPIKey()

        self.city = city
        if country:
            self.country = country.title()
            self.countryCode = Country.retrieveCountryCode(self.country)

        self.zip = zip
        self.units = units
    
    def checkAPIKey(self):
        if os.getenv('API_KEY'):
            return True
        else:
            logging.error("API KEY not found")
            raise Exception("API key not found in .env file")

    def getWeatherByCity(self):
        '''
            Returns weather data in JSON format
        '''
        if self.city:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/forecast?q={self.city}&units={self.units}&appid={os.getenv('API_KEY')}")
            if response.status_code == 200:
                info = json.loads(response.text)
                weatherData = Weather(info)
                return weatherData
            else:
                logging.error("Could not retrieve the weather info")
                raise Exception("Could not retrieve the weather info")
        else:
            raise Exception("Please provide city name to get weather info")
    
    def getWeatherByZip(self):
        if self.zip and self.countryCode:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/forecast?zip={self.zip},{self.countryCode}&units={self.units}&appid={os.getenv('API_KEY')}")
            if response.status_code == 200:
                info = json.loads(response.text)
                weatherData = Weather(info)
                return weatherData
            else:
                logging.error("Could not retrieve the weather info")
                raise Exception("Could not retrieve the weather info")
        else:
            raise Exception("Please provide Zip code and Country")            