import sys
g = lambda x: 'FizzBuzz' if x % 3 == 0 and x % 5 == 0 else 'Fizz' if x % 3 == 0 else 'Buzz' if x % 5 == 0 else x
for i in range(1, int(sys.argv[1])+1): print(g(i)) 
	
	
