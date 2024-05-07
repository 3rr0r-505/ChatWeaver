import os
import markdown
import webbrowser
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

# MongoDB connection
MONGODB_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGODB_URI)
db = client.get_default_database()
chats_collection = db.get_collection('chats')

# Your existing code
import google.generativeai as genai
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.0-pro-latest')

app = Flask(__name__)

@app.route("/")
def index():
    # Load previous chats from MongoDB
    previous_chats = list(chats_collection.find())
    
    # Convert bot responses to markdown format
    for chat in previous_chats:
        chat['bot_response'] = markdown.markdown(chat['bot_response'])
    
    return render_template('chat.html', previous_chats=previous_chats)


@app.route("/get", methods=["POST"])
def chat():
    user_message = request.form["msg"]
    bot_response_markdown , raw_response = get_chat_response(user_message)  # Get the markdown-formatted response
    
    # print(bot_response_markdown)
    # Save the chat to MongoDB with markdown-formatted response
    chats_collection.insert_one({"user_message": user_message, "bot_response": raw_response})
    
    return bot_response_markdown

def get_chat_response(question):
    response = model.generate_content(question)

    markdown_response = markdown.markdown(response.text)
    return markdown_response, response.text


if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8000')
    app.run(host='127.0.0.1', port=8000)
