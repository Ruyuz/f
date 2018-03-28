pos = 0
num_list = []
num_new = input('Please enter an intrger: ')
while num_new:
	num_list.append([int(num_new), pos])
	pos = pos + 1
	num_new = input('Please enter an integer: ')

num_list.sort()
for i in range(0,pos):
	print(num_list[i][0], end = ' (')
	print(num_list[i][1], end = ')\n')
