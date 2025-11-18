import streamlit as st
from groq import Groq

st.set_page_config(page_title="Kelly – The AI Scientist Poet", layout="centered")

# Title
st.title("🧪 Kelly – The AI Scientist Poet Chatbot")

# API key input
api_key = st.text_input("Enter your Groq API Key", type="password")

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
        st.error("Please enter your Groq API Key.")
    elif not user_input.strip():
        st.error("Please write a question for Kelly.")
    else:
        try:
            client = Groq(api_key=api_key)
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Fast and capable Groq model
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.7,
                max_tokens=1024
            )
            
            answer = response.choices[0].message.content
            
            st.markdown("### ✍️ Kelly's Poetic Analysis:")
            st.write(answer)
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.info("Make sure your Groq API key is valid. Get one free at: https://console.groq.com")
