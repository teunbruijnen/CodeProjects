#! python3
#This module grabs a funny daily quote

import requests, bs4, sys
from twython import Twython

<<<<<<< HEAD
#Create a .txt file in the directory of your script with your API keys.
keys = {}
with open("API_keys.txt") as f:
    for line in f:
       (key, val) = line.split()
       keys[int(key)] = val

api = Twython(keys[1],keys[2],keys[3],keys[4])
=======
apiKey = 'SECRET'
apiSecret = 'VERY SECRET'
accessToken = 'ALSO SECRET'
accessTokenSecret = 'EVEN MORE SECRET'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
>>>>>>> 36266f5ec1ebc042a3a005ba7d31e984620dae23

print("Looking up quotes...") #Loading text

quotePage = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
quotePage.raise_for_status()
quotePageSoup = bs4.BeautifulSoup(quotePage.text, "html.parser")

AllQuotes = quotePageSoup.find_all('div', class_='bqcpx')

tweetThis = AllQuotes[4].getText()

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
