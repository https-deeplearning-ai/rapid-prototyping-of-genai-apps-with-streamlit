# Import the Streamlit library
import streamlit as st

# Set the page layout to wide
st.set_page_config(layout="wide")
# Set the title of the app
st.title("🔤 Fundamentals")

# Display text
st.write("Hello, Streamlit!")
# Display a list
st.write([1, 2, 3, 4])

# Add a title to the sidebar
st.sidebar.title("My Sidebar")
# Write to the sidebar
with st.sidebar:
    st.write("This is the sidebar.")

# Create two columns
col1, col2 = st.columns(2)

# Content for the first column
with col1:
    # Write to the first column
    st.write("This is the first column.")
    # Add a subheading in the first column
    st.header("A subheading")

# Content for the second column
with col2:
    # Write to the second column
    st.write("This is the second column.")