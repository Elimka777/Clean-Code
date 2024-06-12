# weather/weather_forecast.py
from weather.weather_data import WeatherDataFetcher
from weather.weather_parser import WeatherDataParser

class WeatherForecast:
    def get_detailed_forecast(self, city):
        # Function to provide a detailed weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(city)
        return WeatherDataParser.parse_weather_data(data)

    def display_weather(self, city):
        # Function to display the basic weather forecast for a city
        data = WeatherDataFetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = WeatherDataParser.parse_weather_data(data)
            print(weather_report)
