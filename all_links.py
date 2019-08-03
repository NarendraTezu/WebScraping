"""
In this program scraping all the links form website of give link
"""

import bs4		#importing beautyful shop library
import requests

url = "http://www.burjeel.com/abu-dhabi"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')	# Use html parser for parsing the web data

for links in soup.find_all('a'):                #it will use for ancor tag
    link =  links.get('href')                  #it will take attribute of href
    if link != "#":
        print("http://www.burjeel.com/" + str(link))


