date =[]
count = 0

#讀取系統

with open('reviews.txt', 'r') as f:
	for line in f:
		date.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(date))
print('檔案讀取完畢,總共有', len(date),'筆資料')

#增新字典

wc = {} #字典數目
for d in date:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc [word] = 1 #增加新的key到字典中

#查詢字典中的資料

print('以下是超過出現1,000,000次的單字:')
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print('本資料總共有', len(wc), '種單字')
print('本系統為查詢出現過幾次的單字，如果沒有要收尋請打"q"為離開建')

while True:
	word = input('請問你想查什麼字:')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為:', wc[word])
	else:
		print('字典沒有出現這個字')
print('感謝使用本收尋功能')