import streamlit as st
import pandas as pd
import numpy as np

st.title("🧹 Data Preparation and Transformation")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Data Cleaning (handling missing values)
df.loc[10:15, 'y'] = np.nan # add some NaN for example
df_cleaned = df.dropna()
st.write("Cleaned DataFrame (dropna)")
st.dataframe(df_cleaned)
