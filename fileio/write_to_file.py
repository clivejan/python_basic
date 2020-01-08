# AOverwrite a file (create it if does not esist)
bacon_file = open('/tmp/py_test_dir/bacon.txt', 'w')
bacon_file.write('Hello world!\n')
bacon_file.close()

# Append content to a file (create it if does not esist)
bacon_file = open('/tmp/py_test_dir/bacon.txt', 'a')
bacon_file.write('Bacon is not vegetable.\n')
bacon_file.close()

# Read file content
bacon_file = open('/tmp/py_test_dir/bacon.txt', 'r')
bacon_content = bacon_file.read()
bacon_file.close()
print(bacon_content)
