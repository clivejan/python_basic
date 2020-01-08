import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]

file_cats = open('/tmp/py_test_dir/cats.txt', 'w')
file_cats.write(pprint.pformat(cats))
file_cats.close()

file_cats = open('/tmp/py_test_dir/cats.txt', 'r')
content = file_cats.read()
file_cats.close()

print(content)
