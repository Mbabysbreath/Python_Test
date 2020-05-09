# 多重判断
age = int(input("请输入你的年龄："))
if age < 18:
    print(f"{age}属于童工")
elif(age >= 18) and (age <= 60):
    print(f"{age}属于合法工龄")
else:
    print("该退休了")
