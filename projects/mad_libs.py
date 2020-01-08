#!/usr/bin/env python3
# mad_libs.py - Modified specified keyword in a file

file_src = '/tmp/py_test_dir/mad_libs.txt'
file_dst = '/tmp/py_test_dir/mad_libs_new.txt'

# Read in original text from src file 
file_src_obj = open(file_src, 'r')
text = file_src_obj.read()
file_src_obj.close()

# Find the keywords and prompt user to modify it
text_list = text.split()

for i in range(len(text_list)):
	if text_list[i] == 'ADJECTIVE':
		text_list[i] = input("Enter a adjective: ")
	elif text_list[i] == 'NOUN':
		text_list[i] = input("Enter a noun: ")
	elif text_list[i] == 'VERB.':
		text_list[i] = input("Enter a verb: ")

final_str = ' '.join(text_list)

# Write the modified context to a new file
file_dst_obj = open(file_dst, 'w')
file_dst_obj.write(f"{final_str}\n")
file_dst_obj.close
