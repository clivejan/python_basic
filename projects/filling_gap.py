#!/usr/bin/env pytjon3
# filling_gap.py - make spam001.txt spam003.txt getting close gap

import os, shutil, re

finename_regex = re.compile(r'(^spam)(\d){3}(\.txt$)')

path = '/tmp/py_test_dir'

filenames = os.listdir(path)

# Find the file matches the specific pattern
hitnames = []
for filename in filenames:
	if finename_regex.search(filename):
		hitnames.append(filename)

# Rename file to close gap
file_num = len(hitnames)
hitnames.sort()

for i in range(file_num):
	if hitnames[i] == f"spam{i+1:03}.txt":
		continue
	old_file = os.path.join(path, hitnames[i])
	new_file = os.path.join(path, f"spam{i+1:03}.txt")
	#print(f"{old_file} > {new_file}")
	shutil.move(old_file, new_file)
