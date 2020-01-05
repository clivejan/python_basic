#!/usr/bin/env python3

def spam():
	global eggs
	eggs = 'spam'	# global

def bacon():
	eggs = 'bacon'	# bacon local

def ham():
	print(eggs)		# global

eggs = 42			# global
spam()				# value will be changed
print(eggs)
