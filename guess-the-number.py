s = input ('請輸入最小值 : ')
b = input ('請輸入最大值 : ')
s = int(s)
b = int(b)
import random
num = random.randint(s,b)
count =0
while True:
	g = input('請輸入你猜的數字 : ')
	g = int(g)
	count +=1
	if g == num :
		print ('恭喜你猜對了')
		break
	elif g < num :
		print ('比你猜的數字大')
	elif g > num :
		print ('比你猜的數字小')
	print ('這是第' , count, '次')


