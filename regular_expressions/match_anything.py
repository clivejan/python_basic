import re

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')

mo = name_regex.search('First Name: Tzuyu Last Name: Chou')
print(mo.group(1))
print(mo.group(2))
