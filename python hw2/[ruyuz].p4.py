import string

str1 = input('Please enter a string: ')
for punc in string.punctuation:
	str1 = str1.replace(punc,'') #ignoring punctuation
str2 = str1.replace(' ','') #delete all the spaces in string, 
str3 = str2.lower() #ignoring case

str4 = str3[::-1]
if str3 == str4:
	print('True')
else:
	print('False')
