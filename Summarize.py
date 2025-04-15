import streamlit as st

st.set_page_config(page_title="Summarize", layout="centered")

st.title("🧠 Text Summarizer")

text = st.text_area("Enter the text to summarize:")

if st.button("Summarize"):
    summary = text[:100] + "..." if len(text) > 100 else text  # Dummy summary
    st.subheader("Summary:")
    st.write(summary)
