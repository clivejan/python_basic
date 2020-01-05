#!/usr/bin/env python3

import random

def get_answer(answer_number):
	if answer_number == 1:
		return "one"
	elif answer_number == 2:
		return "two"
	elif answer_number == 3:
		return "three"
	elif answer_number == 4:
		return "four"
	elif answer_number == 5:
		return "five"
	elif answer_number == 6:
		return "six"
	elif answer_number == 7:
		return "seven"
	elif answer_number == 8:
		return "eight"
	elif answer_number == 9:
		return "nine"

r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)
