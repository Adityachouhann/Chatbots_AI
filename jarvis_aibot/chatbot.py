import random
import json
import pickle

# Load intents
with open("intents.json") as file:
    data = json.load(file)

# Load trained model
with open("chatbot_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def get_response(user_input):
    X = vectorizer.transform([user_input])
    intent = model.predict(X)[0]

    for item in data["intents"]:
        if item["tag"] == intent:
            return random.choice(item["responses"])

    # Fallback message if no intent matched
    return "🤖 I'm not sure how to answer that. Try asking about sports, leaders, programming, or motivation!"

