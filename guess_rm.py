import random
s = input('請輸入開始值的範圍:')
end = input('請輸入結束值的範圍:')
s = int(s)
end = int(end)
r = random.randint(s,end)
n = 0
while True:
    n +=1# n=n + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('恭喜!')
        print('你總共猜對了',n,'次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('你猜了第',n,'次')