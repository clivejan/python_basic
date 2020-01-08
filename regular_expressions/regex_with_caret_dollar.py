import re

begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello world!').group())
print(begins_with_hello.search('He said hello.') == None)

ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 40').group())
print(ends_with_number.search('Your number is forty.') == None)

whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('1234567890').group())
print(whole_string_is_num.search('12345xyx67890') == None)
print(whole_string_is_num.search('12 34567890') == None)
