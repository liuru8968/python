#Dictionary 字典 應用範例ex:1
#利用pH指示劑做範例

#新增一個字典使用{}
#key和value的對應,key就是我們指定的名稱，value就是根據key找到的資料

ph_indicator = {'4':'紅色', '5':'橘色', '6':'黃色', '7':'綠色', 
				'8':'藍色', '9':'靛色'}

ph_indicator['10'] = '紫色'#增加一個key

print(ph_indicator['5'])#顯示字典
print(ph_indicator['10'])#如果不包含字典中，中途加進字典也會顯示出來
