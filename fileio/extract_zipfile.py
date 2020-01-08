import zipfile, os

os.chdir('/private/tmp/py_test_dir')

python_zip = zipfile.ZipFile('Python_basic-master.zip')

# Extract a single file
python_zip.extract('Python_basic-master/README.md', 
	'/private/tmp/py_test_dir')

# Extract entire zip archive into current directory
python_zip.extractall()

# Extract entire zip archive into specified directory
python_zip.extractall('/private/tmp/py_test_dir/Python')

python_zip.close()
