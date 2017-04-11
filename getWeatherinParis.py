#!/usr/bin/python3
#This module grabs the weather in Paris

import requests, bs4, sys
from twython import Twython

#Create a .txt file in the directory of your script with your API keys.
keys = {}
with open("API_keys.txt") as f:
    for line in f:
       (key, val) = line.split()
       keys[int(key)] = val

api = Twython(keys[1],keys[2],keys[3],keys[4])

print("Checking the weather...") #Loading text

weatherPage = requests.get('https://weather.com/weather/today/l/FRXX0076:1:FR')
weatherPage.raise_for_status()
weatherSoup = bs4.BeautifulSoup(weatherPage.text, "html.parser")

degreesNowF = weatherSoup.find_all(class_='today_nowcard-temp')
sliceF = degreesNowF[0].getText()
print(type(sliceF))
print(sliceF)

degreesNowC = ((int)(sliceF[:2]) - 32) / 1.8
print(degreesNowC)
tweetThis = ("The temperature in Paris at this moment is: " + degreesNowF[0].getText() + " Fahrenheit." " Or " + str(round(degreesNowC)) + "° Celsius. Have a wonderful day!")

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
