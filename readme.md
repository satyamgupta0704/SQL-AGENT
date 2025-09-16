Natural Language to SQL Query Agent with Gemini
This project is a web-based application that leverages Google's Gemini AI to convert plain English questions into executable SQL queries. It allows non-technical users to interact with a database using natural language, removing the need to write complex SQL code.

Features
Natural Language Processing: Translates English questions into SQL queries.

Interactive Web UI: A simple and user-friendly interface built with Streamlit.

AI-Powered: Utilizes the powerful gemini-1.5-flash model from Google for accurate query generation.

Database Integration: Connects to a local SQLite database to fetch and display live data.

Secure API Key Handling: Uses a .env file to securely manage your Google API key.

Technology Stack
Language: Python 3.9+

AI Model: Google Gemini (google-generativeai)

Web Framework: Streamlit

Database: SQLite3

Environment Management: python-dotenv

Setup and Installation
Follow these steps to set up and run the project on your local machine.

1. Clone the Repository
Bash

git clone <your-repository-url>
cd sql-agent-project
2. Create a Python Virtual Environment
It's highly recommended to use a virtual environment to isolate project dependencies.

Bash

# Create the environment
python -m venv venv

# Activate the environment
# On macOS / Linux:
source venv/bin/activate

# On Windows:
.\venv\Scripts\activate
3. Install Dependencies
Create a requirements.txt file with the following content:

requirements.txt:

Plaintext

streamlit
google-generativeai
python-dotenv
Now, install these packages using pip:

Bash

pip install -r requirements.txt
Configuration
1. Set Up Your Google API Key
You need a Google API key to use the Gemini model.

Create a file named .env in the root of your project directory.

Add your API key to this file as shown below:

.env:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
2. Create the Sample Database
The application is designed to query a sample SQLite database named student.db. To create this database with some sample data, run the following command in your terminal:

Bash

python -c "import sqlite3; conn = sqlite3.connect('student.db'); cur = conn.cursor(); cur.execute('CREATE TABLE STUDENT(NAME TEXT, CLASS TEXT, SECTION TEXT)'); cur.execute('INSERT INTO STUDENT VALUES (\"Ankit\", \"Data Science\", \"A\"), (\"Rohan\", \"Data Science\", \"B\"), (\"Priya\", \"Web Development\", \"A\"), (\"Shivangi\", \"Machine Learning\", \"B\")'); conn.commit(); conn.close(); print('student.db created successfully.')"
This command will create the student.db file in your project directory.

Usage
Once you have completed the setup and configuration, you can run the application.

Make sure your virtual environment is activated.

Run the following command in your terminal:

Bash

streamlit run app.py
Streamlit will start the server and open the application in a new tab in your web browser.

Project Structure
sql-agent-project/
├── venv/
├── .env                  # Stores your API key (not committed to Git)
├── app.py                # The main Streamlit application script
├── requirements.txt      # List of Python dependencies
└── student.db            # The SQLite database file