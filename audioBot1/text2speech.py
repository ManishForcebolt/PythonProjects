import pyttsx3

def speak_text(text):
    engine = pyttsx3.init('nsss')
    engine.say(text)
    engine.runAndWait()


speak_text("Hello! I am your voice assistant. How can I assist you today?")
