def generate_outfit(wardrobe, weather, event):
    wardrobe = [item.strip().lower() for item in wardrobe]

    outfit = []

    # Weather logic
    if weather.lower() == "hot":
        outfit.append("t-shirt")
    elif weather.lower() == "cold":
        outfit.append("hoodie")
    elif weather.lower() == "rainy":
        outfit.append("waterproof jacket")

    # Event logic
    if event.lower() == "casual":
        outfit.append("jeans")
    elif event.lower() == "formal":
        outfit.append("blazer")

    # Match with wardrobe
    final_outfit = [item for item in outfit if item in wardrobe]

    # fallback
    if not final_outfit:
        print("Fallback triggered")
        return wardrobe[:2]

    return final_outfit