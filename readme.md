<h1 align="center">
🤖 Natural Language to SQL Agent with Gemini
</h1>

<p align="center">
<img alt="Python" src="https://img.shields.io/badge/Python-3.9%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-1.30-orange.svg?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img alt="Google" src="https://img.shields.io/badge/Google-Gemini_AI-4285F4.svg?style=for-the-badge&logo=google&logoColor=white"/>
<img alt="License" src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge"/>
</p>

<p align="center">
A web-based application that leverages Google's Gemini AI to convert plain English questions into executable SQL queries, allowing users to interact with a database using natural language.
</p>

<p align="center">

</p>

🚀 Features
Natural Language to SQL: Translates English questions into accurate SQL queries.

Interactive Web UI: Simple and user-friendly interface built with Streamlit.

AI-Powered: Utilizes the powerful gemini-1.5-flash model from Google for query generation.

Live Database Interaction: Connects to a local SQLite database to fetch and display data in real-time.

Secure API Key Handling: Safely manages your Google API key using a .env file.

⚙️ How It Works
The application follows a simple yet powerful workflow:

User Input: The user enters an English question into the web interface.

AI Translation: The question is sent to the Gemini AI model with a carefully engineered prompt.

SQL Generation: Gemini translates the question into a precise SQL query.

Database Execution: The generated query is executed against the connected SQLite database.

Display Results: The query results are fetched and displayed back to the user on the dashboard.

🛠️ Technology Stack
Backend: Python 3.9+

AI Model: Google Gemini (google-generativeai)

Web Framework: Streamlit

Database: SQLite3

Environment Management: python-dotenv

📦 Setup and Installation
Follow these steps to get the project running on your local machine.

1. Clone the Repository
Bash

git clone <your-repository-url>
cd sql-agent-project
2. Create and Activate a Virtual Environment
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

Plaintext

streamlit
google-generativeai
python-dotenv
Now, install these packages using pip:

Bash

pip install -r requirements.txt
🔧 Configuration
1. Set Up Your Google API Key
You'll need a Google API key to use the Gemini model.

Create a file named .env in the root of your project directory.

Add your API key to this file as shown below:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
2. Create the Sample Database
The application is designed to query a sample SQLite database. To create the student.db with some sample data, run the following command in your terminal:

Python

python -c "import sqlite3; conn = sqlite3.connect('student.db'); cur = conn.cursor(); cur.execute('CREATE TABLE STUDENT(NAME TEXT, CLASS TEXT, SECTION TEXT)'); cur.execute('INSERT INTO STUDENT VALUES (\"Ankit\", \"Data Science\", \"A\"), (\"Rohan\", \"Data Science\", \"B\"), (\"Priya\", \"Web Development\", \"A\"), (\"Shivangi\", \"Machine Learning\", \"B\")'); conn.commit(); conn.close(); print('✅ student.db created successfully.')"
▶️ Usage
Once the setup and configuration are complete, you can run the application.

Make sure your virtual environment is activated.

Run the following command in your terminal:

Bash

streamlit run app.py
Streamlit will start the server and open the application in a new tab in your web browser.

📁 Project Structure
sql-agent-project/
├── venv/
├── .env                  # Stores your API key (not committed to Git)
├── app.py                # The main Streamlit application script
├── requirements.txt      # List of Python dependencies
└── student.db            # The SQLite database file
