g = input('請輸入體重:')
cm = input('請輸入身高:')
g = int(g)
cm = int(cm)
cm = cm /100 
bmi =g / cm / cm
if bmi < 18.5 :
    print(' bmi為:', bmi ,' ,體重過輕 ')
elif bmi >= 18.5 and bmi<24:
    print(' bmi為:', bmi ,',正常範圍')
elif bmi >= 24 and bmi <27:
    print(' bmi為:', BMI ,',異常範圍:過重')
elif bmi >= 27 and bmi <30:
    print(' bmi為:', bmi ,',異常範圍:中度肥胖')
elif bmi >= 30 and bmi <35:
    print(' bmi為:', bmi ,',異常範圍:輕度肥胖')
elif bmi>=35:
    print(' bmi為:', bmi ,',異常範圍:輕度肥胖') 