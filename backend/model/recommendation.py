def generate_outfit(wardrobe, weather, event):
    outfit = []

    # Weather logic
    if weather.lower() == "rainy":
        outfit.append("waterproof jacket")
    elif weather.lower() == "hot":
        outfit.append("t-shirt")
    elif weather.lower() == "cold":
        outfit.append("hoodie")

    # Event logic
    if event.lower() == "formal":
        outfit.append("blazer")
        outfit.append("formal shoes")
    elif event.lower() == "casual":
        outfit.append("jeans")
        outfit.append("sneakers")

    # Match with wardrobe
    final_outfit = [item for item in outfit if item in wardrobe]

    # fallback if nothing matches
    if not final_outfit:
        final_outfit = wardrobe[:2]

    return final_outfit

import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    data = requests.get(url).json()

    temp = data["main"]["temp"]

    if temp > 300:
        return "hot"
    elif temp < 285:
        return "cold"
    else:
        return "moderate"