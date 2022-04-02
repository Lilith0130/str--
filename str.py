# 字串當清單

car = 'Audi'
# ['A', 'u', 'd' ,'i']
#python 認定'Audi'是個清單 每個字母拆開為一個項目
# A
# u
# d
# i
for c in car:
	print(c)
print(len(car))
print('A'in car)
print('Au'in car)
print('x'in car)
# 4
# True
# True
# False

