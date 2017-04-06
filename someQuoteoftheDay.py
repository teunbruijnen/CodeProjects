#!/usr/local/bin/python3.5
#This grabs a random daily quote(out of 5 options) and uploads it to twitter
#BE AWARE this was written to run on raspberry pi specifically

apiSecret = 'VERY SECRET'
accessToken = 'ALSO SECRET'
accessTokenSecret = 'EVEN MORE SECRET'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

print("Looking up quotes...") #Loading text

quotePage = requests.get('https://www.brainyquote.com/quotes_of_the_day.html')
quotePage.raise_for_status()
quotePageSoup = bs4.BeautifulSoup(quotePage.text, "html.parser")

AllQuotes = quotePageSoup.find_all('div', class_='bqcpx')
#print(AllQuotes)
randomQuote = AllQuotes[randint(0,5)].getText()

print(randomQuote)

api.update_status(status=tweetThis)

print("Tweeted: " + randomQuote)
