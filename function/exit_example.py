#!/usr/bin/env python3

import sys

while True:
	response = input("Type exit to exit: ")
	if response == 'exit':
		sys.exit()
	print(f'You entered {response}')
