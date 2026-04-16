from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store feedback in memory
feedback_data = []

@app.route("/")
def home():
    return "Backend Running"

@app.route("/recommend", methods=["POST"])
def recommend():
    print(" /recommend HIT")

    data = request.get_json()
    print("Incoming:", data)

    wardrobe = [item.lower() for item in data.get("wardrobe", [])]
    weather = data.get("weather", "").lower()
    event = data.get("event", "").lower()

    outfit = []

    # Base logic
    if weather == "hot":
        outfit.append("t-shirt")
    elif weather == "cold":
        outfit.append("hoodie")

    if event == "casual":
        outfit.append("jeans")
    elif event == "formal":
        outfit.append("blazer")

    # Match with wardrobe
    final_outfit = [item for item in outfit if item in wardrobe]

    if not final_outfit:
        final_outfit = wardrobe[:2]

    # LEARNING FROM FEEDBACK (FIXED)
    disliked_items = set()

    for entry in feedback_data:
        if entry.get("feedback") == "dislike":
            for item in entry.get("outfit", []):
                disliked_items.add(item.lower())

    print("Disliked Items:", disliked_items)

    # Remove disliked items
    final_outfit = [item for item in final_outfit if item not in disliked_items]

    # fallback again
    if not final_outfit:
        final_outfit = [item for item in wardrobe if item not in disliked_items][:2]

    print("Final Outfit:", final_outfit)

    return jsonify({"recommended_outfit": final_outfit})

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.get_json()

    print("FEEDBACK RECEIVED:", data)

    feedback_data.append(data)

    return jsonify({"message": "Feedback stored"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)