a = 0
b = 1
c =2

# 1.and:全真为真
print((a<b)and(a<c))
# 2.or 全假为假
print(a>b or b>c)
# 3.not 取反
print(not False)
print(not c>b)
# and运算符，只要有一个值为0，则结果为0，否则结果为做后一个非0数字
print(a and b) # 0
print(b and c)# c--2
# or 运算符，只有所有值为0结果为0，否则为法第一个非0 数字
print(a or a) # 0
print(a or b)# b--1
print(b or c)# b--1