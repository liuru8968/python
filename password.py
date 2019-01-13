i = 3
password='a123456'
while True:
    pwd=input ('請輸入密碼:')
    if pwd == password:
        print('密碼正確') 
        break
    else:
    	i = i - 1
    	print('密碼錯誤! 還剩',i,'次機會')
    	if i == 0:
    	   break