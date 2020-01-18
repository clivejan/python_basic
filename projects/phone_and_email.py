#!/usr/bin/env python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard

import re, pyperclip

# Create phome number regex
phone_regex = (r'''
	(\d{3}|\(\d{3}\))?				# area code
	(\s|-|\.)?						# separator
	(\d{3})							# first 3 digits
	(\s|-|\.)?						# separator
	(\d{4})							# last 4 digits
	(\s*(ext|x|.ext)\s*(\d{2,5}))?	# extension
	''', re.VERBOSE)
