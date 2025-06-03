import streamlit as st
import plotly.express as px
import numpy as np

st.title("📈 Plotly")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)

# Scatter plot
fig = px.scatter(x=x, y=y)
st.plotly_chart(fig)
