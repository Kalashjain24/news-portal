from flask import Flask, jsonify
import feedparser

app = Flask(__name__)

# RSS feeds (Hindi, Marathi, English)
RSS_FEEDS = {
    "Lokmat (Marathi)": "https://www.lokmat.com/rss/headlines.xml",
    "Sakal (Marathi)": "https://www.esakal.com/rss.xml",
    "Loksatta (Marathi)": "https://www.loksatta.com/feed/",
    "Dainik Bhaskar (Hindi)": "https://www.bhaskar.com/rss-v1--category-1051.xml",
    "Navbharat Times (Hindi)": "https://navbharattimes.indiatimes.com/rssfeedsdefault.cms",
    "Times of India (English)": "https://timesofindia.indiatimes.com/rssfeedstopstories.cms",
}

from flask import send_file

@app.route("/")
def home():
    return send_file("index.html")

    return """
    <h1>📰 Multilingual News Portal is LIVE</h1>
    <p>Hindi + Marathi + English news connected.</p>
    <p>Open <a href='/api/news'>/api/news</a> to see live headlines.</p>
    """

@app.route("/api/news")
def get_news():
    all_news = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            all_news.append({
                "source": source,
                "title": entry.title,
                "link": entry.link
            })

    return jsonify(all_news)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)


