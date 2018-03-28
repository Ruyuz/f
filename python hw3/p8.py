import math
import random

def approximate_pi(n):
	count = 0
	for i in range(0, n):
		x = random.random () * 2 -1
		y = random.random () * 2 -1
		dist = math.sqrt(x ** 2 + y ** 2)
		if dist <= 1:
			count += 1
	return 4 * count / n 
