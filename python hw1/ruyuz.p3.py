my_number = input('Please enter a number: ')
number = int(my_number)
if number >= 1:
	print(1)
if number >= 2:
	print(1)
if number >= 3:
	x,y,count = 1,1,3
	while count <= number:
		x, y, count = y, x+y, count+1
		print(y)

