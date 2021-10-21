from pathlib import Path
from rich import print
from rich.progress import track
from time import sleep
import random as rd
import os

os.system('cls')
dictionaryFile = open(Path.cwd() / Path('liste_francais.txt'))
listofDictionary = dictionaryFile.readlines()
totalLines = len(listofDictionary)
#ShouldContainLetter = ''

# randomWord = listofDictionary[rd.randrange(totalLines)]
print("[bold green]Hello!\nThis program can generate a random word from a French dictionary.\nThe generated word will contain the letter of your choosing.\n")
def ChooseLetter():
    global ShouldContainLetter
    while True:
        print("Enter letter: ")
        ShouldContainLetter = input()
        ShouldContainLetter = ShouldContainLetter.lower()
        if ShouldContainLetter not in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','à','â','ç','æ','é','è','ê','ë','ï','î','ô','œ','ù','û','ü','ÿ']:
            print('\rPlease only use supported letters.')
            continue
        break

def GenerateWord():
    os.system('cls')
    for step in track(range(100), description="Thinking really hard..."):
        sleep(0.001)
        randomWord = listofDictionary[rd.randrange(totalLines)]
        while ShouldContainLetter not in randomWord:
            randomWord = listofDictionary[rd.randrange(totalLines)]
    print('Found a [bold green]GREAT[/bold green] word! How about this: [bold red]%s[/bold red]\nDo you like it?' % (randomWord))

ChooseLetter()
GenerateWord()

while True:
    print("Type y to accept or n to generate a new word.\nChoose c to change letter!")
    answer = input()
    if answer not in {'y', 'n','c'}:
        print("[bold yellow]Come on, it's not hard: y, n or c?[/bold yellow]")
        continue
    if answer == 'y':
        os.system('cls')
        print('[bold blue]Good luck!')
        break
    if answer == 'n':
        os.system('cls')
        for step in track(range(100), description="Thinking really hard..."):
            sleep(0.001)
        randomWord = listofDictionary[rd.randrange(totalLines)]
        while ShouldContainLetter not in randomWord:
            randomWord = listofDictionary[rd.randrange(totalLines)]
        print('New word: [bold red]%s[/bold red]' %(randomWord))
        continue
    if answer == 'c':
        ChooseLetter()
        GenerateWord()
        continue
    break
