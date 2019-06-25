import os #作業系統
products = []
#讀取檔案
if os.path.isfile('products.csv'):#檢查檔案是否存在
	print('讀取中...')
	print('找到檔案了')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
		name,price = line.strip().split(',')
		products.append([name,price])
	print(products)
else:
	print('找不到檔案,請去products.py建立檔案')
#使用者輸入
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':#離開按 q
        break
    price = input('請輸入商品價格:')#清單中的小清單[0,0]
    price =int(price)
    products.append([name, price])
print(products)
#印出商品價格
for p in products:
    print(p[0],'的價格',p[1])
#寫入檔案
with open('products.csv','w',encoding='utf-8') as f:#w=寫入
    f.write('商品,價格\n')
    for p in products:
    	f.write(p[0]+','+str(p[1])+'\n')