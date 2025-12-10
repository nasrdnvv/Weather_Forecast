from .weather_services import WeatherService

class LocationService:
    def __init__(self):
        self.weather_service = WeatherService()

    def search_location_weather(self, query: str):
        query = query.strip()
        if not query:
            return []
        weather = self.weather_service.get_weather(city_name=query)
        if not weather:
            return []
        weather["from_db"] = False
        return [weather]