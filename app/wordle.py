from guesslist import guesslist
from wordlist import wordlist 
import random
from datetime import date
from matchhistory import *

lastday = ''
word = 'hello'

#Checks User Guesses
def check(guess): 
    global word
    if len(guess) == 5:
        if guess == word:
            print('You Win!')
            record()
            return True
        elif guess in guesslist:
            session['game']['guesses'].append(guess)
            session['game']['colors'].append([])
            l = len(session['game']['colors']) - 1
            for i in range(len(guess)):
                if guess[i] == word[i]:
                    session['game']['colors'][l].append(0)
                elif guess[i] in word:
                    session['game']['colors'][l].append(1)
                else:
                    session['game']['colors'][l].append(2)
            return True
        else:
            print('Not a Word')
    else:
        print('Word must be 5 letters long')
        
    return False

#Creates a new Wordle
def new_word():
    new =  str(random.choice(wordlist))
    return new

#New Game
def new_game(session):
    if 'game' in session:
        del session['game']

    session['game'] = dict()
    session['game']['guesses'] = []
    session['game']['colors'] = []
        
if __name__ == "__main__":    
    if lastday != date.today():
        new_word()
        new_game(session)
        lastday = date.today()
    
    if 'game' not in session:
        new_game(session)

    while True:
        for i in range (len(session['game']['guesses'])):
            print(session['game']['guesses'][i])
            print(session['game']['colors'[i]])

        while (len(session['game']['guesses']) < 6):
            inp = input("").lower()
            inp = inp.rsplit()

            if len(inp) == 5 & check(inp):
                session['game']['attempts'] += 1
            elif len(inp) != 5:
                print('Word must be 5 letters long')
            else:
                print('Not a Word')

        if session['game']['attempts'] == 6:
            record()
            print ('The word was: {word}. Try again tomorrow!')
