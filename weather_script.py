import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # Use metric units for temperature in Celsius
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Example usage:
if __name__ == "__main__":
    api_key = "d9660777d8703f83462782ab4f0f72d1"
    weather_fetcher = WeatherFetcher(api_key)
    city = input("Enter the city name: ")
    try:
        weather_data = weather_fetcher.get_weather(city)
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
