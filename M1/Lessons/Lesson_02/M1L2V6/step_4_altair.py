import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.title("📈 Altair")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Scatter plot
chart = alt.Chart(df).mark_circle().encode(
    x='x',
    y='y'
)
st.altair_chart(chart, use_container_width=True)