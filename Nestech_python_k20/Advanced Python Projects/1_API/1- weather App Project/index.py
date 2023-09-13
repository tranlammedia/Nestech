import requests

API_KEY = '98e2e0cf79ff2288d97496ea7a3830b3'
CITY = 'Vietnam'
UNITS = 'imperial'
URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&units={UNITS}&appid={API_KEY}'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    print(f'Temperature: {temp} F\nHumidity: {humidity}%\nDescription: {description}')
else:
    print('Failed to fetch weather data')
