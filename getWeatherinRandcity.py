#!/usr/local/bin/python3.5
#This module grabs the weather in a random city and uploads it to twitter
#BE AWARE: This script was written to run on a raspberry pi specifically

import requests, bs4, sys
from random import randint
from twython import Twython

<<<<<<< HEAD
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
=======
apiKey = 'SECRET'
apiSecret = 'VERY SECRET'
accessToken = 'ALSO SECRET'
accessTokenSecret = 'EVEN MORE SECRET'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

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
>>>>>>> 36266f5ec1ebc042a3a005ba7d31e984620dae23
weatherSoup = bs4.BeautifulSoup(weatherPage.text, "html.parser")

degreesNowF = weatherSoup.find_all(class_='today_nowcard-temp')
sliceF = degreesNowF[0].getText()
degreesNowC = ((int)(sliceF[:2]) - 32) / 1.8

<<<<<<< HEAD
niceWords = ['nice', 'great', 'good', 'wonderful', 'beautiful']

tweetThis = ("The temperature in %s at this moment is: %s Fahrenheit. Or %s° Celsius. Have a %s day!" % (randomCity, degreesNowF[0].getText(), str(round(degreesNowC)), niceWords[randint(0,4)]))
=======
tweetThis = (cityToTweet + degreesNowF[0].getText() + " Fahrenheit." " Or " + str(round(degreesNowC)) + "° Celsius. Have a wonderful day!")
>>>>>>> 36266f5ec1ebc042a3a005ba7d31e984620dae23

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
