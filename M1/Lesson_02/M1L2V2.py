# import packages
from dotenv import load_dotenv
import os
import openai


# load environment variables from .env file
load_dotenv()

# load OpenAI API key from environment variables
client = openai.OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",  # Use the latest chat model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},  # Set behavior
        {"role": "user", "content": "Explain generative AI in one sentence."}  # Prompt
    ],
    temperature=0.7,  # A bit of creativity
    max_tokens=100  # Limit response length
)

# print the response from OpenAI
print(response.choices[0].message.content)
