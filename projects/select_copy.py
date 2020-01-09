#!/usr/bin/env python3
# select_copy.py - Copied *.py under the specified dir to another path

import os, shutil

src_path = '/Users/clive/CliveSpace/github/Python'
dst_path = '/tmp/py_test_dir'

for dirname, sub_dirnames, filenames in os.walk(src_path):
	for filename in filenames:
		if filename.endswith('.py'):
			#print(filename)
			shutil.copy(os.path.join(dirname, filename), \
				os.path.join(dst_path, filename))
