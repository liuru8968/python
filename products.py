products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    products.append([name, price])
print(products)
#清單中的小清單[0,0]
for p in products:
    print(p[0],'的價格',p[1])