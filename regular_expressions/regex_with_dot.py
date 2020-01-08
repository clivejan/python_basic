import re

at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))
