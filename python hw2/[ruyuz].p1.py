path_1 = input('Please enter file path 1: ')
path_2 = input('Please enter file path 2: ')
fg1 = open(path_1)
fg2 = open(path_2)
list1 = fg1.readlines()
list2 = fg2.readlines()
length1 = len(list1)
length2 = len(list2)
min1 = min(length1, length2)
max1 = max(length1, length2)
list_linenum = []
for i in range(0,min1):
	if list1[i].strip('\n') != list2[i].strip('\n'):
		list_linenum.append(str(i))
for j in range(min1,max1):
	list_linenum.append(str(j))
print(', '.join(list_linenum))
fg1.close()
fg2.close()
