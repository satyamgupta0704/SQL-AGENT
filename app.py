from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
## Define Your Prompt (Improved Version)
prompt=[
    """
    You are an expert in converting English questions to a SQL query.
    The SQL database is named STUDENT and has the columns: NAME, CLASS, SECTION.

    -- RULES --
    1. Your response MUST be ONLY the SQL query.
    2. Do NOT include any explanations, introductions, or conversational text like "Here is the query".
    3. Do NOT wrap the SQL code in markdown backticks like ```sql or ```.

    -- EXAMPLES --
    Question: How many entries of records are present?
    SQL Query: SELECT COUNT(*) FROM STUDENT;

    Question: Tell me all the students studying in Data Science class?
    SQL Query: SELECT * FROM STUDENT WHERE CLASS="Data Science";
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("SQL AGENT To Retrieve Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response_from_gemini = get_gemini_response(question,prompt)

    # Add this print statement to see the raw AI output
    print(f"DEBUG: The AI returned -> '{response_from_gemini}'")

    # Now, send it to the database
    db_response = read_sql_query(response_from_gemini, "student.db")

    st.subheader("The Response is")
    for row in db_response:
        print(row)
        st.header(row)







