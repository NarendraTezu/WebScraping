"""
In this file we scraping the data from given link it will give the weather report in csv file 
"""
# importing requried library

import pandas as pd
import requests
from bs4 import BeautifulSoup


url = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.0535&lon=-118.2453')          # from this link data will be scraping
soup = BeautifulSoup(url.content, 'html.parser')   # use html parser for parsing data
week = soup.find(id='seven-day-forecast-body')
#print(week)
elements = (week.find_all(class_='tombstone-container'))
#print(elements[0])

#print(elements[0].find(class_='period-name').get_text())
#print(elements[0].find(class_='short-desc').get_text())
#print(elements[0].find(class_='temp').get_text())

period_names = [element.find(class_='period-name').get_text() for element in elements]
#print(period_names)

short_descriptions = [element.find(class_='short-desc').get_text() for element in elements]
#print(short_descriptions)

temperatures = [element.find(class_='temp').get_text() for element in elements]
#print(temperatures)

# using data fram from pandas to conver in dictnory
weatherinfo = pd.DataFrame(
    {
        'period': period_names,
        'short_descriptions': short_descriptions,
        'temperatures':temperatures
    }
)

print(weatherinfo)

# Changing weather report in csv file 

weatherinfo.to_csv('weather.csv')

print("====================================================")
print("csv file genrated with name weather.csv")
