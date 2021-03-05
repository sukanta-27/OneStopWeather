import json

class Country:

    def retrieveCountryCode(countryName):
        file = open("data\country_code.json", 'r')
        countryData = json.load(file)
        countryCode = ''
        for i in countryData:
            if i['Name'] == countryName:
                countryCode = i['Code']

        file.close()
        return countryCode

    def retrieveCountryName(countryCode):
        file = open("data\country_code.json", 'r')
        countryData = json.load(file)
        countryName = ''
        for i in countryData:
            if i['Code'] == countryCode:
                countryName = i['Name']

        file.close()
        return countryName    