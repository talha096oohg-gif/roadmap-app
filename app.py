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

st.set_page_config(page_title="AI Roadmap Generator", page_icon="🚀")
st.title("🚀 AI Learning Roadmap Generator")

field = st.text_input("What do you want to learn?", "data science")
level = st.selectbox("Your skill level", ["Beginner", "Intermediate", "Advanced"])
time_input = st.selectbox("How much time?", ["8 weeks", "1 week", "1 month", "3 months"])

if st.button("Generate Roadmap"):
    prompt = f"Create detailed roadmap for {field}, level {level}, time {time_input}. Give Week, Core Topics, Order, Practice Exercise, Resources."
    with st.spinner("Generating roadmap..."):
        try:
            r = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.3-70b-versatile","
            
            st.success("Roadmap generated!")
            st.markdown(r.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
