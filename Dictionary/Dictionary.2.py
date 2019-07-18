#Dictionary 字典 應用範例ex:2(利用AQI指標)

#利用字典查詢指定答案

AQI_colour = {'綠色':'良', '黃色':'普通','橘色':'對敏感組群不良', 
			'紅色':'對所有組群不良', '紫色':'不良', '橘紅色':'有害'}

print('AQI的顏色是查詢空氣品質')
print('請選擇AQI的顏色:綠色,黃色,橘色,紅色,紫色,橘紅色')

colour = input('請打以上這幾種顏色查詢:')

print(AQI_colour[colour])
