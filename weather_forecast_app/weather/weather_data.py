# weather/weather_data.py
class WeatherDataFetcher:
    @staticmethod
    def fetch_weather_data(city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        # Simulated data based on city
        weather_data = {
            "Chicago": {"city": "Chicago", "temperature": 55, "condition": "Windy", "humidity": 60},
            "San Jose": {"city": "San Jose", "temperature": 68, "condition": "Sunny", "humidity": 45},
            "South Korea": {"city": "South Korea", "temperature": 72, "condition": "Humid", "humidity": 80}
        }
        return weather_data.get(city, None)
