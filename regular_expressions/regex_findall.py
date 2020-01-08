import re

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
# search() only return the first occurrence
mo = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

# findall() will return a list containing all matches.
# if there is no group, findall will retrun a list
# if there has group, findall will retrun a list of tuple
print(phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
