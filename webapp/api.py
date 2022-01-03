import requests
import json

API_KEY = '888a0ae798984bd699191644220101'

def get_current_weather(query):
    CURRENT_URL = 'https://api.weatherapi.com/v1/search.json'
    parameters = {
        'key': API_KEY,
        'q': query,
    }
    r = requests.get(CURRENT_URL, params=parameters)
    result_weather = json.loads(r.text)
    for i in result_weather:
        return i['name']