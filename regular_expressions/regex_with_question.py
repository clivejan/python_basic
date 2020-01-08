import re

bat_regex = re.compile(r'Bat(wo)?man')

mo1 = bat_regex.search('The adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The adventures of Batwoman')
print(mo2.group())
