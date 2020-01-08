import re

names_regex = re.compile(r'Agent (\w)\w+')

print(names_regex.sub(r'Agent \1****', 
	'Agent Alice gave the secert documennts to Agent Bob.'))
