import requests
import json
import os

class WeatherInfo:
    
    def __init__(self, city=None, region=None, country=None, zip=None, id=None):
        self.city = city
        self.region = region
        self.country = country
        self.zip = zip
        self.id = id
    
    def getWeatherByCity(self):
        '''
            Returns weather data in JSON format
        '''
        if self.city:
            response = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={os.getenv('API_KEY')}")
            if response.status_code == 200:
                info = json.loads(response.text)
                return info
            else:
                raise Exception("Could not retrieve the weather info")
        else:
            raise Exception("Please provide city name to get weather info")