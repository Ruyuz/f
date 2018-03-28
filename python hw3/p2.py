import math
def triangle(**args): 
	val = list(args.values())
	return 1/2 * val[0] * val[1]
def rectangle(**args):
	val = list(args.values())
	return val[0] * val[1]
def circle(**args):
	val = list(args.values())
	if "radius" in args.keys():
		return math.pi*val[0]**2
	else:
		return math.pi*(val[0]/2)**2
def area(shape, **args):
	dict = {'triangle':triangle, 'rectangle': rectangle, 'circle': circle} 
	

	return dict[shape](**args)
