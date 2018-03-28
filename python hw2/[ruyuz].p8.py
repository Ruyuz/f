category = input('Enter an offensive category:')
data = []
with open('/Users/ruyuzhou/Desktop/fangraphs_leaderboard.csv', encoding = 'utf-8-sig') as csv:
	fp = csv.readline()
	col = fp.replace('"', '').split(',')
	for line in csv:
		data.append(line.replace('"', '').split(','))
name = [i[0] for i in data]
if category in col:
	back = col.index(category)
	scores = [float(x) for x in [i[back] for i in data]]
	tag_scores = []
	for i in range(0, len(scores)):
		tag_scores.append([scores[i], i])
	seq = [s[1] for s in sorted(tag_scores, reverse = True)]
	top5 = sorted(scores, reverse = True); 
	print('Result:')
	for j in range(5) :
		if int(top5[j]) == top5[j]: 
			print(name[seq[j]] + ',' + str(int(top5[j])))
		else:
			print(name[seq[j]] + ',' + str(top5[j]))
else:
	print('Error:')
	print('Category not available')
