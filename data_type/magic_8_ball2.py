import random

messages = ['one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine']

print(f"{messages[random.randint(0, len(messages)-1)]}")
