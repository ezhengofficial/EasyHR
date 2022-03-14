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
        session['game']['guesses'].append(guess)
        session['game']['colors'].append([])
        l = len(session['game']['colors']) - 1
        for i in range(len(guess)):
            if guess[i] == word[i]:
                session['game']['colors'][l].append('green')
            elif guess[i] in word:
                session['game']['colors'][l].append('yellow')
            else:
                session['game']['colors'][l].append('gray')
        return True
    return False

#Creates a new Worlde
def new_word():
    new =  str(random.choice(wordlist))
    global word
    while (new == word):
        new =  str(random.choice(wordlist))
    word = new

def new_game(session):
    if 'game' in session:
        del session['game']

    session = dict()
    session['game']['guesses'] = []
    session['game']['colors'] = []
    session['game']['attempts'] = 0
        
if __name__ == "__main__":    
    if lastday != date.today():
        new_word()
        new_game()
        lastday = date.today()
    
    if 'game' not in session:
        new_game()

    while True:
        for i in range (len(session['game']['guesses'])):
            print(session['game']['guesses'][i])
            print(session['game']['colors'[i]])

        while (session['game']['attempts'] < 6):
            inp = input("").lower()
            inp = inp.rsplit()

            if len(inp) == 5 & check(inp):
                session['game']['attempts'] += 1
            else:
                print('Invalid Word')

        if session['game']['attempts'] == 6:
            print ('The word was: {word}. Try again tomorrow!')
