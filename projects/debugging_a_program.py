#!/usr/bin/env python3

import random, logging

logging.basicConfig(level=logging.DEBUG, filename='/tmp/python_error.log',\
	format=' %(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
	guess = input('Guessthe coin toss! Enter heads or tails: ')

toss = ['heads', 'tails']
random.shuffle(toss)
logging.debug(f"toss_list: {toss}")

logging.debug(f'toss: {toss[0]}, guess: {guess}')

if toss[0] == guess:
	print('You got it!')
else:
	guess = input('Nopt! Guess again! ')
	logging.debug(f'toss: {toss[0]}, guess: {guess}')

	if toss[0] == guess:
		print('You got it!')
	else:
		print('Nopt! You are really bad at this game.')
