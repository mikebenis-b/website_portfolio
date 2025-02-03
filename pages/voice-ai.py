import streamlit as st
import requests
import io
import sounddevice as sd
import numpy as np
import pydub
from pydub import AudioSegment
import soundfile as sf
# print(sf.__version__)
st.set_page_config(page_title="chat_bot", page_icon=":material/smart_toy:")
# Set up Streamlit app
st.title("talk like Cristiano Ronaldo")

# User input
user_text = st.text_input("Enter text to be spoken:", "Siiuuu! I am Cristiano Ronaldo.")
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"
# C:\ffmpeg\ffmpeg-2025-01-30-git-1911a6ec26-full_build\bin
API_KEY = "sk_5da397f51751dbb6148d8ae0f815e444589ccc3e45af3794"  # REPLACE THIS with a new, safe API key.
VOICE_ID = "rnIy5eYNlSQXFinIc1sP"  # Example voice (Modify if needed)
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": user_text,
    "model_id": "eleven_monolingual_v1"
}

# Button to generate audio
if st.button("Generate Voice"):
    with st.spinner("Generating audio..."):
        response = requests.post(URL, json=data, headers=headers)

        if response.status_code == 200:
            # Convert MP3 response to WAV format using pydub
            audio_mp3 = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
            audio_wav = np.array(audio_mp3.get_array_of_samples())  # Convert to NumPy array
            sample_rate = audio_mp3.frame_rate  # Get sample rate

            # Play the audio
            sd.play(audio_wav, samplerate=sample_rate)
            sd.wait()  # Wait until audio finishes playing
            st.success("Audio played successfully!")
        else:
            st.error(f"Error: {response.json()}")
print("Streamlit ==", st.__version__)
print("Requests ==", requests.__version__)
print("SoundDevice ==", sd.__version__)
print("NumPy ==", np.__version__)
