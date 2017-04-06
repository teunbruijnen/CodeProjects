#! python3
#This module grabs a funny daily quote

import requests, bs4, sys
from twython import Twython

apiKey = 'SECRET'
apiSecret = 'VERY SECRET'
accessToken = 'ALSO SECRET'
accessTokenSecret = 'EVEN MORE SECRET'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

print("Looking up quotes...") #Loading text

quotePage = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
quotePage.raise_for_status()
quotePageSoup = bs4.BeautifulSoup(quotePage.text, "html.parser")

AllQuotes = quotePageSoup.find_all('div', class_='bqcpx')

tweetThis = AllQuotes[4].getText()

api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
