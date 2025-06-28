# import packages
from dotenv import load_dotenv
import os
import openai
import streamlit as st

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# load environment variables from .env file
load_dotenv()

# load OpenAI API key from environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
response = client.chat.completions.create(
    model="gpt-3.5-turbo",  # Use the latest chat model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # Set behavior
        {"role": "user", "content": "Explain generative AI in one sentence."}  # Prompt
    ],
    temperature=0.7,  # A bit of creativity
    max_tokens=100  # Limit response length
)

# print the response from OpenAI
st.write(response.choices[0].message.content)