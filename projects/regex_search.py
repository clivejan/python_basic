#!/usr/bin/env python3
# regex_search.py <regex> - search *.txt baesd on user specified regex

import re, sys, os

user_regex = re.compile(sys.argv[1])

file_list = os.listdir('/tmp/py_test_dir')

hit = []
for filename in file_list:
	if filename.endswith('txt'):
		file = os.path.join('/tmp/py_test_dir', filename)
		file_obj = open(file, 'r')
		context = file_obj.read()
		file_obj.close()
		hit = hit + user_regex.findall(context)

for item in hit:
	print(item, end=" ")
print()
