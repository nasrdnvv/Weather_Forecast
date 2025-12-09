import requests
from django.conf import settings


def get_weather(city_name: str):
    api_key = settings.OPENWEATHER_API_KEY
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city_name}"
        f"&appid={api_key}&units=metric&lang=ru"
    )
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