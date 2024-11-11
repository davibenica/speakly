from logging import config
from re import A
from urllib import response
import openai
import os
from pathlib import Path
from openai import OpenAI, api_key, audio
from dotenv import load_dotenv
import sounddevice as sd
import wave
from google.cloud import speech

load_dotenv()


class TextToSpeech:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.speech_key = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        openai.api_key = self.api_key

    
    # this function get the input(text) and a prodece a mp3 file with the input(speech), in any language!
    def txt_to_speech(self, input_text):
         
        # file paths
        # we need to make input = from chat input for speakly.py
        speech_file_path = Path(__file__).parent / "speech.mp3"
        client = OpenAI(api_key=api_key)
        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="alloy",
            input= input_text
        ) as response:
            # speech_file_path -> .mp3
            response.stream_to_file(speech_file_path)
    
    def record_audio(self):
        speech_client = speech.SpeechClient()
        print("Google Cloud Speech Client initialized successfully!")
        print("bruh")
       
    
    def speech_to_text(self, audio_file_path):
        print("speeching to texting... ")
        speech_client = speech.SpeechClient()

        with open(audio_file_path, "rb") as audio_file:
            data = audio_file.read()
        
        audio = speech.RecognitionAudio(content=data)
        
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=48000,
            language_code="en-US"
        )

        response = speech_client.recognize(config=config,audio=audio)

        for result in response.results:
            print("Wrds",result.alternatives[0].transcript)

        print("bruh")
        

tts = TextToSpeech()

tts.record_audio()
tts.speech_to_text("/Users/maycolmeza/Desktop/Uhack/20241110 024231.wav")
#audio_file = tts.record_audio(duration=5) 
#transcribed_text = tts.speech_to_text(audio_file)       





