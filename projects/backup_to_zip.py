#!/usr/bin/env python3
# backup_to_zip.py - Copies an entire folder and its contens into
# a ZIP file whose filename increments.

import zipfile, os

# Backup the entire content of "folder" into a ZIP file
def backup_to_zip(folder):
	folder = os.path.abspath(folder)

	# Figure out the filename this code should use based on 
	# what files already exists.
	number = 1
	while True:
		zip_filename = f"/tmp/{os.path.basename(folder)}_{number}.zip"
		if not os.path.exists(zip_filename):
			break
		number += 1

	# Create the ZIP file
	print(f"Creating {zip_filename}...")
	backup_zip = zipfile.ZipFile(zip_filename, 'w')

	# TODO: Walk the entire folder tree and compress the file in each folder.


	backup_zip.close()
	print('Done.')

backup_to_zip('/Users/clive/CliveSpace/github/Python')
