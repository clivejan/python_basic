while True:
	age = input("Enter your age: ")
	if age.isdecimal():
		break
	print("Please enter a number for your age.")

while True:
	password = input("Enter your password (letters and numbers only): ")
	if password.isalnum():
		break
	print("Passwords can olny have letters and numbers.")
