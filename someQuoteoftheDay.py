#!/usr/local/bin/python3.5
#This module grabs a funny daily quote

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

print("Looking up quotes...") #Loading text

quotePage = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
quotePage.raise_for_status()
quotePageSoup = bs4.BeautifulSoup(quotePage.text, "html.parser")

AllQuotes = quotePageSoup.find_all('div', class_='bqcpx')
#todo: edit the text in quotes?
randomQuote = AllQuotes[randint(0,5)].getText()

api.update_status(status=randomQuote)

print("Tweeted: " + randomQuote)
