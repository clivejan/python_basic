import re

no_newline_regex = re.compile('.*')
print(no_newline_regex.search('Serve the public trust.\nProtect the innocent.'
	'\nUphold the law.').group())

print("==========")

newline_regex = re.compile('.*', re.DOTALL)
print(newline_regex.search('Serve the public trust.\nProtect the innocent.'
	'\nUphold the law.').group())
