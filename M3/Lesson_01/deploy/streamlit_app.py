import streamlit as st
from snowflake.snowpark.context import get_active_session
import pandas as pd
import matplotlib.pyplot as plt

# Initialize the Streamlit app
st.title("Avalanche Streamlit App")

# Get data from Snowflake
session = get_active_session()
query = """
SELECT
    *,
    SNOWFLAKE.CORTEX.SENTIMENT(REVIEW_TEXT) as SENTIMENT_SCORE
FROM
    CLEAN_REVIEWS
"""
df_reviews = session.sql(query).to_pandas()

# Convert date columns to datetime
df_reviews['REVIEW_DATE'] = pd.to_datetime(df_reviews['REVIEW_DATE'])
df_reviews['SHIPPING_DATE'] = pd.to_datetime(df_reviews['SHIPPING_DATE'])

# Visualization: Average Sentiment by Product
st.subheader("Average Sentiment by Product")
product_sentiment = df_reviews.groupby("PRODUCT")["SENTIMENT_SCORE"].mean().sort_values()

fig, ax = plt.subplots()
product_sentiment.plot(kind="barh", ax=ax, title="Average Sentiment by Product")
ax.set_xlabel("Sentiment Score")
plt.tight_layout()
st.pyplot(fig)

# Product filter on the main page
st.subheader("Filter by Product")
products = df_reviews['PRODUCT'].unique()
selected_products = st.multiselect(
    "Select Products to View:",
    options=products,
    default=products  # Default to showing all products
)

# Filter data based on selected products
filtered_data = df_reviews[df_reviews['PRODUCT'].isin(selected_products)]

# Display the filtered data as a table
st.subheader("Filtered Data Table")
st.dataframe(filtered_data)

# Visualization: Sentiment Distribution for Selected Products
st.subheader("Sentiment Distribution for Selected Products")
fig, ax = plt.subplots()
filtered_data['SENTIMENT_SCORE'].hist(ax=ax, bins=20)
ax.set_title("Distribution of Sentiment Scores")
ax.set_xlabel("Sentiment Score")
ax.set_ylabel("Frequency")
st.pyplot(fig)