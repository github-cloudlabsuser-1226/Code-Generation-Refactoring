import requests

API_KEY = 'fdb46ee3b76d2ef4450eb4909fe12afe'
CITY = 'London'
URL = f'https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.0&appid={API_KEY}'

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    weather_desc = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    print(f"Weather in {CITY}: {weather_desc}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("Failed to fetch weather data.")
