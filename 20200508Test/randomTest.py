'''
猜拳游戏，
导入random模块--import random
使用这个模块中的功能--random.randint(开始，结束)
'''
import random
# 1.玩家出拳
player = int(input("玩家请出拳：0--石头，1--剪刀，2--布"))
computer = random.randint(0 ,2)
print(computer)
if (player == 0 and computer==1)or(player == 1 and computer==2) or (player == 2 and computer==0):
    print("玩家赢了")
elif player==computer:
    print("平局")
else:
    print("电脑获胜")
