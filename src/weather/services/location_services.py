from .weather_services import get_weather

def search_location_weather(query: str):
    query = query.strip()  # убираем пробелы
    if not query:  # если пусто, возвращаем пустой список
        return []

    # Передаём именно строку в get_weather
    weather = get_weather(city_name=query)

    if not weather:
        return []

    weather["from_db"] = False
    return [weather]