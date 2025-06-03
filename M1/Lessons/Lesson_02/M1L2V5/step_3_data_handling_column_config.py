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
st.write("st.dataframe(df) with column_config")
column_config = {
    "y": st.column_config.ProgressColumn(
        "Y Value",
        help="The y value of the data",
        min_value=df['y'].min(),
        max_value=df['y'].max(),
    ),
    "x": st.column_config.NumberColumn(
        "X Value",
        help="X value",
        width="medium"
    )
}
st.dataframe(df, column_config=column_config)