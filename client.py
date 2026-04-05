
import requests
import streamlit as st

# Function to call LangServe API
def get_groq_response(input_text):
    url = "http://127.0.0.1:8000/chain/invoke"

    payload = {
        "input": {
            "topic": input_text
        }
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        data = response.json()

        # LangServe usually returns output like this
        return data.get("output", "No response received")

    except requests.exceptions.RequestException as e:
        return f"❌ API Error: {e}"


# Streamlit UI
st.set_page_config(page_title="AI Translator", layout="centered")

st.title("🌍 AI French Translator")

input_text = st.text_input("Enter text to translate into French:")

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        with st.spinner("Translating... ⚡"):
            result = get_groq_response(input_text)
            st.success(result)
