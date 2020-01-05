#/usr/bin/env python3

def spam():
	global eggs
	eggs = 'spam'

eggs = 'global'
spam()			# eggs will be modified in spam()
print(eggs)
