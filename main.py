import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBbK4ySluL9mGV0w0GTL8S_NalKlB0p1Mw")

st.title("Trợ lý học tập AI – Gemini")
user_input = st.text_input("Nhập câu hỏi:")
if user_input:
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(user_input)
    st.write(response.text)
