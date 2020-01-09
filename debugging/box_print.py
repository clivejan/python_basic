# raise statement commonly insode a function
def box_print(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Sumbol must be a single character string.')

	if width <= 2:
		raise Exception('Width must be grater than 2.')

	if height <= 2:
		raise Exception('height must be grater than 2.')

	print(symbol * width)
	for i in range(height-2):
		print(f"{symbol}{' '*(width-2)}{symbol}")
	print(symbol * width)

# try and except statement in the code calling the function
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
	try:
		box_print(sym, w, h)
	except Exception as err:
		print(f"An exception happened: {err}")
