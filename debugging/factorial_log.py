#!/usr/bin/env python3

import logging

# Disable logging
#logging.disable(logging.CRITICAL)

logging.basicConfig(level=logging.DEBUG, filename='/tmp/python_error.log' ,\
	format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

def factorial(n):
	logging.debug(f'Start of factorial({n})')

	total = 1
	for i in range(1, n+1):
		total *= i
		logging.debug(f'i is {i}, total is {total}')

	logging.debug(f'End of factorial({n})')
	return total

print(factorial(5))
logging.debug(f'End of program.')
