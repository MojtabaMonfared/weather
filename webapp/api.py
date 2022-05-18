import requests
import json

API_KEY = '364aa06d02544383a24220616221805'

def get_current_weather(query):
    URL = 'https://api.weatherapi.com/v1/current.json'
    parameters = {
        'key': API_KEY,
        'q': query,
    }
    r = requests.get(URL, params=parameters)
    result_weather = json.loads(r.text)
    return result_weather