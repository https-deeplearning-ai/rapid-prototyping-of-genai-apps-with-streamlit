import streamlit as st
import pandas as pd
import numpy as np

st.title("🧹 Data Preparation and Transformation")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Data Aggregation (grouping and summarizing)
df['x_int'] = df['x'].astype(int)
grouped_data = df.groupby('x_int')['y'].mean().reset_index()
st.write("Aggregated Data (groupby)")
st.dataframe(grouped_data)