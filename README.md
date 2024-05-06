# ChatWeaver <br><a href="https://www.python.org/"><img alt="" src="https://img.shields.io/badge/python-3.9%2B-blue?logo=python&logoColor=88d4d7"/></a> <a href="https://nodejs.org/en"><img alt="" src="https://img.shields.io/badge/Node.js-v16.4.0-339933?logo=node.js"/></a> <a href="https://www.mongodb.com/"><img alt="" src="https://img.shields.io/badge/MongoDB%20Atlas-v4.4.6-009441?logo=mongodb&logoColor=009441"/></a> <a href="https://www.microsoft.com/en-us/windows?r=1"><img alt="" src="https://img.shields.io/badge/OS-Windows-brighten?logo=windows&logoColor=blue&label=OS&labelColor=grey&color=blue"/></a>

This is a simple chatbot application built using Python, Flask, and the Gemini API.

## Overview
This chatbot allows users to interact with it through a web interface. It leverages the Gemini API to provide responses to user queries. The backend is implemented in Python using the Flask framework.

## Prerequisites
Before running this application, make sure you have the following installed:
- Python (version >= 3.6)
- Flask
- Python-dotenv (to interact with the Gemini API)
You can install Flask and Requests using pip:
`pip install flask python-dotenv`


## Usage
1. Clone this repository:
`git clone https://github.com/3rr0r-505/ChatWeaver.git`
2. Navigate to the project directory:
cd `ChatWeaver`
3. Run the Flask application:
python `app.py`
4. Once the application is running, open your web browser and go to `http://localhost:5000` to access the chatbot interface.

## Configuration
Before running the application, you need to configure the Gemini API credentials. Open the `.env` file and replace `'YOUR_API_KEY'` with your actual Gemini API key.

## Contributing
Contributions are welcome! If you have any suggestions or find any issues, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
