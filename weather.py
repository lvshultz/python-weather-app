import requests
from datetime import datetime

API_KEY = "27aba962c428bf04ada751cddae13305"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("=== Weather Checker ===")
print("Type 'exit' to stop")

while True:
    city = input("\nEnter the city name: ").strip()
    if city.lower() == 'exit':
        print("\nGoodbye!")
        break

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial" # or "metric" for Celcius
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if(response.status_code == 200):
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"\nWeather in {city.title()} at ({time}):")
        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°F")
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind} m/s")

        with open("weather_log.txt", "a") as file:
            file.write(f"{time} | {city.title()} | {temp}°F | {weather} | Humidity: {humidity}% | Wind: {wind} m/s\n")
    else:
        print("\nCity not found. PLease check your spelling.")

