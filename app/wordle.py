from guesslist import guesslist
from wordlist import wordlist 
import random
from datetime import date
from login import *

lastday = ''
word = ''

#Checks User Guesses
def check(guess): 
    if guess in guesslist:
        result = []
        for i in range(len(guess)):
            if guess[i] == word[i]:
                result.append('green')
            elif guess[i] in word:
                result.append('yellow')
            else:
                result.append('gray')
        return result
    else:
        return ("Not a valid word")

#Creates a new Worlde
def new_word():
    while (new == word):
        new =  str(random.choice(wordlist))
    word = new

#Play
def play():
    if lastday != date.today():
        new_word()
        attempt = 0
        lastday = date.today()
    
    while (attempt < 6):
        pass

    if attempt == 6:
        return ('The word was: {word}. Try again tomorrow!')

