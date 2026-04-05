import requests
import streamlit as st


import requests


def get_groq_response(input_text: str) -> str:
    groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
    if not groq_api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it to .env or Streamlit secrets under GROQ_API_KEY."
        )

    model = ChatGroq(model="llama-3.3-70b-versatile", api_key=groq_api_key)
    system_template = "Translate the following into {language}:"
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_template),
        ("user", "{text}")
    ])
    parser = StrOutputParser()
    chain = prompt_template | model | parser

    return chain.invoke({"text": input_text, "language": "french"})


st.title("LLM Application Using LCEL")
input_text = st.text_input("Enter the text you want to convert to French")

if input_text:
    try:
        result = get_groq_response(input_text)
        st.write(result)
    except Exception as exc:
        st.error(f"Error: {exc}")
