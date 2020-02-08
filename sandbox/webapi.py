import requests
import pprint

# url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList?appId=e62bc4b6e9ddd4742de927ec92be2557f06c5674&lang=J&statsField=1001'
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city': '130010'}
weather_data = requests.get(url, params=payload).json()

for weather in weather_data['forecasts']:
    print(weather['dateLabel'] + 'の天気は' + weather['telop'])
