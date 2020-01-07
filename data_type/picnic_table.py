def print_picnic(items_dict, left_width, right_width):
	print(f"PICNIC ITEMS".center(left_width + right_width, '-'))

	for key, value in items_dict.items():
		print(f"{key.ljust(left_width, '.')}{str(value).rjust(right_width)}")

picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)