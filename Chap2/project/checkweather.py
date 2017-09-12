import requests
import json
import time

print("欢迎使用天气通查询天气")
print("数据由心知天气提供")
# 读取天气文件，提取城市和天气情况
data = {}
with open('weather_info.txt', 'r', encoding='utf-8') as f:
    for line in f:
        (key, value) = line.strip().split(',')
        data[key] = value

# 保存历史查询记录
history = []
while True:
    user_input = input("请输入指令或要查询的城市名：")
    # 1.输入城市名，返回该城市的天气数据
    if user_input in data:
        date = int(input("请输入要查询的日期【‘0’今天，‘1’明天，‘2’后天】: "))
        # 联网查询
        const_value = {
            'key': 'ngwxhjgdgipkjzqw',
            'location': user_input,
            'language': 'zh-Hans',
            'unit': 'c',
            'start': '0',
            'days': '3'
        }
        api_url = 'https://api.seniverse.com/v3/weather/daily.json'
        xinzhi_data = requests.get(api_url, params=const_value).json()
        info = xinzhi_data['results'][0]['daily']
        weather_date = info[date]['date']
        weather = info[date]['text_day']
        tem_high = info[date]['high']
        tem_low = info[date]['low']
        wind = info[date]['wind_direction']
        # 打印查询结果
        weather_output = f"""
            {weather_date}
            {user_input}的天气为{weather}
            风向为{wind}
            最高温度为{tem_high}摄氏度
            最低温度为{tem_low}摄氏度
        """
        print(weather_output)
        ticks = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        print(f"更新时间: {ticks}")
        if weather_output in history:
            continue
        else:
            history.append(weather_output)
    # 2.输入指令，打印帮助文档（使用help)
    elif user_input == "help":
        print("""
            \t 输入城市名，查询该城市的天气；
            \t 输入 hlep，获取帮助文档；
            \t 输入 history，获取查询历史；
            \t 输入 quit，退出天气查询系统。
        """)
    elif user_input == "history":
        print("已经查询过的城市：")
        for output in history:
            print(output)
    # 3.输入指令，退出程序的交互（使用quit）
    # 4.在退出程序之前，打印查询过的所有城市
    elif user_input == "quit":
        print("欢迎再次使用天气查询")
        break
    else:
        print("不能识别的指令，输入help获取帮助文档")
