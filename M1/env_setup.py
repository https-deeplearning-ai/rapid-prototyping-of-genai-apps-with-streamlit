''' 

From your command line, you can set up a Python virtual environment for your project using the following steps:
# 1. Open the VSCode terminal (View > Terminal).

# 2. Run the following command to create a virtual environment:
python -m venv venv

# 3. Activate the virtual environment:
# On Windows:
'venv\Scripts\activate'

# On macOS/Linux:
source venv/bin/activate

# 4. VSCode should detect and use the virtual environment automatically.

# 5. Install the required packages:
pip install -r requirements.txt 
'''


# import packages
from dotenv import load_dotenv
import os
import openai

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
print(response.choices[0].message.content)
