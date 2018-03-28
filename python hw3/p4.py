import math

def distance( xlist, ylist ):
	sum = 0
	for i in range(0,len(xlist)):
		sum = sum + (int(xlist[i]) - int(ylist[i]))** 2 
	return math.sqrt(sum)

out_list = []
new_point = input('Enter a point: ')
while new_point:
	point_list = new_point.split(',')
	orig_list = [0] * len(point_list)
	dist = distance (point_list, orig_list)
	dimen_list = [ dist ]
	for i in point_list:
		dimen_list.append(int(i))
	out_list.append(dimen_list)
	new_point = input('Enter a point: ')
out_list.sort()


des_path = input('Enter a destination file path: ')
fg = open (des_path, 'w')
for i in range(0, len(out_list)):
	fg.write('(')
	for j in range(1, len(point_list)):
		fg.write( str(out_list[i][j]) + ', ' )
	fg.write(str(out_list[i][len(point_list)]) + '): ' + str( out_list[i][0] ) + '\n')

fg.close()


