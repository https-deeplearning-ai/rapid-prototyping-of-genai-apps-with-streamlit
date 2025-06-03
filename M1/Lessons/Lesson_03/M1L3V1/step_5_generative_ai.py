import streamlit as st
import openai

openai_api_key = st.secrets["OPENAI_API_KEY"]

st.title("🤖 Gen AI Example")

if not openai_api_key:
    st.error("OPENAI_API_KEY not found in secrets. Please add it.")
else:
    openai.api_key = openai_api_key

    model = st.selectbox("Model:", ["gpt-4o", "gpt-4o-mini"])
    prompt = st.text_input("Prompt:")
    messages = [
        {"role": "assistant", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    if st.button("Submit", type="primary"):
        try:
            client = openai.OpenAI()
            completion = client.chat.completions.create(
                model=model,
                messages=messages,
                max_completion_tokens=150
            )
            st.write(completion.choices[0].message.content)
        except Exception as e:
            st.error(e)
