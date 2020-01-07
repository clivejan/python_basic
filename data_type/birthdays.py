birthdays = {'Clive': 'Aug 12', 'Carrie': 'Jul 13', 'Tzuyu': 'Jun 14'}

while True:
	name = input('Enter a name (blank to exit): ')
	if name == '':
		break

	if name in birthdays:
		print(f"{birthdays[name]} is the birthday of {name}.")
	else:
		print(f'I do not have birthday information for {name}.')
		bday = input(f'What is {name}\'s birthday: ')
		birthdays[name] = bday
		print('Birthday database updated.')
