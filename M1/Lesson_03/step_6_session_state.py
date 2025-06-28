import streamlit as st

# Initialization
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
    # st.session_state.key = 'value'

# Update an item in Session State by assigning it a value
st.session_state['key'] = 'value2'  # Dictionary like API
# st.session_state.key = 'value2'   # Attribute API

# Display session state value
st.write(st.session_state.key)
