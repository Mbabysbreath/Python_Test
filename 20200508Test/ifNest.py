# if条件嵌套
# 如果有钱可以上车，否则，不能上车。上车了，有座位可以坐下
money = int(input("你现在的零钱有："))
if money >= 1:
    print("土豪请上车")
    seat = int(input("车上的空座有："))
    if seat >= 1:
        print("土豪请上座")
    else:
        print("土豪请站着吧")
else:
    print("没钱，跟着跑")
