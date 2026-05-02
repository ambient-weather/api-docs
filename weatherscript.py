import requests

API_KEY = 'fe8b3049b2ab4b6f8b3049b2ab2b6f04'
STATION_ID = 'KCOBOULD1002'
BASE_URL = 'https://api.weather.com/v2/pws/observations/current'

def fetch_weather_underground_data():
  params = {
    'stationId': KCOBOULD1002,
    'format': 'json',
    'units': 'm', #using metric system
    'apiKey': fe8b3049b2ab4b6f8b3049b2ab2b6f04
  }

try: 
  response = requests.get(BASE_URL, params=params)
  response.raise_for_status()
  data = response.json()

obs = data['observations'][0]
weather_data = {
  'temperature_c': obs['metric']['temp'],
  'humidity': obs['humidity'],
  'wind_kph': obs['metric']['windSpeed'],
  'precip_mm': obs['metric']['precipTotal']
}

return weather_data


except requests.RequestException as e:
  print(f"API error: {e}")
  return None
  except KeyError:
        print("Error parsing weather data.")
        return None

def main():
    weather = fetch_weather_underground_data()
    if weather:
        print("Weather Underground Data:")
        for key, value in weather.items():
            print(f"{key}: {value}")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
