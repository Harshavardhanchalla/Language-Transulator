import streamlit as st
from googletrans import Translator, LANGUAGES
import pyttsx3

# Set page title and configuration
st.set_page_config(
    page_title="Language Converter",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 2.5em;
        color: #1f77b4;
        text-align: center;
        padding: 20px;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #333;
        text-align: center;
        margin-bottom: 40px;
    }
    .text-area {
        margin-bottom: 20px;
    }
    .selectbox {
        margin-bottom: 20px;
    }
    .translate-button {
        background-color: #1f77b4;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1em;
    }
    .translate-button:hover {
        background-color: #005999;
    }
    .audio-container {
        text-align: center;
        margin-top: 30px;
    }
    .result {
        font-size: 1.2em;
        color: #4CAF50;
        margin-top: 20px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Render title and subtitle
st.markdown('<div class="title">Language Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Easily translate text into your preferred language</div>', unsafe_allow_html=True)

# Initialize the translator
translator = Translator()

# Text input for the text to be translated
text_to_translate = st.text_area("Enter text here to translate", "", height=200)
st.markdown('<div class="text-area"></div>', unsafe_allow_html=True)

# Dropdowns for selecting source and target languages
col1, col2 = st.columns(2)
with col1:
    source_language = st.selectbox("Select source language", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index('en'))
with col2:
    target_language = st.selectbox("Select target language", list(LANGUAGES.values()), index=list(LANGUAGES.keys()).index("es"))

# Language codes
source_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(source_language)]
target_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(target_language)]

# Translate button
if st.button("Translate"):
    if text_to_translate:
        translation = translator.translate(text_to_translate, src=source_language_code, dest=target_language_code).text

        # Display the translated text
        st.write(f"**Your Translated text:** {translation}")

        # Text-to-Speech functionality
        try:
            engine = pyttsx3.init()
            engine.say(translation)
            engine.runAndWait()
        except Exception as e:
            st.error(f"Text-to-Speech error: {e}")

    else:
        st.error("Please enter some text to translate.")

# Add footer or additional instructions
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <p>Enter text in the text area above, select the source and target languages, and click 'Translate' to see the translation.</p>
    </div>
    """,
    unsafe_allow_html=True
)
