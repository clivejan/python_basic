#!/sur/bin/env python3

while True:
	name = input('Please input your username: ')
	if name != 'Clive':
		continue
	
	password = input(f'Hello, {name}. What is your password: ')
	if password == 'swordfish':
		break

print('Access granted')
