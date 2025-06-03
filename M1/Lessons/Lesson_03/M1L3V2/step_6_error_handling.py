import streamlit as st

try:
    number = st.slider("Select a number:", 0, 10, 5)
    result = 10 / number
    st.write(f"Result: {result}")
except ZeroDivisionError:
    st.error("Division by zero is not allowed!")