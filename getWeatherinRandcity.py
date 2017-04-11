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
citiestoSelect = ['Amsterdam', 'Paris', 'Barcelona', 'London', 'Berlin']
randomCity = citiestoSelect[randint(0,4)]

weatherPage = 0
cityToTweet = 0

#todo: Use something other then an elif here
if randomCity == 'Amsterdam':
    cityToTweet = "The temperature in Amsterdam at this moment is: "
    weatherPage = requests.get('https://weather.com/weather/today/l/NLXX0002:1:NL')
elif randomCity == 'Paris':
    cityToTweet = "The temperature in Paris at this moment is: "
    weatherPage = requests.get('https://weather.com/weather/today/l/FRXX0076:1:FR')
elif randomCity == 'Barcelona':
    cityToTweet = "The temperature in Barcelona at this moment is: "
    weatherPage = requests.get('https://weather.com/weather/today/l/SPXX0015:1:SP')
elif randomCity == 'London':
    cityToTweet = "The temperature in London at this moment is: "
    weatherPage = requests.get('https://weather.com/weather/today/l/UKXX0085:1:UK')
elif randomCity == 'Berlin':
    cityToTweet = "The temperature in Berlin at this moment is: "
    weatherPage = requests.get('https://weather.com/weather/today/l/GMXX0007:1:GM')

weatherPage.raise_for_status()
weatherSoup = bs4.BeautifulSoup(weatherPage.text, "html.parser")

degreesNowF = weatherSoup.find_all(class_='today_nowcard-temp')
sliceF = degreesNowF[0].getText()
degreesNowC = ((int)(sliceF[:2]) - 32) / 1.8

tweetThis = (cityToTweet + degreesNowF[0].getText() + " Fahrenheit." " Or " + str(round(degreesNowC)) + "° Celsius. Have a wonderful day!")

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
