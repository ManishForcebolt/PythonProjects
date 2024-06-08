"""File to create a voice"""
import speech_recognition as sr
import pyaudio
import pyttsx3
from gtts import gTTS
import os
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

# Calling Mistral from Ollama
ai_llm = Ollama(
    model="mistral",
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

# _____________________________Taking input from Mic _____________________

# Initialize the recognizer
recognizer = sr.Recognizer()


def listen_and_transcribe():
    """
To listen and transcribe
    :return:
    """
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = recognizer.listen(source)

    # Recognize speech using Google Web Speech API
    try:
        transcribed_text = recognizer.recognize_google(audio)
        print(f"You said: {transcribed_text}")
        return transcribed_text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")


# Capture and transcribe audio
transcribed_audio = listen_and_transcribe()
# print(transcribed_audio)

# generating output from the LLM

text = ai_llm(f"You are a home owner with name Jon, want to sell your home. Give reply for"
              f"the following \n"
              f" \n{transcribed_audio}")

print("\nLLM has generated a reply")


# Function to speak input text from LLM

# Initialize the TTS engine
converter = pyttsx3.init()
print("Engine Start")

# Set properties (optional, can be customized)
converter.setProperty('rate', 150)  # Speed of speech
converter.setProperty('volume', 0.7)  # Volume of the speech
converter.setProperty('voice', 'voices[1].id')
print("Engine Set")

def speak(input_text):
    #
    # Convert text to speech
    converter.say(input_text)
    converter.runAndWait()  # Wait for the speech to finish

# Example usage
speak(text)
