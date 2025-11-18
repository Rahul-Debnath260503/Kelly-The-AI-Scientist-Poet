import streamlit as st
from groq import Groq

st.set_page_config(page_title="Kelly – The AI Scientist Poet", layout="centered")

st.title("🧪 Kelly – The AI Scientist Poet (Groq)")

# Groq API key field
api_key = st.text_input("Enter your Groq API Key", type="password")

user_input = st.text_area("Ask Kelly anything:", height=120)

SYSTEM_PROMPT = """
You are Kelly, an AI Scientist Poet.
You respond ONLY in poems.
Tone: skeptical, analytical, and professional.
Each poem must:
- Question broad claims about AI
- Highlight limitations of AI systems
- Provide practical, evidence-based suggestions
- Maintain the poetic style of Kelly, the great poet.
Do not break character.
"""

if st.button("Generate Response"):
    if not api_key:
        st.error("Please enter a Groq API key.")
    elif not user_input.strip():
        st.error("Please type a question for Kelly.")
    else:
        client = Groq(api_key=api_key)

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]
        )

        answer = completion.choices[0].message["content"]

        st.markdown("### ✍️ Kelly's Poetic Analysis:")
        st.write(answer)
