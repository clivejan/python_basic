#!/usr/bin/env python3

def spam():
	eggs = 'spam local'
	print(eggs) # print in smap local scope

def bacon():
	eggs = 'bacon local'
	print(eggs)	# print in bacon local scope
	spam()
	print(eggs) # print in bacon local scope

eggs = 'global'
bacon()
print(eggs) # print in global scope
