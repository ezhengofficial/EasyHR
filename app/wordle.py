from guesslist import guesslist
from wordlist import wordlist 
import random
from datetime import date

lastday = ''
word = ''

#Checks User Guesses
def check(guess): 
    if guess in guesslist:
        pass
    else:
        return ("Not a word")

#Creates a new Worlde
def new_word():
    while (new == word):
        new =  str(random.choice(wordlist))
    word = new

#Play
def play():
    today = date.today()
    if lastday != today:
        new_word()
        attempt = 0
        lastday = today
    
    while (attempt < 6):
        pass

