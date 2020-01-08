import re

ha_regex = re.compile(r'(Ha){3}')

mo1 = ha_regex.search('HaHaHa')
print(mo1.group())

mo2 = ha_regex.search('Ha')
print(mo2 == None)
