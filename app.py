from flask import Flask, jsonify, send_from_directory
import feedparser
import os

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

# Homepage → show index.html
@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.html")

# API → return live news JSON
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


