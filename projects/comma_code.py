# Covert a list to a string that insert a space and a comma in each item
# and a "and" before last item

def commma_code(list_arg):
	final_str = list_arg[0]
	for i in range(1, len(list_arg)):
		if i != len(list_arg) - 1:
			final_str = f"{final_str}, {list_arg[i]}"
		else:
			final_str = f"{final_str}, and {list_arg[i]}"
	return final_str

list_ori = ['apples', 'banana', 'tofu', 'cats']
print(commma_code(list_ori))
