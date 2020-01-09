#!/usr/bin/env python3
# rename_dates.py - Rename filenames with US MM-DD-YYYY date format
# to EU DD-MM-YYYY

import shutil, os, re

# Create a regex that meatches files with the US date format.
date_regex = re.compile(r'''(
	^(.*?)					# all text before the date
	((0|1)?\d)-				# one or two digits for the month
	((0|1|2|3)?\d)-			# one or four digits for the month
	((19|20)\d\d)			# four digits for the year
	(.*?)$					# all text after the date
	)''', re.VERBOSE)

# Loop over the files in the specified directory.
path = '/tmp/py_test_dir'
for filename in os.listdir(path):
	mo = date_regex.search(filename)
	# skip files without a date.
	if mo == None:
		continue
	# Get the different parts of the filename.
	before_part = mo.group(2)
	month_part = mo.group(3)
	day_part = mo.group(5)
	year_part = mo.group(7)
	after_part = mo.group(9)

# Form the EU-style filename
	eu_filename = f"{before_part}{day_part}-{month_part}-{year_part}{after_part}"

# Get file absolute file paths
	us_file = os.path.join(path, filename)
	eu_file = os.path.join(path, eu_filename)
	
# Rename the files
	#print(f"{us_file} > {eu_file}")
	shutil.move(us_file, eu_file)
