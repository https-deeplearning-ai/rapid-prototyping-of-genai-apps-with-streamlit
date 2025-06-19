# import packages
from dotenv import load_dotenv
import os
import openai
import streamlit as st

# load environment variables from .env file
load_dotenv()

# load OpenAI API key from environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Display app title
st.title("Hello, GenAI!")

# Add a prompt for user input
user_input = st.text_input("How can I help you today?")

# check for user input
if user_input:
    st.write(f"You asked: {user_input}")

    # display a spinner while waiting for the response
    with st.spinner("Contacting the model..."):
        response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the latest chat model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},  # Set behavior
            {"role": "user", "content": "Explain generative AI in one sentence."}  # Prompt
        ],
        temperature=0.7,  # A bit of creativity
        max_tokens=100  # Limit response length
     )

        # display the response in the Streamlit app
        st.success("Done!")

        # display the response in the Streamlit app
        st.write("Response:")
        st.write(response.choices[0].message.content)
