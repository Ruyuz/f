import math

poi1 = input('Please enter point 1: ')
poi2 = input('Please enter point 2: ')
poi1_list = poi1.split(',')
poi2_list = poi2.split(',')
poi1_x = int(poi1_list[0])
poi1_y = int(poi1_list[1])
poi2_x = int(poi2_list[0])
poi2_y = int(poi2_list[1])

distance = math.sqrt((poi1_x -  poi2_x) ** 2 + (poi1_y - poi2_y) ** 2)
dis = str(distance)

print('The distance between these points is '+ dis)
