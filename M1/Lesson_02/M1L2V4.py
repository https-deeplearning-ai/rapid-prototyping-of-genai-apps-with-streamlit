# import packages
from dotenv import load_dotenv
import os
import openai
import streamlit as st

@st.cache_data
def get_response(user_prompt, temperature):
    response = client.chat.completions.create(
            model="gpt-4o",  # Use the latest chat model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},  # Set behavior
                {"role": "user", "content": user_prompt}  # Use user input as prompt
            ],
            temperature=temperature,  # Use the value from the slider
            max_tokens=100  # Limit response length
        )
    return response


st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# Add a text input box for the user prompt
user_prompt = st.text_input("Enter your prompt:", "Explain generative AI in one sentence.")

# Add a slider for temperature
temperature = st.slider("Select creativity (temperature):", min_value=0.0, max_value=1.0, value=0.7, step=0.05)

# load environment variables from .env file
load_dotenv()

# load OpenAI API key from environment variables
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with st.spinner("AI is working..."):
    if user_prompt:
        response = get_response(user_prompt, temperature)
        # print the response from OpenAI
        st.write(response.choices[0].message.content)
