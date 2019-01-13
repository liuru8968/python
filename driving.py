print('請輸入(只限制):台灣/美國/中國/紐西蘭')
country = input('請輸入你的國家:')
age = input('請輸入你的年齡:')
if country=='台灣':
    if int(age) >=18 :
        print('你可以考駕照')
    else:
        print('你還不可以考駕照')
elif country=='美國':
    if int(age) >=16 :
        print('你可以考駕照')
    else:
        print('你還不可以考駕照')
elif country=='紐西蘭':
    if int(age) >=15 :
        print('你可以考駕照')
    else:
        print('你還不可以考駕照')
elif country=='中國':
    age=int(age)
    if age >=18 and age <= 70:
        print('你已經過考駕照的年齡駕照')
    elif age >= 70:
        print('你已經過考駕照的年齡駕照')
    else:
        print('你還不可以考')
else:
    print('沒有這資料')