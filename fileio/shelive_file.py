import shelve

cats = ['Zophie', 'Pooka', 'Simon']
program = ['C', 'Java', 'Python']

# Write content to shevle file
shelve_file = shelve.open('/tmp/py_test_dir/my_data')
shelve_file['cats'] = cats
shelve_file['program'] = program
shelve_file.close()

# Read content from shelve file
shelve_file = shelve.open('/tmp/py_test_dir/my_data')
for key in shelve_file.keys():
	print(shelve_file[key])
shelve_file.close()
