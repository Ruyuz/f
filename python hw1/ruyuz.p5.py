sentence = input('Please enter a sentence: ')
list = sentence.split(' ')
dict = {}
for element in list:
	if element not in dict: 
		dict[element] = 1
	else:
		dict[element] = dict[element] + 1
max = 0
for element in dict:
	if dict[element] > max:
		max = dict[element]

for element in dict:
	if dict[element] == max:
		print(element)
		print(max)
