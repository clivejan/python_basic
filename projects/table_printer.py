def print_table(table):
	# Get the max length for each cloume
	length = []
	for items in table:
		leng = 0
		for item in items:
		    if len(item) > leng:
		        leng = len(item)
		length.append(leng+2)

	# turn 90 degree and print with rjust
	for x in range(len(table[0])):
		for y in range(len(table)):
			print(f"{table[y][x].rjust(length[y])}", end="")
		print()

table_date = [['apples', 'oranges', 'cherries', 'banana'],
			  ['Alice', 'Bob', 'Carol', 'David'],
			  ['dogs', 'cats', 'moose', 'goose']]

print_table(table_date)
