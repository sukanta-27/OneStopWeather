from datetime import datetime
from util.Helper import Country

class WeatherOfTheDay:
    """
        Contains weather data for a specific day
        For referrence: https://openweathermap.org/forecast5#parameter
    """
    
    def __init__(self, daySpecificData:dict):
        if not isinstance(daySpecificData, dict):
            raise Exception("Day specific weather data is not in correct format")

        self.date = daySpecificData['dt_txt'].split()[0]
        self.main = daySpecificData['weather'][0]['main']
        self.weather_description = daySpecificData['weather'][0]['description']
        self.icon = daySpecificData['weather'][0]['icon']
        self.temperature = daySpecificData['main']['temp']
        self.humidity = daySpecificData['main']['humidity']
        self.feels_like = daySpecificData['main']['feels_like']
        self.wind = daySpecificData['wind']['speed']


class Weather:
    """
        Contains all the necessary fields that needs to be
        displayed as part of weather search result
    """
    def __init__(self, searchResult):
        if not isinstance(searchResult, dict):
            raise Exception("InValid Search Result")

        self.city = searchResult['city']['name']
        self.coords = searchResult['city']['coord']
        self.country = Country.retrieveCountryName(searchResult['city']['country'])
        self.days = self.populateForecast(searchResult['list'])

    def populateForecast(self, listOfDays):
        days = []

        for i in range(0, len(listOfDays), 8):
            day = WeatherOfTheDay(listOfDays[i])
            days.append(day)
        
        return days