def my_reduce(func, iterable):
	generable = iterable
	generator = iter(generable)
	value = next(generator)
	for i in generator:
		value = func(value, i)
	return value

