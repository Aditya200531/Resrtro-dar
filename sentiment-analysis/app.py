from flask import Flask, render_template, request
import spacy
from textblob import TextBlob
import re

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

def preprocess_review(review):
    review = review.lower()
    return re.sub(r'[^\w\s]', '', review)

def detect_food_items(review):
    doc = nlp(review)
    food_items = []
    food_keywords = ["biryani", "rice", "kebab", "chicken", "roll", "egg", "curry", "sandwich", "porota"]

    for chunk in doc.noun_chunks:
        if any(word in chunk.text for word in food_keywords):
            food_items.append(chunk.text.strip())
    
    return food_items if food_items else None

def detect_sentiment(review):
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity

    if polarity > 0.3:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

def analyze_review(review):
    cleaned_review = preprocess_review(review)
    sentiment = detect_sentiment(cleaned_review)
    food_items = detect_food_items(cleaned_review)
    
    return {
        "sentiment": sentiment,
        "food_items": food_items
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        review = request.form["review"]
        result = analyze_review(review)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
