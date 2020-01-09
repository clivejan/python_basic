import zipfile

new_zip = zipfile.ZipFile('/tmp/new.zip', 'w')

# Add file to zip archive
new_zip.write('/Users/clive/CliveSpace/github/Python/README.md',\
	compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()
