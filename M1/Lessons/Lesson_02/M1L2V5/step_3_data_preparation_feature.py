import streamlit as st
import pandas as pd
import numpy as np

st.title("🧹 Data Preparation and Transformation")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Feature Engineering (creating new features)
df['y_squared'] = df['y']**2
st.write("Feature Engineered DataFrame (y_squared)")
st.dataframe(df)
