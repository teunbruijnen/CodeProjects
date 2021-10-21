import random, tweepy, logging, datetime, time
from functools import reduce

today = datetime.datetime.now()

logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d.%m.%Y %H:%M:%S', filename="budgetBot.log", level=logging.INFO, filemode='w')#enable logging!

with open('keysbot.txt','r') as keys:
    keys_dict = eval(keys.read())

auth = tweepy.OAuthHandler(keys_dict["api key"],keys_dict["api key secret"])#text file contained the info in a dictionary, so convenient :)
auth.set_access_token(keys_dict["access token"],keys_dict["access token secret"])
api = tweepy.API(auth)#calls tweety to initiate the API

try:
    api.verify_credentials()#tries to verify
    logging.info("Credentials verified, good to go!")
except:
    logging.info("Error during authentication, check credentials")

user_input = input("What user should we send the budget to? ") #twitter username the bot will DM (without @ !) e.g. TEUNOOM
user = api.get_user(user_input)
logging.info("Succesfully taken input for User: %s" % (user_input))

AverageAday_input = input("What do you want your average budget to be?\n\nPlease note that an average that is lower than 10 could break the program.\n")
AverageAday = int(AverageAday_input)  #my average a day is 10
logging.info("Succesfully taken input for the Average A Day: %s" % (AverageAday))

HighNum = 25
LowNum = 0

DaysOfBudgetting_input = input ("How many days would you like to budget? ") #my budget cycle is 90 days
DaysOfBudgetting = int(DaysOfBudgetting_input)
logging.info("Succesfully taken input for Days of Budgetting: %s" % (DaysOfBudgetting))

StartTime_input = input("At what time do you want to be sent your budget? (HH:MM) ")
logging.info("Succesfully taken input for Starting Time: %s" % (StartTime_input))

StartTimeSplit = StartTime_input.split(':',1)
StartTimeHour = StartTimeSplit[0]
StartTimeMinute = StartTimeSplit[1]

dayOutofBudgetting = 0

def gen_avg_randint(expected_avg=AverageAday, n=DaysOfBudgetting, a=LowNum, b=HighNum):
   while True:
       l = [random.randint(a, b) for i in range(n)]
       avg = reduce(lambda x, y: x + y, l) / len(l)
       if avg == expected_avg:
           logging.info("Succesfully calculated a batch. Amount of zeros in calculated batch: %s\nAmount of 25s: %s" % (sum(i == 0 for i in l), sum(i == 25 for i in l)))
           return l

TheBudget = gen_avg_randint()
logging.info("Succesfully calculated your budget for the coming %s days ! Sleeping until start time now" % (DaysOfBudgetting))

sleep = (datetime.datetime(today.year, today.month, today.day, int(StartTimeHour), int(StartTimeMinute), 0) - today).seconds
print('Waiting for ' + str(datetime.timedelta(seconds=sleep)))
time.sleep(sleep)

# def act(x):
#     return x+10
#
# def wait_start(runTime, action):
#     startTime = time(*(map(int, runTime.split(':'))))
#     while startTime > datetime.today().time(): # you can add here any additional variable to break loop if necessary
#         sleep(60)# you can change 1 sec interval to any other
#     return action
#
print("Here is the starting time I am supposed to wait for: %s" % (StartTime_input))
# wait_start(StartTime_input, lambda: act(100))

while dayOutofBudgetting < DaysOfBudgetting:
    TextToSend = "Hi!\n\nToday is day %s out of %s.\nYour budget for today is \n€ %s,-\n\nHave a nice day!\n\n" % ((dayOutofBudgetting+1), DaysOfBudgetting, TheBudget[dayOutofBudgetting])
    api.send_direct_message(user.id, TextToSend)
    logging.info("Succesfully sent message ! The text was '\n\n%s\n\n'" % (TextToSend))
    dayOutofBudgetting += 1
    sleep(86400)
