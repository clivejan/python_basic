#/usr/bin/env python3
"""
multi_clipboard.pyw - Saves and loads pieces of text to the clipboard.
Usage: 
	multi_clipboard.pyw save <keyword> - Saves clipborad to keyword.
	multi_clipboard.pyw list <keyword> - Loads all keywords to clopboard.
	multi_clipboard.pyw <keyword> - Loads keyword to clipboard.
"""

import sys, pyperclip, shelve

mcb_shelve = shelve.open('/tmp/py_test_dir/mcb')

# Save clopboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcb_shelve[sys,argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
# TODO: List leywords and load content

mcb_shelve.close()
