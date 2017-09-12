from flask import Flask, request, render_template
import requests

app = Flask(__name__)

def internet_weather(user_input):
    const_value = {
        'key': 'ngwxhjgdgipkjzqw',
        'location': user_input,
        'language': 'zh-Hans',
        'unit': 'c'
    }
    api_url = 'https://api.seniverse.com/v3/weather/now.json'
    result = requests.get(api_url, params=const_value, timeout=10).json()
    ticks = result['results'][0]['last_update'][:-9].replace('T', ' ')
    city_name = result['results'][0]['location']['name']
    weather = result['results'][0]['now']['text']
    tem = result['results'][0]['now']['temperature']
    wind = result['results'][0]['now']['wind_direction']
    # weather_output = ['{city_name}天气: {weather}', '风向: {wind}', '温度: {tem}摄氏度']
    weather_info = f'{city_name}天气: {weather}, 风向: {wind}, 温度: {tem}摄氏度'
    return weather_info

def assist():
    ass = [
        '输入城市名，点击【查询】，获取该城市最新天气情况',
        '点击【帮助】，获取帮助信息',
        '点击【历史】，获取历史查询信息'
    ]
    return ass

history_info = []
def history(info):
    for i in range(0, 1):
        if info in history_info:
            continue
        else:
            history_info.append(info)
    return history_info

@app.route('/', methods=['GET', 'POST'])
def home():
    message = []
    if 'history' in request.form.keys():
        message = history_info
    elif 'help' in request.form.keys():
        message = assist()
    elif 'city_name' in request.form.keys():
        try:
            info = internet_weather(request.form['city_name'])
            history(info)
            # for i in info.split(','):
            #     message.append(i)
            message = [i for i in info.split(',')]
        except KeyError:
            message = ['服务器开小差啦，请重新输入']
    return render_template('home.html', message=message)

if __name__=='__main__':
    app.run(debug=True)
