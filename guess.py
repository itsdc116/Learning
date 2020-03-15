# 產生隨機整數1-100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話, 印出 "終於猜對了!"
# 猜錯的話, 要告訴他 比答案大/小

import random
r = random.randint(1, 100)
while True: # 重複去猜
	num = input('請輸入一個數字: ')
	num = int(num)
	if num == r: 
		print('終於猜對了!')
		break
	else:
		if num > r:
			print('太大了!')
		if num < r:
			print('太小了!')
