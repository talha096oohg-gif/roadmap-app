import streamlit as st
from groq import Groq
import os

try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = os.environ.get("GROQ_API_KEY", "")

if not api_key:
    st.error("Add GROQ_API_KEY in Streamlit Secrets!")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(page_title="AI Roadmap Generator", layout="centered")
st.title("🚀 AI Learning Roadmap Generator")

topic = st.text_input("What do you want to learn?", "data science")
level = st.selectbox("Your skill level", ["Beginner", "Intermediate", "Advanced"])
duration = st.selectbox("How much time?", ["4 weeks", "8 weeks", "12 weeks"])

if st.button("Generate Roadmap"):
    with st.spinner("Generating..."):
        try:
            completion = client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=[{"role": "user", "content": f"Create a detailed {duration} learning roadmap for {topic} at {level} level. Include weekly breakdown, projects, and resources."}]
            )
            st.success("Roadmap Generated!")
            st.markdown(completion.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
