# main.py
from weather.weather_forecast import WeatherForecast

def main():
    forecast = WeatherForecast()
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        if city.lower() == 'exit':
            break
        detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
        if detailed == 'yes':
            print(forecast.get_detailed_forecast(city))
        else:
            forecast.display_weather(city)

if __name__ == "__main__":
    main()
