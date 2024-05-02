import requests
import json
def weather_app():
    city = input('Enter your city name: ')
    url = f"https://api.weatherapi.com/v1/current.json?key=e721b6a900734e1f9a1162912240401&q={city}"
    r = requests.get(url)
    print(r.text)
    print("--------------------------------------------------------------------------")
    wdic = json.loads(r.text)
    temp = wdic["current"]["temp_c"]
    curr_weather = wdic["current"]["condition"]["text"]
    wind_speed = wdic["current"]["wind_kph"]
    if __name__ == '__main__':
        print("Welcome to ROBO Speaker 1.00")
        x =f"the current temperature in {city} is {temp} degrees Celsius"
        y = f"the current weather in {city} is {curr_weather}"
        z = f"the current wind speed in {city} is {wind_speed} km/h"
        print(x)
        print(y)
        print(z)
