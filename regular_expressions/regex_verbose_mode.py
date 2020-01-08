import re

phone_regex = re.compile(r'''
	(\d{3}|\(\d{3}\))?				# area code
	(\s|-|\.)?						# separator
	\d{3}							# first 3 digits
	(\s|-|\.)?						# separator
	\d{4}							# last 4 digits
	(\s*(ext|x|ext.)\s*\d{2,5})?	# extension
	''', re.VERBOSE)

print(phone_regex.search('555-9999').group())
print(phone_regex.search('(415) 555-9999').group())
print(phone_regex.search('415.555.9999  ext.  1234').group())
