
import openai
import os
from pathlib import Path
from openai import OpenAI, api_key
from dotenv import load_dotenv
import sounddevice as sd
import wave

load_dotenv()


class TextToSpeech:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        openai.api_key = self.api_key
    
    # this function get the input(text) and a prodece a mp3 file with the input(speech), in any language!
    def txt_to_speech(self, input_text):
         
        # file paths
        # we need to make input = from chat input for speakly.py
        speech_file_path = Path(__file__).parent / "speech.mp3"

        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="alloy",
            input= input_text
        ) as response:
            # speech_file_path -> .mp3
            response.stream_to_file(speech_file_path)
  
    def record_audio(self, duration = 5, filename = 'user_speech.wav'):

        frequency = 44100

        audio_data = sd.rec(int(duration * frequency), rate = frequency, channels = 2)
        sd.wait()

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(frequency)
            wf.writeframes(audio_data.tobytes())
        
        return filename
    
    def speech_to_text(self, audio_file_path):
        with open(audio_file_path, "rb") as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        
        transcribed_text = response.get("text", "")
        return transcribed_text
    

            
            
tts = TextToSpeech()
chatout = "bruh"
tts.txt_to_speech(chatout)
audio_file = tts.record_audio(duration=5) 
transcribed_text = tts.speech_to_txt(audio_file)






