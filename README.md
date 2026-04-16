# Clueless AI – Smart Outfit Recommendation System

Clueless AI is a full-stack AI-powered fashion assistant that recommends outfits based on a user's wardrobe, weather conditions, and event context. It also incorporates a feedback-driven learning system to improve recommendations over time.

---

## Features

-  Personalized outfit recommendations
-  Weather-based outfit selection
-  Event-based styling (casual/formal)
-  Feedback-driven learning system (👍 / 👎)
-  Adaptive recommendations based on user preferences

---

## Tech Stack

- **Frontend:** React.js (Vite)
- **Backend:** Flask (Python)
- **API:** RESTful architecture
- **Deployment:** GitHub Codespaces

---

## How It Works

1. User inputs:
   - Wardrobe (e.g., t-shirt, jeans, blazer)
   - Weather (hot/cold)
   - Event (casual/formal)

2. Backend generates outfit using rule-based logic

3. User provides feedback:
   - 👍 Like → reinforces choices
   - 👎 Dislike → removes items from future suggestions

4. System adapts by filtering disliked items in future recommendations

---

##  Example

**Input:**
Wardrobe: t-shirt, jeans, blazer
Weather: hot
Event: casual

**Output**
t-shirt, jeans


After 👎 Dislike → next recommendation avoids disliked items.

![alt text](<Screenshot (26).png>)