import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Step 1: Get your API key
api_key = os.getenv("OPENAI_API_KEY")

# Step 2: Initialize the OpenAI client
client = OpenAI(api_key=api_key)

# Step 3: Ask GPT function
def ask_gpt(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo"
    )
    return chat_completion.choices[0].message.content

# Step 4: Main chat loop
def main():
    print("🤖 AI Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = ask_gpt(user_input)
        print("Bot:", response)

# Step 5: Run chatbot
if __name__ == "__main__":
    main()