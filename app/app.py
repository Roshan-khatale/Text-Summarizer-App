import streamlit as st
from scripts.summarize import summarize

st.title("Text Summarizer App")
text = st.text_area("Enter your text below:")
if st.button("Summarize"):
    result = summarize(text)
    st.write("### Summary")
    st.success(result)