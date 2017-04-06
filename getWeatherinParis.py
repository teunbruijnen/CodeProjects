#!/usr/bin/python3
#This module grabs the weather in Paris

import requests, bs4, sys
from twython import Twython

apiKey = 'tJBz2topdypr1BnOqodAxyK3o'
apiSecret = 'DD5YwsEJByUDRgl3axF4iGFxHdLaWxbh4bmi3t6iNZZDFkrRKL'
accessToken = '848859293222916096-lSd5ZGPWGBb6ZZDSVh2qVet9dHPCgoS'
accessTokenSecret = 'qKsiNpp7u0ILIfaetJxpKpsp90LtP1TTGNIkL5bXkJUvW'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

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
