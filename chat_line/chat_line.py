
lines = []
with open('[LINE]Hsin_1.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]#取第一組字串中的前5個
	name = s[0][5:]#取第一組字串中的第5個以後
	chat = s[1]
	print(name + ':' + chat)

