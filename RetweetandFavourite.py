#!/usr/local/bin/python3.5
#This module grabs the weather in Paris
#BE AWARE: This script was written to run on a raspberry pi specifically
from twython import TwythonStreamer, Twython, TwythonError

#Create a .txt file in the directory of your script with your API keys.
keys = {}
with open("API_keys.txt") as f:
    for line in f:
       (key, val) = line.split()
       keys[int(key)] = val

api = Twython(keys[1],keys[2],keys[3],keys[4])

search_results = api.search(q="#bottest2017", count=100)
try:
    for tweet in search_results["statuses"]:
        api.retweet(id = tweet["id_str"])
        api.create_favorite(id =tweet["id_str"])
        print("I favourited and retweeted a couple of tweets!")
except TwythonError as e:
    print(e)
