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
        for i in range(len(guess)):
            if guess[i] == word[i]:
                session['game']['colors'].append('green')
            elif guess[i] in word:
                session['game']['colors'].append('yellow')
            else:
                session['game']['colors'].append('gray')
        return True
    return False

#Creates a new Worlde
def new_word():
    while (new == word):
        new =  str(random.choice(wordlist))
    word = new

def new_game(session):
    if 'game' in session:
        del session['game']
        return True
    return False



if __name__ == "__main__":
    session = dict()
    session['game']['guesses'] = []
    session['game']['colors'] = []
    session['game']['attempts'] = 0

    if lastday != date.today():
        new_word()
        lastday = date.today()
    
    while True:
        
        while (session['game']['attempts'] < 6):


            inp = input("").lower()
            inp = inp.rsplit()

            if len(inp) == 5 & check(inp):
                session['game']['attempts'] += 1
            else:
                print('Invalid Word')

        if session['game']['attempts'] == 6:
            print ('The word was: {word}. Try again tomorrow!')
