import streamlit as st
import pandas as pd

@st.cache_data
def read_data(url):
    # Read data with pandas
    return pd.read_csv(url)

# First call with URL_1: function executes
d1 = read_data("https://data.example.com/customer_reviews.csv")

# Second call with same URL: returns cached result
d2 = read_data("https://data.example.com/customer_reviews.csv")  # d1 and d2 are identical

# Call with different URL: function executes again
d3 = read_data("https://data.example.com/shipping_log.csv")