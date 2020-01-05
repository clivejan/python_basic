def spam():
	# pythin assume eggs is a global variable
	print(eggs)
	# conflict with a local variable when usging the assignment
	eggs = 'spam local'

eggs = 'global'
spam()
