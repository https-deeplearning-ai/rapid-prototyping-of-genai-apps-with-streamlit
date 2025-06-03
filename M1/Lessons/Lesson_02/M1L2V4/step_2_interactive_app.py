import streamlit as st

st.title("🕹️  Interactive Widgets")

# Initialize session state for the slider value
if 'x' not in st.session_state:
    st.session_state.x = 0

# Function to reset the slider value
def reset_slider():
    st.session_state.x = 0

# Use a slider widget to capture a numeric value
st.slider("Select a value:", 0, 100, key="x")

st.write(f"You selected `{st.session_state.x}`")

# Conditional coloring logic based on user input
if st.session_state.x > 50:
    st.success(f"You selected a value greater than 50!")
else:
    st.error(f"You selected a value less than or equal to 50!")

# Reset button
st.button("Reset Slider", on_click=reset_slider)