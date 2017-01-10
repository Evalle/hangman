#!/usr/bin/env python3

import random
import sys

words = ['titanic', 'diehard', 'starwars', 'startrek']

def main():
    
    guesses = 7
    keyword = random.choice(words)
    keyword_on_screen = ''.join(list('-' * len(keyword)))
    guessed_letters = list()

    print(keyword_on_screen)

    while guesses > 0: 
        user_letter = input('=> ')
        
        if user_letter in keyword:
            guessed_letters.append(user_letter)
            keyword_on_screen = list()

            for i in keyword:
                if i not in guessed_letters:
                    i = '-'
                keyword_on_screen.append(i)
            keyword_on_screen = (''.join(keyword_on_screen))
            print(keyword_on_screen)
            
            if keyword_on_screen == keyword:
                print("You won! The word was %s" % keyword)
                sys.exit(0)

        else:
            guesses -= 1

            if guesses == 0:
                print("Sorry, you don't have gueeses anymore")
                print("The word was %s" % keyword)
            else:
                print('Guesses left: %d' % guesses)

main()