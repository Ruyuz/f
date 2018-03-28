list_player = []
with open('/Users/ruyuzhou/Desktop/fangraphs_leaderboard.csv', encoding = 'utf-8-sig') as csv:
	fp = csv.readline()
	for line in csv:
		list_player.append(line.replace('"','').split(','))
name = input('Enter a player name: ')
tag = input('Enter an offensive category: ')
namelist = [n[0] for n in list_player]
if name not in namelist:
	print('Error:')
	print('Player not found')
else:
	point = fp.replace('"','').split(',')
	if tag not in point:
		print('Error:')
		print('Category not available')
	else:
		Id = namelist.index(name)
		tagId = point.index(tag)
		print('Result:')
		print( name + ', ' + str(list_player[Id][1])+ ', ' + tag + ': ' + str(list_player[Id][tagId]))
