class Weather:
    """
        Contains weather data for a specific day
    """
    def __init__(self, date=None, city=None, country=None, icon=None, \
        temperature=None, humidity=None, uvi=None, wind=None):
        self.date = date
        self.city = city
        self.country = country
        self.icon = icon
        self.temperature = temperature
        self.humidity = humidity
        self.uvi = uvi
        self.wind = wind

