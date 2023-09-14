drink = input('有沒有喝過酒: ')
if drink != '有' and drink != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
age = input("請輸入你的年齡: ")
age = int(age)
if drink == '有':
	if age >= 18:
		print('適量飲酒,開車不喝酒')
	else:
		print('未成年請勿飲酒')
elif drink == '沒有':
	if age >= 18:
		print('你真健康')
	else:
		print('再過幾年才能嘗試')