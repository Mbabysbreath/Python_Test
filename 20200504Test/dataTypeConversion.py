# 数据类型转化函数
num1 = "1"
num = 123
num2 = int(num1) # 将num1转化为整型
print(type(num2))
print(num2)

num3 = float(num1)
print(num3,type(num3))# 将num1转化为浮点型

str1 = str(num)# 将num转化为字符串
print(str1,type(str1))

list1 = [1,2,3]
tuple1 = tuple(list1)# 将一个序列转化为元组
print(tuple1,type(tuple1))
ss = (4,5,6)# 将一个序列转化为列表
print(list(ss),type(list(ss)))

str2 = '1'
str3 = '1.1'
str4 = '(1,2,3)'
str5 = '[4,5,6]'
print(eval(str2), type(eval(str2)))
print(eval(str3), type(eval(str3)))
print(eval(str4), type(eval(str4)))
print(eval(str5), type(eval(str5)))
