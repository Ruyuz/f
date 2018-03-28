def max(num_list):
	max_num = num_list[0]
	for element in num_list:
		if element > max_num:
			max_num = element
	return max_num

def min(num_list):
	min_num = num_list[0]
	for element in num_list:
		if element < min_num:
			mix_num = element
	return mix_num

def mean(num_list):
	sum = 0
	for element in num_list:
		sum = sum + element
	return sum / len(num_list)

def median(num_list):
	if len(num_list) % 2 == 1 :
		index = len(num_list) // 2 
		return num_list[index]
	else:
		return (num_list[len(num_list) // 2] + num_list[len(num_list) // 2 - 1]) / 2

def variance(num_list):
	num_mean = mean(num_list)
	sum = 0
	for element in num_list:
		sum = sum + (element - num_mean) ** 2
	return sum / len(num_list)

def summary_statistics(num_list, func):
	return func(num_list)

