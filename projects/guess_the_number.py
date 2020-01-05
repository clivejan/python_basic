# This is a guess the number game

import random

secret_number = random.randint(1, 20)

# Ask the player to guess 6 times
print('Guess the secret number between 1 and 20 in six tries.')
for guess_taken in range(1, 7):
	guess = int(input("Take a guess: "))
	if guess < secret_number:
		print('Your guess is too low.')
	elif guess > secret_number:
		print('Your guess is too high.')
	else:
		break # the corrent guess

if guess == secret_number:
	print(f"Good job! You guessed th number in {guess_taken} guesses.")
else:
	print(f'Nope. The secret number is {secret_number}')
