import requests

API_KEY = "27aba962c428bf04ada751cddae13305"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city name: ")
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

    print(f"\nWeather in {city.title()}:")
    print(f"Temperature: {temp}°F")
    print(f"Condition: {weather}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} m/s")
else:
    print("\nCity not found. PLease check your spelling.")

