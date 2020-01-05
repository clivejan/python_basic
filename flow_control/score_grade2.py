#!/usr/bin/env python3

score = int(input("What is your score: "))

if score >= 90:
	print('You got an A')
# Swap the order of the following two statements
elif score >= 70:
	print('You got a C')
elif score >= 80:
	print('You got a B')
else:
	print('Oops! You failed.')
