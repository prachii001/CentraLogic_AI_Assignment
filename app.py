import streamlit as st
import requests
from io import BytesIO
from transformers import pipeline # type: ignore
from pydub import AudioSegment # type: ignore

# Function to transcribe audio file
def transcribe_audio(file):
    try:
        response = requests.post("http://localhost:8000/transcribe/", files={'file': file})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to summarize text using Hugging Face transformers
def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to convert audio to WAV format
def convert_to_wav(audio_file):
    audio = AudioSegment.from_file(audio_file)
    wav_io = BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)
    return wav_io

# Streamlit app title
st.title("Audio Transcription, Summarization and Timestamps App")

# File uploader for the user to upload an audio file
uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "m4a", "flac"])

if uploaded_file is not None:
    # Convert the uploaded audio file to WAV format
    wav_file = convert_to_wav(uploaded_file)
    
    # Display a loading spinner while the file is being processed
    with st.spinner('Transcribing...'):
        # Transcribe the audio file
        data = transcribe_audio(wav_file)
        
        if data:
            # Get the transcribed text and segments with timestamps
            transcription = data.get("transcription")
            segments = data.get("segments")

            # Display the transcribed text
            st.subheader("Transcription")
            st.write(transcription)

            # Save transcription to a local file
            transcription_file = "transcription.txt"
            with open(transcription_file, "w", encoding="utf-8") as file:
                file.write(transcription)

            st.success(f"Transcription saved as {transcription_file}")

            # Summarize the transcribed text
            summarized_text = summarize_text(transcription)
            
            # Display the summary
            st.subheader("Summary")
            st.write(summarized_text)
            
            # Save summary to a local file
            summary_file = "summary.txt"
            with open(summary_file, "w", encoding="utf-8") as file:
                file.write(summarized_text)
            
            st.success(f"Summary saved as {summary_file}")
            
            # Display the transcribed text with timestamps
            st.subheader("Timestamps")
            for segment in segments:
                start = segment['start']
                end = segment['end']
                text = segment['text']
                st.write(f"[{start:.2f}s - {end:.2f}s]: {text}")
            
            # Save timestamps to a local file
            timestamps_file = "timestamps.txt"
            with open(timestamps_file, "w", encoding="utf-8") as file:
                for segment in segments:
                    start = segment['start']
                    end = segment['end']
                    text = segment['text']
                    file.write(f"[{start:.2f}s - {end:.2f}s]: {text}\n")
            
            st.success(f"Timestamps saved as {timestamps_file}")             

else:
    st.write("Please upload an audio file.")
