#!/usr/bin/env python3

score = int(input("What is your score: "))

if score >= 90:
	print('You got an A')
elif score >= 80:
	print('You got a B')
elif score >= 70:
	print('You got a C')
else:
	print('Oops! You failed.')
