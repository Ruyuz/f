my_string = input('Please enter some words: ')
my_split = my_string.split(' ')
for element in my_split:
	if element[0] == 's':
		continue
	print (element)
