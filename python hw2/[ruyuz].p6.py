import math

t_dime = input('Enter a point: ')
list_point = []
while t_dime:
	dime_list = t_dime.split(',')
	x, y = int(dime_list[0]), int(dime_list[1])
	dist = math.sqrt(x ** 2 + y ** 2)
	if int(dist) == dist:
 		dist = int(dist)
	list_point.append([dist, x, y])
	t_dime = input('Enter a point: ')

list_point.sort()
path = input('Enter a destination file path: ')
fg = open(path, 'w')

for i in range(0, len(list_point)):
	fg.write('('+str(list_point[i][1])+','+str(list_point[i][2])+'): '+str(list_point[i][0])+'\n')

fg.close()
