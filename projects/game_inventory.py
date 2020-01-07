def display_inventory(inv):
	total = 0
	print("Inventory:")

	for key, value in inv.items():
		total += value
		print(f"{value} {key}")
	print(f"\nTotal number pf items: {total}")

inventory = {'rope': 1,
             'torch': 6,
             'gold coin': 42,
             'dagger': 1,
             'arrow': 12}

display_inventory(inventory)
