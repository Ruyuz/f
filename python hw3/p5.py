def number_manipulation_maker (func, x):
	if func == 'add':
		def func(y):
			return y + x
	if func == 'subtract':
		def func(y):
			return y - x
	if func == 'multiply':
		def func(y):
			return y * x
	if func == 'divide':
		def func(y):
			return y / x
	if func == 'exponent':
		def func(y):
			return y ** x
	return func
