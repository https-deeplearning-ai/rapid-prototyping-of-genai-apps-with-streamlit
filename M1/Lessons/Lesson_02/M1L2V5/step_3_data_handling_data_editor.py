import streamlit as st
import pandas as pd
import numpy as np

st.title("𝌏 Data Loading and Display")

# Sample data
np.random.seed(42)
x = np.arange(0, 10, 0.1)
y = 2 * x + np.random.rand(100)
df = pd.DataFrame({'x': x, 'y': y})

# Display data using different Streamlit methods
st.write("st.data_editor(df)")
edited_df = st.data_editor(df)