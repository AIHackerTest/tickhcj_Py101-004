# 读取天气文件，提取城市和天气情况
data = {}
with open('weather_info.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        (key, value) = line.strip().split(',')
        data[key] = value

# 保存历史查询记录
history = []

while True:
    user_input = input("\n请输入指令或要查询的城市名：")
    # 1.输入城市名，返回该城市的天气数据
    if user_input in data:
        print(f"\n{user_input} 的天气状况是：{data[user_input]}")
        city_weather = f"{user_input}:{data[user_input]}"
        if city_weather in history:
            continue
        else:
            history.append(city_weather)
    # 2.输入指令，打印帮助文档（使用help)
    elif user_input == "help":
        print("""
            \t 输入城市名，查询该城市的天气；
            \t 输入 hlep，获取帮助文档；
            \t 输入 history，获取查询历史；
            \t 输入 quit，退出天气查询系统。
        """)
    elif user_input == "history":
        print("\n已经查询过的城市：")
        for output in history:
            print(output)
    # 3.输入指令，退出程序的交互（使用quit）
    # 4.在退出程序之前，打印查询过的所有城市
    elif user_input == "quit":
        print("\n欢迎再次使用天气查询")
        print("\n以下是您的查询记录：")
        for output in history:
            print(output)
        break
    else:
        print("\n不能识别的指令，输入help获取帮助文档")
