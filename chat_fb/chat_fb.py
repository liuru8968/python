

def read_file(filename):#filename檔名
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
	#-sig是用來去掉前面的\ufeff的
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new = []
	person = None #None=無
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue #continue:繼續待在迴圈，並跳一迴
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)


main()