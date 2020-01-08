import re

non_greedy_regex = re.compile(r'<.*?>')
print(non_greedy_regex.search('<To servve man> for dinner.>').group())

greedy_regex = re.compile(r'<.*>')
print(greedy_regex.search('<To servve man> for dinner.>').group())
