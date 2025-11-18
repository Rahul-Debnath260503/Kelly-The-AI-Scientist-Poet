import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Kelly – The AI Scientist Poet", layout="centered")

# Title
st.title("🧪 Kelly – The AI Scientist Poet Chatbot")

# API key input
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# User prompt
user_input = st.text_area("Ask Kelly anything:", height=120)

SYSTEM_PROMPT = """
You are Kelly, an AI Scientist Poet.
You respond ONLY in poems.
Your tone is skeptical, analytical, and professional.
Each poem must:
- Question broad claims about AI
- Highlight limitations of AI systems
- Offer practical, evidence-based suggestions
- Maintain the poetic style of Kelly, the great poet.
Do not break character.
"""

if st.button("Generate Response"):
    if not api_key:
        st.error("Please enter your OpenAI API Key.")
    elif not user_input.strip():
        st.error("Please write a question for Kelly.")
    else:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message["content"]
        st.markdown("### ✍️ Kelly's Poetic Analysis:")
        st.write(answer)
