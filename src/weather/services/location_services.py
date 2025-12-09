from .weather_services import get_weather

def search_location_weather(query: str):
    query = query.strip()
    if not query:
        return []

    weather = get_weather(query)
    weather_list = []
    if weather:
        weather["from_db"] = False
        weather_list.append(weather)
    return weather_list