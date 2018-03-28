str_list = []
str_new = input('Please enter a string: ').lower()
while str_new:
	str_list.append(str_new)
	str_new = input('Please enter a string: ').lower()
str_list.sort()
print('You entered:')
print(', '.join(str_list))
