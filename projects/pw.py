#!/usr/bin/env python3
# pw.py Am insecure password locker program.

import sys, pyperclip

PASSWORD = {'email': 'emailpassword',
			'blog': 'blogpassword',
			'luggage': '12345'}


if len(sys.argv) < 2:
	print("Usage: python3 pw.py [accounnt] - copy account passowrd")
	sys.exit()

# First command line arg is the account name
account = sys.argv[1]
if account in PASSWORD.keys():
	pyperclip.copy(PASSWORD[account])
	print(f"Password for {account} copied to clipboard.")
else:
	print(f"There is no account named {account}.")

