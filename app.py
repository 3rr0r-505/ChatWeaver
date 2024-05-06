import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro-latest')

# Initialize Flask app
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    # Get user message from request
    user_message = request.form["msg"]
    return get_chat_response(user_message)

# Function to generate chatbot response
def get_chat_response(question):
    # Send user message to the model and receive response
    response = model.generate_content(question)
    # Return the response
    return response.text

# Main entry point of the application
if __name__ == '__main__':
    # Run the Flask app
    app.run()
