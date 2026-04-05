import requests
import streamlit as st


import requests

def get_groq_response(input_text):
    url = "http://127.0.0.1:8000/chain/invoke"

    json_body = {
    "input": {
        "text": input_text,
        "language": "french"
    }
}

    response = requests.post(url, json=json_body)  # ✅ define first

    print(response.json())  # ✅ now safe
    return response.json()
## Streamlit app
st.title("LLM Application Using LCEL")
input_text=st.text_input("Enter the text you want to convert to french")

if input_text:
    st.write(get_groq_response(input_text))