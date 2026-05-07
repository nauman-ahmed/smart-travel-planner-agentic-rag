import requests
import pandas as pd

cities = {
    "Paris": (48.8566, 2.3522),
    "Rome": (41.9028, 12.4964),
    "Berlin": (52.5200, 13.4050),
    "Barcelona": (41.3851, 2.1734),
    "Istanbul": (41.0082, 28.9784)
}

weather_data = []
print("Starting to fetch weather data for cities...")
for city, (lat, lon) in cities.items():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    print(f"Fetching weather data for {city}...")
    response = requests.get(url).json()

    current = response.get("current_weather", {})

    weather_data.append({
        "city": city,
        "temperature": current.get("temperature"),
        "windspeed": current.get("windspeed")
    })

df = pd.DataFrame(weather_data)

df.to_csv("data/processed/weather.csv", index=False)

print(df)