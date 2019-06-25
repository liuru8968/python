#Function 是用來"收納"的程式碼
#它是個"功能"的函數

#例如:日期範例
def date1(year,month,day):#無預設值
	print('今天的日期:',year,month,day)
date1(2019,6,25)

def date2(year=2019,month=3,day=25):#預設預設值
	print('今天的日期:',year,month,day)
date2(month=6)#可指定某一個預設值

def date3(year,month,day=25):#無預設值的放前面,有預設值放最後
	print('今天的日期:',year,month,day)
date3(year=2019,month=6)#可指定某一個參數

#數字的應用
def add(x,y):#加法
	return x + y #return:回傳
ans = add(3,4)
print('加總:', ans)

def average(unmbers):#平均
	return sum(unmbers) / len(unmbers)
print('平均:' , average([1, 2, 3]))
print('平均:' , average([90, 67, 53]))
print('平均:' , average([210, 39, 54]))