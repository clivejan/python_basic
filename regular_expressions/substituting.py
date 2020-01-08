import re

names_regex = re.compile(r'Agent \w+')

print(names_regex.sub('CENSORED', 'Agent Alice gave the secert documennts to Agent Bob.'))
