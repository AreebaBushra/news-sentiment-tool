from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

app = Flask(__name__)

# HuggingFace sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Get latest BBC headlines
def get_news():
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    titles = [item.title.text for item in soup.find_all("item")]
    return titles[:10]

@app.route("/")
def index():
    headlines = get_news()
    results = []
    for headline in headlines:
        sentiment = sentiment_pipeline(headline)[0]
        results.append({
            "headline": headline,
            "label": sentiment["label"],
            "score": round(sentiment["score"], 2)
        })
    return render_template("index.html", news=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
