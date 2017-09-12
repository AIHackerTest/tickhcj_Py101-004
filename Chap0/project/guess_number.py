import random

print("""
    \t猜数字游戏
    系统随机生成一个小于20的数
    猜猜这个数是多少
    友情提示：你有10次机会
""")

num = random.randint(0,20)
time = 10

while time >0:
    time -= 1
    try:
        gnum = int(input("\n输入一个你想到的数："))
    except ValueError:
        print(f'\n请确认你输入的是数字,你还有{time}次机会')
        continue

    if gnum == num:
        print("\n恭喜你猜对了！")
        break
    elif gnum != num and time == 0:
        print(f"\n机会已经用完了,还是没有猜对，这个数是：{num}")
        break
    elif gnum > num:
        print(f"\n数大了，你还有{time}次机会")
    else:
        print(f"\n数小了，你还有{time}次机会")

print('\n', '*' * 6, "Game over", '*' * 6)
