import string

path = input('Please enter a file path:')
fg = open(path, encoding = 'utf-8-sig')
dic = {}
w_count = 0
max1 = 0
max2 = 0

file_line_list = fg.readlines()
l_count = len(file_line_list)

fg2 = open(path, encoding = 'utf-8-sig')
file_str = fg2.read() #read entire file into a single string  ?will enter be white space

for punc in string.punctuation:
	file_str = file_str.replace(punc,'')# ignoring the punctuation
file_str = file_str.lower() #ignoring the case

file_word_list = file_str.split()

for word in file_word_list:
	w_count = w_count + 1
	if word not in dic:
		dic[word] = 1
	else:
		dic[word] = dic[word] + 1
	if dic[word] > max1:
		max2 = max1
		max1 = dic[word]

print('File stats:')
print('Word count: '+str(w_count))
print('Line count: '+str(l_count))
print('Most frequent words:')
count = 0
for word in dic:
	if dic[word] == max1 and count < 2:
		print(word+' '+'('+str(max1)+')')
		count = count + 1
for word in dic:
	if dic[word] == max2 and count < 2:
		print(word+' '+'('+str(max2)+')')
		count = count + 1
fg.close()
fg2.close()
