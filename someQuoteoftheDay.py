#!/usr/local/bin/python3.5
#This module grabs a some daily quote and uploads it to twitter
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

print("Looking up quotes...") #Loading text

quotePage = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
quotePage.raise_for_status()
quotePageSoup = bs4.BeautifulSoup(quotePage.text, "html.parser")
AllQuotes = quotePageSoup.find_all('div', class_='bqcpx')

randomQuote = AllQuotes[randint(0,5)].getText()
printFrom = int(randomQuote.index("Day") + 5) #I want to edit the output so I can add some hashtags(twitter only allows 140 characters per tweet).
randomQuote = randomQuote[printFrom:]

ExistingTweets = api.get_home_timeline(count = 9)
#Here we check if the quote hasn't been tweeted already.
while True:
    already_tweeted = False
    for tweets in ExistingTweets:
        if randomQuote[:15] == tweets['text'][:15]:
            already_tweeted = True
            break
    if already_tweeted:
        randomQuote = AllQuotes[randint(0,5)].getText()
        printFrom = int(randomQuote.index("Day") + 5)
        randomQuote = randomQuote[printFrom:]
    else:
        break

LonghashTags= ['#inspiration', '#motivation', '#getmotivated', '#dailyquote', '#brainyquote']
ShorthashTags = ['#quote', '#dailyquote', '#quotes', '#python', '#learn']

if len(randomQuote) > 110:
    hashTags = ShorthashTags
elif len(randomQuote) < 110:
    hashTags = LonghashTags
#have to make sure not to duplicate any tags!(Not sure if this works yet..)
Tag1 = hashTags[randint(0,4)]
Tag2 = hashTags[randint(0,4)]
while True:
    same_tag = False
    if Tag1 == Tag2:
        same_tag = True
        break
    if same_tag:
        Tag2 = hashTags[randint(0,4)]
    else:
        break

tweetThis = randomQuote  + "%s %s" % (Tag1, Tag2)
if len(tweetThis) > 140:
    tweetThis = randomQuote #I want to add the option of having only one hashtag if it is possible in stead of removing BOTH of them.
#api.update_status(status=tweetThis)

print("Tweeted: " + tweetThis)
