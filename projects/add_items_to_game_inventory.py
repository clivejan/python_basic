def add_to_inventory(inv, items):
	for item in items:
		inv.setdefault(item, 0)
		inv[item] += 1
	return inv

def display_inventory(inv):
	total = 0
	print("Inventory:")
	for key, value in inv.items():
		print(f"{value} {key}")
		total += value
	print(f"\nTotal number of items: {total}")

inventory = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

updated_inventory = add_to_inventory(inventory, dragon_loot)

display_inventory(updated_inventory)
