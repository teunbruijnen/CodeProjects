#! python

import tweepy, itertools, random, time, logging, requests, sys
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

with open('keysbot.txt','r') as keys:
    keys_dict = eval(keys.read())

auth = tweepy.OAuthHandler(keys_dict["api key"],keys_dict["api key secret"])#text file contained the info in a dictionary, so convenient :)
auth.set_access_token(keys_dict["access token"],keys_dict["access token secret"])
api = tweepy.API(auth)#calls tweety to initiate the API

try:
    api.verify_credentials()#tries to verify
    print("Credentials verified, good to go!")
except:
    print("Error during authentication, check credentials")

def getPage(url):
    global PageName, PageLink, TopViews, nation

    if url == Url['Netherlands']:
        nation = 'The Netherlands'
    elif url == Url['France']:
        nation = 'France'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    try:
        driver.get(url)
        print('Browsing the interweb...')
        logging.info("Browsing the interweb...")
        time.sleep(20)#changed from 5 to 20 because of slow connection
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content,"html.parser")
        PopularElement = soup.find(id="topview-entry-1")
        soClose = PopularElement.select_one('.topview-entry--label') #I still don't know enough about tags, elements to efficiently browse html...
        print("Retrieving URL...")
        logging.info("Retrieving URL...")
        PageLink = soClose.findChild('a')['href'] #this is the link of no.1 page!
        PageName = soClose.findChild('a').contents[0] #This is the page name
        TopviewTag = PopularElement.select_one('.topview-entry--views')
        TopViews = TopviewTag.contents[0] #this is the amount of views!
        print("Succesfully retrieved all info!")
        logging.info("Succesfully retrieved all info!")
        driver.quit()
    except:
        print("Could not go to webpage :(")
        logging.info("Could not go to webpage :(")
        driver.quit()
        sys.exit()


def WikiMessage():
    print("Crafting message of today...")
    logging.info("Crafting message of today...")
    startList = ["hi", "hello", "hey", "helloo", "hellooo", "gmorning", "good morning", "morning", "good day", "good afternoon", "good evening", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how has life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what is good", "what's good", "what is happening", "what's happening", "what is new", "what's new", "whatsup", "g’day", "howdy", "salut", "bonjour", "hola", "nǐ hǎo", "namaste", "marhabaan", "alô", "hyālō", "privet", "kon’nichiwa", "nggoleki", "ciao", "Allianchu"]
    endList = ["Buena suerte", "Bonne chance", "Viel Glück", "In bocca al lupo", "Boa sorte", "Lykke til", "udachi", "Veel succes", "Bon courage", "Good luck!", "Break a leg!", "Knock ‘em dead!", "Blow them away!", "Best of luck!", "You’ll do great!","Fingers crossed!"]

    message = "%s!\n\nYesterday's most popular wikipedia page in %s was about '%s'. \n\nHere's the link: %s. \nIt had %s views yesterday :o \n\n%s" % (random.choice(startList).capitalize(), nation, PageName, PageLink, TopViews, random.choice(endList))
    user = api.get_user("TEUNOOM")#Send to user "TEUNOOM"
    try:
        api.send_direct_message(user.id, message)
        print("Succesfully sent:\n '%s'" % message)
        logging.info("Succesfully sent:\n '%s'" % message)
    except:
        print("Could not send message :(")
        logging.info("Could not send message :(")

Url = {
    'France': 'https://pageviews.toolforge.org/topviews/?project=fr.wikipedia.org&platform=all-access&date=yesterday&excludes=',
    'Netherlands': 'https://pageviews.toolforge.org/topviews/?project=nl.wikipedia.org&platform=all-access&date=yesterday&excludes='
}

getPage(Url['Netherlands'])
WikiMessage()
getPage(Url['France'])
WikiMessage()
