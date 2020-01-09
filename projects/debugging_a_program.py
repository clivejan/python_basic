import random

guess = ''
while guess not in ('heads', 'tails'):
	guess = input('Guessthe coin toss! Enter heads or tails: ')

toss = random.randint(0, 1)

if toss == guess:
	print('You got it!')
else:
	print('Nopt! Guess again!')
	guesss = input()
	if toss == guess:
		print('You got it!')
	else:
		print('Nopt! You are really bad at this game.')
