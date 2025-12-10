import requests
from django.conf import settings


class WeatherService:
    def __init__(self):
        self.api_key = settings.OPENWEATHER_API_KEY
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city_name: str):
        url = (
            f"{self.base_url}?q={city_name}"
            f"&appid={self.api_key}&units=metric&lang=ru")
        try:
            resp = requests.get(url, timeout=5)
            resp.raise_for_status()
        except requests.RequestException:
            return None

        data = resp.json()
        return {
            "name": data.get("name"),
            "temperature": data.get("main", {}).get("temp"),
            "description": data.get("weather", [{}])[0].get("description"),
        }