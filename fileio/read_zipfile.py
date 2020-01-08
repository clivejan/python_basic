import zipfile

python_zip = zipfile.ZipFile('/private/tmp/py_test_dir/Python_basic-master.zip')

# List the content of the zipfile
print(python_zip.namelist())

# Read the original file size in the zipfile
readme_info = python_zip.getinfo('Python_basic-master/README.md')
print(readme_info.file_size)
# Read the compressed file size in the zipfile
print(readme_info.compress_size)

python_zip.close()
