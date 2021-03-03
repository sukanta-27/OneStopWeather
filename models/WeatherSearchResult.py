from models.Weather import Weather
from datetime import datetime
class WeatherSearchResult:
    """
        Contains all the necessary fields that needs to be
        displayed as part of weather search result
    """
    def __init__(self, searchResult):
        if not isinstance(searchResult, dict):
            raise Exception("InValid Search Result")


    def populateSpecificDay(self, dayResult:dict):
        if not isinstance(dayResult, dict):
            raise Exception("Invalid format for Day result")

        day = Weather()
        
        # Change Unix timestamp to datetime
        day.date = print(datetime.utcfromtimestamp(\
            dayResult["dt"]).strftime('%Y-%m-%d'))

        day.city