import os

# Get the current working firectory
print(os.getcwd())

# Change current working firectory
os.chdir('/tmp')
print(os.getcwd())

# List the contents of specfied directory
print(os.listdir('/tmp'))

# Create directory
if not os.path.exists('/tmp/py_test_dir'):
    os.makedirs('/tmp/py_test_dir')

# Get the absolute path from a relative path
print(os.path.abspath('../'))

# Check weather the argument is a absolute path
print(os.path.isabs('/tmp/py_test_dir'))

# Get the relative path from a specified location
print(os.path.relpath('/tmp/py_test_dir', '.'))

# Get the directory path from a full path
print(os.path.dirname('/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'))

# Get the filename from a full path
print(os.path.basename('/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'))

# Get the directory path and filename from a full path at the same time
print(os.path.split('/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'))

# Get the separator paths from a full path
print('/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'.split(os.path.sep))

# Get filesize in bytes
print(os.path.getsize('/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'))

# Check whether a specified directory exist
print(os.path.isdir('/tmp/py_test_dir'))

# Check whether a specified file exist
print(os.path.isfile('/Library/Frameworks/Python.framework/Versions/3.7/bin/python3'))
