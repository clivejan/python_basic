#!/usr/bin/env python3
# bullet_point_adder.py - Adds Wikipedoa bullet points to the start
# of each lin of text on the clipboard

import pyperclip

text = pyperclip.paste

#Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):
	lines[i] = '* ' + lines[i]

text = '\n'.join(lines)

pyperclip.paste()
