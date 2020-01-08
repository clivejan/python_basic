#!/usr/bin/env python3
# strip_with_regex.py - remove whitespace at begins and ends
# strip_with_regex.py [char] - remove [char] at begins and ends  

import re, sys

if len(sys.argv) > 1:
	pattern = sys.argv[1]
else:
	pattern = ' '

strip_regex = re.compile(f"^({pattern})*(.*?)({pattern})*$")

print("##" + strip_regex.sub(r'\2', ' TWICE ') + "##")
print("##" + strip_regex.sub(r'\2', '=TWICE=') + "##")
