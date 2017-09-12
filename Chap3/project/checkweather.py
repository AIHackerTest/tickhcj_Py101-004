import requests
import json
# import logging

print("欢迎使用天气通查询天气")
print("数据由心知天气提供")

# 联网查询实时天气并返回结果
def internet_weather(user_input):
    const_value = {
        'key': 'ngwxhjgdgipkjzqw',
        'location': user_input,
        'language': 'zh-Hans',
        'unit': 'c',
    }
    api_url = 'https://api.seniverse.com/v3/weather/now.json'
    result = requests.get(api_url, params=const_value, timeout=30).json()
    return result

# 解读返回的天气数据并打印
def weather_info(result):
    ticks = result['results'][0]['last_update'][:-9].replace('T', ' ')
    city_name = result['results'][0]['location']['name']
    weather = result['results'][0]['now']['text']
    tem = result['results'][0]['now']['temperature']
    wind = result['results'][0]['now']['wind_direction']
    weather_output = f"{city_name}天气: {weather},风向: {wind},温度: {tem}摄氏度"
    return weather_output, ticks

history = []
while True:
    user_input = input("请输入指令或是要查询的城市名：")
    if user_input == "help":
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
    elif user_input == "quit":
        print("欢迎再次使用天气查询")
        break
    else:
        try:
            result = internet_weather(user_input)
            weather_output, ticks = weather_info(result)
            print(weather_output)
            print(f"更新时间: {ticks}")
            if weather_output in history:
                continue
            else:
                history.append(weather_output)
        except Exception:
            # logging.exception(e)
            print("不能识别的指令，输入help获取帮助文档")
