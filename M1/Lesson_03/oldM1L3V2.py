import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load data from CSV
df = pd.read_csv("data/customer_reviews.csv")
st.write("Here's your data:")
st.write(df.head())

# Clean and transform the data
df.dropna(inplace=True)
df["SUMMARY"] = df["SUMMARY"].astype(str)
df["PRODUCT"] = df["PRODUCT"].str.strip().str.title()

# Group and summarize data
summary = df.groupby("PRODUCT").size()
st.write("Product summary:")
st.write(summary)

# Define sentiment analysis function with caching
@st.cache_data
def get_sentiment(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"What's the sentiment of this review? {text}"}]
    )
    return response.choices[0].message.content

# Apply sentiment analysis to each review
# Note: Keep your dataset small (10-15 rows) for testing
df["Sentiment"] = df["SUMMARY"].apply(get_sentiment)

# Display the results
st.write("Data with sentiment analysis:")
st.write(df)
