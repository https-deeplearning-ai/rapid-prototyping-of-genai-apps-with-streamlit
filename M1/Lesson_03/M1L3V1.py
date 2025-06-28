import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 AI Code Generator")
st.write("Ask AI to write a Python function, then use it!")

user_request = st.text_input("What function do you want?", 
                           placeholder="Create a function to clean text")

if st.button("Generate Code") and user_request:
    # Show a spinner while AI is thinking
    with st.spinner("AI is writing code..."):
        # Send the request to OpenAI and ask for Python code
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Write a Python function for: {user_request}. Return only the code, no explanation."}
            ],
            temperature=0.3,  # Keep responses focused, not too creative
            max_tokens=300    # Limit the length of the response
        )
    
    # Extract the code from AI's response
    st.session_state.generated_code = response.choices[0].message.content
    
    st.code(st.session_state.generated_code, language="python")
    

if st.button("Run This Code"):
    st.write("Running the AI-generated code...")
    try:
        # Execute the AI's code and make it available in our app
        exec(st.session_state.generated_code, globals())
        st.success("✅ Code executed! Function is now available.")
        
        if "clean_text" in st.session_state.generated_code:
            test_input = st.text_input("Test your function:", "Hello, World! 123")
            if test_input:
                try:
                    # Call the function AI just created for us
                    result = clean_text(test_input)
                    st.write(f"Result: {result}")
                except:
                    st.write("Function created but needs different input")
                    
    except Exception as e:
        st.error(f"Error: {e}")

st.write("**Example:** Try 'Create a function to clean text'")

