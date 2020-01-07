#!/usr/bin/env python3
# pw.py Am insecure password locker program.

import sys

PASSWORD = {'email': 'emailpassword',
			'blog': 'blogpassword',
			'luggage': '12345'}


if len(sys.argv) < 2:
	print("Usage: python3 pw.py [accounnt] - copy account passowrd")
	sys.exit()

account = sys.argv[1]
