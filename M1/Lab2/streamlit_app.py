import streamlit as st
import pandas as pd

# app title
st.title("🏔️ Avalanche Data Set")

# read in and display dataframe
df = pd.read_csv("data/customer_reviews.csv")
df.head()

# Drop-down widget
unique_products = sorted(df.PRODUCT.unique())
selected_products = st.multiselect('Select product(s)', unique_products, unique_products)
st.write('Selected products:', list(selected_products))
df[df.PRODUCT.isin(selected_products)]

# Calendar widget
st.subheader('Dates')

df['DATE'] = pd.to_datetime(df['DATE'])

d = st.date_input(
    "Select dates",
    (df['DATE'].min().date(), df['DATE'].median().date() ),
    df['DATE'].min().date(),
    df['DATE'].max().date(),
)