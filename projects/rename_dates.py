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

# TODO: Loop over the files in the specified directory.

# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the EU-style filename

# TODO Rename the files
