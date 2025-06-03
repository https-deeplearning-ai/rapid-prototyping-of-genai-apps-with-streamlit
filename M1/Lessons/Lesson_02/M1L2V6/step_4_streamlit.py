import streamlit as st
import numpy as np
import pandas as pd

st.title("📈 Streamlit Native Chart")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Use Streamlit's built-in scatter plot function
st.scatter_chart(data=df, x='x', y='y')