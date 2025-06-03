import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("📈 Matplotlib")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)

# Scatter plot
fig, ax = plt.subplots()
ax.scatter(x, y)
st.pyplot(fig)

