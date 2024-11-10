import openai
import os
from pathlib import Path
from openai import OpenAI, api_key
from dotenv import load_dotenv

load_dotenv()


class TextToSpeech:
    
    # this function get the input(text) and a prodece a mp3 file with the input(speech), in any language!
    def txt_to_speech():

        api_key = os.getenv("API_KEY")
        # we need to hide the api key
        
        
        client = OpenAI(api_key=api_key)
         

        # file paths
        # we need to make input = from chat input for speakly.py
        speech_file_path = Path(__file__).parent / "speech.mp3"

        with client.audio.speech.with_streaming_response.create(
            model="tts-1",
            voice="alloy",
            input=" Mateus, me bota, me arranha, me joga "
        ) as response:
            # speech_file_path -> .mp3
            response.stream_to_file(speech_file_path)

TextToSpeech.txt_to_speech()        





