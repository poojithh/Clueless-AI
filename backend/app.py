from flask import Flask, request, jsonify
from model.recommendation import generate_outfit

app = Flask(__name__)

@app.route('/')
def home():
    return "Clueless AI Backend Running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json

    wardrobe = data.get("wardrobe", [])
    weather = data.get("weather", "")
    event = data.get("event", "")

    outfit = generate_outfit(wardrobe, weather, event)

    return jsonify({
        "recommended_outfit": outfit
    })

if __name__ == '__main__':
    app.run(debug=True)

city = data.get("city", "")
weather = get_weather(city)