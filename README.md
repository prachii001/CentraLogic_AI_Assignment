# Audio Transcription and Summarization App
This project provides a web-based application for transcribing and summarizing audio files. It utilizes advanced machine learning models to convert speech to text and generate concise summaries of the transcriptions. The application is built using FastAPI for the backend and Streamlit for the front end.

# Features
- Audio Transcription: Converts audio files into text using the Whisper model.
- Text Summarization: Generates a concise summary of the transcribed text using the BART model from the Hugging Face transformers library.
- Timestamps: Provides timestamps for each segment of the transcribed text.
- Automatic File Saving: Automatically saves the transcription and summary as text files on the user's local machine.
- User-Friendly Interface: Easy-to-use interface for uploading audio files and viewing results.

# Technologies Used
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Streamlit: An open-source app framework for Machine Learning and Data Science projects.
- Whisper: A powerful speech recognition model.
- Hugging Face Transformers: A library of state-of-the-art pre-trained models for Natural Language Processing tasks.

# Running the Application
1. Start the FastAPI backend:
<pre>
```
python backend.py
  
```
</pre>

