import pprint

message = "I hope I can find a job in Canada before running out my money."

count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] += 1

pprint.pprint(count)
