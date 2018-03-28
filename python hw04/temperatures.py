def convert_temperatures(*temp_argu, degree):
	list1 = list(temp_argu)
	res = []
	if degree == 'Celsius':
		res = list(map(celsius_to_fahrenheit(), list1))
	elif degree == 'Fahrenheit':
		res = [fahrenheit_to_celsius(x) for x in list1]
	return res

def fahrenheit_to_celsius(x):
	return (x - 32) / 1.8

def celsius_to_fahrenheit(x):
	return x * 1.8 + 32
