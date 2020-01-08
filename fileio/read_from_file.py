hello_file = open('/tmp/py_test_dir/hello.txt', 'r')

# Read the entire content as a single string
hello_content = hello_file.read()
print(hello_content)

# Set the cursor to the beginning of the file
hello_file.seek(0, 0)

# To get a list of string from the file
hello_content = hello_file.readlines()
print(hello_content)
