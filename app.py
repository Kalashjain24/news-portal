from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>📰 News Portal Backend is LIVE</h1>
    <p>Deployment successful on Render.</p>
    <p>Next step: Connect real news API.</p>
    """

@app.route("/api/news")
def news():
    sample_news = [
        "India latest headlines",
        "Maharashtra breaking news",
        "Technology updates today",
        "Sports top stories"
    ]
    return jsonify(sample_news)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

