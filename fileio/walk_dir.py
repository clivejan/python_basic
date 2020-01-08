import os

for dirname, sub_dirnames, filenames in \
	os.walk('/private/tmp/py_test_dir/Python'):

	print(f'The current folder is {dirname}')

	for sub_dirname in sub_dirnames:
		print(f"Sub-directory of {dirname}: {sub_dirname}")

	for filename in filenames:
		print(f"File inside {dirname}: {filename}")

	print()
