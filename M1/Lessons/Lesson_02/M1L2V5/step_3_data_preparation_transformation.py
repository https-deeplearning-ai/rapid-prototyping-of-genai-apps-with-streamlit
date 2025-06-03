import streamlit as st
import pandas as pd
import numpy as np

st.title("🧹 Data Preparation and Transformation")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Data Transformation (converting data types, scaling)
df['y'] = df['y'].astype(float)
df['y_scaled'] = (df['y'] - df['y'].min()) / (df['y'].max() - df['y'].min())
st.write("Transformed DataFrame (astype, scaling)")
st.dataframe(df)
