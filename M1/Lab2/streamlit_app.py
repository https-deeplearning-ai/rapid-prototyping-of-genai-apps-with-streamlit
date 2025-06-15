import streamlit as st
import pandas as pd

# app title
st.title("🏔️ Avalanche Data Set")

# read in and display dataframe
df = pd.read_csv("data/customer_reviews.csv")
df.head()

# Drop-down widget


# Calendar widget
