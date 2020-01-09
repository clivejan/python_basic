#!/usr/bin/env python3
# large_file.py - Find and print files which larger than 1MB

import os

path = '/Users/clive/CliveSpace'

for dirname, sub_dirnames, filenames in os.walk(path):
	for filename in filenames:
		if os.path.getsize(os.path.join(dirname, filename)) > 1024000:
			print(os.path.join(dirname, filename))
