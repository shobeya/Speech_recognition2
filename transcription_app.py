import streamlit as st
from tkinter import filedialog
import soundfile as sf
import os
import whisper  # Assuming you're using Whisper for transcription

# Load the Whisper model
model = whisper.load_model("base")

# Function to check and load the audio file
def check_audio_file(audio_file):
    try:
        audio, sample_rate = sf.read(audio_file)
        return audio, sample_rate
    except Exception as e:
        st.error(f"Error loading audio: {e}")
        return None, None

# Function to transcribe the audio
def transcribe_audio(audio_file):
    audio_data, sample_rate = check_audio_file(audio_file)
    if audio_data is None:
        return None
    # Use Whisper to transcribe the audio file
    result = model.transcribe(audio_file)
    return result['text']

# Streamlit UI
st.title("Speech-to-Text Transcription")

st.subheader("Select Audio File")
uploaded_file = st.file_uploader("Choose an audio file (wav/mp3)", type=["wav", "mp3"])

if uploaded_file is not None:
    # Save the uploaded file to a temporary path
    temp_file_path = os.path.join("temp", uploaded_file.name)
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.audio(temp_file_path, format="audio/wav")  # Play the uploaded audio file

    # Transcribe the file and display results
    if st.button("Transcribe"):
        st.info("Transcribing...")
        transcription = transcribe_audio(temp_file_path)
        if transcription:
            st.subheader("Transcription Result")
            st.write(transcription)
