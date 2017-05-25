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
CityandSite = {'Amsterdam':'https://weather.com/weather/today/l/NLXX0002:1:NL', 'Paris':'https://weather.com/weather/today/l/FRXX0076:1:FR', 'Barcelona':'https://weather.com/weather/today/l/SPXX0015:1:SP', 'London':'https://weather.com/weather/today/l/UKXX0085:1:UK', 'Berlin':'https://weather.com/weather/today/l/GMXX0007:1:GM', 'Lima':'https://weather.com/weather/today/l/PEXX0011:1:PE', 'Moscow':'https://weather.com/weather/today/l/RSXX0063:1:RS', 'Istanbul':'https://weather.com/weather/today/l/TUXX0014:1:TU', 'New York':'https://weather.com/weather/today/l/USNY0996:1:US', 'Los Angeles':'https://weather.com/weather/today/l/USCA0638:1:US', 'Buenos Aires':'https://weather.com/weather/today/l/ARBA0009:1:AR', 'Alert':'https://weather.com/weather/today/l/CAXX0829:1:CA'}

City = list(CityandSite.keys())
randomCity = City[randint(0,(len(City)-1))]
print(randomCity)
weatherPage = requests.get(CityandSite[randomCity])
weatherSoup = bs4.BeautifulSoup(weatherPage.text, "html.parser")

degreesNowF = weatherSoup.find_all(class_='today_nowcard-temp')
print(degreesNowF)
sliceF = degreesNowF[0].getText()
degreesNowC = ((int)(sliceF[:2]) - 32) / 1.8

niceWords = ['nice', 'great', 'good', 'wonderful', 'beautiful']
hashTags = ['#weather', '#dailyweather', '#bot', '#python', '#programming', '#daily', '#data', '#temp', '#temperature']
hashTags.extend([randomCity])

tweetThis = ("The temperature in %s at this moment is: %s Fahrenheit. Or %s° Celsius. Have a %s day! %s %s #%s" % (randomCity, degreesNowF[0].getText(), str(round(degreesNowC)), niceWords[randint(0,4)], hashTags[randint(0,1)], hashTags[randint(2,4)], hashTags[(len(hashTags)-1)]))

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
