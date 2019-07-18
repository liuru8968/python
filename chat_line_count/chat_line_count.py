

def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())#append():用於()中的添增新對象
	return lines	#.strip()去除換行符號


def convert(lines):
	person = None
	liu_word_count = 0#算字數
	liu_sticker_count = 0#算貼圖
	liu_image_count = 0#算圖片
	Hsin_word_count = 0
	Hsin_sticker_count = 0
	Hsin_image_count = 0
	for line in lines:
		s = line.split(' ')#split('')以''的方式切割字
		time = s[0]
		name = s[1]
		if name == 'liu':
			if s[2] == '貼圖':
				liu_sticker_count += 1
			elif s[2] == '圖片':
				liu_image_count += 1
			else:
				for m in s[2:]:
					liu_word_count += len(m)#len計算字串
		elif name == 'Hsin':
			if s[2] == '貼圖':
				Hsin_sticker_count += 1
			elif s[2] == '圖片':
				Hsin_image_count += 1
			else:
				for m in s[2:]:
					Hsin_word_count += len(m)
	print('liu說了', liu_word_count, '個字')
	print('liu傳了', liu_sticker_count, '個貼圖')
	print('liu傳了', liu_image_count, '張圖片')

	print('Hsin說了', Hsin_word_count, '個字')
	print('Hsin傳了', Hsin_sticker_count, '個貼圖')
	print('Hsin傳了', Hsin_image_count, '張圖片')


def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]Hsin.txt')
	lines = convert(lines)


main()
