from PIL import Image
import os

for file in os.listdir('capoo_original'):
	if file.endswith('.png'):#endswith:如果最後是()字的話執行
		image_file = Image.open(os.path.join('capoo_original',file))#os.path.join:路徑合併( )
		image_file = image_file.convert('L')#不同像素表示之間轉換圖像
		image_file.save(os.path.join('capoo_change', file[:-4] + '_grey.png'))#[:-4]:從倒數第4個不要
		
