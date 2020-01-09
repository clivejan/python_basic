import traceback

try:
	raise Exception('This is error message.')
except:
	error_file = open('/tmp/python_error.log', 'a')
	error_file.write(traceback.format_exc())
	error_file.close()

	print("The traceback info was written to /tmp/python_error.log")
