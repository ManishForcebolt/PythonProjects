
import speech_recognition as sr

def recognize_speech_from_file(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(audio_file_path) as source:
        # Listen to the file
        audio_data = recognizer.record(source)

        try:
            # Recognize the audio
            text = recognizer.recognize_google(audio_data)
            print("Text recognized from audio:")
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"

# Example usage
audio_file_path = 'output.wav'
text = recognize_speech_from_file(audio_file_path)
print(text)
