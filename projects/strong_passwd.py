#!/usr/bin/env python3
# string_passwd.py - varify password has 1 digit, 1 upper, 1 lower,
# and at least 8 characters

import re

upper_regex = re.compile(r'[A-Z]+')
lower_regex = re.compile(r'[a-z]+')
digit_regex = re.compile(r'\d+')

while True:
    passwd = input('Enter a password: ')

    if len(passwd) < 8:
        print('The password must have at least 8 characters.')
    elif upper_regex.search(passwd) == None:
        print('The password must have at least 1 upper case.')
    elif lower_regex.search(passwd) == None:
        print('The password must have at least 1 lower case.')
    elif digit_regex.search(passwd) == None:
        print('The password must have at least 1 digit.')
    else:
        print('Password accepted')
        break
