#!/usr/bin/env python3

# This program says hello and asks for my name.

print('Hello world!')

my_name = input('What is your name? ')
print('It is a goot time to meet you, ' + my_name)
print('The length of your name is: ' + str(len(my_name)))

my_age = input('What is your age? ')
print(f"You will be {int(my_age) + 1} in a year.")
