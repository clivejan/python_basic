import re

bat_regex = re.compile(r'Bat(wo)+man')

mo1 = bat_regex.search('The adventures of Batman')
print(mo1 == None)

mo2 = bat_regex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = bat_regex.search('The adventures of Batwowowowoman')
print(mo3.group())
