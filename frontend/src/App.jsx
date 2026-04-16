import { useState } from "react";

function App() {
  const [wardrobe, setWardrobe] = useState("");
  const [weather, setWeather] = useState("");
  const [event, setEvent] = useState("");
  const [outfit, setOutfit] = useState([]);

  const API_BASE = "https://animated-engine-g46qjgwjvwwxc9g44-5000.app.github.dev"; 

  const getOutfit = async () => {
    try {
      const response = await fetch(`${API_BASE}/recommend`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          wardrobe: wardrobe.split(",").map(item => item.trim().toLowerCase()),
          weather: weather.trim().toLowerCase(),
          event: event.trim().toLowerCase()
        })
      });

      const data = await response.json();
      console.log("Response:", data);

      setOutfit(data.recommended_outfit);
    } catch (err) {
      console.error(err);
    }
  };

  const sendFeedback = async (type) => {
    try {
      await fetch(`${API_BASE}/feedback`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          outfit,
          feedback: type
        })
      });

      console.log("Feedback sent:", type);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Clueless AI</h1>

      <input
        placeholder="Wardrobe (t-shirt, jeans, blazer)"
        onChange={(e) => setWardrobe(e.target.value)}
      />

      <input
        placeholder="Weather (hot/cold)"
        onChange={(e) => setWeather(e.target.value)}
      />

      <input
        placeholder="Event (casual/formal)"
        onChange={(e) => setEvent(e.target.value)}
      />

      <button onClick={getOutfit}>Get Outfit</button>

      <h3>Recommended Outfit:</h3>

      <ul>
        {outfit.map((item, i) => (
          <li key={i}>{item}</li>
        ))}
      </ul>

      {outfit.length > 0 && (
        <div style={{ marginTop: "20px" }}>
          <button onClick={() => sendFeedback("like")}>👍 Like</button>
          <button onClick={() => sendFeedback("dislike")}>👎 Dislike</button>
        </div>
      )}
    </div>
  );
}

export default App;