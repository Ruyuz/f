import sys

def fibonacci(x):
	if x == 0:
		return 1
	if x == 1:
		return 1
	return fibonacci(x - 1) + fibonacci(x - 2)

n = int(sys.argv[1])
for i in range(0, n + 1):
	print (fibonacci(i))