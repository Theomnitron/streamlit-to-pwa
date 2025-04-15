import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="Speak", layout="centered")

st.title("🔊 Text-to-Speech")

text = st.text_input("Enter text to convert to speech:")

if st.button("Speak"):
    if text.strip():
        tts = gTTS(text)
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        st.audio(mp3_fp, format="audio/mp3")
    else:
        st.warning("Please enter some text.")
