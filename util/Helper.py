import json
import pathlib
import logging
class Country:
    

    def retrieveCountryCode(countryName):
        filePath = pathlib.Path.joinpath(pathlib.Path.cwd(), "data", "country_code.json")
        file = open(filePath, 'r')
        countryData = json.load(file)
        countryCode = ''
        for i in countryData:
            if i['Name'] == countryName:
                countryCode = i['Code']

        file.close()
        return countryCode

    def retrieveCountryName(countryCode):
        filePath = pathlib.Path.joinpath(pathlib.Path.cwd(), "data", "country_code.json")
        file = open(filePath, 'r')
        countryData = json.load(file)
        countryName = ''
        for i in countryData:
            if i['Code'] == countryCode:
                countryName = i['Name']

        file.close()
        return countryName    