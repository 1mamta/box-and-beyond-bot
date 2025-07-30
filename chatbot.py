import json
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline

# Load intents
with open("intents.json", "r") as file:
    data = json.load(file)

# Prepare training data
tags = []
patterns = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tags.append(intent["tag"])
        patterns.append(pattern)

# Build ML model
model = make_pipeline(TfidfVectorizer(), LinearSVC())
model.fit(patterns, tags)

# Get a random response for the matched tag
def get_response(user_input):
    try:
        tag = model.predict([user_input])[0]
        for intent in data["intents"]:
            if intent["tag"] == tag:
                return random.choice(intent["responses"])
    except:
        return "Sorry, I didn't understand that. Can you rephrase?"
