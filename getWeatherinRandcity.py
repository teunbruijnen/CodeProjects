#!/usr/local/bin/python3.5
#This module grabs the weather in Paris
#BE AWARE: This script was written to run on a raspberry pi specifically

import requests, bs4, sys
from random import randint
from twython import Twython

#Create a .txt file in the directory of your script with your API keys.
keys = {}
with open("API_keys.txt") as f:
    for line in f:
       (key, val) = line.split()
       keys[int(key)] = val

api = Twython(keys[1],keys[2],keys[3],keys[4])

print("Checking the weather...") #Loading text
#todo: Add more cities?
CityandSite = {'Amsterdam':'https://weather.com/weather/today/l/NLXX0002:1:NL', 'Paris':'https://weather.com/weather/today/l/FRXX0076:1:FR', 'Barcelona':'https://weather.com/weather/today/l/SPXX0015:1:SP', 'London':'https://weather.com/weather/today/l/UKXX0085:1:UK', 'Berlin':'https://weather.com/weather/today/l/GMXX0007:1:GM'}

City = list(CityandSite.keys())
randomCity = City[randint(0,4)]

weatherPage = requests.get(CityandSite[randomCity])
weatherSoup = bs4.BeautifulSoup(weatherPage.text, "html.parser")

degreesNowF = weatherSoup.find_all(class_='today_nowcard-temp')
sliceF = degreesNowF[0].getText()
degreesNowC = ((int)(sliceF[:2]) - 32) / 1.8

niceWords = ['nice', 'great', 'good', 'wonderful', 'beautiful']
hashTags = ['#weather', '#dailyweather', '#bot', '#python', '#programming']
hashTags.extend([randomCity])

tweetThis = ("The temperature in %s at this moment is: %s Fahrenheit. Or %s° Celsius. Have a %s day! %s %s #%s" % (randomCity, degreesNowF[0].getText(), str(round(degreesNowC)), niceWords[randint(0,4)], hashTags[randint(0,1)], hashTags[randint(2,4)], hashTags[5]))

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
