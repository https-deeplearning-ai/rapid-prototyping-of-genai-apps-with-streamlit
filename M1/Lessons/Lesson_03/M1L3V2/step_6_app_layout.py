import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.write("This is column 1")

with col2:
    st.write("This is column 2")