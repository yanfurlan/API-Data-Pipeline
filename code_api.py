# Código Python para extrair dados da API
import requests
import pandas as pd

# API Settings
API_KEY = "api_key"  # Substitua pela sua chave de API do OpenWeatherMap
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITIES = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Paris", "New York"]

# Collect data from API
data = []
for city in CITIES:
    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    if response.status_code == 200:
        weather_data = response.json()
        data.append({
            "City": city,
            "Temperature (°C)": weather_data["main"]["temp"],
            "Humidity (%)": weather_data["main"]["humidity"],
            "Weather": weather_data["weather"][0]["description"]
        })
    else:
        print(f"Erro ao buscar dados para {city}: {response.status_code}")

# Create DataFrame
df = pd.DataFrame(data)
print(df)
