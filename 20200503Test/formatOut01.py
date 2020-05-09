# 格式化输出字符串
age = 18
name = "zhaomin"
weight = 90.5
stu_id = 1
# 我是zhaomin ,今年18岁，体重是 90.5斤,学号001
print("我是%s" % name)
print("体重：%.2f" % weight)
print("我的学号%03d" % stu_id)
print("我是%s ,今年%d岁，体重是%.2f斤,学号%03d" %(name,age,weight,stu_id))
# 比较%s和f'{}'格式字符串,f表达式更高效
print("我是%s ,今年%s岁，体重是%s斤,学号%s" %(name,age,weight,stu_id))
print(f"我是{name} ,今年{age}岁，体重是{weight}斤,学号{stu_id}")