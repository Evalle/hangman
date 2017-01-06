#!/usr/bin/env python3

import random

words = ['titanic']  # , 'diehard', 'starwars', 'startrek']

def main():
	
	guesses = 2
	keyword = random.choice(words)
	while guesses > 0:
		keyword_splitted = list(keyword)
		keyword_on_screen = ''.join(list('-' * len(keyword)))
		print(keyword_on_screen)

		user_letter = input('>>> ')
		
		if user_letter in keyword:
			keyword_on_screen = list()
			for i in keyword_splitted:
				if i != user_letter:
					i = '-'
				keyword_on_screen.append(i)
		else:
			guesses -= 1
		print('Guesses left: %d' % guesses)

main()