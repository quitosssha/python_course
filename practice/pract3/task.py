import requests
import json

def parse_wind(speed, degrees):
    wind_directions = ["С", "СВ", "В", "ЮВ", "Ю", "ЮЗ", "З", "СЗ"]
    index = round(wind_deg / 45) % 8
    direction = wind_directions[index]
    return f"{speed} м/с, направление {direction} ({degrees}°)"

def parse_status(main_info, description):
    if main_info == "Clear":
        return "Ясно"
    elif main_info == "Clouds":
        if "few" in description or "scattered" in description:
            return "Малооблачно"
        else:
            return "Облачно"
    elif main_info == "Rain":
        return "Дождь"
    elif main_info == "Snow":
        return "Снег"
    elif main_info == "Thunderstorm":
        return "Гроза"
    elif main_info == "Drizzle":
        return "Морось"
    elif main_info == "Mist" or weather_main == "Fog":
        return "Туман"
    else:
        return description

city = input("Введите название города: ")
url = 'https://api.openweathermap.org/data/2.5/weather'
query_params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
}
response = requests.get(url, params=query_params)
data = response.json()

if response.status_code != 200 or data["cod"] != 200:
    print(f"Ошибка {response.status_code}:")
    print(json.dumps(data, indent=4))
    exit(1)

city_name = data["name"]
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
pressure = data["main"]["pressure"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
wind_deg = data["wind"]["deg"]
weather_main = data["weather"][0]["main"]  # Clear, Rain, Snow, Clouds...
weather_description = data["weather"][0]["description"]

wind_message = parse_wind(wind_speed, wind_deg)
weather_status = parse_status(weather_main, weather_description)

print(f"\nПогода в городе: {city_name}\n")
print(f"Температура: {temp:.1f}°C")
print(f"Ощущается как: {feels_like:.1f}°C")
print(f"Ветер: {wind_message}")
print(f"Давление: {pressure} гПа")
print(f"Влажность: {humidity}%")
print(f"Состояние: {weather_status}")